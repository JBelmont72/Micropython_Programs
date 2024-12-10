'''
PW lesson 84 Pico button debouncing, works fine
'''
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
# tUp=time.ticks_ms() ## tinme button from 1 to zero, when the button comes up (though the value goes to zero)
# tDown=time.ticks_ms() ### time button  down. is when the button is pushed down(and becomes zero)   the t Diff will be the time between the button coming up minus time down
# ## the real tDown when value goes to one from zero afgter a long intgerval of time.
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
#         time.sleep(.4)           


# except KeyboardInterrupt:
#     print('All done')
#     gLed.value(0)
#     bLed.value(0)
#     rLed.value(0)
###~~~~~~~~~~~~~
# i can substitute the PIR and it works fine as well as with a Pushbutton
# next i can try to include a timer to turn on another led (r Led)or a buzzer etc
from machine import Pin,Timer
import time
butPin=0
butPin2=14
gPin=17
rPin=16
bPin=18
watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
Button=Pin(butPin2,Pin.IN,Pin.PULL_DOWN)
rLed=Pin(rPin,Pin.OUT)
gLed=Pin(gPin,Pin.OUT)
bLed=Pin(bPin,Pin.OUT)
butStateOld=0
debounceTime=25
tUp=time.ticks_ms()
tDown=time.ticks_ms()
def button_press(pin):
    butState=watchButton.value()
    global butStateOld,tUp,tDown
    if butState==0:
        tUp=time.ticks_ms()
    if butState==1:
        tDown=time.ticks_ms()
    tDiff=tDown-tUp
    if butStateOld==0 and butState==1 and tDiff>300:
        gLed.toggle()
        print('Hi')
        for i in range(10):
            rLed.toggle()
            time.sleep(.2)
        
    butStateOld=butState


watchButton.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING,handler =button_press)

try:
    while True:
  
        for i in range(50):
            print(i)
            time.sleep(.3)
            if i %2 ==0:
                bLed.toggle()
        time.sleep(.4)           


except KeyboardInterrupt:
    print('All done')
    gLed.value(0)
    bLed.value(0)
    rLed.value(0)
    
    
    
    
    

    