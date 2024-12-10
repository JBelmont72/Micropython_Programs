'''

'''
# from machine import Pin,PWM
# import time
# import _thread
# def OtherCore(redOn,redOff):
#     while True:
#         rLed.value(1)
#         time.sleep(redOn)
#         rLed.value(0)
#         time.sleep(redOff)
# def GreenBlink(gOn,gOff):
#     while True:
#         gLed.value(1)
#         time.sleep(greenOn)
#         gLed.value(0)
#         time.sleep(greenOff)
    
    
# gPin=16
# rPin=17
# gLed=Pin(gPin,Pin.OUT)
# rLed=Pin(rPin,Pin.OUT)
# redOn=2
# redOff=2
# greenOn=.5
# greenOff = .5
# greenBlinks=10
# redBlinks =2
# _thread.start_new_thread(OtherCore,(redOn,redOff))
# time.sleep(.1)

# GreenBlink(greenOn,greenOff)
#### above is the function for two LEDs, below is adding a servo. THe servo will be on a thread
# import SERVO
# from machine import Pin,PWM
# import time
# import _thread
# gPin=16
# rPin=17
# gLed=Pin(gPin,Pin.OUT)
# rLed=Pin(rPin,Pin.OUT)
# servoPin=18
# gOn=.05
# gOff=.05
# rOn=.05
# rOff=.05
# def LEDS():
#     j=0
#     while j<10:
#         for i in range(0,180,1):
#             gLed.value(1)
#             time.sleep(gOn)
#             gLed.value(0)
#             time.sleep(gOff)
            
#         for i in range(179,-1,-1):
#             rLed.value(1)
#             time.sleep(rOn)
#             rLed.value(0)
#             time.sleep(rOff)
#     j+=1
# def servoFx():
#     import time
#     myServo=SERVO.ServoClass(servoPin)
    
#     j=0
#     while j<10:
#         for deg in range(0,180,1):
#             myServo.enterDegree(deg)
#             time.sleep(.1)
#         j+=1        
#     k=0
#     while j<10:
#         for deg in range(0,180,1):
#             myServo.enterDegree(deg)
#             time.sleep(.1)
#         k+=1
# _thread.start_new_thread(servoFx,())    

# LEDS()
### how to exit thread  https://forums.raspberrypi.com/viewtopic.php?t=366626
# import _thread
# import time

# running  = True
# finished = False

# def my_thread():
#   global finished
#   while running:
#     print('GoodBye')
#   print("New thread is terminating gracefully.")
#   finished = True
    
# _thread.start_new_thread(my_thread, ())

# try:
#   while True:
#     print('Hi')
#     time.sleep(1)
# except KeyboardInterrupt:
#   pass
# finally:
#   running = False
# while not finished:
#   pass
# print("Thread has finished and so will we")


# import SERVO
# from machine import Pin,PWM
# import time
# import _thread
# running =True
# finished =False
# gPin=16
# rPin=17
# gLed=Pin(gPin,Pin.OUT)
# rLed=Pin(rPin,Pin.OUT)
# servoPin=18
# gOn=.05
# gOff=.05
# rOn=.05
# rOff=.05
# def LEDS():
#     j=0
#     while j<1:
#         for i in range(0,180,1):
#             gLed.value(1)
#             time.sleep(gOn)
#             gLed.value(0)
#             time.sleep(gOff)
            
#         for i in range(179,-1,-1):
#             rLed.value(1)
#             time.sleep(rOn)
#             rLed.value(0)
#             time.sleep(rOff)
#     j+=1
# def servoFx():
#     global finished
#     import time
#     myServo=SERVO.ServoClass(servoPin)
    
#     j=0
#     while j<1:
#         for deg in range(0,180,1):
#             myServo.enterDegree(deg)
#             time.sleep(.1)
#         j+=1        
#     k=0
#     while k<1:
#         for deg in range(180,0,-1):
#             myServo.enterDegree(deg)
#             time.sleep(.1)
#         k+=1
#     print('Exiting gracefully')
#     finished =True
# _thread.start_new_thread(servoFx,())    

# # LEDS()
# try:
#   while True:
#     LEDS()
#     time.sleep(.05)
# except KeyboardInterrupt:
#   pass
# finally:
#   running = False
# while not finished:
#   pass
# print("Thread has finished and so will we")

##### Another attempt this time with the leds in thge thread and the servo in main loop

import _thread
from machine import Pin
import time
import SERVO 
sPin=18  
gPin=16
rPin=17
gLed=Pin(gPin,Pin.OUT)
rLed=Pin(rPin,Pin.OUT)
timeOn=.4
timeOff=.4
Led=''
# global Led
global running
running =True
def Leds(timeOn,timeOff,running):
    global Led
    # global running
    while running:
        if Led=='Green':
            gLed.value(1)
            time.sleep(timeOn)
            gLed.value(0)
            time.sleep(timeOff)
            print(timeOff)
        if Led =='Red':
            rLed.value(1)
            time.sleep(timeOn)
            rLed.value(0)
            time.sleep(timeOff) 

    
    print('The myLeds in other core has ended.')
_thread.start_new_thread(Leds,(timeOn,timeOff,running)) 
time.sleep(.25)
myServo=SERVO.ServoClass(sPin)

try:
    while True:
        Led='Green'
        for deg in range(0,180,1):
            myServo.enterDegree(deg)
            time.sleep(.03)
        Led ='Red'
        for deg in range(180,0,-1):
            myServo.enterDegree(deg)
            time.sleep(0.03)
except KeyboardInterrupt:
    running = False
    print("Thread has finished and so will we")
    time.sleep(1)
    gLed.value(0)
    rLed.value(0)
        
        
    print("Program is complete")
    _thread.exit()
    
         

# while True:
#     try:
#         Led='Green'
#         for deg in range(0,180,1):
#             myServo.enterDegree(deg)
#             time.sleep(.03)
#         Led ='Red'
#         for deg in range(180,0,-1):
#             myServo.enterDegree(deg)
#             time.sleep(0.03)
#     except KeyboardInterrupt:
#         running = False
#         print("Thread has finished and so will we")
#         time.sleep(1)
#         gLed.value(0)
#         rLed.value(0)
        
        
#         print("Program is complete")
#         _thread.exit()
        
#         break       
           
# from machine import Pin
# import time
# import _thread
# import SERVO
 
# greenPin=16
# redPin=17
# servoPin=18
 
# LED=""
 
# redLED=Pin(redPin,Pin.OUT)
# greenLED=Pin(greenPin,Pin.OUT)
 
# delOn=.1
# delOff=.1
# myServo=SERVO.ServoClass(servoPin)
# running =True
 
# def othCore(del1,del2):
#     global LED
#     while True:
#         if LED=="RED":
#             redLED.value(1)
#             time.sleep(del1)
#             redLED.value(0)
#             time.sleep(del2)
#         if LED=="GREEN":
#             greenLED.value(1)
#             time.sleep(del1)
#             greenLED.value(0)
#             time.sleep(del2)
# _thread.start_new_thread(othCore,(delOn,delOff))
# time.sleep(.25)
# while True:
#     LED="RED"
#     for i in range(0,180,1):
#         myServo.enterDegree(i)
#         time.sleep(.01)
#     LED="GREEN"
#     for i in range(180,0,-1):
#         myServo.enterDegree(i)
#         time.sleep(.01)
