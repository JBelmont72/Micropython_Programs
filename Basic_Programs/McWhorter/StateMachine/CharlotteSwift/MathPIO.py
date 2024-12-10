'''
Charlotte Swift lesson 90
I can also add addition
'''
from machine import Pin
from time import sleep
from rp2 import PIO, StateMachine,asm_pio

@asm_pio(sideset_init=None,
         out_init==(PIO.OUT_LOW,) * 4,
         set_init= = None,
         in_shiftdir= 0,
         out_shiftdir= PIO.SHIFT_RIGHT)
def pioProg():
    set(x,11)
    set(y,4)
    label('loop')
    jmp(y_dec,'substract')
    mov(osr,x)
    out(pins,4)
    jmp('loop')
    label('substract')
    jmp(x_dec,'loop')
    
sm0 =StateMachine(0, pioProg, freq=2000,
                  out_base=Pin(16),
                  in_base=0,
                  set_base=None,
                side_set_base=None 
                jmp_pin=None,
                in_shiftdir=None,
                out_shiftdir=None,)
sm0.active(1)