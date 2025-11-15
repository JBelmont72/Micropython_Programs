
'''
the last program combines PW s lesson 11 using potval, exponents based on 2**16 and exponent with 50 steps. 1.2483 =c. c**50=65535
/Users/judsonbelmont/Documents/SharedFolders/Pico/Micropython_Programs/Basic_Programs/McWhorter/Pot_ADC_1.py

'''

# import machine 
# import utime
# potPin = 28
# myPot= machine.ADC(potPin)
# RedLed = 16
# YellowLed =17
# GreenLed =18
# redLed = machine.Pin(RedLed,machine.Pin.OUT)
# yellowLed = machine.Pin(YellowLed,machine.Pin.OUT)
# greenLed = machine.Pin(GreenLed,machine.Pin.OUT)

# #set up potentiometer on ADC GPIO 28
# while True:
#     potVal = myPot.read_u16()
#     print(potVal)
#     voltage = (3.3/65535)*potVal
#     print("The voltage is eqaul to:  ",voltage)
#     percent=(100/65535)*potVal
#     print("Percent of PotVal is:  ",percent)
#     utime.sleep(.5)
#     if (percent < 70):
#         redLed.value(1)
#         yellowLed.value(0)
#         greenLed.value(0)

    
#     elif (percent >= 70 and percent <= 80):
#         redLed.value(0)
#         yellowLed.value(1)
#         greenLed.value(0)
#     elif (percent >80):
#         redLed.value(0)
#         yellowLed.value(0)
#         greenLed.value(1)


# led_external=machine.Pin(17,machine.Pin.OUT)
# button=machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)

# while True:
#     if button.value() ==1:
#         led_external.value(1)
#         x=button.value()
#         print("x")
#         utime.sleep(1)
#     led_external.value(0)
#     y = button.value()
#     print("Value =  ", y)
#.    utime.sleep(.5)

'''   
import machine
import utime as time
potPin = 28
myPot= machine.ADC(potPin)
RedLed = 16
YellowLed =17
GreenLed =18
redLed=machine.PWM(RedLed)
redLed.freq(1000)
redLed.duty_u16(0)
redLed = machine.Pin(RedLed,machine.Pin.OUT)
yellowLed = machine.Pin(YellowLed,machine.Pin.OUT)
greenLed = machine.Pin(GreenLed,machine.Pin.OUT)

try: 
    while True:
        potVal=myPot.read_u16()
        voltage = potVal*3.3/65535
        print(potVal,voltage)
        # exp=16*potVal/65535
        brightness =1.248**(50*potVal/65535)
        print(brightness,(50*potVal/65535))
        # brightness =2**exp
        redLed.duty_u16(int(brightness))
        
        
        time.sleep(.4)
except KeyboardInterrupt:
    redLed.duty_u16(0)
    # greenLed.duty_u16(0)
    # yellowLed.duty_16(0) 
    print('Good-bye')       
'''
from machine import Pin, ADC,PWM
import time
import sys 


butPin =15
But=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
ledPin=16
potPin= 28
Pot=ADC(potPin)
led=PWM(ledPin)
led.freq(1000)
led.duty_u16(100) 
led2pin=17
led2=PWM(led2pin)
led2.freq(1000)
led2.duty_u16(600)
led3pin=18
led3 = PWM(led3pin)
led3.freq(1000)
led3.duty_u16(1200)
try:
    while True:
        potVal=Pot.read_u16()
        potVal=potVal-50
        led.duty_u16(potVal)
        time.sleep(.5)
        
        
        ## to convert to using an exponenet:  base**16 =65535. here base =2
        exp=(16/65525)*potVal
        brightness=int(2**((16/65525)*potVal))
        led2.duty_u16(brightness)
        
        print(f'For 16 steps:  potval: {potVal} , exp {exp}, brightness {brightness}')
        ## To convert to 50 steps. base**50=65535
        # c **50 =65535. == c**(50*(1/50))  =65535 ** (1/50) = 1.2483
        baseTimeExp50= 1.2483 ** ((50/65535)*potVal)# can see that potVal is max gives exponent = 50
        led3.duty_u16(int(baseTimeExp50))
        print(f'For 50 steps:  potval: {potVal} , exp {(50/65535)*potVal}, brightness {baseTimeExp50})')
        
except KeyboardInterrupt:
    led.duty_u16(0)
    led2.duty_u16(0)
    print('exiting')
    sys.exit()

#   ####~~~~~~
# from machine import PWM,Pin
# from time import sleep

# # first sketch asks for Voltage, converts to PWM

# outPin1 = 16
# #analogOut1 = machine.PWM(outPin1)  these are the same
# analogOut1 = PWM(outPin1)
# analogOut1.freq(1000)
# analogOut1.duty_u16(0)

# outPin2 =17
# analogOut2=PWM(outPin2)
# analogOut2.freq(1000)
# analogOut2.duty_u16(0)


# while True:
#     myVoltage = float(input("Input Output Voltage Please:"))
#     pwmVal = myVoltage *(65535/3.3)
#     if pwmVal >= 65535:
#         pwmVal =65500
#     analogOut1.duty_u16(int(pwmVal))
#     analogOut2.duty_u16(int(65535-pwmVal))
    