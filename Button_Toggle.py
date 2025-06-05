from machine import Pin
from time import sleep

# #basic Button
# rPin=16
# rLed=Pin(rPin,Pin.OUT)
# buttonPin = 20
# pushButton = Pin(buttonPin,Pin.IN,Pin.PULL_DOWN)
# newButtonVal =1
# while True:
#     newButtonVal = pushButton.value()
#     print("New Button Value:  ",newButtonVal)
#     if newButtonVal==1:
#         rLed.value(1)
#     else:
#         rLed.value(0)
#     sleep(0.5)

# toggle Button

# buttonPin = 20
# pushButton = Pin(buttonPin,Pin.IN,Pin.PULL_UP)
# newButtonVal = 1
# oldButtonVal = 1
# buttonState = False


# while True:
#     newButtonVal = pushButton.value()
#     print(newButtonVal, oldButtonVal)
#     sleep(.4)
    
#     if( newButtonVal == 0 and oldButtonVal == 1):
#         if (buttonState == False):
#             print("Button State is False and Button is: ", newButtonVal)
            
#             print(buttonState)
#             buttonState = True
            
            
#         elif (buttonState == True):
#             print("Button State is True and Button is: ", newButtonVal)
#             print(buttonState)
            
#             buttonState = False
#     oldButtonVal = newButtonVal    
#     #buttonState != buttonState
#     print("ButtonState is:  ",buttonState)

bPin =15 # tried with 10,19,20,18,22
pushButton = Pin(bPin, Pin.IN, Pin.PULL_DOWN)#tried with PULL_UP and PULL_DOWN
# # pushButton = Pin(bPin, Pin.IN, Pin.PULL_UP) #tried with PULL_UP and PULL_DOWN
# while True:
#     butVal = pushButton.value()
#     print("Button Value: ", butVal)
 
#     sleep(0.5)
newButtonVal = 1
oldButtonVal = 1
buttonState = False
buttonState2 = False
buttonState3 = False
while True:
    newButtonVal = pushButton.value()
    print(newButtonVal, oldButtonVal)
    sleep(0.5)
    if newButtonVal == 1 and oldButtonVal == 0:
        print("Button Pressed",buttonState, buttonState2, buttonState3)
    
        if not buttonState and not buttonState2 and not buttonState3:
            print("Button State is False and Button is: ", newButtonVal)
            buttonState = True
        if buttonState and not buttonState2 and not buttonState3:
            print("Button State is True and Button is: ", newButtonVal)
            buttonState = False
            buttonState2 = True
        elif not buttonState and buttonState2 and not buttonState3:
            print("Second Toggle Activated")
            buttonState2 = False
            buttonState3 = True
        elif not buttonState and not buttonState2 and buttonState3:
            print("Third Toggle Activated")
            buttonState3 = False
    oldButtonVal =newButtonVal    # elif buttonState and not buttonState2 and not buttonState3:
    







