'''

bring all pins low on Pico
'''
import sys
# import rp2
import time
from machine import Pin
bPin=16
rPin =17
yPin=18
gPin=19
Pin5=20
bLed=Pin(bPin,Pin.OUT)
rLed=Pin(rPin,Pin.OUT)
yLed=Pin(yPin,Pin.OUT)
gLed=Pin(gPin,Pin.OUT)
Led5=Pin(Pin5,Pin.OUT)
pin0=0
pin1=1
pin2=2
pin3=3
pin4=4
pin5=5
pin6=6
pin7=7
pin8=8
pin9=9
pin10=10
pin11=11
pin12=12
pin13=13


Pin0=Pin(pin0,Pin.IN,Pin.PULL_DOWN)
pin1=Pin(pin1,Pin.IN,Pin.PULL_DOWN)
Pin2=Pin(pin2,Pin.IN,Pin.PULL_DOWN)
pin3=Pin(pin3,Pin.IN,Pin.PULL_DOWN)
Pin4=Pin(pin4,Pin.IN,Pin.PULL_DOWN)
Pin5=Pin(pin5,Pin.IN,Pin.PULL_DOWN)
Pin6=Pin(pin6,Pin.IN,Pin.PULL_DOWN)
pin7=Pin(pin7,Pin.IN,Pin.PULL_DOWN)
Pin8=Pin(pin8,Pin.IN,Pin.PULL_DOWN)
pin9=Pin(pin9,Pin.IN,Pin.PULL_DOWN)
Pin10=Pin(pin10,Pin.IN,Pin.PULL_DOWN)
Pin10=Pin(pin10,Pin.IN,Pin.PULL_DOWN)

try:
    while True:
        pass
except KeyboardInterrupt:
    
    bLed.value(0)
    rLed.value(0)
    gLed.value(0)
    yLed.value(0)
    Led5.value(0)
    print('\nprogram ended')
    sys.exit()