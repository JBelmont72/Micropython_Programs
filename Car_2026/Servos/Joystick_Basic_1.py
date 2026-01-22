'''
same in micropython_programs/Basic/Joystick_1.py
This program reads the analog values from a joystick connected to the specified ADC pins.
It also reads the digital values from two buttons connected to specified GPIO pins.
The joystick values are scaled to a range of -100 to 100, and small values around zero are set to zero for deadzone handling.
The program prints the button states and joystick values every half second.

from Joystick_Calibrate import JOY_X_PIN, JOY_Y_PIN
Calibration complete!
Values saved:
{'center_y': 30854, 'center_x': 31043, 'min_y': 24, 'max_y': 65535, 'min_x': 31043, 'max_x': 31082}
the pan will be Joy_X_PIN: 9 , the tilt will be Joy_Y_PIN: 6now use these pins in Joystick_Basic_1.py 
the reason is the way i have the joystick wired the X axis is on pin 9 and the Y axis is on pin 6  
full left is 59700,full right is 100
full up is 0 an full down is 65535
neutral y is 30500  =/- 150.  neutral x is 30500 =/- 150
For pan tilt servos we will use the following mapping
X axis (pan):   
    - Full Left (max_x)   -> -100
    - Center (center_x)   -> 0
    - Full Right (min_x)  -> 100    
Y axis (tilt):
    - Full Up (min_y)     -> 100
    - Center (center_y)   -> 0
    - Full Down (max_y)   -> -100   
 for pan center will be 0 degrees, full left -90 degrees, full right +90 degrees
 for tilt center will be 0 degrees, full up +90 degrees, full down -90 degrees 
 for tilt if <= 7 degrees , degrees =7
   
'''

# from machine import Pin,ADC
# from time import sleep
# # JOY_Y_PIN=32
# # JOY_X_PIN=33
# JOY_Y_PIN=9
# JOY_X_PIN=6
# # JOY_Y_PIN=18
# # JOY_X_PIN=17
# yJoy=ADC(JOY_Y_PIN) #Pan
# xJoy=ADC(JOY_X_PIN) #Tilt
# yJoy.atten(ADC.ATTN_11DB)   # Full range: 3.3v
# xJoy.atten(ADC.ATTN_11DB)   # Full range: 3.3v

# black=Pin(36,Pin.IN,Pin.PULL_DOWN)

# green=Pin(35,Pin.IN,Pin.PULL_DOWN)

# try: 
#     while True:
#         blackVal=black.value()
#         greenVal=green.value()
#         print(f'blackVal: {blackVal} , greenVal: {greenVal}')
#         yVal=yJoy.read_u16()
#         xVal=xJoy.read_u16()
#         print(f'yVal: {yVal} , xVal: {xVal}')
#         fx_xVal =(-100/30615)*xVal + 100
#         fx_yVal = (- 0.003053)*yVal +99.9267
 
#         if fx_yVal<= -100:
#             fx_yVal= -100
#         if fx_yVal>+100:
#             fx_yVal=100 
            
           
            
            
            
#         if fx_xVal<7 and fx_xVal > -7 and fx_yVal <7 and fx_yVal >-7:
#             fx_xVal,fx_yVal= 0,0            
#         print(f'fx_yVal: {fx_yVal} , fx_xVal: {fx_xVal}')
#         sleep(.5)
# except KeyboardInterrupt:
#     print('exit')
# finally:
#     print('we are exiting')
    
###############
'''
set up my PROTOTYPE board with an ESP32S3 feather  connected to joystick, and pan and tilt servos
Button on GPIO37 (labelled MI for MISO)

servo1 is PAN  Orange jumpers A0 pin 18
servo2 is TILT Red jumper  A1 pin    17
gray to ground
Joystick.  black  pin 5 SW
           White. pin 6 Y
           Gray.  pin 9 x
           blue GND
           purple 3.3v 
# instantiate servo objects on pins 18 and 17  
servoPinPan=18
servoPinTilt =17
led yellow 36 sck
led red MO. 35
'''
from machine import Pin,ADC,PWM
from time import sleep
import sys
# pins for panPin (attached to x on joystick) and tiltPin attached to y on joystick
panPin=6
tiltPin=9
Pan=ADC(panPin)
Tilt=ADC(tiltPin)
Pan.atten(ADC.ATTN_11DB)   # Full range: 3.3v
Tilt.atten(ADC.ATTN_11DB)   # Full range: 3.3v
# instantiate servo objects on pins 18 and 17  
servoPinPan=18
myServoPan=PWM(Pin(servoPinPan))
myServoPan.freq(50)
servoPinTilt =17
myServoTilt=PWM(Pin(servoPinTilt))
myServoTilt.freq(50)
myServoTilt.duty_u16(3830)
myServoPan.duty_u16(3830)
try: 
    while True:
        ADC_PanVal=Pan.read_u16()
        ADC_TiltVal=Tilt.read_u16()
        print(f'PanVal: {ADC_PanVal} , TiltVal: {ADC_TiltVal}')
        scalePanVal=  -0.003053 * ADC_PanVal + 99.9267
        scaleTiltVal=  0.00264 * ADC_TiltVal - 82.84
        
        # print(f'scalePanVal: {scalePanVal} , scaleTiltVal: {scaleTiltVal}' )
        if scalePanVal > 0 and scalePanVal < 14:
            scalePanVal=6
        pwmPanServo= (-1)*514/20 *scalePanVal  +3830
        myServoPan.duty_u16(int(pwmPanServo))
        if scaleTiltVal < 6:
            scaleTiltVal= 6
        pwmTiltServo= (-1)* 37.777 *scaleTiltVal  +5900
   
            
        myServoTilt.duty_u16(int(pwmTiltServo))
        
        sleep(.05)
except KeyboardInterrupt:
    print('exit')
finally:
    print('we are exiting')
    
    
'''  
# test_adc_pins.py — run in raw REPL on your Feather
from machine import ADC, Pin
import time

candidates = [1,2,3,4,5,6,7,8,9,10,16]  # try a set of likely GPIOs (edit as needed)

def test_pin(gp):
    try:
        a = ADC(Pin(gp))
        a.atten(ADC.ATTN_11DB)
        # read a few samples
        vals = [a.read() if hasattr(a,'read') else a.read_u16() for _ in range(5)]
        print("GPIO", gp, "ok, sample:", vals)
        return True
    except Exception as e:
        print("GPIO", gp, "not ADC or error:", e)
        return False

for p in candidates:
    test_pin(p)
    time.sleep(0.5)

'''

'''
To control a pan servo with your joystick using MicroPython on an ESP32-S3, you'll need to convert your joystick’s `ADC_val` to a corresponding PWM value for the servo. Below is a breakdown of how to implement this logic.

## Scaling the ADC Value
Given your scaling formula, you convert `ADC_val` to a range of -100 to 100:
for Pan:
scale_val = -0.003053 * ADC_val + 99.9267


### PWM Value Calculation
Next, you need to map `scale_val` to the PWM duty cycle values. The duty cycle for a 50 Hz servo control signal varies between 0.5 ms and 2.5 ms as follows:

- When `scale_val = -100`: PWM duty cycle = 0.5 ms
- When `scale_val = 100`: PWM duty cycle = 2.5 ms

### Duty Cycle Conversion
In order to compute the PWM duty cycle based on the `scale_val`, you can use the formula:

1. For the PWM duty cycle (in milliseconds), when `scale_val` is in the range from -100 to 100:

 
   PWM\ms = 0.5 + \frac{(scale\_val + 100)}{200} \times (2.5 - 0.5)
 

In this formula:
- `0.5` is the minimum pulse width (in ms).
- `2.5` is the maximum pulse width (in ms).
- Dividing by `200` scales the value appropriately.

### Example Code
Here’s a simplified example of how to implement this in MicroPython:

'''
# import machine
# import time

# # Constants
# PWM_MIN_MS = 0.5  # Minimum pulse width
# PWM_MAX_MS = 2.5  # Maximum pulse width
# FREQ = 50  # PWM frequency
# ADC_CHANNEL = 9  # Adjust according to your setup for PAN

# # Setup ADC
# adc = machine.ADC(machine.Pin(ADC_CHANNEL))
# adc.atten(machine.ADC.ATTN_11DB)  # Configure ADC to full range

# # Setup PWM on the servo pin
# servo_pin = machine.Pin(18)  # Replace with your actual pin
# pwm = machine.PWM(servo_pin, freq=FREQ)

# # Main loop
# while True:
#     ADC_val = adc.read()  # Assume ADC readings are taken here
#     scale_val = -0.003053 * ADC_val + 99.9267
#     print(f'{scale_val}')
#     # Calculate PWM duty cycle in ms
#     pwm_ms = PWM_MIN_MS + ((scale_val + 100) / 200) * (PWM_MAX_MS - PWM_MIN_MS)
#     duty_cycle = pwm_ms / 20  # Duty cycle for 20 ms period (50 Hz)

#     # Update PWM
#     pwm.duty_u16(int(duty_cycle * 65535))  # Scale duty_cycle to 16-bit value (0-65535)
    
#     time.sleep(0.1)  # Adjust loop frequency as needed


### Key Points:
# - **ADC Configuration**: Ensure you configure the ADC correctly for the required range and accuracy.
# - **PWM**: Make sure to adjust the `servo_pin` and `ADC_CHANNEL` according to your hardware setup.
# - **Updating PWM**: The duty cycle must be converted to a value between 0 and 65535 using appropriate scaling to match the ESP32's PWM resolution.
# - **Loop Control**: The loop has a sleep to avoid overwhelming the processor but can be adjusted based on the requirements.