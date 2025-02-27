## will have to modify it to include this instantiation:

import machine
import utime
#from ssd1306 import SSD1306_I2C
#madori button
button1 = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_DOWN)
#Pinacolada Button
button2 = machine.Pin(1, machine.Pin.IN, machine.Pin.PULL_DOWN)

led = machine.Pin(25, machine.Pin.OUT)


'''
sda=machine.Pin(2)
scl=machine.Pin(3)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)
print(i2c.scan())
from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c, addr = 0x3d)

'''

while True:
    led.value(0)
    oled.fill(0)
    oled.show()
    if button1.value()== 1:
       from ssd1306 import SSD1306_I2C
       oled.fill(0)
       oled.show()
       oled.text("Madori", 0, 0)
       oled.text("Splice", 0, 10)
       oled.show()
       led.value(1)
       utime.sleep(0.5)
       print("button pressed")
       
    if button2.value()== 0:
       from ssd1306 import SSD1306_I2C
       oled.fill(0)
       oled.show()
       oled.text("Pina", 0, 0)
       oled.text("Colada", 0, 10)
       oled.show()
       led.value(1)
       utime.sleep(0.5)
       print("button pressed")

