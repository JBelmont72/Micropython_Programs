'''Lissajous

'''

import machine
import utime
from ssd1306 import SSD1306_I2C
import math
'''
button1 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)
led = machine.Pin(25, machine.Pin.OUT)
'''
sda=machine.Pin(14)
scl=machine.Pin(15)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)
print(i2c.scan())
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 64, i2c, addr = 0x3d)

r = 20  #radius of circle
x_center = 64	# halfway across on x axis
y_center = 32   # halfway down from top on y axis
r_inner =20
r_outer = 23

#while True:
    #while True:
while True:
    for r in range (r_inner,r_outer,1):
    
    
       for deg in range(0,360,1):
            rad = (deg / 360 ) *2 *3.14
            x = r* math.cos(rad) +x_center
            y = r* math.sin(rad) +y_center
            oled.pixel(int(x), int(y),1)
            oled.show()                          
                
            
