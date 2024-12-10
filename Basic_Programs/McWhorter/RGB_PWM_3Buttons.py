from machine import Pin,PWM
import utime
'''
In this sketch I have each of the three 'primary' colors on separate pins-pins 16-18
Also have three pushbuttons on three pins.
Used PWM for the analogout control of the RGB.
Next I will alter this to use potentiometers to control the threecolors and then maybe use
a rotary encoder to control and use the switch to "switch" /select the different PWM analogOut pins/leds


'''
Red =16
Green =17
Blue = 18
ledRed = machine.PWM(Red)
ledRed.freq(1000)
ledRed.duty_u16(0)

ledGreen = machine.PWM(Green)
ledGreen.freq(1000)
ledGreen.duty_u16()
ledBlue =machine.PWM(Blue)
ledBlue.freq(1000)
ledBlue.duty_u16()
redBUT = 19
greenBUT =20
blueBUT =21
redButton = machine.Pin(redBUT, machine.Pin.IN, machine.Pin.PULL_UP)
greenButton = machine.Pin(greenBUT,machine.Pin.IN,machine.Pin.PULL_UP)

blueButton = machine.Pin(blueBUT,machine.Pin.IN,machine.Pin.PULL_UP)

newButValRed = 1
oldButValRed = 1
ledStateRed = True

newButValGreen =1
oldButValGreen = 1
ledStateGreen =True

newButValBLue =1
oldButValBlue = 1
ledStateBlue =True




while True:
    newButValRed = redButton.value()
    
    newButValGreen =greenButton.value()
    newButValBlue = blueButton.value()
    
    if (newButValRed == 0) and (oldButValRed == 1):
        if ledStateRed ==True:
            ledRed.duty_u16(65535)
            ledStateRed = False
        else:
            ledRed.duty_u16(0)
            ledStateRed = True
                    
    if(newButValGreen ==0 and oldButValGreen ==1):
        if ledStateGreen ==True:
            ledGreen.duty_u16(15000)
            ledStateGreen =False
        else:
            ledGreen.duty_u16(0)
            ledStateGreen =True
    
    if(newButValBlue == 0 and oldButValBlue ==1):
        if ledStateBlue ==True:
            ledBlue.duty_u16(65535)
            ledStateBlue =False
        else:
            ledBlue.duty_u16(0)
            ledStateBlue =True
                 
     
            
            
    oldButValBlue = newButValBlue       
            
            
    oldButValGreen = newButValGreen            
            
    print(f"Red new value: ",newButValRed,"\n\tRed old value: ",oldButValRed)
    oldButValRed = newButValRed
    utime.sleep(.3)
       