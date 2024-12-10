'''
https://microcontrollerslab.com/micropython-dc-motor-l298n-driver-esp32-esp8266/
'''
# from machine import Pin,PWM
# import time

# # Set up the pins for the motor driver inputs
# input_1 = Pin(1, Pin.OUT)
# input_2 = Pin(2, Pin.OUT)

# # Set the motor direction to forward
# input_1.value(1)
# input_2.value(0)

# ## Set up the PWM output for the motor speed
# #motor_speed = Pin(0, Pin.OUT)
# ## or
# motor_speed= 0
# pwm = PWM(motor_speed)
# pwm.freq(8500)
# # Set the motor speed to 50%
# pwm.duty_u16(50)

# # Wait for 5 seconds
# time.sleep(1)
# # Stop the motor
# input_1.value(0)
# input_2.value(0)
# # pwm.deinit()
# try:
#     while True:
#         PWMVal =int(input('enter a PWM value'))
#         pwm.duty_u16(PWMVal)
#         input_1.value(1)
#         input_2.value(0)
#         time.sleep(1.0)
#         print('PWM value: ',PWMVal)
# except KeyboardInterrupt:
#     pwm.deinit()
#     print('all done')
############
from machine import Pin,PWM,ADC
import time

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
pwm.duty_u16(50)
motor_speedB=5
pwm2 =PWM(motor_speedB)
pwm2.freq(8500)
pwm2.duty_u16(50)


xPin=27
xJoy=ADC(xPin)



# Wait for 1 seconds
time.sleep(1)
# Stop the motor
input_1.value(0)
input_2.value(0)
input_3.value(0)
input_4.value(0)
# pwm.deinit()
try:
    while True:
        
        # PWMVal =int(input('enter a PWM value'))
        
        
        percent =int(input('enter a percent speed 0-100'))
        PWMVal= int(405.35 *percent +25000)
        PWMVal2=PWMVal
        # PWMVal=xJoy.read_u16()
        #### for adding joystick with x axis controlling the speed
        ####taake the above PWM for 0 and 100 percent and plot with joystick linear equation  that as PWM for x axis gives the y being the percent
        # xJoyVal=xJoy.read_u16()
        # xJoyCalc= 0.00152823 * xJoyVal -.152823
        # print('xJoyVal: ',xJoyVal,'     xJoyCalc: ',xJoyCalc)
        
        # PWMVal= int(405.35 * (0.00152823 * xJoyVal -.152823)     +25000)
        
        
        
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
except KeyboardInterrupt:
    print('done')
    PWMVal =0
    pwm.duty_u16(0)
    pwm2.duty_u16(0)
    time.sleep(.1)
    pwm.deinit()
    pwm2.deinit()
    print('all done')
          
        
        
