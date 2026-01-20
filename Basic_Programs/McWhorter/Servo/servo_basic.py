'''

'''
# from time import sleep
# from machine import Pin, PWM

# pwm = PWM(Pin(16))
# pwm.freq(50)

# while True:
#     for position in range(1000,9000,50):
#         pwm.duty_u16(position)
#         print(position)
#         sleep(0.01)
#     for position in range(9000,1000,-50):
#         pwm.duty_u16(position)
#         sleep(0.01)

# create a servo class to control a servo motor for ESP32S3 using pin number 8, frequency 1000, and 4095 resoluttion

# import sys
# from time import sleep

# class Servo:
#     def __init__(self, pinNum, freq=50, dutyRes=65535):
#         from machine import Pin, PWM
#         self.pinNumber = pinNum
#         self.frequency = freq
#         self.dutyResolution = dutyRes
#         self.pwmObject = PWM(Pin(self.pinNumber))
#         self.pwmObject.freq(self.frequency)

#     def setAngle(self, angle):
#         minDuty = int(self.dutyResolution * 0.025)  # 0 degrees
#         maxDuty = int(self.dutyResolution * 0.125)  # 180 degrees
#         dutySpan = maxDuty - minDuty
#         duty = int(minDuty + (dutySpan * angle / 180))
#         self.pwmObject.duty_u16(duty)   
#         print(f'Servo on pin {self.pinNumber} set to angle {angle} with duty {duty}')   
# try: 
#     while True:
#         myServo = Servo(8)
#         for angle in range(0, 181, 10):
#             myServo.setAngle(angle)
#             from time import sleep
#             sleep(0.5)
#         for angle in range(180, -1, -10):
#             myServo.setAngle(angle)
#             sleep(0.5)  
            
# except KeyboardInterrupt:
#     print('Program stopped by user')
#     sys.exit()


# get user input for PWMValue between 0 and 65535 and set the PWM duty cycle accordingly
import sys
from time import sleep
from machine import Pin, PWM    
servoPin=8
myServo=PWM(Pin(servoPin))
myServo.freq(1000)
try:
    while True:
        pwmInput=input('Enter PWM value between 0 and 65535 or q to quit: ')
        if pwmInput.lower()=='q':
            print('Exiting program')
            sys.exit()
        pwmValue=int(pwmInput)
        if 0 <= pwmValue <= 65535:
            myServo.duty_u16(pwmValue)
            print(f'Servo on pin {servoPin} set to PWM value {pwmValue}')
        else:
            print('Invalid input. Please enter a value between 0 and 65535.')
except KeyboardInterrupt:
    print('Program stopped by user')
    sys.exit()  