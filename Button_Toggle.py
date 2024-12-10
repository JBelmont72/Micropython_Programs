from machine import Pin
from time import sleep

#basic Button
rPin=16
rLed=Pin(rPin,Pin.OUT)
buttonPin = 15
pushButton = Pin(buttonPin,Pin.IN,Pin.PULL_DOWN)
newButtonVal =1
while True:
    newButtonVal = pushButton.value()
    print("New Button Value:  ",newButtonVal)
    if newButtonVal==1:
        rLed.value(1)
    else:
        rLed.value(0)
    sleep(0.5)

# toggle Button

# buttonPin = 15
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


      
            







