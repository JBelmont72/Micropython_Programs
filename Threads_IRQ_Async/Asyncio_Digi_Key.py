'''
Syncio from Digi_key
concurrency and mutitasking
TIme_slicing
RTOS real time operating sysytem
https://github.com/peterhinch/micropython-async/blob/46438be23632cc3d74d9ecd72768c9108dde1298/v3/README.md
uasuyncio does not have queue function, version three, primitives has a 
https://github.com/peterhinch/micropython-async/blob/46438be23632cc3d74d9ecd72768c9108dde1298/v3/docs/TUTORIAL.md#35-queue

https://github.com/peterhinch/micropython-async/blob/46438be23632cc3d74d9ecd72768c9108dde1298/v3/docs/THREADING.md

'''
import uasyncio
# from machine import Pin
# import time

# gPin=16
# gLed=Pin(gPin,Pin.OUT)
# rPin = 17
# rLed=Pin(rPin,Pin.OUT)
# ##1 make co-routine on a timer. will not switch between functions automatically, 
# ## so need a function to do so,  whis is the  await uasyncio.sleep(delay) 
# ##  'await' = It tells us to wait for the funtion to finish the future object, in this case 'sleep'
# async def blink(delay):
#     while True:
#         gLed.toggle()
#         await uasyncio.sleep(delay)
# ## Every uasyncio function must be part of the event loop. works as scheduler
# ## Need to call ' .run ' function to call on the main function. The 'create_task()'  is similar to await BUT returns IMMEDIATELY
# ## to start running the multi task program, need to start the event loop and run the 'entry point.'  Only can 
# ## call one co-routine program from .run at a tinme.  
# async def main():
#     # await blink(.3)
#     uasyncio.create_task(blink(.5))
#     ### if have 'await blink(.3)', instead of the above 'create_task' , the  blink fx never runs. it just becomes a 'futyure object.'  
#     count=0

#     while True:  ## looks like I have to have the while loop be shorter than the called co Routine Blink
#         timeStart=time.time()
#         print(timeStart)
#         rLed.value(1)
#         time.sleep(.2)
#         rLed.value(0)
#         time.sleep(.2)
#         print('bloop  ',count)
#         count +=1
#         timeStop=time.time()
#         timeDelta=time.ticks_diff(timeStop,timeStart)
#         print(timeDelta)
#         timeStart=timeStop
#         await uasyncio.sleep(.001)
        
# uasyncio.run(main())

'''



'''
# import machine
# import uasyncio
# # settings
# gPin=17
# gLed=machine.Pin(gPin,machine.Pin.OUT)

# # CoRoutine: blink in a timer  Co-poperative mutltitasking
# async def blink(delay):
#     while True:
#         gLed.toggle()
#         await uasyncio.sleep(delay) # need to have an await function/ is a keyword whdcih says wait for the functio to complete
        
# # co routine: create an entry point for the asycncio program.  without await and just a delay, it creates a future object.Need to call with await
# ########### option 1
# # async def main():
# #     blink(0.2)  ## as is, the blink function is not called, just gives us a 'future object.
# #     print('done')
# # uasyncio.run(main()) 
# ################## option 2
# ## need to point uasyncio to the entry point to get it running.
# ## start event loop and run entry point coroutine
# ## only one run function being called ferom the .run
# # uasyncio.run(main())    

# ########### option 3
# # async def main():
# #     await blink(0.2)
# #     print('done')

# # uasyncio.run(main())
# #########  every routine has to yield to other tasks so they can run
# async def main():
    
#     uasyncio.create_task(blink(0.2))
#     while True:
#         print('done')
#         await uasyncio.sleep_ms(1000)## by adding this, this routine yields to the main function so they both run
# ## the function yields  so that two trasks run at same time. an alternaitve to tme stamp to check a sensor of wi fi connection
# uasyncio.run(main())

#### will add a button zthis allows functions to be performed while awaiting another function( in this case abutton) to be returend 
'''
import machine
import uasyncio

# settings
import time
gPin=17
gLed=machine.Pin(gPin,machine.Pin.OUT)
butPin=15
btn=machine.Pin(butPin,machine.Pin.IN,machine.Pin.PULL_DOWN)
## the below 10 lines just ot work out the button values.  I used a PULLdown , i had different wiring 
# btn_prev=btn.value()      ## tis is my working out the logic of the while loop. . when the btn.value() becomes one  and btn_prev is still 0 , we have 'and'  not 'or'
# print(btn.value())
# while (btn.value()==1) or (btn.value()==btn_prev):
#         a=btn.value()
#         print(btn.value(),'  ',btn_prev)
#         btn_prev =btn.value()

#         time.sleep(.5)
#         # await uasyncio, .sleep_ms(40)
#         try:
#             if btn.value()==1 and (btn_prev==0):
#                 print('Hit')
#             btn_prev=btn.value()
#         except:
#             continue


# CoRoutine: blink in a timer  Co-poperative mutltitasking
async def blink(delay):  #3 cabn be used to check a sensor at freqeunt intervals
    while True:
        gLed.toggle()
        await uasyncio.sleep(delay) # need to have an await function/ is a keyword whdcih says wait for the functio to complete
      ### the uasyncio.create_task(blink(0.2)) in the  async def main() refers up to here and this await ... causes the procecessor to yield up here to the other function.  
# co routine : only return on button press
async def wait_button():
    btn_prev =btn.value()
    print(btn_prev)
    while (btn.value()==1) or (btn.value()==btn_prev):## so when I let up on the button, the button..value becomes 0 and at that moment the btn_prev was 1. so for an instant the while loop criteria are not met!!!
        print(btn.value(),'  ',btn_prev)
        btn_prev =btn.value()
        await uasyncio.sleep_ms(40)
        print(btn_prev)
    ## 1 1      1   let up  bloop    0     0 0 btn_prev becomnes one as the button i
async def main():
    uasyncio.create_task(blink(0.2)) #3 this is similar to await but it returns immediately
    
    while True:
        await wait_button() # entry point needs await to call the wait_button function
        print('bloop') 
        ## i think that 'await uasyncio.sleep(delay)' has to be in this main() function OR ,as in this case, is in the 'wait_button' function. onw or the other.
        
          
uasyncio.run(main())
### the WHile loop keeps checking the 'wait_button' function until the condition of the the button_value =0 and the prev button value which was 1 Now  does not equal the new button.value().
### the OR condition is not met and the  await wait_button gets to kick in, the time functionpermits the next item in the while loop to be performed.
### in this case the next in line is the print('bloop') 
'''
'''
import machine
import uasyncio

# settings
import utime
gPin=17
gLed=machine.Pin(gPin,machine.Pin.OUT)
butPin=15
btn=machine.Pin(butPin,machine.Pin.IN,machine.Pin.PULL_DOWN)
## the below 10 lines just ot work out the button values.  I used a PULLdown , i had different wiring 
# btn_prev=btn.value()      ## tis is my working out the logic of the while loop. . when the btn.value() becomes one  and btn_prev is still 0 , we have 'and'  not 'or'
# print(btn.value())
# while (btn.value()==1) or (btn.value()==btn_prev):
#         a=btn.value()
#         print(btn.value(),'  ',btn_prev)
#         btn_prev =btn.value()

#         time.sleep(.5)
#         # await uasyncio, .sleep_ms(40
#         try:
#             if btn.value()==1 and (btn_prev==0):
#                 print('Hit')
#             btn_prev=btn.value()
#         except:
#             continue


# CoRoutine: blink in a timer  Co-poperative mutltitasking
async def blink(delay):  #3 cabn be used to check a sensor at freqeunt intervals
    while True:
        gLed.toggle()
        await uasyncio.sleep(delay) # need to have an await function/ is a keyword whdcih says wait for the functio to complete
      ### the uasyncio.create_task(blink(0.2)) in the  async def main() refers up to here and this await ... causes the procecessor to yield up here to the other function.  
# co routine : only return on button press
async def wait_button():
    btn_prev =btn.value()
    # print(btn_prev)  ### when I let up in the button, the 'OR' is not met because btnvlaue is becomes 0 and the btn_prev is still 1
    while (btn.value()==1) or (btn.value()==btn_prev):## so when I let up on the button, the button..value becomes 0 and at that moment the btn_prev was 1. so for an instant the while loop criteria are not met!!!
## let up ++btn.value=0       btn.value does not = btn_prev which was 1 (o != 1), therefore conditions not met
 ## remember, when I let up, the btn_prev was 1 and now it just went to zero!!       
        # print(btn.value(),'  ',btn_prev)
        btn_prev =btn.value()
        await uasyncio.sleep_ms(40)
        # print(btn_prev)
    ## 1 1      1   let up  bloop    0     0 0 btn_prev becomes one as the button i
async def main():
    ## Start coroutine as a task and immediately return
    uasyncio.create_task(blink(0.2)) #3 this is similar to await but it returns immediately
    ##Main loop
    timeStamp=utime.ticks_ms()
    while True:
        await wait_button() # entry point needs await to call the wait_button function
        newTime=utime.ticks_ms()
        deltaTime=newTime-timeStamp
        # deltaTime=utime.ticks_diff(newTime,timeStamp)
        print('bloop') 
        ## i think that 'await uasyncio.sleep(delay)' has to be in this main() function OR ,as in this case, is in the 'wait_button' function. onw or the other.
        print(deltaTime)
        timeStamp=newTime
          
uasyncio.run(main())
### the WHile loop keeps checking the 'wait_button' function until the condition of the the button_value =0 and the prev button value which was 1 Now  does not equal the new button.value().
### the OR condition is not met and the  await wait_button gets to kick in, the time functionpermits the next item in the while loop to be performed.
### in this case the next in line is the print('bloop') 
'''

import machine
import uasyncio
import utime
import queue
gPin=16
gLed=machine.Pin(gPin,machine.Pin.OUT)
butPin=15
btn=machine.Pin(butPin,machine.Pin.IN,machine.Pin.PULL_DOWN)

# async def blink(delay):
async def blink(q):
    delay_ms = 0
    while True:
        if not q.empty():
            delay_ms=await q.get()
        gLed.toggle()
        await uasyncio.sleep(delay_ms)
async def wait_button():
    but_prev = btn.value()
    if btn.value()==1 or btn.value()==but_prev:
        btn_prev = btn.value()
        await uasyncio.sleep_ms(40)
async def main():
    q=queue.Queue()
    uasyncio.create_task(blink(q))
    timeStart=utime.ticks_ms()
    while True:
        await wait_button()
        timeStop=utime.ticks_ms()
        delayTime = utime.ticks_diff(timeStop,timeStart)
        timeStart=timeStop
        print(delayTime)
        delayTime=min(delayTime,2000)
        await q.put(delayTime)
uasyncio.run(main())   