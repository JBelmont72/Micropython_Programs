''' At bottom is SHillehs debouncing function for a PIR
works well , very similar to PW 84 but no irq
https://shillehtek.com/blogs/news/how-to-connect-and-use-the-hcsr501-pir-sensor-with-a-raspberry-pi-pico-pico-w?utm_source=youtube&utm_medium=product_shelf
page 160 Random Nerds Micropython
debounce_timer=None
button.irg trigger is the button press.Rising   and the handler is the def button_pressed

def button_pressed(pin):
    global counter,debounce_timer
    counter +=1
    
    led.toggle or some short function
    debounce_timer =Timer()
    debounce_timer=init(period  200 ms,  mode timer.One_Shot callback=debounce_callback)
def debounce_callback(pin):
    global debounce_timer
    debounce_timer=None
'''
# from machine import Pin    ### program 1 of lesson 83
# import time
# butPin=15
# rPin=17
# gPin=16
# bPin=18
# pTime=0
# watchButton=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# press =0
# def IntSwitch(pin):
#     global press
#     pTIme=time.ticks_ms()
#     press =press +1
#     gLed.toggle()
#     print('Triggered: ',press)
#     pTImeOld=pTime


# watchButton.irq(trigger=Pin.IRQ_RISING,handler=IntSwitch)

# try:
#     while True:
#         pass
  
# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#######~~~~~~~~
####does not work  this is from the Random Nerds interupt/tiomer lesson section p 160
from machine import Pin,Timer
import time
butPin=15
gPin=17
rPin=16
bPin=18
yPin=19
Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
rLed=Pin(rPin,Pin.OUT)
gLed=Pin(gPin,Pin.OUT)
bLed=Pin(bPin,Pin.OUT)
yLed=Pin(yPin,Pin.OUT)
x=0
press=0
downTime=time.ticks_ms()
upTime=time.ticks_ms()
OldButState=0
def button_pressed(pin):
    global press,upTime,downTime,OldButState
    ButState=Button.value()
    # upTime=time.ticks_ms()
    
    # if NewButState==1:##Pressed, record the time the button was pressed 
    #     downTime=time.ticks_us()
    # if OldButState==0:
    #     upTime=time.ticks_us()  
    # if NewButState==1 and OldButState==0 and (time.ticks_diff(downTime,upTime)<25):
    # # if NewButState==1 and OldButState==0 :
    #     time_diff=time.ticks_diff(downTime,upTime)
    #     print(time_diff)
    #     print(f'{downTime}  {upTime}')
    #     rLed.toggle
    #     OldButState=NewButState
 
    #     print('Trigger: ',press)
    #     press +=1
    # # upTime=downTime
    # OldButState=NewButState
    # downTime=time.ticks_us()
    
    if ButState==1:##Pressed, record the time the button was pressed 
        downTime=time.ticks_ms()
    
    
    if ButState==0:
        upTime=time.ticks_ms() 
    # if ButState==1:##Pressed, record the time the button was pressed 
    #     downTime=time.ticks_ms()  
    if ButState==1 and OldButState==0 and (time.ticks_diff(downTime,upTime)>25):
    # if ButState==1 and OldButState==0 and (downTime-upTime<25):
    # if NewButState==1 and OldButState==0 :
        time_diff=time.ticks_diff(downTime,upTime)
        print('time_diff',time_diff)
        print(f'{downTime}   time  {upTime}')
        press+=1
        if press>16:
            press =press-16
        if press%2==0:
            gLed.toggle()
        if press%4==0:
            bLed.toggle()
        if press%8==0:
            yLed.toggle()
        rLed.toggle()
        print('Trigger: ',press)    
    # upTime=downTime
    OldButState=ButState
    # print("old but state ",OldButState)
    
    
    
    
Button.irq(trigger=Button.IRQ_RISING|Button.IRQ_FALLING,handler = button_pressed)
try:
    while True:
        # ButVal=Button.value()
        # print(ButVal)
        print(x)
        # if ButVal==1:
        #     rLed.value(1)
        # else:
        #     rLed.value(0)
        time.sleep(1)
        x+=1
except KeyboardInterrupt:
    print('all done')
    rLed.value(0)
    gLed.value(0)
    bLed.value(0)
### debouncing from the keith lohmeyer version of homework for lesson 83 PW
### this works fine SORT OF - not really
# from machine import Pin,Timer
# import time
# butPin=15
# rPin=17
# gPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# counter=0
# myTimer=Timer()
# def myCallback(pin):
#     global counter
    
#     if Button.value()==1:
#         counter+=1
#         gLed.toggle()
#         print('Button Pressed: ',counter)
#     Button.irq(handler=HandFx)

# def HandFx(pin):
#     Button.irq(handler=None)
#     myTimer.init(period=1500,mode=Timer.ONE_SHOT,callback=myCallback)
    

# Button.irq(trigger=Button.IRQ_RISING,handler = HandFx)
# try:
#     while True:
#         # ButVal=Button.value()
#         # print(ButVal)
#         print(x)
#         # if ButVal==1:
#         #     rLed.value(1)
#         # else:
#         #     rLed.value(0)
#         time.sleep(1)
#         x+=1
# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#     myTimer.deinit()
#############my THIS WORKS 
# from machine import Pin,Timer
# import time
# butPin=15
# rPin=17
# gPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# counter=0
# myTimer=Timer()
# oldTime=time.ticks_ms()
# oldButVal=0
# def myCallback(pin):
#     global counter
#     if Button.value()==1:
#         gLed.value(1)
#         counter+=1
#         print('Trigger= ',counter)
#     Button.irq(handler=myHand)

# def myHand(pin):
#     Button.irq(handler=None)
#     myTimer.init(mode=Timer.ONE_SHOT,period=1000,callback=myCallback)     
# Button.irq(trigger=Button.IRQ_RISING,handler=myHand)
# try:
#     while True:
#         newTime=time.ticks_ms()
#         for x in range(20):
#         # print(newButVal)
#             print(x)
#             time.sleep(.1)

# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
#########oct6 2024 attempt at debouncing with interrrupt and timer- WORKS

# from machine import Pin,Timer
# import time
# butPin=14
# rPin=17
# gPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# counter=0
# myTimer=Timer()
# oldTime=time.ticks_ms()
# oldButVal=0
# counter=0
# def myCallback(pin):
#     global counter
#     if Button.value()==1:
#         counter+=1
#         rLed.toggle()
#         print('Button Pressed: ',counter)
    
#     # print('myCallback and Counter= ',counter)
#     print('')
#     Button.irq(handler=myHand)   
    
    


# def myHand(pin):
#     Button.irq(handler=None)
#     myTimer.init(period=1000,mode=Timer.ONE_SHOT,callback=myCallback)        
# Button.irq(trigger=Button.IRQ_RISING,handler=myHand)
# try:
#     while True:
#         # for i in range(20):
#         #     print(i)
#         #     time.sleep(.1)
            
#         print(Button.value())
        
#         newTime=time.ticks_ms()
#         print(newTime)
#         # ButVal=Button.value()
#         # if ButVal ==1:
#         #     print('ButVal: ',ButVal)
#         time.sleep(.1)
 
# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)
########  PW lesson 84  uses an interrupt but no Timer
# from machine import Pin,Timer
# import time
# butPin=15
# gPin=17
# rPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# x=0
# press=0
# myTimer=Timer()
# oldTime=time.ticks_us() ## same as tUp which is when button is 0
# newTime=time.ticks_us() ## same as tDown which is whne button is 1 and pressed down
# oldButVal=0
# butStateOld =0
# def myHand(pin):
#     global oldTime,newTime,butStateOld,press
#     newTime=time.ticks_ms()
#     butStateNew=Button.value() 
#     if butStateNew==1:
#         newTime=time.ticks_us()
#     if butStateOld==0:
#         oldTime=time.ticks_us()           
#     # if butStateOld ==0 and butStateNew==1 :
#     if butStateOld ==0 and butStateNew==1 and (newTime-oldTime)  <25:
        
#         press +=1
#         print('TRIGGER: ',press) 
#         rLed.toggle()
#         # deltaTime=time.ticks_diff(newTime,oldTime)
#         deltaTime=newTime-oldTime
#         print('deltatime: ',deltaTime)
#     butStateOld=butStateNew
# Button.irq(trigger=Pin.IRQ_RISING|Pin.IRQ_FALLING ,handler=myHand)
# try:
#     while True:
#         newTime=time.ticks_ms()
#         for x in range(30):
#         # print(newButVal)
#             print(x)
#             time.sleep(.1)

# except KeyboardInterrupt:
#     print('all done')
#     rLed.value(0)
#     gLed.value(0)
#     bLed.value(0)


# from machine import Pin,Timer
# import time
# butPin=15
# gPin=17
# rPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# But_state=False
# last_time=0
# debounce_time =5
# stop_state=False
# def button_pressed(pin):
#     global But_state, debounce_time,last_time ,stop_state      
#     current_time=time.time()
#     Button.irq(handler = None)
#     stop_state=False
#     if But_state==False and (current_time-last_time>debounce_time):
#         print('hi, button pressed')
#         print('Duration = ',current_time-last_time)
#         last_time=current_time
#         stop_state=True
#         reset(stop_state)
#     else:
#         stop_state=False    
# def reset(stop_state):
#     global But_state, debounce_time,last_time 
#     print('bye')
#     Button.irq(handler=button_pressed)
     
# Button.irq(trigger=Pin.IRQ_RISING,handler=button_pressed)
# while True:
#     reset(stop_state)
#     if stop_state==True:
#         gLed.value(1)
#         time.sleep(.5)
#         gLed.value(0)
#         time.sleep(.1)
#     else:
#         gLed.value(0)
#         print('resting')
#         time.sleep(2)



# from machine import Pin,Timer
# import time
# butPin=15
# gPin=17
# rPin=16
# bPin=18
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# rLed=Pin(rPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# bLed=Pin(bPin,Pin.OUT)
# last_time=0
# debounce_time =5
# stop_state=False
# def button_pressed(pin):
#     global  debounce_time,last_time ,stop_state      
#     current_time=time.time()
#     Button.irq(handler = None)
#     stop_state=False
#     if stop_state==False and (current_time-last_time>debounce_time):
#         print('hi, button pressed')
#         print('Duration = ',current_time-last_time)
#         last_time=current_time
#         stop_state=True
#         reset(stop_state)
#     else:
#         stop_state=False    
# def reset(stop_state):
#     global debounce_time,last_time 
#     print('bye')
#     Button.irq(handler=button_pressed)
#     stop_state=False
     
# Button.irq(trigger=Pin.IRQ_RISING,handler=button_pressed)
# while True:
#     reset(stop_state)
#     if stop_state==True:
#         gLed.value(1)
#         time.sleep(.5)
#         gLed.value(0)
#         time.sleep(.1)
#     else:
#         gLed.value(0)
#         print('resting')
#         time.sleep(2)
# ## shilleh    https://shillehtek.com/blogs/news/how-to-connect-and-use-the-hcsr501-pir-sensor-with-a-raspberry-pi-pico-pico-w?utm_source=youtube&utm_medium=product_shelf

# from machine import Pin
# import time

# # Initialize PIR sensor on GPIO 0
# pir = Pin(0, Pin.IN, Pin.PULL_DOWN)
# led = Pin(16, Pin.OUT)  # Initialize LED on GPIO 2
# pir_state = False  # Start assuming no motion detected
# last_motion_time = 0  # Timestamp of the last motion detected
# debounce_time = 3  # Debounce period in seconds

# print("PIR Module Initialized")
# time.sleep(1)  # Allow the sensor to stabilize
# print("Ready")

# while True:
#     val = pir.value()  # Read input value from PIR sensor
#     current_time = time.time()

#     if val == 1:  # Motion detected
#         if not pir_state and (current_time - last_motion_time >= debounce_time):
#             print(current_time - last_motion_time)
#             print("Motion detected!")
#             pir_state = True
#             led.on()  # Turn on LED
#             last_motion_time = current_time  # Update the last motion timestamp

#     elif val == 0: 
#         if pir_state and (current_time - last_motion_time >= debounce_time):
#             pir_state = False
#             led.off()
#             last_motion_time = current_time  # Update the last motion timestamp

#     time.sleep(0.1)  # Small delay to prevent spamming
    