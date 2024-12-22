'''
PW_56 basic joystick, calibrated x and y for -100 to +100 each and then used math.atan2 to find arc tangent (in radians) and then angle.
PW_59 will be beginning of using joystic to control the servo
'''
from machine import ADC,Pin
from time import sleep
import math
xPin=26
yPin=27
xJoy=ADC(Pin(xPin))
yJoy=ADC(Pin(yPin))
try:
    while True:
        xVal=xJoy.read_u16()
        yVal=yJoy.read_u16()
        # print('xVal: ',xVal,' yVal: ',yVal)
        sleep(.05)
        vCal=int(-0.00306*yVal +100.766)
        hCal= int(0.00306*xVal -100.766)
        mag =math.sqrt(hCal**2 + vCal**2)
        if mag<=2:
            vCal =0  
            hCal=0
        print(hCal,'  ',vCal)
        angle= math.atan2(vCal,hCal)*180/math.pi
        if angle <0:
            # angle = angle+360   ## this makes the negatives into 180 to 360
            angle = angle*(-1)  
        print('Angle ',angle)
        
        
except KeyboardInterrupt:
    print('END')
    