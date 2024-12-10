from machine import PWM,Pin
from time import sleep

outPin = 16
# LED on pin16  always give GPIO pin number
analogOut = PWM (Pin(outPin))	# analogOut is an object of the PWM method
analogOut.freq(1000)	# freq is 1/ period, high freq turning off real fast. period is 1 ms
analogOut.duty_u16(0)	#if set to zero then duty cycle is on zero%
#	closer to zero , the closer to off all the time
#closer to 65,550 the closer to being on all thetime

#led_red = machine.Pin(16,Pin.OUT)


while True:
    myVoltage = float(input("What voltage would you like?"))
    if (myVoltage >= 3.3):
        myVoltage =3.3
    pwmVal = myVoltage * (65550/3.3)
    analogOut.duty_u16(int(pwmVal))
    print(pwmVal)
    #led_red.value(pwmVal)
    
    
    