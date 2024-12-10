'''

'''
from machine import Pin
import time
import _thread
import SERVO
 
servoToggle=False
running = True
servoPin=18
myServo=SERVO.ServoClass(servoPin)
 
redButPin=15
myRedButton=Pin(redButPin,Pin.IN,Pin.PULL_DOWN)
redButStateNow=1
redButStateOld=1
 
def othCore():
    global servoToggle
    global running
    servoState=0
    while running:
        if servoState==0 and servoToggle==True:
            for i in range(0,180,1):
                myServo.enterDegree(i)
                time.sleep(.05)
            servoToggle=False
            servoState=180
        if servoState==180 and servoToggle==True:
            for i in range(180,0,-1):
                myServo.enterDegree(i)
                time.sleep(.05)
            servoToggle=False
            servoState=0
    print("othCore Terminated")
    
_thread.start_new_thread(othCore,())
time.sleep(.25)
                
while True:
    try: 
        redButStateNow=myRedButton.value()
        if redButStateNow==0 and redButStateOld==1:
            print("Toggle")
            servoToggle =True
        redButStateOld=redButStateNow
        time.sleep(.1)
    except KeyboardInterrupt:
        print('Keyboard Interrupt')
        running=False
        time.sleep(.1)
        print("Program is Done")
        _thread.exit()
        break
        
## i like the above modification I made to cleanly exit the program and it worked       
        
'''        
try:
    while True:
        redButStateNow=myRedButton.value()
        if redButStateNow==0 and redButStateOld==1:
            print("Toggle")
            servoToggle =True
        redButStateOld=redButStateNow
        time.sleep(.1)
except KeyboardInterrupt:
    print('Keyboard Interrupt')
    running=False
    time.sleep(.1)
    print("Program is Done")
    _thread.exit()
    break
    
'''