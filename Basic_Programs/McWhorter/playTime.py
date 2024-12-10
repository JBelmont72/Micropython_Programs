from machine import Pin,PWM,ADC
from time import sleep

potPin = 28     #this is red controlling ADC on pin 28 
pot =ADC(potPin)
potPinBlue = 26
potBlue =ADC(potPinBlue)
potPinGreen = 27
potGreen = ADC(pot)




ledR = 18
ledRed =PWM(ledR)
ledRed.freq(1000)
ledRed.duty_u16(0)

ledG = 17
ledGreen =PWM(ledG)
ledGreen.freq(1000)
ledGreen.duty_u16(0)
ledB = 16
ledBlue =PWM(ledB)
ledBlue.freq(1000)
ledBlue.duty_u16(0)
ledBa = 19
ledBluea =PWM(ledBa)
ledBluea.freq(1000)
ledBluea.duty_u16(0)

while True:
    potVal = pot.read_u16()
    potValGreen = potGreen.read_u16()
    potValBlue = potBlue.read_u16()
    exponentVal = (16/65535) * potVal
    exponentVal = (exponentVal)
    brightness =( 2 ** exponentVal)
    ledRed.duty_u16(int(brightness))
    print(f"Pot Value: ",potVal,"\n\tBrightness: ", brightness,"\n\t\tExponent: ",exponentVal)
    
    exponentValGreen = (16/65535) * potValGreen
    
    brightnessGreen =( 2 ** exponentValGreen)
    ledGreen.duty_u16(int(brightnessGreen))
    print(f"Pot Value Green: ",potValGreen,"\n\tBrightness Green: ", brightnessGreen,"\n\t\tExponent Green: ",exponentValGreen)
    
    exponentValBlue = (16/65535) * potValBlue
    
    brightnessBlue =( 2 ** exponentValBlue)
    ledRed.duty_u16(int(brightnessBlue))
    print(f"Pot Value Blue: ",potValBlue,"\n\tBrightness Blue: ", brightnessBlue,"\n\t\tExponent Blue: ",exponentValBlue)
    sleep(.1)













# potPin =28
# pot = ADC(potPin)

# ledR =16
# ledRed = Pin(ledR,Pin.OUT)
# i =1
# ledRed.value(0)
# for i in range(i,10,1):
#     potVal = pot.read_u16()
#     ledRed.value(1)
#     sleep(1)
#     ledRed.value(0)
#     sleep(.5)
    
#     print(i,"  ",potVal)
    
# from machine import Pin
# from utime import sleep
# led =19
# pin = Pin(led, Pin.OUT)

# print("LED starts flashing...")
# i =1
# for i in range(20):
#     try:
#         pin.toggle()
#         sleep(.4) # sleep 1sec
#     except KeyboardInterrupt:
#         break
# pin.off()
# print("Finished.")
   
    