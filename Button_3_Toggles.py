


from machine import Pin
from time import sleep

#basic Button

'''
buttonPin = 15
pushButton = Pin(buttonPin,Pin.IN,Pin.PULL_UP)
newButtonVal =1
while True:
    newButtonVal = pushButton.value()
    print("New Button Value:  ",newButtonVal)
    sleep(0.5)
    '''
# toggle Button

buttonPin = 15
pushButton = Pin(buttonPin,Pin.IN,Pin.PULL_DOWN)
# newButtonVal = 1
oldButtonVal = 0
buttonState = False


# to add a third toggle

buttonState3 =False

while True:
    newButtonVal = pushButton.value()
    print(newButtonVal, oldButtonVal)
    sleep(1)
    
    if( newButtonVal == 1 and oldButtonVal == 0):
        if buttonState3 == False:
    
            if buttonState == False and buttonState3 == False:
                print("Button State is False and Button is: ", newButtonVal)
                print(" #1 ",buttonState3)
                print(buttonState)
                buttonState = True
                buttonState3 =True
            
            
            elif (buttonState == True and buttonState3 ==False):
                print("Button State is True and Button is:  #2", newButtonVal)
                print(buttonState)
                buttonState = False
                buttonState3 = True
       
        elif buttonState3 ==True:
            print("The button state is the third option. #3")
            buttonState3 = False
                  
    
    oldButtonVal = newButtonVal    
    #buttonState != buttonState
    print("ButtonState is:  ",buttonState)
    print("ButtonState3 is: ",buttonState3)
    
