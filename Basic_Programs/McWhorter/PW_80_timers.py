'''creating and using timers Lesson 80
'''
# from machine import Pin,Timer
# import time
# rPin=17
# gPin=16
# bPin=13
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# buzzPin=14
# Buzzer=Pin(buzzPin,Pin.OUT)
# def redBlinker(source):
#     rLed.toggle()
#     print('red led toggle')
# def buzzer(source):
#     print('Buzzer beep')
#     Buzzer.value(1)
#     time.sleep(.1)
#     Buzzer.value(0)
#     # time.sleep(.1)
# def greenBlinker(pin):
#     print("green blinking")
#     gLed.value(1)
#     time.sleep(.1)
#     gLed.value(0)       
# ## timer is in milliseconds  100 millisecs =.1sec
# redTimer=Timer(period=500,mode=Timer.PERIODIC,callback=redBlinker)
# buzzerTimer= Timer(period=5000,mode=Timer.PERIODIC,callback=buzzer)
# greenTimer=Timer(period=2000,mode=Timer.PERIODIC,callback=greenBlinker)
# x=0
# try:
#     while True:
#         print(x)
#         x+=1
#         # rLed.value(1)
#         # gLed.value(1)
#         bLed.value(1)
#         print('Blue LED')
#         time.sleep(.5)
#         # rLed.value(0)
#         # gLed.value(0)
#         bLed.value(0)
#         time.sleep(.5)
# except KeyboardInterrupt:
#     print('all done')
#     redTimer.deinit()
#     # buzzerTimer.deinit()
#     greenTimer.deinit()
#     time.sleep(.5)
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     Buzzer.value(0)
################# now lesson 81 with an assymetric pulse using gthe one shot

# from machine import Pin,Timer
# import time
# rPin=17
# gPin=16
# bPin=13
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# buzzPin=14
# Buzzer=Pin(buzzPin,Pin.OUT)
# def gLedOFF(pin):
#     gLed.value(0)
#     print('Green OFF')
# def turnRedOff(pin):
#     rLed.value(0)
#     print('Red Off')
# def BuzzOff(Pin):
#     Buzzer.value(0)  
# def redBlinker(source):
#     rLed.value(1)
#     print('red led on')
#     redOFF=Timer(period=100,mode=Timer.ONE_SHOT,callback=turnRedOff)
      
# def buzzer(source):
#     print('Buzzer beep')
#     Buzzer.value(1)
#     BuzzerOff=Timer(period=100,mode=Timer.ONE_SHOT,callback=BuzzOff)

# def greenBlinker(pin):
#     print("green blinking")
#     gLed.value(1)
#     greenOff=Timer(period=2500,mode=Timer.ONE_SHOT,callback=gLedOFF)
        
# ## timer is in milliseconds  100 millisecs =.1sec
# redTimer=Timer(period=3000,mode=Timer.PERIODIC,callback=redBlinker)
# buzzerTimer= Timer(period=3000,mode=Timer.PERIODIC,callback=buzzer)
# greenTimer=Timer(period=3000,mode=Timer.PERIODIC,callback=greenBlinker)

# x=0
# try:
#     while True:
#         print(x)
#         x+=1
#         # rLed.value(1)
#         # gLed.value(1)
#         bLed.value(1)
#         print('Blue LED')
#         time.sleep(.5)
#         # rLed.value(0)
#         # gLed.value(0)
#         bLed.value(0)
#         time.sleep(.5)
# except KeyboardInterrupt:
#     print('all done')
#     redTimer.deinit()
#     # buzzerTimer.deinit()
#     greenTimer.deinit()
#     time.sleep(.5)
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     Buzzer.value(0)
#########charlotte swift  I sent a comment to Charlotte Swift about this
####~~~ did not work for me
# import time
# from machine import Pin,Timer
# rPin=16
# gPin=17
# bPin=18
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# blueP=100
# greenP=  10000
# redP= 1000
# redOnPerc =0.1
# redOnP=int(redP*redOnPerc)
# def redBlinker(timer):
#     global redTimer, redP
#     rLed.toggle()
#     print('redBlinker rLed value: ',rLed.value())
#     print('redP: ',redP)
#     redTimer = Timer(mode = Timer.PERIODIC, period=redP,callback= redBlinker2)
    
# def redBlinker2(timer):
#     print('first redBlinker2 rLed Value: ',rLed.value())
#     rLed.toggle()
#     print('redBlinker2 rLed value: ',rLed.value())
# def greenBlinker(timer):
#     gLed.toggle()
# def blueBlinker(Timer):
#     bLed.toggle()
    
# rLed.on()
# gLed.on()
# bLed.on()

# if rLed.value()==1:
#     redPeriod =redOnP
# else:
#     redPeriod= redP-redOnP
# x=0
# redTimer= Timer(period=redPeriod,mode=Timer.ONE_SHOT,callback=redBlinker)
# redTimer2=Timer(period=redP,mode=Timer.PERIODIC,callback=redBlinker2)
# greenTimer=Timer(period=greenP,mode=Timer.PERIODIC,callback=greenBlinker)
# blueTimer=Timer(period=blueP,mode=Timer.PERIODIC,callback=blueBlinker)
# try:
#     while True:
#         print(x)
#         time.sleep(1)
#         x+=1
# except KeyboardInterrupt:
#     print('all done')
#     redTimer.deinit()
#     # buzzerTimer.deinit()
#     greenTimer.deinit()
#     blueTimer.deinit()

#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
###############from making stuff with chris deHut   

# import time
# from machine import Pin,Timer
# rPin=17
# gPin=16
# bPin=13
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)

# def blueBlinker(source):
#     bLed.toggle()

# def redBlinker(source):
#     rLed.toggle()
# def redOff(source):
#     rLed.value(0)
# def greenBlinker(source):
#     gLed.toggle()
# x=0
# blueTimer=Timer(period= 2000,mode=Timer.PERIODIC,callback=blueBlinker)
# # redTimer=Timer(period=1000,mode=Timer.PERIODIC,callback=redBlinker)

# greenTimer=Timer(period=2000,mode=Timer.PERIODIC,callback=greenBlinker)
# try:
#     while True:
#         print(x)
#         time.sleep(1)
#         x+=1
#         if x%5==0:
#             rLed.value(1)
#             red_off_timer=Timer(period=1000,mode=Timer.ONE_SHOT,callback=redOff)
#             print('red one shot timer activated')
# except KeyboardInterrupt:
#     print('all done')
#     red_off_timer.deinit()
#     # redTimer.deinit()
#     # buzzerTimer.deinit()
#     greenTimer.deinit()
#     blueTimer.deinit()
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
    ############### variation of above chris deHut one shot example
# import time
# from machine import Pin,Timer
# rPin=17
# gPin=16
# bPin=13
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# def Function(source):
#     print('Hi')
# def greenOff(source):
#     gLed.value(0)
#     print('Green Off')
# def blueBlinker(source):
#     bLed.toggle()
# def redOff(source):
#     rLed.value(0)
#     print('Red Off')
# def redBlinker(source):
#     rLed.value(1)
#     print('Red On')
#     red_off_timer=Timer(period=100,mode=Timer.ONE_SHOT,callback=redOff)
# def redOff(source):
#     rLed.value(0)
#     print('Red Off')
# def greenBlinker(source):
#     gLed.value(1)
#     green_off_timer=Timer(period=1000,mode=Timer.ONE_SHOT,callback=greenOff)
# x=0
# blueTimer=Timer(period= 2000,mode=Timer.PERIODIC,callback=blueBlinker)
# redTimer=Timer(period=2000,mode=Timer.PERIODIC,callback=redBlinker)
# # red_off_timer=Timer(period=1000,mode=Timer.ONE_SHOT,callback=redOff)
# greenTimer=Timer(period=2000,mode=Timer.PERIODIC,callback=greenBlinker)
# try:
#     while True:
#         print(x)
#         time.sleep(1)
#         if x%5==0:
#             blue_one_shot=Timer(period=4000,callback=Function)
#         x+=1
# except KeyboardInterrupt:
#     print('all done')
#     # red_off_timer.deinit()
#     redTimer.deinit()
#     # buzzerTimer.deinit()
#     greenTimer.deinit()
#     blueTimer.deinit()

#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)

##################
## this is a binary counter using perioid timers, works fine
# import time
# from machine import Pin,Timer
# rPin=16
# gPin=17
# bPin=18
# yPin=19
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# yLed=Pin(yPin,Pin.OUT)

    
# rLed.off()
# gLed.off()
# bLed.off()
# yLed.off()
# count=0
# def redBlinker(pin):
    
#     rLed.toggle()
# def greenBlinker(pin):
#     gLed.toggle()
# def blueBlinker(pin):
#     bLed.toggle()   
# def yellowBlinker(pin):
#     yLed.toggle()
# period=300
# redTimer=Timer(period=period,mode=Timer.PERIODIC,callback=redBlinker)
# greenTimer=Timer(period=period*2,mode=Timer.PERIODIC,callback=greenBlinker)
# blueTimer=Timer(period=period*4,mode=Timer.PERIODIC,callback=blueBlinker)
# yellowTimer=Timer(period=period*8,mode=Timer.PERIODIC,callback=yellowBlinker)
# try:
#     while True:
#         pass
       
# except KeyboardInterrupt:
#     print('all done')
#     redTimer.deinit()
#     # buzzerTimer.deinit()
#     greenTimer.deinit()
#     blueTimer.deinit()
#     yellowTimer.deinit()

#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     yLed.value(0)
##############binary counter using a push button and interrupts

import time
from machine import Pin,Timer
rPin=16
gPin=17
bPin=18
yPin=19
butPin=15
rLed=Pin(rPin,Pin.OUT)
gLed=Pin(gPin,Pin.OUT)
bLed=Pin(bPin,Pin.OUT)
yLed=Pin(yPin,Pin.OUT)
Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)

    
rLed.off()
gLed.off()
bLed.off()
yLed.off()
press=0
tUP=time.ticks_ms
tDown=time.ticks_ms
# tDelta=time.ticks_diff(tDown,tUP)
butStateOld=0
def Binary(pin):
    global press , butStateOld, tUP, tDown
    butState=Button.value()
    if butState==1:
        tDown=time.ticks_ms()
    if butState==0:
        tUp=time.ticks_ms()
    if butState==1 and butStateOld==0 and (time.ticks_diff(tDown,tUP)< (-130000000)) :
    # if butState==1 and butStateOld==0:
        press +=1
        print('TRIGGER: ',press)
        tDelta=time.ticks_diff(tDown,tUP)
        print(tDelta)
        rLed.toggle()
        if press>16:
            press =press-16
        if press%2==0:
            gLed.toggle()
        if press%4==0:
            bLed.toggle()
        if press%8==0:
            yLed.toggle()
        
    # butStateOld=0
    
    
Button.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING ,handler=Binary)  ## i got around using Pin.IRQ_Falling by resetting the butStateOld to 0 

try:
    while True:
        pass
       
except KeyboardInterrupt:
    print('all done')
    rLed.value(0)
    gLed.value(0)
    bLed.value(0)
    yLed.value(0)