'''27 March 2025 I used the inverse  log  to create a yellowLed to use a calculated 
inverse of the brightness   2** exponent   and 2**(16-exponent)    
'''


from machine import PWM,Pin,ADC 
from time import sleep
import math
RedLed = 16
YellowLed =17
GreenLed =18

potPin = 28
myPot = machine.ADC(potPin)

redLed = machine.PWM(RedLed)
yellowLed =machine.PWM(YellowLed)
greenLed = machine.PWM(GreenLed)

redLed.freq(1000)
redLed.duty_u16(0)
yellowLed.freq(1000)
yellowLed.duty_u16(0)
greenLed.freq(1000)
greenLed.duty_u16(0)
# 	this takes the pot value which is u16 and puts it directly into the
# duty_u16() which is already u16. thus no conversion necessary.
# The problem is that it is difficult to adjust the brightness since the values of the potVal go up linearly'''
# 	Want to control brightness in steps. 16 steps are convenient since we know that the base is 2 and the exponent is 16 at the top range
# Want to turn the u16 pwmVal to a scale of 16
# y = 2**x  and we want to calculate the x value.

# 1st calculate the slope of the line from (0,0) to 65535,16)
# m = 16 / 65535
# y = (16 /65535) * x
# x is the pwmVal and (Important!) the y is the EXPONENT

# brightness = 2**y   (y is the exponent)
# Now have an exponent value that goes from zero to 16

# now need "brightness" that goes from 0 to 16 by 2**exponent

while True:
    potVal = myPot.read_u16()
    print("The pwm value is:  ",potVal)
    
    exponentVal= (.00026046 * potVal -0.733)
    # exponentVal= int(16/65535* potVal)
    #the exponentVal is the int fo the slope times the potVal
    # easy to see that when the potVal is max at 65535, the exponent is 16.WOW!
    print("Exponential Value:  ",exponentVal,int(exponentVal))
    brightness = int(2 **exponentVal-1) ## subtract the one so lowest value is zero.complely off!
    print('brightness',brightness)
    inverseBrightness=int(2**(16-exponentVal))
    if inverseBrightness <0:
        inverseBrightness=0
    print(brightness, inverseBrightness)
    
    redLed.duty_u16(int(brightness))
    
    yellowLed.duty_u16(int(inverseBrightness))
    sleep(.2)
  
  

# Third case where we take any number of steps and convert to exponential use


# while True:
#     potVal =myPot.read_u16()
#     print("The pwm value is:   ", potVal)
## step one:  get the exponenVal for however many divisions chosen!
    # exponentVal= int(.00026046 * potVal -0.733)
## step two: get the constant tha raised to the division number chosen will give 65535
#     ##exponentVal =((50/65535) * potVal) ## this correlates the exponentVal to the potVal
#  ## step three: the brightness value will be the constant raised to the exponentValue   
# brightness =  (1.24833 ** exponentVal)
#     redLed.duty_u16(int(brightness))
#     print(f"potVal = ",potVal,  "\n\tconstant value: ","1.24833","\n\t\texponentVal: ",exponentVal,"\n\t\t\tbrightness: ",brightness)
#     sleep(1)
                      
                      
# in this case we want the brightness to be equal to a Constant to the expeonentVal
#     65535 = constant to exponent value
#     before we knew that the constant was 2
#     here we don't.  just pick how many steps are desired.
#     65535 = C **50
#     65535 ** (1/50) === (C **50) ** (1/50)
    
    
#     C = 65535**(1/50)    C = 1.24833
#     go back to expVal = (50/65535) *potVal
#     (In reality, this is not just the exponent but also has the potval built into it
    
#     brightness = int(C**exponentVal)
#     brightness = 
    

  