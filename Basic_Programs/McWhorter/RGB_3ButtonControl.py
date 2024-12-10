
from machine import Pin,PWM
from time import sleep

pinRed = 16
pinGreen = 17
pinBlue = 18
'''
analogOutRed= PWM(pinRed)
analogOutGreen = PWM(pinGreen)
analogOutBlue = PWM(pinBlue)

analogOutRed.freq(1000)
analogOutGreen.freq(1000)
analogOutBlue.freq(1000)


analogOutRed.duty_u16(0)
analogOutGreen.duty_u16(0)
analogOutBlue.duty_u16(0)

analogOutRed.duty_u16(65535)
analogOutGreen.duty_u16(65535)
analogOutBlue.duty_u16(65535)
'''
ledR =16
ledG =17
ledB = 18
ledRed = machine.Pin(ledR,Pin.OUT)
ledGreen = machine.Pin(ledG,Pin.OUT)
ledBlue = machine.Pin(ledB,Pin.OUT)

butRED =19
butGREEN = 20
butBLUE = 21

buttonRed = machine.Pin(butRED,Pin.IN,Pin.PULL_UP)
buttonGreen = machine.Pin(butGREEN,Pin.IN,Pin.PULL_UP)
buttonBlue = machine.Pin(butBLUE,Pin.IN,Pin.PULL_UP)

ledStateRed = True
newButValRed = 1
oldButValRed = 1

ledStateGreen =True
newButValGreen =1
oldButValGreen = 1
ledStateBlue = True
newButValBlue =1
oldButValBlue = 1



while True:
    newButValRed =buttonRed.value()
    newButValGreen = buttonGreen.value()
    newButValBlue = buttonBlue.value()
    print("the blue button value is:  ", newButValBlue)
    print(newButValRed, oldButValRed)
    sleep(.3)
    if (newButValRed == 0) and oldButValRed ==1:
        ledRed.value(ledStateRed)
        ledStateRed = not ledStateRed
        
    
    oldButValRed = newButValRed
    if (newButValGreen ==0 and oldButValGreen == 1):
        ledGreen.value(ledStateGreen)
        
        ledStateGreen = not ledStateGreen
           
    oldButValGreen = newButValGreen 
    if (newButValBlue ==0 and oldButValBlue ==1 ):
        ledBlue.value(ledStateBlue)
        ledStateBlue = not ledStateGreen
    oldButValBlue = newButValBlue           
        
