'''
lesson 94 
1- create a sumple two button counter to switch between to x values
'''
# import rp2
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     wrap_target()
#     label('readAgain')
#     mov(isr,null)
#     in_(pins,2)
    
#     nop()[31]
#     nop()[31]
#     mov(x,isr)
#     jmp(not_x,'readAgain')
#     set(y,0b01)
#     jmp(x_not_y,'checkRed')
#     set(y,0b1010)
#     mov(pins,y)
#     jmp('readAgain')   
#     label('checkRed')
#     set(y,0b10)
#     jmp(x_not_y,'readAgain')
#     set(y,0b0101)
#     mov(pins,y)
#     jmp('readAgain')  
#     wrap()

# pin14=Pin(14,Pin.IN,Pin.PULL_DOWN)    
# pin15=Pin(15,Pin.IN,Pin.PULL_DOWN)    
# sm0=rp2.StateMachine(0,pioProg,2000,in_base=pin14,out_base=Pin(16,Pin.OUT))
# sm0.active(1)
# while True:
#     pass

##~~~~~~~~~~~~~~~~~~~~~~~
import rp2
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    wrap_target()
    label('readAgain')
    mov(isr,null)
    in_(pins,2)
    nop()[31]
    nop()[31]
    mov(x,isr)
    jmp(not_x,'readAgain')
    ## not_x jumps if nothing in x, if x = 0,  same not_y for y =o
    ## x_not_y  jumps if x is not = to y
    ## x_dec   loops if x is not zero, then decrements
    ## input pin, jump if pin is not zero. 
    ##  not_osre  jumps if OSR is empty
    set(y,0b01)
    jmp(x_not_y,'checkBlue')
    set(y,0b0101)
    mov(pins,y)
    jmp('readAgain')
    
    label('checkBlue')
    set(y,0b10)
    jmp(x_not_y,'readAgain')
    set(y,0b1010)
    mov(pins,y)
    jmp('readAgain')
    wrap()
pin14=Pin(14,Pin.IN,Pin.PULL_DOWN)
pin15=Pin(15,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,pioProg,2000,in_base=pin14,out_base=Pin(16,Pin.OUT))
sm0.active(1)
while True:
    pass