from machine import PWM,Pin
from time import sleep
#import machine

outPin =16
analogOut =machine.PWM(outPin)
outPinYellow =17
analogOutYellow =machine.PWM(outPinYellow)
analogOutYellow.freq(1000)
analogOutYellow.duty_u16(0)
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    myVoltage = float(input("What voltage is desired?"))
    PWM = (65535/3.3)* myVoltage
    analogOut.duty_u16(int(PWM))
    
               
               