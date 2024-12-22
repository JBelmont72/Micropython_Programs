'''PW-60 control neopixels with joystick
PW_56 basic joystick, calibrated x and y for -100 to +100 each and then used math.atan2 to find arc tangent (in radians) and then angle.
PW_59 will be beginning of using joystic to control the servo

https://www.youtube.com/watch?v=8UCJHY7uTH4&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=60
'''
from machine import ADC,Pin
from time import sleep
import math
import neopixel
xPin=26
yPin=27
xJoy=ADC(Pin(xPin))
yJoy=ADC(Pin(yPin))

pixPin =0
pixSize =8
bright =1
pix=neopixel.NeoPixel(Pin(pixPin),pixSize)
pix.fill((0,255,0))
pix.write()
#### this function  is from lesson 34
def getRGB(deg):
    m=1/60
    if deg>=0 and deg<60:
        R=1
        G=0
        B=m*deg
    if deg>=60 and deg<120:
        R=1-m*(deg-60)
        G=0
        B=1
    if deg>=120 and deg<180:
        R=0
        G=m*(deg-120)
        B=1
    if deg>=180 and deg<240:
        R=0
        G=1
        B=1-m*(deg-180)
    if deg>=240 and deg<300:
        R=m*(deg-240)
        G=1
        B=0
    if deg>=300 and deg<360:
        R=1
        G=1-m*(deg-300)
        B=0
    myColor=(R,G,B)  ## could convert  the 0 to 1 values here by multiplying each by int(255*R) etc
                        ##or do it below
    return myColor



try:
    while True:
        xVal=xJoy.read_u16()
        yVal=yJoy.read_u16()
        # print('xVal: ',xVal,' yVal: ',yVal)
        sleep(.05)
        vCal=int(-0.00306*yVal +100.766)
        hCal= int(0.00306*xVal -100.766)
        magMax =math.sqrt(100**2+100**2)
        mag =math.sqrt(hCal**2 + vCal**2)
        brightness =mag/magMax
        if mag<=2:
            vCal =0  
            hCal=0
            bright =0 ## around zero we want the leds just to be off
            
        print(hCal,'  ',vCal)
        
        angle= math.atan2(vCal,hCal)*180/math.pi
        if angle <0:
            # angle = angle+360   ## this makes the negatives into 180 to 360
            angle = angle*(-1)  
        print('Angle ',angle)
        myColor=getRGB(angle)
        red,green,blue=myColor
        red=(int(red*255))
        green=int(green*255)
        blue=int(blue*255)
        pix.fill((int(red* bright),int(green*bright),int(blue*bright)))  ## note that the neopixels want numbers between 0 and 255,
        ### myColor are numbers between 0 and 1
        pix.write()
        
        
except KeyboardInterrupt:
    print('END')
    