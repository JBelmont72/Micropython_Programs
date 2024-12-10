'''
i am importing my SERVO library which i have on my pico
'''

#from SERVO import *
import SERVO
import time
servoPin =18
myNewServo=SERVO.ServoClass(servoPin)
#myNewServo=ServoClass(servoPin)

while True:
    for deg in range(0,180,1):
        
        myNewServo.enterDegree(deg)
        time.sleep(.02)
    
    for deg in range(180,1,-1): 
        myNewServo.enterDegree(deg)
        time.sleep(.02)

