'''
first progran is to get the motor running oin PWM
'''
# from machine import PWM,Pin
# import utime

# EnPin1=5
# In1Pin=4
# In2Pin=3
# In3Pin=2
# In4Pin=1
# EnPin2=0
# EnA=PWM(EnPin1)
# EnA.freq(50)
# EnA.duty_u16(5000)
# EnB=PWM(EnPin2)
# EnB.freq(50)
# EnB.duty_u16(0)
# In1=Pin(In1Pin,Pin.OUT)
# In2=Pin(In2Pin,Pin.OUT)
# In1.value(1)
# In2.value(0)
# print(In1.value())
# while True:
#     for i in range(1,200,1):
#         In1.value(1)
#         In2.value(0)
#         EnB.duty_u16(i)
#         utime.sleep(.5)
    
#     In1.value(0)
#     In2.value(0)

from machine import Pin,PWM
import time #importing time for delay  


# Defining motor pins

#OUT1  and OUT2
In1=Pin(3,Pin.OUT) 
In2=Pin(4,Pin.OUT)  
EnB=Pin(5,Pin.OUT)

EnA=PWM(0)
EnA.freq(150)
EnA.duty_u16(5000)
EnB=PWM(5)
EnB.freq(150)
EnB.duty_u16(5000)


#OUT3  and OUT4
In3=Pin(2,Pin.OUT)  
In4=Pin(1,Pin.OUT)  
EN_B=Pin(0)
# Forward
def move_forward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    
# Backward
def move_backward():
    In1.low()
    In2.high()
    In3.low()
    In4.high()
    
#Turn Right
def turn_right():
    In1.low()
    In2.low()
    In3.low()
    In4.high()
    
#Turn Left
def turn_left():
    In1.low()
    In2.high()
    In3.low()
    In4.low()
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
try:    
    while True:
        move_forward()
        print("Forward")
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(1)
        move_backward()
        print("Backward")   
        time.sleep(2)
        stop()
        print("Stop")
        time.sleep(1)
except KeyboardInterrupt:
    print('done')