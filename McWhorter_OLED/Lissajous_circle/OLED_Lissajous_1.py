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

r = 30  #radius of circle
x_center = 64	# halfway across on x axis
y_center = 32   # halfway down from top on y axis
r_inner =20
r_outer = 23
phase = 0
i =1
'''
while True:
    #for r in range (r_inner,r_outer,1):
    #   
    
    for deg in range(0,360,1):
        
        
        rad = (deg / 360 ) *2 *3.14
        x = int(  r* math.cos(rad +phase) +x_center)
        y = int( 0.4 *r* math.sin(2*rad) +y_center)
        oled.pixel((x), (y),1)
        #phase = (phase +5) * 2 * 3.14 / 360                             
                
      
    oled.show()
    oled.fill(0)
    phase = (phase +5) * 2 * 3.14 / 360
'''
#save this one.  the figures appear to change rotation 
while True:
    for i in range (1,360,15):
        phase =(phase+i) * 2 * 3.14/360
        for deg in range(0,360,1):
        
        
            rad = (deg / 360 ) *2 *3.14
            x = int(  r* math.cos(2*rad +phase) +x_center)
            y = int( .4*1 *r* math.sin(1*rad) +y_center)
            oled.pixel((x), (y),1)
        phase = (phase +5) * 2 * 3.14 / 360                             
                
      
        oled.show()
        oled.fill(0)

