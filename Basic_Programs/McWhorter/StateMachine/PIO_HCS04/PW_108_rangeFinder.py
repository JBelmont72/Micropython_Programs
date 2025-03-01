'''
PW_108  HCS04  with oled display
create a portable distance measurement widget using the Raspberry Pi Pico W, the HC-SR04 Ultrasonic Sensor, and the SSD1306 OLED display.
https://github.com/PerfecXX/MicroPython-SSD1306/tree/main the best ssd1306 library
'''
# from machine import Pin, I2C, SoftI2C
# from ssd1306 import SSD1306_I2C
# import framebuf
# import math
# import utime
# from time import sleep
# WIDTH  = 128                                            # oled display width
# HEIGHT = 64                                             # oled display height

# i2c=SoftI2C( scl=Pin(19),sda =Pin(18), freq=400000)	# worked without frequency as well!
# I2C_ADDR = i2c.scan()[0]
# print(hex(I2C_ADDR)) 
# # Note, progranm did not work when I fed the number values for width and height in directly
# oled_width = 128
# oled_height = 64
# oled = SSD1306_I2C(oled_width, oled_height, i2c, addr = 0x3d)
# sleep(1)
# oled.fill(0)
# oled.show()
# oled.text('Hello, Jan', 0, 0)
# oled.text('I love you!', 0, 10)
# oled.text('You are GREAT!', 0, 20)

# #oled.show()# Clear the display
# # oled.fill(0)

# # Draw a horizontal line
# #          x y  lenth color
# oled.hline(0,60,100,1)
# oled.show()
# sleep(5) 
# oled.fill(1) 
# sleep(1)      




# import rp2
# from machine import Pin,I2C  #***************
# import time
 
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
# def pulse_program():
#     wrap_target()
#     pull(block)
#     mov(x,osr)
#     set(pins,1)[31-1]
#     set(pins,0)
#     wait(1,pin,0)
#     label("land")
#     in_(pins,1) # 1 Cycle
#     mov(y,isr)  # 1 Cycle
#     jmp(not_y,"moveOn") # 1 Cycle
#     jmp(x_dec,"land")  # 1 Cycle
#     label("moveOn")
#     mov(isr,invert(x))
#     push()
#     wrap()
# triggerPin = Pin(1,Pin.OUT)
# echoPin = Pin(0, Pin.IN)
# sm=rp2.StateMachine(0,pulse_program, freq=1000000, set_base=triggerPin,in_base=echoPin)
# sm.active(1)
# while True:
#     sm.put(0xFFFFFFFF)
#     print("Pulse Launched")
#     clockCycles=(sm.get())*4/2
#     distance=clockCycles*.0342
#     print("Distance to Target: ",distance)
#     oled.text("Distance: "+str(distance),0,16)
#     oled.show()
#     oled.fill(0)
#     time.sleep(.25)

#########

import rp2
from machine import Pin, PWM
import time

## set up oled
from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c=SoftI2C( scl=Pin(19),sda =Pin(18), freq=400000)	# worked without frequency as well!
I2C_ADDR = i2c.scan()[0]
print(hex(I2C_ADDR)) 
# Note, progranm did not work when I fed the number values for width and height in directly
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr = 0x3d)


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
triggerPin = Pin(1, Pin.OUT)
echoPin = Pin(0, Pin.IN)
buzzer = PWM(Pin(17))  # Buzzer connected to GPIO2

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
    else:
        print("Measurement failed.")
    time.sleep(0.25)