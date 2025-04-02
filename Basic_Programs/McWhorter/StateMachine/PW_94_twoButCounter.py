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
#     ## not_x jumps if nothing in x, if x = 0,  same not_y for y =o
#     ## x_not_y  jumps if x is not = to y
#     ## x_dec   loops if x is not zero, then decrements
#     ## input pin, jump if pin is not zero. 
#     ##  not_osre  jumps if OSR is empty
#     set(y,0b01)
#     jmp(x_not_y,'checkBlue')
#     set(y,0b0101)
#     mov(pins,y)
#     jmp('readAgain')
    
#     label('checkBlue')
#     set(y,0b10)
#     jmp(x_not_y,'readAgain')
#     set(y,0b1010)
#     mov(pins,y)
#     jmp('readAgain')
#     wrap()
# pin14=Pin(14,Pin.IN,Pin.PULL_DOWN)
# pin15=Pin(15,Pin.IN,Pin.PULL_DOWN)
# sm0=rp2.StateMachine(0,pioProg,2000,in_base=pin14,out_base=Pin(16,Pin.OUT))
# sm0.active(1)
# while True:
#     pass

######## make two button control and then counter
# import rp2
# import sys
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)

# def pioProg():
#     wrap_target()
#     label('readAgain')
#     mov(isr,null)
#     in_(pins,2)
#     mov(x,isr)
#     jmp(not_x,'readAgain')
#     set(y,0b10)
#     jmp(x_not_y,'checkRed')## if y 10 does not equal x from the pins then it must be 1 or 11
#     set(y,0b1010)
#     mov(pins,y)
#     jmp('readAgain')
    
#     label('checkRed')
#     set(y,0b01)
#     jmp(x_not_y,'readAgain')## this covers if the pins are not 01 (could be 11 if both pushed)
#     set(y,0b0101)
#     mov(pins,y)
#     jmp('readAgain')
#     wrap()
# RedBut=Pin(15,Pin.IN,Pin.PULL_DOWN)  
# sm0= rp2.StateMachine(0,pioProg,freq=2000,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),out_base=Pin(16,Pin.OUT))
# sm0.active(1)
# try:
#     while True:
#         pass
# except KeyboardInterrupt:
#     sm0.active(0)
#     sys.exit()
import rp2 ## this works great
import sys
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    set(y,0b1111)
    wrap_target()
    # set(y,0b1111) either location should be good since it always runs between the readagain 
    label('readAgain')
    mov(isr,null)
    in_(pins,2)
    nop()[31]
    nop()[31]
    mov(x,isr)
    jmp(not_x,'readAgain')
    mov(osr,y)## i am storing the y value in OSR and will retrieve it as necessary
    set(y,0b10)
    jmp(x_not_y,'checkRed')## if y 10 does not equal x from the pins then it must be 1 or 11
    mov(y,osr)
    
    jmp(y_dec,'decrement')
    label('decrement')
    
    wait(0,pin,1)
    nop()[31]
    nop()[31]
    mov(pins,y)
    # mov(osr,y) ## do not need it since it is above when the readAgain occurs
    jmp('readAgain')
    
    label('checkRed')
    set(y,0b01)
    jmp(x_not_y,'readAgain')## this covers if the pins are not 01 (could be 11 if both pushed)
    mov(y,osr)
    mov(y,invert(y))
    jmp(y_dec,'increment') ## this does increment 
    label('increment')
    mov(y,invert(y))
    wait(0,pin,0)
    nop()[31]
    nop()[31]
    
    mov(pins,y)
    jmp('readAgain')
    wrap()
RedBut=Pin(15,Pin.IN,Pin.PULL_DOWN)  
sm0= rp2.StateMachine(0,pioProg,freq=2000,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),out_base=Pin(16,Pin.OUT))
sm0.active(1)
try:
    while True:
        pass
except KeyboardInterrupt:
    sm0.active(0)
    sys.exit()
### below working up down counter   
# import rp2
# from time import sleep
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     set(y,0b1111)
#     wrap_target()
#     label('readAgain')
#     # mov(osr,y) ## okay to have almost anywhere before it is first used. maintains active count
#     mov(isr,null)   
#     in_(pins,2)
#     nop()[31]
#     nop()[31]
#     mov(x,isr)
#     jmp(not_x,'readAgain')
#     mov(osr,y)
#     set(y,0b0001)
#     jmp(x_not_y,'checkBlue')
#     mov(y,osr)
#     # wait(1,pin,0)
#     nop()[31]
#     nop()[31]
#     # wait(0,pin,0)
#     ## note inverted y then decremented and then inverted again, and THEN moved the twice inverted y to pins!!!!!!!
#     mov(y,invert(y)) ## is y is 0010 then invert is 1101, then dec to 1100, invert to 0011 and show in pins 
    
#     jmp(y_dec,'dec')
#     label('dec')
#     mov(y,invert(y))
#     wait(0,pin,0)
#     mov(pins,y)
#     jmp('readAgain')
    
    
    
#     label('checkBlue')
#     set(y,0b0010)
#     jmp(x_not_y,'readAgain')
#     mov(y,osr)
#     jmp(y_dec,'next')
#     label('next')
#     # wait(1,pin,1)
#     nop()[31]
#     nop()[31]
#     wait(0,pin,1)
#     mov(pins,y)
#     wrap()
# blue15=Pin(15,Pin.IN,Pin.PULL_DOWN)
# red14=Pin(14,Pin.IN,Pin.PULL_DOWN)    
# sm1=rp2.StateMachine(0,pioProg,in_base=Pin(14),freq=2000,out_base=Pin(16,Pin.OUT))
# sm1.active(1)
# while True:
#     pass