import ServoLib
import rp2
from machine import Pin
import time
myServo1=ServoLib.servoState(0)
myServo2=ServoLib.servoState(1)

while True:  
    for angle in range(1,180,1):
        myServo1.servoAngle(angle)
        myServo2.servoAngle(180-angle)
        print(angle)
    for angle in range(180,1,-1):
        myServo1.servoAngle(angle)
        myServo2.servoAngle(180-angle)
        print(angle)


