'''
StateMachine ReadMe
Chapter 3 is about the stateMachine
https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf

sample programs
https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio

https://docs.micropython.org/en/latest/library/rp2.StateMachine.html


count down button counter,  count up if use mov(pins,invert(x))
lesson93
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