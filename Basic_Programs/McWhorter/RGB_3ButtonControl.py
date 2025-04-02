
from machine import Pin,PWM
import time
# import machine
# pinRed = 16
# pinGreen = 17
# pinBlue = 18
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
ledR =17
ledG =18
ledB = 16
ledRed = Pin(ledR,Pin.OUT)
ledGreen = Pin(ledG,Pin.OUT)
ledBlue = Pin(ledB,Pin.OUT)

butRED =13
butGREEN = 14
butBLUE = 15

buttonRed =Pin(butRED,Pin.IN,Pin.PULL_DOWN)
buttonGreen = Pin(butGREEN,Pin.IN,Pin.PULL_DOWN)
buttonBlue = Pin(butBLUE,Pin.IN,Pin.PULL_DOWN)

ledStateRed = True
newButValRed = 1
oldButValRed = 1

ledStateGreen =True
newButValGreen =1
oldButValGreen = 1
ledStateBlue = True
newButValBlue =1
oldButValBlue = 1
tUp=time.time()
tDown=time.time()


while True:
    newButValRed =buttonRed.value()
    newButValGreen = buttonGreen.value()
    newButValBlue = buttonBlue.value()
    print("the blue button value is:  ", newButValBlue)
    print(newButValRed, oldButValRed)
    time.sleep(.3)
    if (newButValRed == 0) and oldButValRed ==1:
        
        ledRed.value(ledStateRed)
        ledStateRed = not ledStateRed
       
    
    oldButValRed = newButValRed
    if (newButValGreen ==0 and oldButValGreen == 1):
        ledGreen.value(ledStateGreen)
        ledStateGreen = not ledStateGreen
        
    ledStateGreen = not ledStateGreen
           
    oldButValGreen = newButValGreen 
    if (newButValBlue ==1 and oldButValBlue ==0 ):
        print('oldButVal',oldButValBlue)
        ledBlue.value(ledStateBlue)
        ledStateBlue = not ledStateBlue
    oldButValBlue = newButValBlue           
        
