

from machine import Pin, SoftI2C
from lib_lcd1602 import LCD
scl_pin = 1 # write your own pin number
sda_pin = 0 # write your own pin number
lcd = LCD(SoftI2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000))

custom_char = [
  0b00111,
  0b00000,
  0b00000,
  0b00111,
  0b00000,
  0b00000,
  0b00000,
  0b11111]

lcd.puts("Hello, World!",1,2)
lcd.create_charactor(0,custom_char)