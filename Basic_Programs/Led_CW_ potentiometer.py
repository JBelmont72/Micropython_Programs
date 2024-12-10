
#https://www.youtube.com/watch?app=desktop&v=TDj2kcSA-68	
#	Explaining Computers on Youtube
from machine import Pin,ADC,PWM
#import machine
import utime

ledY=17
ledG= 18
ledYellow = machine.Pin((ledY),machine.Pin.OUT)
ledGreen = machine.Pin(18,machine.Pin.OUT)
ledRed =machine.Pin(16,machine.Pin.OUT)
led20 = machine.Pin(20,machine.Pin.OUT)
led21 = machine.Pin(21,machine.Pin.OUT)
potPin=machine.ADC(27)

switchButton = machine.Pin(19,Pin.IN,Pin.PULL_DOWN)

pot = machine.ADC(Pin(27))

Lights = [ledYellow,ledGreen, ledRed,led20,led21]

while True:
    while switchButton.value():
        for x in Lights:
            print(switchButton.value())
            print(pot.read_u16())
            x.high()
            utime.sleep(pot.read_u16()/32668)
            x.low()
            

