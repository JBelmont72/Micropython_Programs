# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ssd1306-oled-micropython/

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from utime import sleep


#You can choose any other combination of I2C pins
i2c = I2C(1,scl=Pin(19), sda=Pin(18), freq = 400000)

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr = 0x3d)
sleep(.2)
oled.text('Hello, World 1!', 0, 0)
oled.text('Hello, World 2!', 0, 10)
oled.text('Hello, World 3!', 0, 20)
sleep(2)        
oled.show()
oled.fill()
oled.show()

'''

dsp=SSD1306_I2C(128,64,i2c,addr = 0X3d)
# the ic2 is the created object
msg = "Hello World "
dsp.text(msg,1,50)
#column first and row second
dsp.show()
'''
