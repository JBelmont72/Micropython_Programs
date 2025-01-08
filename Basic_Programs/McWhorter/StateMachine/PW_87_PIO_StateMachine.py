'''
Paul McWhorter Lesson 87
assembly language
lowest freq can run the state machine is 2000 commands per second, can run at 10 million cycles per second, lowest is 2000 operations per second ,  1/2 of a millisecond
can run at 10 million cycles per secopnd
'''
## this program set the pins (4 in this case )were initialized and set to 0 or 1
# import time
# from machine import Pin
# import rp2   ## the   @ is  'decorator' and alerts that we are programming the state machine
# @rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,)*4, out_shiftdir=rp2.PIO.SHIFT_RIGHT)  # defines the number of GPIO pins to use,
# # @rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,)*4)  # defines the number of GPIO pins to use,(THis worked as well)
# def pioProg():
#     set(pins,0b1011)
#     # set(pins,(0b0011 + 0b0001))
#     # set(pins,0xA)
#     # set(pins,15)
  

    

# ### sm0 is instantiating the satemenachine object, using SM 0 put can go all the way to SM 7    
# sm0 = rp2.StateMachine(0, pioProg,freq=2000, set_base=Pin(16))
# try:
#     while True:
#         for i in range(5):
#             # sm0.put(i)
#             # a=sm0.get()
#             time.sleep(.5)
#             print(i) 
#         sm0.active(1)
#         time.sleep(2)
#         sm0.active(0)
# except KeyboardInterrupt:
#     sm0.active(0)
#     print('All Done')
# ############### 2d half of lesson 87  set()   by changing to out() opens the possibilites
### changed set to out!
'''
import time
from machine import Pin
import rp2   ## the   @ is  'descriptor' and alerts that we are programming the state machine
# ### Note that I have changed the 'set' to 'out'
@rp2.asm_pio(out_init=(rp2.PIO.OUT_HIGH,)*6, out_shiftdir=rp2.PIO.SHIFT_RIGHT)  # defines the number of GPIO pins to use,

def pioProg():  ## to get a loop:   if use jump () and the target would each use a full line of instruction.  wrap() to target is more efficieint
    set(x,0b0101)
    in_(x,3)
    set(x,0b1)
    in_(x,1)
    mov(x,isr)
    wrap_target()
    
#     ##option 1
    ## when do a mov(), the value also stays in the original site
    mov(osr,x)  ## the x value stays in x and here it is moved to osr as the target.
    out(pins,6)
#     ## option 2 does the same but does not use the 'osr'  the out shift register
#     mov(pins,x)     ##alternatively  can move the value in x directly to the pins, same outcome 
    
    wrap()

### below moves (the above @rp2. ... if 'HIGH', from the x  to osr and then wrap_target, then the out(pins,4) moves it all to the pins and empties the osr 
### the below shows when out( the osr is emptied and only flashes once if the osr is not reloaed each cycle.
#   however , with mov(pins,x) we don;t need the osr relaoded sichne we are just using a copy of x each cycle.)
# def pioProg():
#     set(x,0b111111)
#     wrap_target()  ## if the wrap target is here, then the osr is reloaded each time trhough the cycle
#     mov(osr,x)      ### moves x to osr ## i found that i could comment this out, i think I'm just skipping loading the OSR
#     # wrap_target()## if the wrap_target is left here. the osr is loaded with x only one time!! it flashes the first time throughthe loop

#     # mov(pins,x)   
#     out(pins,6)     ### out clears the osr and put the osr value to pins with an out, the osr is now empty, so this is a loop because the osr keeps getting freshly reloaed with  the value in x, the number is how many pins to be used
#     wrap()
### sm0 is instantiating the satemenachine object, using SM 0 put can go all the way to SM 7 
##   note that set_base is changed to out_base   
sm0 = rp2.StateMachine(0, pioProg,freq=2000, out_base=Pin(16))
try:
    while True:
        for i in range(4):
            time.sleep(.5)
            print(i) 
        sm0.active(1)   
except KeyboardInterrupt:
    sm0.active(0)
    print('All Done')
'''
# rp2.asm_pio(*, out_init=None, set_init=None, sideset_init=None, in_shiftdir=0, out_shiftdir=0, autopush=False, autopull=False, push_thresh=32, pull_thresh=32, fifo_join=PIO.JOIN_NONE)
###############3d part of lesson 87 on StateMachine, here we PULL data from the tx_fifo()

import time
from machine import Pin
import rp2   ## the   @ is  'decorator' and alerts that we are programming the state machine
### Note that I have changed the 'set' to 'out'.  below is the 'decorator'

ledPin=13
Led=Pin(13,Pin.OUT)
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5, out_shiftdir=rp2.PIO.SHIFT_RIGHT)  # defines the number of GPIO pins to use,
## want to pull data into the OSR of the stateMachine!! below
def pioProg():          ## note the pull() and push() to move data in and out of the FIFO to and from the stateMachine. Note that the original data was placed into the FIFO TX by the put() and then processed data the end & retrieved by the  get() function
    wrap_target()           ### not setting a value in the program and will start with wrap
    ## step 2: the stateMachine is pulling the data int the stateMachine
    pull()      ## when pull the data in the fifo is pulled into the osr, if there is data in the FIFO the pull()will pull one word at a time
    mov(x,osr)      # step 3: we are moving the data from the OSR to 'x' then and from x to the 'ISR', and then to the pins
    mov(isr,x)## the pulled data to the OSR is moved to the x
    mov(pins,x)
    push()          ## step 4:  the isr pushes the data from the stateMachine to the FIFO RX
    wrap()
    

### sm0 is instantiating the satemenachine object, using SM 0 put can go all the way to SM 7 
##   note that set_base is changed to out_base 
## we  need to put data in from the python program  
sm0 = rp2.StateMachine(0, pioProg,freq=2000, out_base=Pin(16))
sm0.active(1)
try:
    # while True:
    #     for i in range(16):
    #         # sm0.put(i)
    #         time.sleep(.5)
    #         print(i) 
    #     # sm0.active(1)## when this is here, nothon happens, have to be before this for loop
    #     time.sleep(1)
    #     sm0.active(0)  ## the statemachine is left in the condition in which it was left even though it is not runnung
   
    while True:
        for i in range(16):
            sm0.put(i)      ## step one:  getting a value (here 0 to 15 and then putting it into the stateMachine)
            # print('TX: ',sm0.tx_fifo())
            # print('RX: ',sm0.rx_fifo())
            a=sm0.get() ##step 5: once the data has been pushed to the RX FIFO, we then 'get()' the data to the Python program and use it
            
            if a%2==0:
                Led.toggle()
                print('Toggle on: ',a) ## this would have to be different pin (not one of 16-19)
            time.sleep(.5)
            # print(i)
            print(a) 
        # sm0.active(1)## when this is here, nothon happens, have to be before this for loop
        time.sleep(1)
        sm0.active(0)

except KeyboardInterrupt:
    sm0.active(0)
    print('All Done')

