from PicoAutonomousRobotics import KitronikPicoRobotBuggy
from time import sleep

buggy = KitronikPicoRobotBuggy()
run = False

DegreesPerSecond = (6/5)*360

def ButtonIRQHandler(pin):
    global run
    if(run):
        run = False
    else:
        run = True

buggy.button.irq(trigger=machine.Pin.IRQ_RISING, handler =  ButtonIRQHandler)   

def Forwards():
    buggy.motorOn("l","f",100)
    buggy.motorOn("r","f",100)
        
def Reverse():
    buggy.motorOn("l","r",100)
    buggy.motorOn("r","r",100)

def Stop():
    buggy.motorOff("r") 
    buggy.motorOff("l")

def Spin():
    buggy.motorOn("l","f",80)
    buggy.motorOn("r","r",80)

def TurnRight(HowFar):
    buggy.motorOn("l","f",80)
    buggy.motorOn("r","r",80)  
    sleep(HowFar/DegreesPerSecond)
    Stop()

def TurnLeft(HowFar):
    buggy.motorOn("l","r",80)
    buggy.motorOn("r","f",80)  
    sleep(HowFar/DegreesPerSecond)
    Stop()


while True:
    if(run):
        sleep(5) # wait so wa can get the hand clear after pressing start.
        for x in range (0,4):
            Forwards()
            sleep(0.5)
            TurnLeft (90)
        run = False
    else:
        Stop()
####~~~~~~~~ i coopied the motor control portion from the PicoAutonomous Robot Class
# buttons 0button 20,19,6,7 motors,servoPins = [21,10,17,11],2,3,14,15 HCS04,18 led
# self.buzzer.duty_u16(0) #ensure silence by setting duty to 0
#         #setup LineFollow Pins
#         self.CentreLF = ADC(27)
#         self.LeftLF = ADC(28)
        # self.RightLF = ADC(26)


import array
from machine import Pin, PWM, ADC, time_pulse_us
from rp2 import PIO, StateMachine, asm_pio
from time import sleep, sleep_ms, sleep_us, ticks_us

# List of which StateMachines we have used
usedSM = [False, False, False, False, False, False, False, False]

class KitronikPicoRobotBuggy:
    #button fo user input:
    button = Pin(0,Pin.IN,Pin.PULL_DOWN)

    def __init__(self):
        self._initMotors()

    
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
        
    def motorOn(self,motor, direction, speed, jumpStart=False):
        #cap speed to 0-100%
        if (speed<0):
            speed = 0
        elif (speed>100):
            speed=100
        
        frequency = 100
        if (speed < 15):
            frequency = 20
        elif (speed < 20):
            frequency = 50
            
        
        self.motor1Forward.freq(frequency)
        self.motor1Reverse.freq(frequency)
        self.motor2Forward.freq(frequency)
        self.motor2Reverse.freq(frequency)
        
        # Jump start motor by setting to 100% for 20 ms,
        # then dropping to speed specified.
        # Down to jump start the motor when set at low speed
        if (not jumpStart and speed > 0.1 and speed < 35):
            self.motorOn(motor, direction, 100, True)
            sleep_ms(20)

        #convert 0-100 to 0-65535
        PWMVal = int(speed*655.35)
        if motor == "l":
            if direction == "f":
                self.motor1Forward.duty_u16(PWMVal)
                self.motor1Reverse.duty_u16(0)
            elif direction == "r":
                self.motor1Forward.duty_u16(0)
                self.motor1Reverse.duty_u16(PWMVal)
            else:
                raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
        elif motor == "r":
            if direction == "f":
                self.motor2Forward.duty_u16(PWMVal)
                self.motor2Reverse.duty_u16(0)
            elif direction == "r":
                self.motor2Forward.duty_u16(0)
                self.motor2Reverse.duty_u16(PWMVal)
            else:
                raise Exception("INVALID DIRECTION") #harsh, but at least you'll know
        else:
            raise Exception("INVALID MOTOR") #harsh, but at least you'll know
    #To turn off set the speed to 0...
    def motorOff(self,motor):
        self.motorOn(motor,"f",0)
 