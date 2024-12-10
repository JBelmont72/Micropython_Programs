from machine import PWM,Pin
from time import sleep

# first sketch asks for Voltage, converts to PWM

outPin1 = 16
#analogOut1 = machine.PWM(outPin1)  these are the same
analogOut1 = PWM(outPin1)
analogOut1.freq(1000)
analogOut1.duty_u16(0)

outPin2 =17
analogOut2=PWM(outPin2)
analogOut2.freq(1000)
analogOut2.duty_u16(0)


while True:
    myVoltage = float(input("Input Output Voltage Please:"))
    pwmVal = myVoltage *(65535/3.3)
    if pwmVal >= 65535:
        pwmVal =65500
    analogOut1.duty_u16(int(pwmVal))
    analogOut2.duty_u16(int(65535-pwmVal))
    
    
                      
                            

