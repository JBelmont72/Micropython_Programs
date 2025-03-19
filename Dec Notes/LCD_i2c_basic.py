'''
   https://microcontrollerslab.com/i2c-lcd-esp32-esp8266-micropython-tutorial/ 
require two libraries: lcd_api.py and i2c_lcd.py

we initialize the SoftI2C method by giving it three arguments. The first argument specifies the GPIO pin for SCL. This is given as GPIO22 for ESP32 and GPIO5 for ESP8266. The second parameter specifies the GPIO pin for the SDA. This is given as GPIO21 for ESP32 and GPIO4 for ESP8266.
There is a very simple way to generate the byte array of your own custom character. Head over to the following custom character generator: (LCD Custom Character Generator).

https://maxpromer.github.io/LCD-Character-Creator/


Note:  if, instead of i2C  want to use the 9 pin lcd connection then  follow this tutorial:

https://circuitdigest.com/microcontroller-projects/interfacing-raspberry-pi-pico-with-16x2-lcd-using-micropython

excellent article on the displays
https://circuitdigest.com/article/16x2-lcd-display-module-pinout-datasheet




'''


'''

import machine
from machine import Pin, SoftI2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
'''
# This line is used to initialize the I2C connection for the library by creating an object ‘lcd’.
# The first argument to the function I2cLcd() is the i2c object declared previously,
# the second argument is the address of our I2C LCD.
# Third and fourth arguments are the size in terms of the number of columns and number of rows.

'''
while True:
    lcd.putstr("I2C LCD Tutorial")
    sleep(2)
    lcd.clear()
    lcd.putstr("Lets Count 0-10!")
    sleep(2)
    lcd.clear()
    for i in range(11):
        lcd.putstr(str(i))
        sleep(1)
        lcd.clear()
        
''' 
###to display cusom characters
import machine
from machine import SoftI2C, Pin
from lcd_api import LcdApi
from i2c_lcd import I2cLcd

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16

i2c = SoftI2C(scl=Pin(3), sda=Pin(2), freq=10000)     #initializing the I2C method for ESP32
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

heart = bytearray([0x00,0x00,0x1B,0x1F,0x1F,0x0E,0x04,0x00])
face = bytearray([0x00,0x00,0x0A,0x00,0x11,0x0E,0x00,0x00])
lcd.custom_char(0, heart)
lcd.custom_char(1, face)
lcd.putstr(chr(0)+" ESP32 with I2C LCD "+chr(1))

'''
  
''' 
# S= bytearray = ([
#   0x04,
#   0x0A,
#   0x11,
#   0x08,
#   0x04,
#   0x12,
#   0x09,
#   0x06
# ])

# A  = bytearray([
#   0x04,
#   0x0E,
#   0x1B,
#   0x11,
#   0x1F,
#   0x11,
#   0x11,
#   0x11
# ])
# M = bytearray ([
#  0x11,
#   0x1B,
#   0x1F,
#   0x15,
#   0x11,
#   0x11,
#   0x11,
#   0x11 
# ])

    