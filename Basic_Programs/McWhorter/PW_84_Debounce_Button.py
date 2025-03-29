'''
PW lesson 84 Pico button debouncing, works fine

important:
# tUp=time.ticks_ms() ## time button from 1 to zero, when the button comes up (though the value goes to zero)
# tDown=time.ticks_ms() ### time button  down. is when the button is pushed down(and becomes zero)   the t Diff will be the time between the button coming up minus time down
# ## the real tDown when value goes to one from zero after a long interval of time.
# ## thus want tDown - tUP  to be greater than what we want as a debounee time ( maybe 25 ms)

'''
import sys
from machine import Pin, Timer
import time

# Button and LED pin definitions
butPin = 15
butPin2 = 14
gPin = 19
rPin = 17
bPin = 16
yPin = 18

# Button setup
watchButton = Pin(butPin, Pin.IN, Pin.PULL_DOWN)
Button = Pin(butPin2, Pin.IN, Pin.PULL_DOWN)

# LED setup
rLed = Pin(rPin, Pin.OUT)
gLed = Pin(gPin, Pin.OUT)
bLed = Pin(bPin, Pin.OUT)
yLed = Pin(yPin, Pin.OUT)

# Initial states
butStateOld = 0
butStateOld2 = 0
tUp = time.ticks_ms()
tDown = time.ticks_ms()
press = 0
tUp2 = time.ticks_ms()
tDown2 = time.ticks_ms()

# Update LED states based on binary representation
def update_leds(press):
    bLed.value(press & 0b0001)  # LSB (1st bit)
    rLed.value((press >> 1) & 0b0001)  # 2nd bit
    yLed.value((press >> 2) & 0b0001)  # 3rd bit
    gLed.value((press >> 3) & 0b0001)  # 4th bit

# Button 1: Increase counter
def button_press(pin):
    global press, butStateOld, tUp, tDown
    ButtonState = watchButton.value()
    if ButtonState == 0:
        tUp = time.ticks_ms()
    if ButtonState == 1:
        tDown = time.ticks_ms()
    timeDiff = time.ticks_diff(tDown, tUp)
    if ButtonState == 1 and butStateOld == 0 and timeDiff > 25:
        press += 1
        print('Button #1 count:', press)
        update_leds(press)
    butStateOld = ButtonState

# Button 2: Decrease counter
def button_press2(pin):
    global press, tUp2, tDown2, butStateOld2
    ButtonState2 = Button.value()
    if ButtonState2 == 0:
        tUp2 = time.ticks_ms()
    if ButtonState2 == 1:
        tDown2 = time.ticks_ms()
    timeDiff = time.ticks_diff(tDown2, tUp2)
    if ButtonState2 == 1 and butStateOld2 == 0 and timeDiff > 25:
        if press > 0:  # Prevent negative values
            press -= 1
            print('Button #2 count:', press)
            update_leds(press)
    butStateOld2 = ButtonState2

# Interrupt setup
watchButton.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_press)
Button.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=button_press2)

# Main loop
try:
    while True:
        pass
except KeyboardInterrupt:
    rLed.value(0)
    gLed.value(0)
    bLed.value(0)
    yLed.value(0)
    sys.exit()



# from machine import Pin,Timer
# import time
# butPin=15
# butPin2=14
# gPin=17
# rPin=16
# bPin=18
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# Button=Pin(butPin2,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# press=0     ## # if tune bu
# tUp=time.ticks_ms() ## time button from 1 to zero, when the button comes up (though the value goes to zero)
# tDown=time.ticks_ms() ### time button  down. is when the button is pushed down(and becomes zero)   the t Diff will be the time between the button coming up minus time down
# ## the real tDown when value goes to one from zero after a long interval of time.
# ## thus want tDown - tUP  to be greater than what we want as a debounee time ( maybe 25 ms)

# butStateOld=0


# def button_pressed(pin):
#     global tUp, tDown,butStateOld, press
#     ButState=watchButton.value()
#     if  ButState==1:
#         tDown=time.ticks_ms()
#     if ButState==0:
#         tUp=time.ticks_ms()
#     tDiff=tDown-tUp
#     if butStateOld==0 and ButState==1 and tDiff>=25:
#         press +=1
#         print('button has been pressed',press)
#         print(tDiff)
#         bLed.toggle()
#     butStateOld=ButState  

# watchButton.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler=button_pressed)

# try:
#     while True:
  
#         for i in range(50):
#             print(i)
#             if i %2 ==0:
#                 gLed.toggle()
#         time.sleep(1.5)           


# except KeyboardInterrupt:
#     print('All done')
#     gLed.value(0)
#     bLed.value(0)
#     rLed.value(0)
###~~~~~~~~~~~~~
# i can substitute the PIR and it works fine as well as with a Pushbutton
# next i can try to include a timer to turn on another led (r Led)or a buzzer etc
# from machine import Pin,Timer
# import time
# butPin=15
# butPin2=14
# gPin=17
# rPin=16
# bPin=18
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# Button=Pin(butPin2,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# butStateOld=0
# tUp=time.ticks_ms()
# tDown=time.ticks_ms()
# press =0
# def button_press(pin):
  
#     if  butState==1 and butStateOld==0 and (tDown-tUp>25):
#         press+=1
#         gLed.toggle()
#         print('Hi')
#         print('TRIGGER: ',press)
#         # for i in range(10):
#         #     rLed.toggle()
#         #     time.sleep(.2)
        
#     butStateOld=butState


# Button.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler =button_press)

# try:
#     while True:
  
#         for i in range(50):
#             print(i)
#             time.sleep(.3)
#             if i %2 ==0:
#                 bLed.toggle()
#         time.sleep(1.4)           


# except KeyboardInterrupt:
#     print('All done')
#     gLed.value(0)
#     bLed.value(0)
#     rLed.value(0)   
 #### creeate a binary up down counter with an interrupt ann debouncing
# import sys
# from machine import Pin,Timer
# import time
# butPin=15
# butPin2=14
# gPin=19
# rPin=17
# bPin=16
# yPin =18
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# Button=Pin(butPin2,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# yLed=Pin(yPin,Pin.OUT)
# butStateOld=0
# tUp=time.ticks_ms()
# tDown=time.ticks_ms()
# press =0
# # def update_leds(press):
# #     print(f'Binary: {bin(press)[2:].zfill(4)}')  # Show 4-bit binary
# #     bLed.value(press & 0b0001)  # 1st bit
# #     rLed.value((press >> 1) & 0b0001)  # 2nd bit
# #     yLed.value((press >> 2) & 0b0001)  # 3rd bit
# #     gLed.value((press >> 3) & 0b0001)  # 4th bit


# def binaryCounter(press):
#     print(' counter',press)
     
#     print(f'Binary: {bin(press)[2:]}')  # Show 4-bit binary 
#     # bLed.toggle()
#     bLed.value(press &0b0001)
#     rLed.value((press>>1) & 0b0001)
#     yLed.value((press >>2 & 0b0001))
#     gLed.value(press>> 3 & 0b0001)

#     # if press % 2 == 0:
#     #     rLed.toggle()
#     # if press % 4 == 0:
#     #     yLed.toggle()
#     # if press % 8 == 0:
#     #     gLed.toggle()


# def button_press(pin):
#     global press,butStateOld,tUp,tDown
#     ButtonState=watchButton.value()
#     if ButtonState ==0:
#         tUp=time.ticks_ms() ## tUp is tghe time the button is UP
#     if ButtonState == 1:
#         tDown = time.ticks_ms()
#     timeDiff =time.ticks_diff(tDown,tUp)## tUp is when the buttonState is back  up 0
#     if ButtonState == 1 and butStateOld == 0 and timeDiff >25:
#         press +=1
#         print('Trigger:  ',press)
#         binaryCounter(press)
#     butStateOld=ButtonState      
# watchButton.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler=button_press)
# # Button.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler=button_press)
# try:
#     while True:
#         pass       
# except KeyboardInterrupt:
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     yLed.value(0)
#     sys.exit()
    
### ~~ bitwise practice

# print(5 & 0b0101)
# 5 in binary: 0101
# 1 in binary: 0001
# Result:      0001 -> 1
# if (5 & 0b0101):
#     print('hi')
# else:
#     print('bye')
# if (5 & 0b010):
#     print('hi')
# else:
#     print('bye')
# print(8 >>1)
# print(8 >>2)
# print(8 >>3)
