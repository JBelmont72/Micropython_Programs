## lesson 92 simple toggle switch minute 13, minute 25 for making it a toggle


'''
import rp2
import time
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def wait_pin_low():
    set(x,0b00000)
    wrap_target()
    # wait(polarity, src,index)
    # Polarity wating for a 0 or a 1
    # SRC  looking at the source for the polarity which can be a gpio pin, or a Pin, or an irq interrupt,
    ## the Pin parameter is relative to the in-base pin, can be 0, 1,2 etc
    # index   parmeter for the source.  woujld be the GPIO_Pin number or the 0,1,2 etc if a Pin for the src
    wait(1,pin,0)

    nop()[31] ## 16 milliseconds
    nop()[31]  ## another 16 milliseconds ot debounce the switch woth 32 milliseconds
    
    mov(x,invert(x))
    mov(pins,x)
    wait(0,pin,0)
    nop()[31] ## 16 milliseconds
    nop()[31]  ## another 16 milliseconds ot debounce the switch woth 32 milliseconds
    wrap()
pin15 = Pin(15,Pin.IN,Pin.PULL_DOWN)    
sm0=rp2.StateMachine(0,wait_pin_low, in_base=Pin(14,Pin.PULL_DOWN),    freq=2000,out_base=Pin(16)) ## note that the input pin is instantiated here
sm0.active(1)
'''
##buttonm controlled binary counter
'''
import rp2
import time
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def wait_pin_low():
    #set(x,0b00000)
    #wrap_target()
    # wait(polarity, src,index)
    # Polarity wating for a 0 or a 1
    # SRC  looking at the source for the polarity which can be a gpio pin, or a Pin, or an irq interrupt,
    ## the Pin parameter is relative to the in-base pin, can be 0, 1,2 etc
    # index   parmeter for the source.  woujld be the GPIO_Pin number or the 0,1,2 etc if a Pin for the src

    wrap_target()
    set(x,0b1111)
    label('bitLoop')
    #mov(pins,x)
    mov(pins,invert(x))
    wait(1,pin,0)
    nop()[31]
    nop()[31]
    wait(0,pin,0)
    nop()[31]
    nop()[31]
    jmp(x_dec,'bitLoop')
    wrap()

pin15 = Pin(15,Pin.IN,Pin.PULL_DOWN)    
sm0=rp2.StateMachine(0,wait_pin_low, in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),    freq=2000,out_base=Pin(16)) ## note that the input pin is instantiated here
sm0.active(1)
'''

'''
count down button counter,  count up if use mov(pins,invert(x))
lesson93
'''
'''
import rp2
from machine import Pin

@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    #set(x,0b0000)   ## for a SIMPLE  switch having gthe set here was fine, but if need to change it, then needs to be in loop
    wrap_target()
    set(x,0b1111)
    label('loop')
    mov(pins,invert(x))		## the invert makes it a count up binary
    wait(1,pin,1)
    nop()[31]
    nop()[31]
    wait(0,pin,1)
    nop()[31]
    nop()[31]
    jmp(x_dec,'loop')
    wrap()
    
## if I use StateMachine.init() I get help with all the parameters and then delete the 'init'
But15=Pin(15,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,pioProg,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),freq=2000,out_base=Pin(16))
sm0.active(1)
#####
### lesson92 wait button control TOGGLE
'''
'''
import rp2
from machine import Pin

@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    set(x,0b0000)
    wrap_target()
    wait(1,pin,1)
    nop()[31]
    nop()[31]
    mov(x,invert(x))
    mov(pins,x)
    wait(0,pin,1)
    nop()[31]
    nop()[31]
    wrap()
    
## if I use StateMachine.init() I get help with all the parameters and then delete the 'init'
But15=Pin(15,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,pioProg,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),freq=2000,out_base=Pin(16))
sm0.active(1)
'''

