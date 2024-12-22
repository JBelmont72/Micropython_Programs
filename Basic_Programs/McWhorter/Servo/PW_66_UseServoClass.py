'''
PW 66  create library
'''
import SERVO
import time

servoPin=16
blueServo=SERVO.servo(servoPin)
while True:
    for i in range(180):
        blueServo.pos(i)
        time.sleep(.01)
    for i in range(180,0,-1):
        blueServo.pos(i)
        time.sleep(.01)
        