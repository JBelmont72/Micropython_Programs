from machine import Pin,PWM
from  time import sleep
import machine
ledRed =16
ledGreen=17
ledBlue = 18
ledYellow =20


Red = machine.PWM(ledRed)
Green = machine.PWM(ledGreen)
Blue = machine.PWM(ledBlue)
Yellow = machine.PWM(ledYellow)
Red.freq(1000)
Green.freq(1000)
Blue.freq(1000)
Yellow.freq(1000)
Red.duty_u16(0)
Green.duty_u16(0)
Blue.duty_u16(65535)
Yellow.duty_u16(0)

colorArray = []

while True:
    numColors=int(input("How many Colors do you want?"))
    flash = int(input("How many times to blink?"))
    for i in range (0,numColors,1):
        myColor = input("What color do you want to add?")
        myColor = myColor.lower()
        colorArray.append(myColor)
    while True:
        for color in colorArray:
            if color == 'red':                
                redBright =65535
                greenBright = 0
                blueBright = 0
                Red.duty_u16(redBright)
                Green.duty_u16(greenBright)
                Blue.duty_u16(blueBright)                
            if color == 'blue':                
                
                redBright =0
                greenBright = 0
                blueBright = 65535
                Red.duty_u16(redBright)
                Green.duty_u16(greenBright)
                Blue.duty_u16(blueBright)
                sleep(.5)     
            
                
        




    
    

'''
Colors =[]
while True:
    numColors=int(input("How many Colors do you want?"))
    flash = int(input("How many times to blink?"))
    for i in range (0,numColors,1):
    
        Color =input("Which Colors do you want to add?")
        Colors.append(Color)
        print(Colors)
        
        if (Colors[i] == red or Color[i] == Red):
            on = 1
            off = 0
            
        for j in range(0,flash,1):
            Colors[j]                
                        
  '''              
                
    
    
    
                    

