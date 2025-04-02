
'''
lesson 92 PW
https://www.youtube.com/watch?v=ob80LODRleo
'''
# import rp2
# import time
# from machine import Pin
# ## decorator
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     wrap_target()
#     set(x,0b1111)
#     label('dooLoop')
#     mov(pins,invert(x))[31]
    
#     set(y,0b1111)[31]


#     mov(isr,y)
#     in_(y,1)
#     #in_(y,4)
#     mov(y,isr)
#     label('loop')
#     # label('delay')##commented these when I run it in vscode
#     nop()[31]
#     jmp(y_dec,'loop')
    
#     jmp(x_dec,'dooLoop')
#     wrap()
    
    # wrap_target()
    # set(x,0b1111)
    # label('dooLoop')
    # mov(pins,invert(x))[31]
    
    # set(y,0b1111)[31]


    # mov(isr,y)
    # in_(y,1)
    # mov(y,isr)
    # # label('delay')##commented these when I run it in vscode
    # # nop()[31]
    # # jmp(y_dec,'delay')
    
    # jmp(x_dec,'dooLoop')
    # wrap()
    
    

    # wrap_target()
    # set(x,0b11111)
    # label('delay')
    # mov(pins,invert(x))
    # #label('delay')## NOTE THIS MUST BE AFTER THE WRAPTARGET BUT BEFORE THE MOV(pins<invert(x))
    # set(y,0b11111)[31]
    # #label('moreDelay')
    # mov(isr,y)
    # in_(y,1)
    # in_(y,1)
    # mov(y,isr)
    # label('moreDelay')
    # nop()[31]
    # #nop()[31]
    # #nop()[31]
    # #nop()[31]
    # jmp(y_dec,'moreDelay')
    # nop()[31]
    # nop()[31]
    # nop()[31]
    # nop()[31]
    # nop()[31]
    # nop()[31]
    # #mov(pins,invert(x))		## for count up timer use the invert
    # jmp(x_dec,'delay')
  
    
    
    
    
    # wrap_target()
    # pull()
    # set(y,0b00000)  ## by changing this I change what is added to y after the in_ function shifts tot he right the inputted value.
    # mov(x,osr)
    # mov(isr,x)
    # in_(y,1)          ##      in_ is a special command just for the ISR to pull in a vlue to ISR, pulling in one bit, the least siginificant
    # ## if going to pull the least siginifiicant bit into the isr, we will have to have something in the ISR
    # ## it shifts to the left one bit which essentially doubles the number
    # mov(pins,isr)
    # push()   
    # wrap()
    
    
# sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
# sm0.active(1)

'''
import rp2
import time
from machine import Pin
## decorator
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    wrap_target()
    pull()
    mov(x,osr)
    # set(x,0b1111)[31]
    label('bitloop')
    mov(pins,x)
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

'''
### countdown timer
# import rp2
# import time
# from machine import Pin
# ## decorator
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     wrap_target()
#     set(x,0b1111) ## the invert makes it 0000  at bottom x is now 1110 new invert is 0001
#     label('bitloop')
#     # mov(pins,x)[31]## for countdown
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
#     set(y,0b1111)[31]
#     mov(isr,y)
#     in_(y,1)
#     # in_(y,1)
#     mov(y,isr)##NEED THIS in order to shift the large number from the isr back to the y which is the counter!!
#     label('dloop')
#     nop()[31]		#1
#     jmp(y_dec,'dloop')
#     nop()[31]

#     #nop()       [31]
#     #nop()       [31]	##14
#     jmp(x_dec,'bitloop')[31]
#     wrap()
# sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=Pin(16))###	if made freq 10million  precision of o.1 micrixseconds
# sm0.active(1)
# while True:
#     pass

## count up binarry counter
import rp2
import sys
from machine import Pin

@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)

def pioProg():
    wrap_target()
    set(x,0b1111)
    label('bitLoop')
    mov(pins,invert(x))
    set(y,0b1111)
    mov(isr,y)
    in_(y,4)
    mov(y,isr)
    label('timer')
    nop()[31]
    jmp(y_dec,'timer')
    jmp(x_dec,'bitLoop')

    wrap()

sm0=rp2.StateMachine(0,pioProg,freq=2000,out_base=(Pin(16))) 
sm0.active(1) 
try:
    while True:
        pass
except KeyboardInterrupt:
    sys.exit()