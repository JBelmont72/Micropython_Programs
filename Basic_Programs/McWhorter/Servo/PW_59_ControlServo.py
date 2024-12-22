'''
remmber that the period for the servo is 20 msec, the freq therefore is 50 (1/period = freq)
o degrees is 1638 which is 0.5 ms/20 msec X 65535 and for 180 degrees is  2.5 msec/20 msec * 65535
thus,  pwn for the servo for a specific angle is=   int(6553/180*angle+1638)
'''

from machine import ADC,Pin,PWM
from time import sleep
import math
xPin=26
yPin=27
xJoy=ADC(Pin(xPin))
yJoy=ADC(Pin(yPin))
servoPin=16
myServo1=PWM(Pin(servoPin))
myServo1.freq(50)
myServo1.duty_u16()
try:
    while True:
        xVal=xJoy.read_u16()
        yVal=yJoy.read_u16()
        # print('xVal: ',xVal,' yVal: ',yVal)

        vCal=int(-0.00306*yVal +100.766)
        hCal= int(0.00306*xVal -100.766)
        mag =math.sqrt(hCal**2 + vCal**2)
        myServo1.duty_u16()
        if mag<=10:
            vCal =0  
            hCal=0
        print(hCal,'  ',vCal)
        angle= math.atan2(vCal,hCal)*180/math.pi
        if angle <0:
            # angle = angle+360   ## this makes the negatives into 180 to 360
            angle = angle*(-1)  
        print('Angle ',angle)
        myServo1.duty_u16(int(6553/180*angle+1638))
        sleep(.2)
except KeyboardInterrupt:
    print('END')