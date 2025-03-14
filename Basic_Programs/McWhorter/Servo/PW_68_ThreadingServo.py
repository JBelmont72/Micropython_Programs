'''

'''
from machine import Pin
import time
import _thread
import SERVO
 
greenPin=14
redPin=15
servoPin=17
 
LED=""
 
redLED=Pin(redPin,Pin.OUT)
greenLED=Pin(greenPin,Pin.OUT)
 
delOn=.1
delOff=.1
myServo=SERVO.servo(servoPin)
running =True
 
def othCore(del1,del2):
    global LED
    while True:
        if LED=="RED":
            redLED.value(1)
            time.sleep(del1)
            redLED.value(0)
            time.sleep(del2)
        if LED=="GREEN":
            greenLED.value(1)
            time.sleep(del1)
            greenLED.value(0)
            time.sleep(del2)
_thread.start_new_thread(othCore,(delOn,delOff))
time.sleep(.25)
while True:
    LED="RED"
    for i in range(0,180,1):
        myServo.pos(i)
        time.sleep(.01)
    LED="GREEN"
    for i in range(180,0,-1):
        myServo.pos(i)
        time.sleep(.01)