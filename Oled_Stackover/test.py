from machine import Pin, I2C
from time import sleep
from ssd1306 import SSD1306_I2C
import framebuf

id = 1 
sda = Pin(2)
scl = Pin(3)
i2c = I2C(id,scl=Pin(3), sda=Pin(2), freq = 400000)

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
# above works, i have to study microcontrollers to understnd below
with open('frame04.pbm', 'rb') as f:
    f.readline() # magic number
    f.readline() # creator comment
    f.readline() # dimensions
    data = bytearray(f.read())

fb = framebuf.FrameBuffer(data, 128, 64, framebuf.MONO_HLSB)

oled.blit(fb, 0,0)
oled.show()

