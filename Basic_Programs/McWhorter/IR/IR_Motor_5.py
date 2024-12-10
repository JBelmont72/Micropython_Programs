'''
https://microcontrollerslab.com/micropython-dc-motor-l298n-driver-esp32-esp8266/
'''
from machine import Pin,PWM,ADC     ##need freq  ?
import time
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

# Set up the pins for the motor driver inputs
input_1 = Pin(1, Pin.OUT)
input_2 = Pin(2, Pin.OUT)
input_3 = Pin(3, Pin.OUT)
input_4 = Pin(4, Pin.OUT)

# Set the motor direction to forward
input_1.value(1)
input_2.value(0)
input_3.value(1)
input_4.value(0)

## Set up the PWM output for the motor speed
#motor_speed = Pin(0, Pin.OUT)
## or
motor_speedA= 0
pwm = PWM(motor_speedA)
pwm.freq(8500)
# Set the motor speed to 50%
pwm.duty_u16(0)
motor_speedB=5
pwm2 =PWM(motor_speedB)
pwm2.freq(8500)
pwm2.duty_u16(0)
xPin=27
xJoy=ADC(xPin)
# Wait for 1 seconds
time.sleep(1)
# Stop the motor
input_1.value(0)
input_2.value(0)
input_3.value(0)
input_4.value(0)

IRdict ={69 : 'POWER', 70: 'MODE',71 : 'OFF',
         68: 'PLAY', 64 : 'BACK', 67 : 'FORWARD', 7: 'ENTER', 21: '-',
         9 : '+', 22 : 0,25 : 'LOOP', 13:'USD' ,
         12: 1, 24 : 2,94 : 3,
        8 :4, 28 : 5, 90 : 6,
        66 : 7, 82 : 8, 74 : 9}
newCommand=[]
beginRecord=False
cmdReady=False
angleString=''      ## this will be speed
newBit=""
irPin=16
myIR = Pin(irPin, Pin.IN)
def boost(PWMVal):
    PWMVal =40000
    time.sleep(1)
    print('Boost')
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
count=0 
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
            # myServo.enterDegree(angleStringINT)
            print(newCommand)
            # cmdReady=False
        # PWMVal =int(input('enter a PWM value'))
        
        
            # percent =int(input('enter a percent speed 0-100'))
            PWMVal= int(405.35 *angleStringINT +25000)
            if PWMVal < 40000 and count ==0:
                boost(PWMVal)
                count+=1
            
            
            # PWMVal=xJoy.read_u16()
            #### for adding joystick with x axis controlling the speed
            ####taake the above PWM for 0 and 100 percent and plot with joystick linear equation  that as PWM for x axis gives the y being the percent
            # xJoyVal=xJoy.read_u16()
            # xJoyCalc= 0.00152823 * xJoyVal -.152823
            # print('xJoyVal: ',xJoyVal,'     xJoyCalc: ',xJoyCalc)
            
            # PWMVal= int(405.35 * (0.00152823 * xJoyVal -.152823)     +25000)
            PWMVal2=PWMVal
            
            time.sleep(.25)
            print(PWMVal)
            # pwm2.duty_u16(PWMVal)
            pwm.duty_u16(PWMVal)
            pwm2.duty_u16(PWMVal2)
            input_3.value(0)
            input_4.value(1)
            input_1.value(1)
            input_2.value(0)
            # input_3.value(0)
            # input_4.value(1)
            time.sleep(1.0)
            print('PWM value: ',PWMVal)
            cmdReady=False
except KeyboardInterrupt:
    print('done')
    PWMVal =0
    pwm.duty_u16(0)
    pwm2.duty_u16(0)
    time.sleep(.1)
    pwm.deinit()
    pwm2.deinit()
    print('all done')
 