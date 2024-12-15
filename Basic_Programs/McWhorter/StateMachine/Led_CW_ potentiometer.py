'''
lesson 92 PW
https://www.youtube.com/watch?v=ob80LODRleo

#set(y,0b1111)[31]  ## note that for this inside loop to use the set value, it must be inside the outer loop!!!
to slow timer
    mov(isr,y)
    in_(y,1)
    in_(y,1)
    mov(y,isr)

another option not as great in potential is:
   label('delay')
    nop() [31]
    jmp(y_dec,'delay')
'''
###this is from lesson 91 with slowing of the minary counter
'''
import rp2
import time
from machine import Pin
## decorator
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    #set(x,0b1111)
    wrap_target()
    set(x,0b1111)
    label('bitLoop')
    mov(pins,invert(x))[31]## invert is count up, not invert is countdown witht he dec_ function
    nop()[31]
    set(y,0b11111)[31]
    #set(y,0b1111)[31]  ## note that for this inside loop to use the set value, it must be inside the outer loop!!!
    
    mov(isr,y)
    in_(y,2)
    in_(y,2)
    mov(y,isr)
    nop()[31]
    nop()[31]
    label('delay')
    nop() [31]
    jmp(y_dec,'delay')
    nop()[31]
   
    jmp(x_dec,'bitLoop')[31]
    wrap()
    
    
sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
sm0.active(1)
'''
## lesson 92 simple toggle switch minute 13
import rp2
import time
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def wait_pin_low():
    set(x,0b01111)
    wrap_target()
    # wait(polarity, src,index)
    # Polarity wating for a 0 or a 1
    # SRC  looking at the source for the polarity which can be a gpio pin, or a Pin, or an irq interrupt,
    ## the Pin parameter is relative to the in-base pin, can be 0, 1,2 etc
    # index   parmeter for the source.  woujld be the GPIO_Pin number or the 0,1,2 etc if a Pin for the src
    wait(1,pin,0)
    nop()[31] ## 16 milliseconds
    nop()[31]  ## another 16 milliseconds ot debounce the switch woth 32 milliseconds
    mov(pins,x)
    
    wrap()
sm0=rp2.StateMachine(0,wait_pin_low, in_base=Pin(15,Pin.PULL_DOWN),    freq=2000,out_base=Pin(16)) ## note that the input pin is instantiated here
sm0.active(1)
'''

'''
### countdown timer


import rp2
import time
from machine import Pin
## decorator
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    wrap_target()
    set(x,0b1111)[31]
    label('bitloop')
    #mov(pins,x)[31]## for countdown
    mov(pins,invert(x))[31]	## for count up binary timer
    nop()[31]	##1
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
    set(y,0b0001)[31]
    mov(isr,y)
    in_(y,1)
    in_(y,1)
    mov(y,isr)##NED THIS inoder to shift the large nmberfrom the isr back to the y which is hte ounter!!
    label('dloop')
    nop()[31]		#1
    jmp(y_dec,'dloop')
    nop()[31]

    #nop()       [31]
    #nop()       [31]	##14
    jmp(x_dec,'bitloop')[31]
    wrap()
sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
sm0.active(1)
'''
### minute 37-40 of lesson 90 multiplying and adding  at minute 40 says cab add 2 or 3


'''
import rp2
import time
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    wrap_target()
    set(y,0b0011)
    pull()
    mov(x,osr)
    mov(isr,x)
    in_(y,1)
    mov(x,isr)
    #set(x,0b01010)
    mov(pins,x)
    push()
    wrap()
    
    
    
    
sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
sm0.active(1)
try:
    while True:
        x = int(input('enter your number'))
        print('your nuumber is: ',x)
        sm0.put(x)
        time.sleep(0.01)
        y = sm0.get()
        print('your double number is: ',y)
        
except KeyboardInterrupt:
    sm0.active(0)
    print('all done')
'''