'''
lesson 91 PW
https://www.youtube.com/watch?v=ob80LODRleo
'''

# import rp2
# import time
# from machine import Pin
# ## decorator
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     wrap_target()
#     set(x,0b11111)
#     label('bitloop')
#     mov(pins,invert(x))[31]
#     nop()[31]		##1
#     nop()[31]		## this equals 32 X .5MS which is 16 milliseconds
#     nop()[31]		#1
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]		##5
#     nop()[31]		##10  
#     nop()[31]
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]	##14
#     jmp(x_dec,'bitloop')[31]
#     wrap()
# sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
# sm0.active(1)
# while True:
#     pass

### this program takes user input and does an up binary counter
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
    mov(pins,invert(x))[31]
    
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
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]
    nop()[31]  
    nop()[31]

    jmp(x_dec,'bitloop')[31]
    push()
    wrap()
sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))
sm0.active(1)
try:
    while True:
        x=int(input('enter a number:'))
        print('your number is: ',x)
        sm0.put(x)
        time.sleep(.01)
        get=sm0.get()
        print('Get value: ',get)
    
except KeyboardInterrupt:
    sm0.active(0)
    print('done')

### countdown timer
# import rp2
# import time
# from machine import Pin
# ## decorator
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     wrap_target()
#     set(x,0b1111)
#     label('bitloop')
#     #mov(pins,x)[31]## for countdown
#     mov(pins,invert(x))[31]	## for count up binary timer
#     nop()[31]	##1
#     nop()[31]		## this equals 32 X .5MS which is 16 milliseconds
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]		##5
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]		##10
#     nop()       [31]
#     nop()       [31]
#     nop()       [31]		##13
    
#     set(y,0b11111)[31]
#     mov(isr,y)
#     in_(y,1)
#     in_(y,1)
#     mov(y,isr)##NEED THIS inoder to shift the large number from the isr back to the y which is hte ounter!!
#     label('dloop')
#     nop()[31]		#1
#     jmp(y_dec,'dloop')
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]		##5
#     nop()[31]
#     nop()[31]
#     #nop()[31]
#     #nop()[31]
#     #nop()[31]		##10  
#     #nop()       [31]
#     #nop()       [31]	##14
#     jmp(x_dec,'bitloop')[31]
#     wrap()
# sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
# sm0.active(1)
# while True:
#     pass

   