'''


'''
# ultrasonic_motor_control.py

import rp2
from machine import Pin
import time
import sys  

# PIO ultrasonic pulse program  
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse_program():
    wrap_target()
    pull(block)
    mov(x, osr)
    set(pins, 1)[10 - 1]
    set(pins, 0)
    wait(1, pin, 0)

    label("land")
    in_(pins, 1)
    mov(y, isr)
    jmp(not_y, "moveOn")
    jmp(x_dec, "land")

    label("moveOn")
    mov(isr, invert(x))
    push()
    wrap()

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin, sm_id):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.sm = rp2.StateMachine(sm_id, pulse_program, freq=1000000, set_base=self.trigger, in_base=self.echo)
        self.sm.active(1)

    def get_distance(self):
        self.sm.put(0xFFFFFFFF)
        try:
            clock_cycles = self.sm.get()
        except:
            return None

        clock_cycles = clock_cycles * 3 / 2
        distance = clock_cycles * 0.0342
        return distance

class MotorController:
    def __init__(self, left_pwm, right_pwm):
        from machine import PWM
        self.left = PWM(Pin(left_pwm))
        self.right = PWM(Pin(right_pwm))
        self.left.freq(1000)
        self.right.freq(1000)

    def set_speed(self, left_duty, right_duty):
        self.left.duty_u16(left_duty)
        self.right.duty_u16(right_duty)

    def stop(self):
        self.set_speed(0, 0)

    def ramp_speed(self, start, end, duration=1.0):
        import time
        steps = 20
        delay = duration / steps
        for i in range(steps + 1):
            duty = int(start + (end - start) * i / steps)
            self.set_speed(duty, duty)
            time.sleep(delay)

# if __name__ == '__main__':
#     front_sensor = UltrasonicSensor(trigger_pin=11, echo_pin=12, sm_id=0)
#     back_sensor = UltrasonicSensor(trigger_pin=13, echo_pin=14, sm_id=1)
#     motors = MotorController(left_pwm=15, right_pwm=16)

def main():
    front_sensor = UltrasonicSensor(trigger_pin=11, echo_pin=12, sm_id=0)
    back_sensor = UltrasonicSensor(trigger_pin=13, echo_pin=14, sm_id=1)
    motors = MotorController(left_pwm=15, right_pwm=16)

    motors.ramp_speed(0, 40000)
    time.sleep(0.1) # Allow time for ramping up


    try:
        while True:
            front = front_sensor.get_distance()
            back = back_sensor.get_distance()

            if front and front < 12:
                print("Obstacle detected in front! Stopping and turning.")
                motors.stop()
                time.sleep(0.5)

                motors.set_speed(40000, 10000)  # turn left
                time.sleep(1)
                motors.stop()
                time.sleep(0.3)

                front = front_sensor.get_distance()
                if front and front > 30:
                    motors.ramp_speed(0, 40000)
                else:
                    motors.set_speed(10000, 40000)  # 180 turn
                    time.sleep(1.2)
                    motors.stop()
                    motors.ramp_speed(0, 40000)

            else:
                motors.ramp_speed(0, 40000)
                time.sleep(0.1)
    except(KeyboardInterrupt, SystemExit):
        motors.stop()
        print("Program stopped.")
        sys.exit()
if __name__ == '__main__':
    main()
#########~~~~~~~~   original code   ~~~~~~~~########## ultrasonic_motor_control.py
'''
import rp2
from machine import Pin
import time

# PIO ultrasonic pulse program
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse_program():
    wrap_target()
    pull(block)
    mov(x, osr)
    set(pins, 1)[10 - 1]
    set(pins, 0)
    wait(1, pin, 0)

    label("land")
    in_(pins, 1)
    mov(y, isr)
    jmp(not_y, "moveOn")
    jmp(x_dec, "land")

    label("moveOn")
    mov(isr, invert(x))
    push()
    wrap()

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin, sm_id):
        self.trigger = Pin(trigger_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)
        self.sm = rp2.StateMachine(sm_id, pulse_program, freq=1000000, set_base=self.trigger, in_base=self.echo)
        self.sm.active(1)

    def get_distance(self):
        self.sm.put(0xFFFFFFFF)
        try:
            clock_cycles = self.sm.get()
        except:
            return None

        clock_cycles = clock_cycles * 3 / 2
        distance = clock_cycles * 0.0342
        return distance

class MotorController:
    def __init__(self, left_pwm, right_pwm):
        from machine import PWM
        self.left = PWM(Pin(left_pwm))
        self.right = PWM(Pin(right_pwm))
        self.left.freq(1000)
        self.right.freq(1000)

    def set_speed(self, left_duty, right_duty):
        self.left.duty_u16(left_duty)
        self.right.duty_u16(right_duty)

    def stop(self):
        self.set_speed(0, 0)

    def ramp_speed(self, start, end, duration=1.0):
        import time
        steps = 20
        delay = duration / steps
        for i in range(steps + 1):
            duty = int(start + (end - start) * i / steps)
            self.set_speed(duty, duty)
            time.sleep(delay)

if __name__ == '__main__':
    front_sensor = UltrasonicSensor(trigger_pin=11, echo_pin=12, sm_id=0)
    back_sensor = UltrasonicSensor(trigger_pin=13, echo_pin=14, sm_id=1)
    motors = MotorController(left_pwm=15, right_pwm=16)

    while True:
        front = front_sensor.get_distance()
        back = back_sensor.get_distance()

        if front and front < 12:
            print("Obstacle detected in front! Stopping and turning.")
            motors.stop()
            time.sleep(0.5)

            motors.set_speed(40000, 10000)  # turn left
            time.sleep(1)
            motors.stop()
            time.sleep(0.3)

            front = front_sensor.get_distance()
            if front and front > 30:
                motors.ramp_speed(0, 40000)
            else:
                motors.set_speed(10000, 40000)  # 180 turn
                time.sleep(1.2)
                motors.stop()
                motors.ramp_speed(0, 40000)

        else:
            motors.ramp_speed(0, 40000)
            time.sleep(0.1)
'''