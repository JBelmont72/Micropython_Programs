from machine import Pin, PWM
from time import sleep, ticks_ms
import network, socket
## server 
class Motor:
    def __init__(self, pin_forward, pin_backward, pwm_speed_pin):
        self.forward = Pin(pin_forward, Pin.OUT)
        self.backward = Pin(pin_backward, Pin.OUT)
        self.pwm = PWM(Pin(pwm_speed_pin))
        self.pwm.freq(1000)
        self.speed = 0
        self.target_speed = 0

    def update_pwm(self):
        if self.speed < self.target_speed:
            self.speed += 1000  # ramp up
        elif self.speed > self.target_speed:
            self.speed -= 1000  # ramp down
        self.pwm.duty_u16(max(0, min(65535, self.speed)))

    def set(self, direction, speed=32768):
        self.target_speed = speed
        if direction == "forward":
            self.forward.on()
            self.backward.off()
        elif direction == "backward":
            self.forward.off()
            self.backward.on()
        else:
            self.forward.off()
            self.backward.off()
            self.target_speed = 0

    def stop(self):
        self.set("stop")

class RobotBuggyUDPServer:
    def __init__(self):
        self.motor_left = Motor(10, 11, 8)
        self.motor_right = Motor(12, 13, 9)
        self.buzzer = PWM(Pin(14))
        self.buzzer.freq(1000)
        self.buzzer.duty_u16(0)
        self.front_trig = Pin(3, Pin.OUT)
        self.front_echo = Pin(2, Pin.IN)
        self.back_trig = Pin(6, Pin.OUT)
        self.back_echo = Pin(7, Pin.IN)
        self.sock = None
        self.last_ramp = ticks_ms()

    def start(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect('SpectrumSetup-41', 'leastdinner914')
        while not wlan.isconnected():
            sleep(0.5)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', 5005))

    def measure_distance(self, trig, echo):
        trig.low()
        sleep(0.002)
        trig.high()
        sleep(0.01)
        trig.low()
        while echo.value() == 0:
            start = ticks_ms()
        while echo.value() == 1:
            end = ticks_ms()
        duration = end - start
        distance = duration * 0.034 / 2
        return distance

    def handle_obstacles(self):
        front = self.measure_distance(self.front_trig, self.front_echo)
        if front < 12:
            self.buzzer.duty_u16(32768)
            self.motor_left.set("backward", 30000)
            self.motor_right.set("backward", 30000)
            sleep(0.5)
            self.motor_left.set("backward", 0)
            self.motor_right.set("backward", 32768)
            sleep(0.6)  # Turn left
            self.buzzer.duty_u16(0)
            side = self.measure_distance(self.front_trig, self.front_echo)
            if side > 30:
                self.motor_left.set("forward")
                self.motor_right.set("forward")
            else:
                # Turn 180
                self.motor_left.set("backward", 0)
                self.motor_right.set("forward", 32768)
                sleep(1.2)
                self.motor_left.set("forward", 32768)
                self.motor_right.set("forward", 32768)

    def handle_command(self, data):
        speed = 32768
        if data == "forward":
            self.motor_left.set("forward", speed)
            self.motor_right.set("forward", speed)
        elif data == "backward":
            self.motor_left.set("backward", speed)
            self.motor_right.set("backward", speed)
        elif data == "left":
            self.motor_left.set("backward", 0)
            self.motor_right.set("forward", speed)
        elif data == "right":
            self.motor_left.set("forward", speed)
            self.motor_right.set("backward", 0)
        elif data == "stop":
            self.motor_left.stop()
            self.motor_right.stop()

    def loop(self):
        self.handle_obstacles()
        if ticks_ms() - self.last_ramp > 50:
            self.motor_left.update_pwm()
            self.motor_right.update_pwm()
            self.last_ramp = ticks_ms()
        self.sock.settimeout(0.01)
        try:
            data, addr = self.sock.recvfrom(1024)
            command = data.decode()
            self.handle_command(command)
        except:
            pass

if __name__ == "__main__":
    robot = RobotBuggyUDPServer()
    robot.start()
    print("Robot ready!")
    while True:
        robot.loop()
