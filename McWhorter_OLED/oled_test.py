'''
OLED only operates on channel 1
gpio pin 2 SDA AND 3 IS SCL and channel 1
gpio 26 and 27 are channel one
gpio 18 and 19 are channel one
manage packages- i installled "micropython-ssd1306.py" library
Beware of "micropython-ssd1306py.py" (might be okay but not the same)
Always need:
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
import time

create an i2c object named "i2c"
use the I2C "method" to create a specific i2c pin
the display object we'll call "dsp" and need to use a method to "call" the I2C object here called 'i2c'

'''
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
#from ssd1306 import SSD1306_I2C
from  time import sleep


sda=machine.Pin(2)
scl=machine.Pin(3)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)
print(i2c.scan())

dsp = SSD1306_I2C(128, 64, i2c, addr = 0x3d)



#i2c = I2C(1,sda=Pin(2),scl = Pin(3),freq = 400000)


# the ic2 is the created object
msg = "Hello World"
while True:
    print("Hello")
    dsp.text("Hello",0,0)
    dsp.show()
    sleep(1)
#column first and row second
    
    dsp.fill(0)
    sleep(1)
    
