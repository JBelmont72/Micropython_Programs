intersting 27 feb 2025  i can use the ssd1306.py that thonny will load and that random nerds etc use:

And I can use MOST of the examples from github site:
        https://github.com/PerfecXX/MicroPython-SSD1306/tree/main
        but not the library in the site??
from machine import Pin, SoftI2C
from time import sleep
from ssd1306 import SSD1306_I2C
import framebuf

id = 1 
sda = Pin(18)
scl = Pin(19)
i2c = SoftI2C(scl=Pin(19), sda=Pin(18), freq = 400000)

oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr = 61)
width = 128
height = 64

print(i2c.scan())

oled.init_display()
oled.text("Hello World", 0, 0)
oled.show()
oled.invert(1)
# Show test text
oled.text("TEST!",40,30)
oled.show()

while True:
    # Rotate the screen to normal
    oled.rotate(1)
    oled.show()
    sleep(1)
    # Rotate the screen 180 degree
    oled.rotate(0)
    oled.show()
    sleep(1)