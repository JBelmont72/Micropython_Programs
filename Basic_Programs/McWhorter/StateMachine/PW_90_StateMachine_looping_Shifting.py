'''
lesson 90 state machine timing, looping, shifting
10 million operations per second
first program is supposed to blink, I can get it switch only by adjusting he number of operations per second

use the in_, nop(), and instructions on the Raspberry Pi Pico W using micropython and the PIO state machines. 
how to use nop() to control timing on the state machine, and  how to do some simple multiplication by shifting.  how to do  a crude for loop using the jmp() command. 
step by step how to easily exchange data between the PIO state machine and the main python core processor. 

https://micropython-docs.readthedocs.io/en/latest/library/rp2.html
'''
## work with wrap and wrap target,  also inter(x)
# import rp2
# import time
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5, out_shiftdir=rp2.PIO.SHIFT_RIGHT) ## deorat
# ## initializing all the leds to zero
# def pioProg():
#     wrap_target()

#     set(x,0b11111)  [11]
#     mov(pins,x)     [10]
#     # nop()           [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
#     # nop()       [31]
    

#     set(x,0b01010)[31]
#     mov(pins,invert(x))[31]
#     # mov(pins,x)[31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]

#     nop()       [31]
#     nop()       [31]
    
    
#     wrap()
# sm0=rp2.StateMachine(1,pioProg,freq=2000,out_base=Pin(16)) ## instantite thestate machine
# sm0.active(1)

############ multiplying with the in_(y,value)
# import rp2
# import time
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5, out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     wrap_target()
#     pull()
#     set(y,0b00000)  ## by changing this I change what is added to y after the in_ function shifts tot he right the inputted value.
#     mov(x,osr)
#     mov(isr,x)
#     in_(y,1)          ##      in_ is a special command just for the ISR to pull in a vlue to ISR, pulling in one bit, the least siginificant
#     ## if going to pull the least siginifiicant bit into the isr, we will have to have something in the ISR
#     ## it shifts to the left one bit which essentially doubles the number
#     mov(pins,isr)
#     push()   
#     wrap()
# sm0=rp2.StateMachine(0,pioProg,freq=1950,out_base=Pin(16)) ## instantite thestate machine
# sm0.active(1)
# try:
#     while True:
#         pass
#         x =int(input('enter a number'))
#         sm0.put(x)
#         print('')
#         print('your number is: ',x)
#         sm0_TX=sm0.tx_fifo()
#         sm0_RX=sm0.rx_fifo()
#         print(sm0_TX,sm0_RX)
#         G =sm0.get()
#         print('')
#         print('your doubled number is:', G)
#         sm0_TX=sm0.tx_fifo()
#         sm0_RX=sm0.rx_fifo()
#         print(sm0_TX,sm0_RX)
        
        
# except KeyboardInterrupt:
#     print('all done')
############# this count downs by one
# import rp2
# import time
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*6, out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     wrap_target()
#     set(x,0b111111)
#     label('bitLoop')
#     mov(pins,x)
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     jmp(x_dec ,'bitLoop')[31]
#     wrap()
# sm0=rp2.StateMachine(0,pioProg,freq=1950,out_base=Pin(16)) ## instantite thestate machine
# sm0.active(1)
# try:
#     while True:
#         x =int(input('enter a number'))
#         sm0.put(x)
#         print('your number is: ',x)
#         G =sm0.get()
#         print('your doubled number is:', G)
# except KeyboardInterrupt:
#     print('all done')
    
    
    ########## source     https://docs.micropython.org/en/latest/rp2/quickref.html
# from machine import Pin
# import rp2    
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
# def blink_1hz():
#     # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
#     set(pins, 1)
#     set(x, 31)                  [6]
#     label("delay_high")
#     nop()                       [29]
#     jmp(x_dec, "delay_high")

#     # Cycles: 1 + 7 + 32 * (30 + 1) = 1000
#     set(pins, 0)
#     set(x, 31)                  [6]
#     label("delay_low")
#     nop()                       [29]
#     jmp(x_dec, "delay_low")

# # Create and start a StateMachine with blink_1hz, outputting on Pin(25)
# sm = rp2.StateMachine(0, blink_1hz, freq=2000, set_base=Pin(16))
# sm.active(1)  

'''
'''
# lesson 91 PW
# https://www.youtube.com/watch?v=ob80LODRleo
'''

import rp2
import time
from machine import Pin
## decorator
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    wrap_target()
    set(x,0b010101)
    label('bitloop')
    mov(pins,invert(x))[31]
    nop()[31]		##1
    nop()[31]		## this equals 32 X .5MS which is 16 milliseconds
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]		##5
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]		##10
    nop()       [31]
    nop()       [31]
    nop()       [31]		##13
    
    set(x,0b101010)
    mov(pins,invert(x))[31]
    nop()[31]		#1
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]		##5
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]		##10  
    nop()[31]
    nop()       [31]
    nop()       [31]
    nop()       [31]	##14
    #jmp(x_dec,'bitloop')[31]
    wrap()
sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
sm0.active(1)
'''
'''
import rp2
import time
from machine import Pin
## decorator
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    wrap_target()
    pull()
    mov(x,osr)
    #set(x,0b1111)
    label('bitloop')
    mov(pins,x)[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]  
    nop()[31]
    nop()       [31]
    nop()       [31]
    nop()       [31]
    nop()       [31]
    jmp(x_dec,'bitloop')[31]
    wrap()
sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))
sm0.active(1)

while True:
    x=int(input('enter a number:'))
    print('your number is: ',x)
    sm0.put(x)
 
import sys
import rp2
import time
from machine import Pin
bPin=16
rPin =17
yPin=18
gPin=19
Pin5=20
bLed=Pin(bPin,Pin.OUT)
rLed=Pin(rPin,Pin.OUT)
yLed=Pin(yPin,Pin.OUT)
gLed=Pin(gPin,Pin.OUT)
Led5=Pin(Pin5,Pin.OUT)

''' 
# import sys
# import rp2
# import time
# from machine import Pin
# bPin=16
# rPin =17
# yPin=18
# gPin=19
# bLed=Pin(bPin,Pin.OUT)
# rLed=Pin(rPin,Pin.OUT)
# yLed=Pin(yPin,Pin.OUT)
# gLed=Pin(gPin,Pin.OUT)
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
    
#     wrap_target()
#     set(y,0b0000)
#     pull()
#     mov(x,osr)
#     mov(pins,x)
#     mov(isr,x)
#     in_(y,1)
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
    
    
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     mov(pins,isr)
#     push()
#     wrap()
    
# sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))
# sm0.active(1)
# try:
#     while True:
#         x=int(input('Enter Number.')) 
#         sm0.put(x) 
#         print('your number is:',x) 
#         y=sm0.get()
#         print('your number doubled is:',y)
# except KeyboardInterrupt:
#     sm0.active(0)
#     bLed.value(0)
#     rLed.value(0)
#     gLed.value(0)
#     yLed.value(0)
#     print('\nprogram ended')
#     sys.exit()
############# This was a up binary counter using mov(isr,y) and in_(y,0) which I commneted out parts and made a button controlled up counter
import sys
import rp2
import time
from machine import Pin
bPin=16
rPin =17
yPin=18
gPin=19
Pin5=20
bLed=Pin(bPin,Pin.OUT)
rLed=Pin(rPin,Pin.OUT)
yLed=Pin(yPin,Pin.OUT)
gLed=Pin(gPin,Pin.OUT)
Led5=Pin(Pin5,Pin.OUT)
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    wrap_target()  
    set(x,0b11111)
    label('loop')
    wait(1,pin,0)
    nop()[31]
    nop()[31]
    mov(pins,invert(x))
    # set(y,0b11111)[31] ## y value has to be set inside loop because it is being decremented inside each 'bitLoop'
    # mov(isr,y)    
    # in_(y,5)
    # mov(y,isr) 
    wait(0,pin,0)
    nop()[31]
    # label('bitLoop')
    # nop()[31]
    # jmp(y_dec,'bitLoop')   
    nop()[31]
    jmp(x_dec,'loop')
    wrap()
   
sm0=rp2.StateMachine(0,pioProg,in_base=Pin(15,Pin.IN,Pin.PULL_DOWN),freq=2000,out_base=Pin(16))
sm0.active(1)
try:
    while True:
        pass
except KeyboardInterrupt:
    
    bLed.value(0)
    rLed.value(0)
    gLed.value(0)
    yLed.value(0)
    Led5.value(0)
    sm0.active(0)
    print('\nprogram ended')
    sys.exit()