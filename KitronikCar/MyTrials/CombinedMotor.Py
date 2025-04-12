# ========== Mini Controller (Sender) ==========
from machine import Pin, ADC
import network, socket
from time import sleep

class MiniControllerUDP:
    def __init__(self, server_ip, port=5005):
        self.server_ip = server_ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Buttons
        self.btn_up = Pin(1, Pin.IN, Pin.PULL_DOWN)
        self.btn_down = Pin(2, Pin.IN, Pin.PULL_DOWN)
        self.btn_left = Pin(3, Pin.IN, Pin.PULL_DOWN)
        self.btn_right = Pin(4, Pin.IN, Pin.PULL_DOWN)
        self.btn_stop = Pin(14, Pin.IN, Pin.PULL_DOWN)

        # ADCs for speed
        self.speed_adc = ADC(1)  # GP27/ADC1

    def get_speed(self):
        raw = self.speed_adc.read_u16()
        return min(int((raw / 65535) * 100), 100)  # Scale 0–100

    def check_buttons(self):
        speed = self.get_speed()
        if self.btn_up.value():
            return f"FWD:{speed}"
        elif self.btn_down.value():
            return f"BACK:{speed}"
        elif self.btn_left.value():
            return f"LEFT:{speed}"
        elif self.btn_right.value():
            return f"RIGHT:{speed}"
        elif self.btn_stop.value():
            return "STOP"
        return None

    def run(self):
        while True:
            msg = self.check_buttons()
            if msg:
                self.sock.sendto(msg.encode(), (self.server_ip, self.port))
            sleep(0.1)


# ========== Robot Buggy (Receiver) ==========
from machine import Pin, PWM
import socket
import time
import _thread
from hcsr04 import HCSR04

class Motor:
    def __init__(self, pwm_pin, in1, in2):
        self.pwm = PWM(Pin(pwm_pin))
        self.pwm.freq(1000)
        self.in1 = Pin(in1, Pin.OUT)
        self.in2 = Pin(in2, Pin.OUT)

    def move(self, speed, direction):
        duty = int((speed / 100) * 65535)
        self.pwm.duty_u16(duty)
        if direction == "FWD":
            self.in1.high()
            self.in2.low()
        elif direction == "BACK":
            self.in1.low()
            self.in2.high()
        else:
            self.in1.low()
            self.in2.low()

    def stop(self):
        self.pwm.duty_u16(0)
        self.in1.low()
        self.in2.low()


class BuggyUDP:
    def __init__(self, port=5005):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("0.0.0.0", port))

        # Motors
        self.left_motor = Motor(18, 19, 20)  # Example pins
        self.right_motor = Motor(21, 22, 26)

        # Ultrasonic sensors
        self.front_sensor = HCSR04(trigger_pin=12, echo_pin=13)
        self.back_sensor = HCSR04(trigger_pin=8, echo_pin=9)

        # Buzzer
        self.buzzer = PWM(Pin(5))
        self.buzzer.freq(1000)

        self.last_speed = 0

    def ramp_speed(self, target):
        step = 5 if self.last_speed < target else -5
        for spd in range(self.last_speed, target + step, step):
            yield spd
        self.last_speed = target

    def sound_buzzer(self, duration=300):
        self.buzzer.duty_u16(30000)
        time.sleep_ms(duration)
        self.buzzer.duty_u16(0)

    def avoid_obstacle(self):
        dist = self.front_sensor.distance_cm()
        if dist < 12:
            self.left_motor.stop()
            self.right_motor.stop()
            self.sound_buzzer()
            self.turn("LEFT", 0.5)
            if self.front_sensor.distance_cm() > 30:
                self.move("FWD", 60)
            else:
                self.turn("LEFT", 1.0)  # Approx 180°
                self.move("FWD", 60)
            return True
        return False

    def move(self, direction, speed):
        for s in self.ramp_speed(speed):
            if direction == "FWD":
                self.left_motor.move(s, "FWD")
                self.right_motor.move(s, "FWD")
            elif direction == "BACK":
                self.left_motor.move(s, "BACK")
                self.right_motor.move(s, "BACK")
            elif direction == "LEFT":
                self.left_motor.move(s, "BACK")
                self.right_motor.move(s, "FWD")
            elif direction == "RIGHT":
                self.left_motor.move(s, "FWD")
                self.right_motor.move(s, "BACK")
            time.sleep(0.01)

    def turn(self, direction, duration):
        if direction == "LEFT":
            self.left_motor.move(60, "BACK")
            self.right_motor.move(60, "FWD")
        elif direction == "RIGHT":
            self.left_motor.move(60, "FWD")
            self.right_motor.move(60, "BACK")
        time.sleep(duration)
        self.left_motor.stop()
        self.right_motor.stop()

    def run(self):
        while True:
            try:
                data, _ = self.sock.recvfrom(1024)
                msg = data.decode()

                if self.avoid_obstacle():
                    continue

                if msg == "STOP":
                    self.left_motor.stop()
                    self.right_motor.stop()
                else:
                    cmd, speed = msg.split(":")
                    self.move(cmd, int(speed))

            except Exception as e:
                print("Error:", e)
                self.left_motor.stop()
                self.right_motor.stop()
