'''

The updated code now includes both client and server programs with clearly structured and commented logic, supporting:
Short press on button (Pin 2) for a stop command.
Long press (4+ seconds) for an exit/kill switch.
On the server side:
Obstacle detection using a front HC-SR04 sensor with PIO.
Automatic avoidance maneuvers if obstruction is closer than 20 cm.
Proper recvfrom timeout and debounced button IRQ handling.
Let me know if you want to:
Add rear sensor behavior.
Include more commands (e.g., speed control).
Log events or sensor data.
Convert to MQTT instead of UDP.


✅ Reused the same pulse_program for both front and rear.
✅ Used separate trigger/echo pins for the rear (6 and 7).
✅ Created self.sm2 as StateMachine(1, ...) and started it with .active(1).
✅ Added a get_rear_distance() method mirroring get_front_distance().
✅ In the run() loop:
Checked rear distance first.
Stopped and paused for 2 seconds if rear obstacle is closer than 20 cm.
'''
# === CLIENT SIDE (Controller Unit) ===
from machine import Pin
import time
import socket
import sys

STOP_PIN = 2  # Dual function pin (stop/exit)
BUTTON_HOLD_DURATION = 4  # seconds

UDP_IP = '192.168.4.1'  # IP of the server Pico W
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

stop_pin = Pin(STOP_PIN, Pin.IN, Pin.PULL_UP)

# Debounce buffer
DEBOUNCE_DELAY = 0.01
last_value = 1
stable_count = 0


def send_command(command):
    sock.sendto(command.encode(), (UDP_IP, UDP_PORT))


def monitor_stop_exit():
    global last_value, stable_count
    pressed_time = None
    while True:
        current_value = stop_pin.value()
        if current_value != last_value:
            stable_count = 0
        else:
            stable_count += 1

        last_value = current_value

        if stable_count >= 3:  # ~30ms stable reading
            if not current_value:
                if pressed_time is None:
                    pressed_time = time.time()
                elif time.time() - pressed_time > BUTTON_HOLD_DURATION:
                    print("Exit button held for 4 seconds. Exiting...")
                    send_command("exit")
                    sys.exit()
            else:
                if pressed_time is not None and time.time() - pressed_time < BUTTON_HOLD_DURATION:
                    print("Stop button short press detected")
                    send_command("stop")
                pressed_time = None

        time.sleep(DEBOUNCE_DELAY)


if __name__ == '__main__':
    print("Controller started. Hold button for 4s to exit.")
    monitor_stop_exit()

# === SERVER SIDE (Buggy Unit) ===
# import socket
# import sys
# from machine import Pin, PWM
# import rp2
# import time
# from time import ticks_ms, ticks_diff

# EXIT_BUTTON_PIN = 2  # Dual function pin
# BUTTON_HOLD_DURATION = 4000  # milliseconds
# CRITICAL_DISTANCE = 200  # mm
# SPEED = 40000
# MEDIUM_SPEED = 30000

# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
# def pulse_program():
#     wrap_target()
#     pull(block)
#     mov(x, osr)
#     set(pins, 1)[10 - 1]
#     set(pins, 0)
#     wait(1, pin, 0)

#     label("land")
#     in_(pins, 1)
#     mov(y, isr)
#     jmp(not_y, "moveOn")
#     jmp(x_dec, "land")

#     label("moveOn")
#     mov(isr, invert(x))
#     push()
#     wrap()

# class Motor:
#     def __init__(self, in1, in2, pwm):
#         self.in1 = Pin(in1, Pin.OUT)
#         self.in2 = Pin(in2, Pin.OUT)
#         self.pwm = PWM(Pin(pwm))
#         self.pwm.freq(1000)
#         self.pwm.duty_u16(0)

#     def forward(self, speed):
#         self.in1.high()
#         self.in2.low()
#         self.pwm.duty_u16(speed)

#     def backward(self, speed):
#         self.in1.low()
#         self.in2.high()
#         self.pwm.duty_u16(speed)

#     def stop(self):
#         self.pwm.duty_u16(0)

# class RobotBuggyUDPServer:
#     def __init__(self):
#         self.motor_left = Motor(10, 11, 8)
#         self.motor_right = Motor(12, 13, 9)
#         self.buzzer = PWM(Pin(14))
#         self.buzzer.freq(1000)
#         self.buzzer.duty_u16(0)
#         self.front_trig = Pin(3, Pin.OUT)
#         self.front_echo = Pin(2, Pin.IN)  # shared with exit/stop button
#         self.sm = rp2.StateMachine(0, pulse_program, freq=1000000,
#                                    set_base=self.front_trig, in_base=self.front_echo)
#         self.sm.active(1)
                
#         self.rear_trig = Pin(6, Pin.OUT)
#         self.rear_echo = Pin(7, Pin.IN)

#         self.sm2 = rp2.StateMachine(1, pulse_program, freq=1000000,
#                                         set_base=self.rear_trig, in_base=self.rear_echo)
#         self.sm2.active(1)

#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.sock.bind(("0.0.0.0", 5005))
#         self.running = True

#         self.button_pin = Pin(EXIT_BUTTON_PIN, Pin.IN, Pin.PULL_UP)
#         self.button_pin.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=self.button_irq)
#         self.pressed_time = None

#     def button_irq(self, pin):
#         time.sleep_ms(10)  # debounce delay
#         if pin.value() == 0:
#             self.pressed_time = ticks_ms()
#         else:
#             if self.pressed_time:
#                 held = ticks_diff(ticks_ms(), self.pressed_time)
#                 if held >= BUTTON_HOLD_DURATION:
#                     print("Exit long press detected. Shutting down.")
#                     self.stop_all()
#                     self.running = False
#                 else:
#                     print("Stop short press detected. Stopping motors.")
#                     self.stop_all()
#             self.pressed_time = None

#     def stop_all(self):
#         self.motor_left.stop()
#         self.motor_right.stop()
#         self.buzzer.duty_u16(0)

#     def get_front_distance(self):
#         self.sm.put(0xFFFF)
#         t0 = ticks_ms()
#         while self.sm.rx_fifo() == 0:
#             if ticks_diff(ticks_ms(), t0) > 100:
#                 return None  # Timeout
#         ticks = self.sm.get()
#         distance_mm = (ticks * 100) // 582  # approximate conversion
#         return distance_mm
# ## if i have a rear distance sensor, uncomment this 
#     # def get_rear_distance(self):
#     #     self.sm2.put(0xFFFF)
#     #     t0 = ticks_ms()
#     #     while self.sm2.rx_fifo() == 0:
#     #         if ticks_diff(ticks_ms(), t0) > 100:
#     #             return None  # Timeout
#     #     ticks = self.sm2.get()
#     #     distance_mm = (ticks * 100) // 582
#     #     return distance_mm

    
    
#     def handle_command(self, cmd):
#         if cmd == 'stop':
#             self.stop_all()
#         elif cmd == 'exit':
#             print("Received exit from controller. Shutting down.")
#             self.stop_all()
#             self.running = False
#         elif cmd == 'forward':
#             self.motor_left.forward(SPEED)
#             self.motor_right.forward(SPEED)
#         elif cmd == 'backward':
#             self.motor_left.backward(SPEED)
#             self.motor_right.backward(SPEED)
#         elif cmd == 'left':
#             self.motor_left.backward(SPEED)
#             self.motor_right.forward(SPEED)
#         elif cmd == 'right':
#             self.motor_left.forward(SPEED)
#             self.motor_right.backward(SPEED)
#         else:
#             print(f"Unknown command: {cmd}")

#     def run(self):
#         print("UDP Server running...")
#         while self.running:
#             try:
#                 self.sock.settimeout(0.5)
#                 data, addr = self.sock.recvfrom(1024)
#                 cmd = data.decode().strip()
#                 print(f"Command: {cmd}")

#                 distance = self.get_front_distance()
#                 ## if i have a rear distance sensor, uncomment this 
#                 # rear_distance = self.get_rear_distance()
#                 # if rear_distance is not None and rear_distance < CRITICAL_DISTANCE:
#                 #     print(f"Rear obstacle {rear_distance}mm detected. Stopping.")
#                 #     self.stop_all()
#                 #     time.sleep(2)
#                 #     continue

                
#                 if distance is not None and distance < CRITICAL_DISTANCE:
#                     print(f"Obstacle {distance}mm detected. Avoiding.")
#                     self.buzzer.duty_u16(40000)
#                     self.stop_all()
#                     time.sleep(0.5)
#                     self.motor_left.backward(MEDIUM_SPEED)
#                     self.motor_right.forward(MEDIUM_SPEED)
#                     time.sleep(0.8)
#                     self.stop_all()
#                     time.sleep(0.3)

#                     distance = self.get_front_distance()
#                     if distance is not None and distance > 400:
#                         self.motor_left.forward(MEDIUM_SPEED)
#                         self.motor_right.forward(MEDIUM_SPEED)
#                         time.sleep(3)
#                         self.motor_left.forward(MEDIUM_SPEED)
#                         self.motor_right.backward(MEDIUM_SPEED)
#                         time.sleep(0.8)
#                     else:
#                         self.motor_left.backward(MEDIUM_SPEED)
#                         self.motor_right.forward(MEDIUM_SPEED)
#                         time.sleep(1.6)
#                         distance = self.get_front_distance()
#                         if distance is not None and distance > 400:
#                             self.motor_left.forward(MEDIUM_SPEED)
#                             self.motor_right.forward(MEDIUM_SPEED)
#                             time.sleep(3)
#                             self.motor_left.backward(MEDIUM_SPEED)
#                             self.motor_right.forward(MEDIUM_SPEED)
#                             time.sleep(0.8)
#                     self.stop_all()
#                     self.buzzer.duty_u16(0)
#                     continue

#                 self.handle_command(cmd)
#             except OSError:
#                 pass

# if __name__ == '__main__':
#     server = RobotBuggyUDPServer()
#     server.run()
#     print("Server exited cleanly.")
