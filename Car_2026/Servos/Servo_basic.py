'''
12 Jan 2026 I used this to test the servo operation and will use the code to create functions for pan tilt servos   
the tilt servo is on pin 18 and pan servo is on pin 23. Adjust tilt between 2500 and 6800 for up and down with 2500 being 90 degrees and 5800 being flat forward  zero degrees elevation.

'''


# get user input for PWMValue between 0 and 65535 and set the PWM duty cycle accordingly 2500 straight up 6800 down,5800 forward
'''
import sys
from time import sleep
from machine import Pin, PWM    
servoPin=18
#servoPin=8
myServo=PWM(Pin(servoPin))
myServo.freq(50)
try:
    while True:
        pwmInput=input('Enter PWM value between 0 and 65535 or q to quit: ')
        if pwmInput.lower()=='q':
            print('Exiting program')
 #           sys.exit()
        pwmValue=int(pwmInput)
        if 0 <= pwmValue <= 65535:
            myServo.duty_u16(pwmValue)
            print(f'Servo on pin {servoPin} set to PWM value {pwmValue}')
        
        else:
            print('Invalid input. Please enter a value between 0 and 65535.')
except KeyboardInterrupt:
    print('Program stopped by user')
    
'''

# import sys
# from time import sleep
# from machine import Pin, PWM    
# servoPin=18
# #servoPin=8
# myServo=PWM(Pin(servoPin))
# myServo.freq(50)
# servoPinTilt =18
# myServoTilt=PWM(Pin(servoPinTilt))
# myServoTilt.freq(50)
# try:
#     while True:
#         pwmInput=input('Enter PWM value between 0 and 65535 or q to quit: ')
#         pwmInputTilt=input('Enter PWM Tilt value between 2500 and 6800 or q to quit:')
#         if pwmInput.lower()=='q':
#             print('Exiting program')
#  #           sys.exit()
#         pwmValue=int(pwmInput)
#         pwmValueTilt = int(pwmInputTilt)
#         if 0 <= pwmValue <= 65535:
#             myServo.duty_u16(pwmValue)
#             print(f'Servo on pin {servoPin} set to PWM value {pwmValue}')
#         if 2500 <= pwmValueTilt <=6800:
#             myServoTilt.duty_u16(pwmValueTilt)
#             print(f'Servo Tilt  on pin {servoPin} set to PWM value {pwmValueTilt}')
#         else:
#             print('Invalid input. Please enter a value between 0 and 65535.')
# except KeyboardInterrupt:
#     print('Program stopped by user')
#     sys.exit()
'''   
# call library and test servo movement   
import SERVO
import time

servoPin=12
blueServo=SERVO.servo(servoPin)
print(f"Controlling servo on GPIO pin: {servoPin}")

while True:
    for i in range(180):
        print(f"Moving to angle: {i}")
        blueServo.pos(i)
        time.sleep(.01)
    for i in range(180,0,-1):
        print(f"Moving to angle: {i}")
        blueServo.pos(i)
        time.sleep(.01)
'''



import sys
from time import sleep
from machine import Pin, PWM    
servoPin=18
#servoPin=8
myServo=PWM(Pin(servoPin))
myServo.freq(50)
servoPinTilt =17
myServoTilt=PWM(Pin(servoPinTilt))
myServoTilt.freq(50)
try:
    while True:
        # pwmInput=input('Enter PWM value between 0 and 65535 or q to quit: ')
        pwmInputTilt=input('Enter PWM Tilt value between 2500 and 6800 or q to quit:')
        if pwmInputTilt.lower()=='q':
            print('Exiting program')
 #           sys.exit()
        # pwmValue=int(pwmInput)
        pwmValueTilt = int(pwmInputTilt)
        # if 0 <= pwmValue <= 65535:
        #     myServo.duty_u16(pwmValue)
        #     print(f'Servo on pin {servoPin} set to PWM value {pwmValue}')
        if 1000 <= pwmValueTilt <=7800:
            myServoTilt.duty_u16(pwmValueTilt)
            print(f'Servo Tilt  on pin {servoPin} set to PWM value {pwmValueTilt}')
        else:
            print('Invalid input. Please enter a value between 0 and 65535.')
except KeyboardInterrupt:
    print('Program stopped by user')
    sys.exit()