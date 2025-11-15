
# from time import sleep
# from machine import PWM, ADC, Pin
# #colorhexa.com
# Red =2
# Green =3
# Blue =4
'''
https://www.youtube.com/watch?v=tCd5PaRR_oA


a very sophisticated response with pattern recognition!!
https://www.youtube.com/watch?v=KqLwsBtJ4t0
another creative solution
https://www.youtube.com/watch?v=b2OqeMuiiAE
https://www.youtube.com/watch?v=8AHNh8e4Be0

https://www.youtube.com/watch?v=YtavbLTpSPM



'''
# PotPin = 28
# potPin = ADC(PotPin)

# analogOutRed = PWM(Red)
# analogOutGreen = PWM(Green)
# analogOutBlue = PWM(Blue)

# analogOutRed.freq(1000)
# analogOutGreen.freq(1000)
# analogOutBlue.freq(1000)

# analogOutRed.duty_u16(0)
# analogOutGreen.duty_u16(0)
# analogOutBlue.duty_u16(0)
# '''
# while True:
#     potVal = potPin.read_u16()
#     print("Pot Value:  ",potVal)
#     analogOutRed.duty_u16(potVal)
#     analogOutBlue.duty_u16(65535-potVal)
#     analogOutGreen.duty_u16(200+potVal)
#     sleep(.5)
# '''

# while True:
#     potVal = potPin.read_u16()
#     exponent=(16/65525)*potVal
#     brightness = 2** exponent
#     analogOutRed.duty_u16(int(brightness))
#     analogOutGreen.duty_u16(int(brightness+1000))
#     analogOutBlue.duty_u16(int(brightness+32217))
#     print(f"potVal: ",brightness,"\n\texponent: ",exponent,"\n\t\tbrightness: ",brightness)
#     sleep(0.5)
'''
while True:
    color = input("What color would you like to see?")
    
    analogOutRed.duty_u16(0)
    analogOutGreen.duty_u16(0)
    analogOutBlue.duty_u16(0)
    
    sleep(0.1)
    if  color == "Red":
        redBright = (65535)
        greenBright = (0)
        blueBright =(0)
        analogOutRed.duty_u16(redBright)
        analogOutGreen.duty_u16(greenBright)
        analogOutBlue.duty_u16(blueBright)
    if color == "Green" :
        
        redBright = (0)
        greenBright = (65535)
        blueBright = (0)
        analogOutRed.duty_u16(redBright)
        analogOutGreen.duty_u16(greenBright)
        analogOutBlue.duty_u16(blueBright)
        
    if color == "Blue" :
        
        redBright = (0)
        greenBright = (0)
        blueBright = (65535)
        analogOutRed.duty_u16(redBright)
        analogOutGreen.duty_u16(greenBright)
        analogOutBlue.duty_u16(blueBright)
    if color == "Cyan" :
       
        redBright = (65535)
        greenBright = (0)
        blueBright = (65535)
        analogOutRed.duty_u16(redBright)
        analogOutGreen.duty_u16(greenBright)
        analogOutBlue.duty_u16(blueBright)
    if color == "Yellow" :
        
        redBright=(65535)
        greenBright = (65535)
        blueBright = (0)
        analogOutRed.duty_u16(redBright)
        analogOutGreen.duty_u16(greenBright)
        analogOutBlue.duty_u16(blueBright)
    if (color == "Magenta" )or (color =="magenta") :
        
        redBright = 65535
        greenBright = 0
        blueBright = 65535
        analogOutRed.duty_u16(redBright)
        analogOutGreen.duty_u16(greenBright)
        analogOutBlue.duty_u16(blueBright)
'''     
'''        
    else:
        analogOutRed.duty_u16(0)
        analogOutGreen.duty_u16(0)
        analogOutBlue.duty_u16(0)
        print(" Please try again")
        
'''
import sys
from machine import PWM,Pin,ADC
from time import sleep
potPin=28
pot=ADC(potPin)
RedPin=2
GreenPin=3
BluePin=4
rLed=PWM(RedPin)
gLed=PWM(GreenPin)
bLed= PWM(BluePin)
rLed.freq(1000)
gLed.freq(1000)
bLed.freq(1000)
rLed.duty_u16(100)
gLed.duty_u16(100)
bLed.duty_u16(100)
def Red(potVal):
    exponent = (16/65535 )*potVal
    brightness =2** exponent
    rLed.duty_u16(int(brightness))
    # print(brightness)
    #  print('potVal:  {potVal}')
    # print('potVal: {:5}'.format(potVal),end='\r')
    print('potVal:    %5d,   brightness:  %5d'  % (potVal, brightness),end='\r')
    sleep(.3)
    
try: 
    while True:
        potVal=pot.read_u16()
            
        Red(int(potVal))   
    

except KeyboardInterrupt:
    rLed.duty_u16(0)
    bLed.duty_u16(0)
    gLed.duty_u16(0)
    print('exiting')
    sys.exit()        
