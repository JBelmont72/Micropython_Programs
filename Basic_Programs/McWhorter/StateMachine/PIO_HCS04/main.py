'''
tutorial on machine.time_pulse_us method
https://www.programcreek.com/python/example/101403/machine.time_pulse_us


'''


import rp2
from machine import Pin, PWM
import time

## set up oled
from machine import Pin, I2C, SoftI2C,PWM
from ssd1306 import SSD1306_I2C

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c=SoftI2C( scl=Pin(3),sda =Pin(2), freq=400000)	# worked without frequency as well!
I2C_ADDR = i2c.scan()[0]
print(hex(I2C_ADDR)) 
# Note, progranm did not work when I fed the number values for width and height in directly
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr = 0x3d)

rPin =15
rLed=PWM(rPin)
rLed.freq(10000)
rLed.duty_u16(0)
gPin =14
gLed=PWM(rPin)
gLed.freq(10000)
gLed.duty_u16(0)
bPin =13
bLed=PWM(rPin)
bLed.freq(10000)
bLed.duty_u16(0)


# Define the PIO program for ultrasonic timing
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse_program():
    wrap_target()
    pull(block)
    mov(x, osr)
    set(pins, 1)[10 - 1]     # Trigger pulse for 10µs
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

# Pin setup
triggerPin = Pin(0, Pin.OUT)
echoPin = Pin(1, Pin.IN)
buzzer = PWM(Pin(16))  # Buzzer connected to GPIO2

# Initialize state machine
sm = rp2.StateMachine(0, pulse_program, freq=1000000, set_base=triggerPin, in_base=echoPin)
sm.active(1)

# Note frequencies for C major chord
notes = {"C": 261, "E": 329, "G": 392}

def play_chord():
 
    """ Play a C major chord (C, E, G) on the passive buzzer. """
    for note, freq in notes.items():
        buzzer.freq(freq)
        buzzer.duty_u16(32768)  # 50% duty cycle
        time.sleep(0.3)
    buzzer.duty_u16(0)         # Turn off buzzer

def get_distance():
    sm.put(0xFFFFFFFF)
    try:
        clock_cycles = sm.get()
    except:
        print("Timeout: No echo received")
        return None

    clock_cycles = clock_cycles * 3 / 2
    distance = clock_cycles * 0.0342

    return distance
def RGB():
    rLed.duty_u16(30000)
    gLed.duty_u16(30000)
    bLed.duty_u16(30000) 
# Main loop
while True:
    distance = get_distance()
    if distance is not None:
        print(f"Distance to Target: {distance:.2f} cm")
        oled.text(str(distance),0,0)
        oled.show()
        oled.fill(0)
        if distance < 20:
            print("Distance < 20 cm  Playing C chord")
            play_chord()
        if distance >= 50:
            RGB()
            print('Warning!!')
        if distance<50:
            rLed.duty_u16(0)
            gLed.duty_u16(0)
            bLed.duty_u16(0) 

            
    else:
        print("Measurement failed.")
    time.sleep(0.25)

# from machine import Pin

# red_led = Pin(13, Pin.OUT)
# green_led = Pin(14, Pin.OUT)
# blue_led = Pin(15, Pin.OUT)
# red_led.on()
# green_led.on()
# blue_led.on()