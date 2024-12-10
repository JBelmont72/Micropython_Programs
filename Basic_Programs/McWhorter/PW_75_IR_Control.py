'''  '''
### SERVO library
# class servo:
#     def __init__(self,sPin):
#         import machine
#         self.servoPin=sPin
#         self.obj=machine.PWM(machine.Pin(self.servoPin))
#         self.obj.freq(50)
    
#     def pos(self,angle):
#         writeVal=6553/180*angle+1638
#         self.obj.duty_u16(int(writeVal))
###### below is convert HSV to RGB library
# def getRGB(deg):
#     m=1/60
#     if deg>=0 and deg<60:
#         R=1
#         G=0
#         B=m*deg
#     if deg>=60 and deg<120:
#         R=1-m*(deg-60)
#         G=0
#         B=1
#     if deg>=120 and deg<180:
#         R=0
#         G=m*(deg-120)
#         B=1
#     if deg>=180 and deg<240:
#         R=0
#         G=1
#         B=1-m*(deg-180)
#     if deg>=240 and deg<300:
#         R=m*(deg-240)
#         G=1
#         B=0
#     if deg>=300 and deg<360:
#         R=1
#         G=1-m*(deg-300)
#         B=0
#     myColor=(R,G,B)
#     return myColor


# import SERVO
# import time
# from machine import Pin, freq,PWM
# from ir_rx.print_error import print_error
# from ir_rx.nec import NEC_8
# IRdict ={69 : 'POWER', 70: 'MODE',71 : 'OFF',
#          68: 'PLAY', 64 : 'BACK', 67 : 'FORWARD', 7: 'ENTER', 21: '-',
#          9 : '+', 22 : 0,25 : 'LOOP', 13:'USD' ,
#          12: 1, 24 : 2,94 : 3,
#         8 :4, 28 : 5, 90 : 6,
#         66 : 7, 82 : 8, 74 : 9}
# newCommand=[]
# beginRecord=False
# cmdReady=False
# angleString=''
# newBit=""
# irPin=16
# sPin=18
# # myServo=PWM(sPin,Pin.OUT)
# # myServo.freq(50)

# myIR = Pin(irPin, Pin.IN)
# def callback(IRbit, addr, ctrl):
#     global newCommand
#     global beginRecord
#     global cmdReady
#     global IRdict
#     if IRbit==69:
#         beginRecord=True
#         newCommand=[]
#         cmdReady=False
#     if beginRecord==True and IRbit!=-1:
#         newCommand.append(IRdict[IRbit])
#     if IRbit==7:
#         cmdReady=True
 
# IR = NEC_8(myIR, callback)  # Instantiate receiver
 
# try:
#     while True:
#         if cmdReady==True:
#             print(newCommand)
#             cmdReady=False
# except KeyboardInterrupt:
#     IR.close()
# print("Program Terminated")

###########
import SERVO
import time
from machine import Pin, freq,PWM
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8
IRdict ={69 : 'POWER', 70: 'MODE',71 : 'OFF',
         68: 'PLAY', 64 : 'BACK', 67 : 'FORWARD', 7: 'ENTER', 21: '-',
         9 : '+', 22 : 0,25 : 'LOOP', 13:'USD' ,
         12: 1, 24 : 2,94 : 3,
        8 :4, 28 : 5, 90 : 6,
        66 : 7, 82 : 8, 74 : 9}
newCommand=[]
beginRecord=False
cmdReady=False
angleString=''
newBit=""
irPin=16
sPin=18
myServo=PWM(Pin(sPin))
myServo.freq(50)
myServo.duty_u16(5000)
myIR = Pin(irPin, Pin.IN)
myServo=SERVO.ServoClass(sPin)
def callback(IRbit, addr, ctrl):
    global newCommand
    global beginRecord
    global cmdReady
    global IRdict
    if IRbit==69:
        beginRecord=True
        newCommand=[]
        cmdReady=False
    if beginRecord==True and IRbit!=-1:
        newCommand.append(IRdict[IRbit])
    if IRbit==7:
        cmdReady=True
 
IR = NEC_8(myIR, callback)  # Instantiate receiver
 
try:
    while True:
        if cmdReady==True:
            angleString=''
            print(newCommand)
            for i in newCommand:
                if i != 'POWER'  and i != 'ENTER':
                    angleString=angleString+ str(i)
            angleStringINT= int(angleString)
            print(angleString)
            myServo.enterDegree(angleStringINT)\
            print(newCommand)
            cmdReady=False
except KeyboardInterrupt:
    IR.close()
    print("Program Terminated")