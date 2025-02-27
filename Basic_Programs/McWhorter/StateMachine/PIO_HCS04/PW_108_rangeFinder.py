'''
PW_108  HCS04  with oled display
create a portable distance measurement widget using the Raspberry Pi Pico W, the HC-SR04 Ultrasonic Sensor, and the SSD1306 OLED display.

'''
from machine import Pin, I2C, SoftI2C
from ssd1306 import SSD1306_I2C
import framebuf
import math
import utime
from time import sleep
WIDTH  = 128                                            # oled display width
HEIGHT = 64                                             # oled display height

i2c=SoftI2C( scl=Pin(19),sda =Pin(18), freq=400000)	# worked without frequency as well!
I2C_ADDR = i2c.scan()[0]
print(hex(I2C_ADDR)) 
# Note, progranm did not work when I fed the number values for width and height in directly
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr = 0x3d)
sleep(.2)
oled.text('Hello, Jan', 0, 0)
oled.text('I love you!', 0, 10)
oled.text('You are GREAT!', 0, 20)
sleep(2)        
oled.show()


import rp2
from machine import Pin,I2C  #***************
import time
 
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse_program():
    wrap_target()
    pull(block)
    mov(x,osr)
    set(pins,1)[31-1]
    set(pins,0)
    wait(1,pin,0)
    label("land")
    in_(pins,1) # 1 Cycle
    mov(y,isr)  # 1 Cycle
    jmp(not_y,"moveOn") # 1 Cycle
    jmp(x_dec,"land")  # 1 Cycle
    label("moveOn")
    mov(isr,invert(x))
    push()
    wrap()
triggerPin = Pin(1,Pin.OUT)
echoPin = Pin(0, Pin.IN)
sm=rp2.StateMachine(0,pulse_program, freq=1000000, set_base=triggerPin,in_base=echoPin)
sm.active(1)
while True:
    sm.put(0xFFFFFFFF)
    print("Pulse Launched")
    clockCycles=(sm.get())*4/2
    distance=clockCycles*.0342
    print("Distance to Target: ",distance)
    oled.text("Distance: "+str(distance),0,16)
    oled.show()
    oled.fill(0)
    time.sleep(.25)

