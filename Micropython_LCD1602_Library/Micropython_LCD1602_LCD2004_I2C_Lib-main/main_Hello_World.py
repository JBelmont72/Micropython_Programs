# -*- coding: utf-8 -*-

from lib_lcd1602 import LCD
from machine import Pin, SoftI2C
#from lib_lcd1602_2004_with_i2c import LCD
import utime as time
scl_pin = 21
sda_pin = 20
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))
while True:
    lcd.clear()
    lcd.puts("Hello, World!")
    time.sleep(1)
    lcd.clear()
    time.sleep(.5)
    myName = input('What is Your Name?')
    greeting1 =('Hello  ' +myName)
    lcd.puts(greeting1)
    time.sleep(2)
    lcd.clear()
    greeting2= 'Welcome home!'
    lcd.puts(greeting1)
    time.sleep(2)
    lcd.clear()
    
    
    
    lcd.puts(greeting2)
    time.sleep(3)
    

'''hardcoded to pins 6 and 7  if just use lcd=LCD()
also use import utime as time   if needed.
sirst is rows and second is columns
'''
'''
from lib_lcd1602 import LCD
import utime as time
#from lib_lcd1602
from machine import Pin, SoftI2C
#from lib_lcd1602_2004_with_i2c import LCD
scl_pin = 21
sda_pin = 20
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))



while True:
    myName = input('What is Your Name?')
    greeting1 =('Hello  ' +myName)
    greeting2= 'Welcome home!'
    lcd.puts(0,0,greeting1)
    lcd.puts(1,0,greeting2)
          
'''




