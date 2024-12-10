# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-ssd1306-oled-micropython/
# have i2c scanner at bottom
from machine import Pin, SoftI2C,I2C
from ssd1306 import SSD1306_I2C
from time import sleep

#You can choose any other combination of I2C pins
i2c = SoftI2C(scl=Pin(3), sda=Pin(2))

I2C_ADDR = i2c.scan()[0]
print(hex(I2C_ADDR)) 


# Note, progranm did not work when I fed the number values for width and height in directly
oled_width = 128
oled_height = 64
oled = SSD1306_I2C(oled_width, oled_height, i2c, addr = 0x3d)
sleep(.2)
oled.text("WELCOME!", 0, 0,1)
# 4th arguembnet is color of text, 1 is white, o is black, 1=white = default
oled.text("This is a text", 0, 16,1)
oled.text("GOOD BYE", 0, 32,1)
oled.text('Hello, Jan', 0, 48)
oled.text('I love you!', 0, 60)
#oled.text('You are GREAT!', 0, 20)
sleep(2)        
oled.show()
sleep(1)
oled.fill(0)
oled.show()



i2c=I2C(1,sda=Pin(2), scl=Pin(3), freq=400000)
oled = SSD1306_I2C(128, 64, i2c, addr = 0x3d)

while True:
      oled.pixel(64,32,1)
      oled.show()
      sleep(1)
      oled.fill(0)

      oled.hline(0,32,128,1)
      oled.show()
      sleep(2)
      oled.fill(0)  


      oled.hline(40,40,10,1)	#the 3d arguement adds the lenghtn of the line
      oled.show()
      sleep(2)
      oled.fill(0)

      oled.vline(0, 0, 64, 1)		#3d arguement is length
      oled.show()
      sleep(2)
      oled.fill(0)
      
      oled.vline(64, 30, 10, 1)
      oled.show()
      sleep(2)
      oled.fill(0)
      

      oled.line(0, 0, 128, 64, 1)
      oled.show()
      sleep(2)
      oled.fill(0)
      x=0
      y=0
      while x<100:
          oled.line(x,10,50,64, 1)
          oled.show()
          sleep(.5)
          oled.fill(0)
          x=x+10
          
      

      oled.rect(20, 20, 64, 32, 1)
      oled.show()
      sleep(.5)
      oled.fill(0)
      x=0
      while x<100:
          oled.rect(20, 20, x, y, 1)
          oled.show()
          sleep(2)
          oled.fill(0)
          x=x+10
          y=y+5
      
      

      oled.fill_rect(20, 20, 64, 32, 1)
      oled.show()
      sleep(2)
      oled.fill(0)







# i2c scanner
'''
import machine
sda=machine.Pin(2)
scl=machine.Pin(3)
i2c=machine.I2C(1,sda=sda, scl=scl, freq=400000)

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
    print("No i2c device !")
else:
    print('i2c devices found:',len(devices))

for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device))

'''



