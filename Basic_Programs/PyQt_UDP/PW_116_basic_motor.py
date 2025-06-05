'''
this is from the Kitronik autonomous vehicle.See if I can get it to run with thke pins from this :
#Motors: controls the motor directions and speed for both motors
    def _initMotors(self):
        self.motor1Forward=PWM(Pin(20))
        self.motor1Reverse=PWM(Pin(19))
        self.motor2Forward=PWM(Pin(6))
        self.motor2Reverse=PWM(Pin(7))
        #set the PWM to 100Hz
        self.motor1Forward.freq(100)
        self.motor1Reverse.freq(100)
        self.motor2Forward.freq(100)
        self.motor2Reverse.freq(100)
        self.motorOff("l")
        self.motorOff("r")
the below code works for the  TA6586 Motor Controller   from the sunfounder kit    
'''
# from machine import Pin,PWM
# import time
# icPin1=Pin(20,Pin.OUT)
# icPin2=Pin(19,Pin.OUT)
# # icPin1=Pin(14,Pin.OUT)
# # icPin2=Pin(15,Pin.OUT)
# fPWM=PWM(icPin1)
# rPWM=PWM(icPin2)
# fPWM.freq(1000)
# rPWM.freq(1000)
# try:
#     while True:
#         for speed in range(20,101,10):
#             rPWM.duty_u16(0)
#             fPWM.duty_u16(int(speed/100*65535))
#             time.sleep(.25)
#         for speed in range(100,-1,-10):
#             rPWM.duty_u16(0)
#             fPWM.duty_u16(int(speed/100*65535))
#             print(int(speed/100*65535))
#             time.sleep(.25)
#         time.sleep(2)
#         for speed in range(20,101,10):
#             fPWM.duty_u16(0)
#             rPWM.duty_u16(int(speed/100*65535))
#             time.sleep(.25)
#         for speed in range(100,-1,-10):
#             fPWM.duty_u16(0)
#             rPWM.duty_u16(int(speed/100*65535))
#             print(int(speed/100*65535))
#             time.sleep(.25)
#         time.sleep(2)
        
        
# except KeyboardInterrupt:
#     print("Program Stopped by User")
#     rPWM.duty_u16(0)
#     fPWM.duty_u16(0)
#     time.sleep(.15)
#     rPWM.deinit()
#     fPWM.deinit()
#     icPin1.off()
#     icPin2.off()
## for two motors. Set up for the autonomous Kitronik vehicle
from machine import Pin,PWM
import time
##left motor
icPin1=Pin(20,Pin.OUT)
icPin2=Pin(19,Pin.OUT)
# icPin1=Pin(14,Pin.OUT)
# icPin2=Pin(15,Pin.OUT)
fPWM=PWM(icPin1)
rPWM=PWM(icPin2)
fPWM.freq(1000)
rPWM.freq(1000)
## right motor
RicPin1=Pin(6,Pin.OUT)
RicPin2=Pin(7,Pin.OUT)
# icPin1=Pin(14,Pin.OUT)
# icPin2=Pin(15,Pin.OUT)
RfPWM=PWM(RicPin1)
RrPWM=PWM(RicPin2)
RfPWM.freq(1000)
RrPWM.freq(1000)
try:
    while True:
        for speed in range(20,101,10):
            rPWM.duty_u16(0)
            fPWM.duty_u16(int(speed/100*65535))
            RrPWM.duty_u16(0)
            RfPWM.duty_u16(int(speed/100*65535))
            time.sleep(.25)
        for speed in range(100,-1,-10):
            rPWM.duty_u16(0)
            fPWM.duty_u16(int(speed/100*65535))
            RrPWM.duty_u16(0)
            RfPWM.duty_u16(int(speed/100*65535))
            print(int(speed/100*65535))
            time.sleep(.25)
        time.sleep(2)
        for speed in range(20,101,10):
            fPWM.duty_u16(0)
            rPWM.duty_u16(int(speed/100*65535))
            RfPWM.duty_u16(0)
            RrPWM.duty_u16(int(speed/100*65535))
            time.sleep(.25)
        for speed in range(100,-1,-10):
            fPWM.duty_u16(0)
            rPWM.duty_u16(int(speed/100*65535))
            RfPWM.duty_u16(0)
            RrPWM.duty_u16(int(speed/100*65535))
            print(int(speed/100*65535))
            time.sleep(.25)
        time.sleep(2)
        
        
except KeyboardInterrupt:
    print("Program Stopped by User")
    rPWM.duty_u16(0)
    fPWM.duty_u16(0)
    RrPWM.duty_u16(0)
    RfPWM.duty_u16(0)
    time.sleep(.15)
    rPWM.deinit()
    fPWM.deinit()
    RrPWM.deinit()
    RfPWM.deinit()
    icPin1.off()
    icPin2.off()
    RicPin1.off()
    RicPin2.off()