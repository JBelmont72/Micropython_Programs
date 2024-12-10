'''
timing
'''
## make a conditional loop with a count up binary counter and slowed  the loop
import rp2
import time
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)

def pioProg(): 
    wrap_target()
    set(x,0b1111)[31]
    label('bitloop')
    
    mov(pins,invert(x))
    set(y,0b11111)
    mov(isr,y)
    in_(y,1)
    mov(y,isr)
    label('timeloop')
    nop()[31]
    jmp(y_dec,'timeloop')
    nop()[31]
    nop()[31]
 
    jmp(x_dec,'bitloop')[31] 
    wrap() 

sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16,Pin.OUT))
sm0.active(1)
while True:
    pass
## i can shift the bytes to the left to double,quadruple etc and can add as well.
# import rp2
# from time import sleep
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)

# def pioProg():
#     wrap_target()
#     pull()
#     mov(x,osr)
#     mov(isr,x)
#     set(y,0b0010)
#     in_(y,2)
#     out(pins,isr)    

#     push()
#     wrap() 

# sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16,Pin.OUT))
# sm0.active(1)
# while True:
#     x =int(input('enter number'))
#     print('your number is: ',x)
#     sm0.put(x)
#     y=sm0.get()
#     print('doubled number is:  ',y)