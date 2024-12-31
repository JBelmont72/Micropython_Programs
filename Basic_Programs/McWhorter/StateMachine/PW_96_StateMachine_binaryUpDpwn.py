'''run on thonny
lesson 96  two button up down binary counter
TO Increment need to 1- invert, 2- decrement, 3- invert

ob0110  starting point
invert to 0b1001
decrement to 0b1000
3d step is to invert to 0b0111  which gives us an increment from the startin point
NOTE that we are skipping the first step by starting with the inverse of 0b0000 by 
using 0b1111, then we decrement(0b1110) and then invert(0b0001) for example in the first go around

'''
## thie first program is a count jup on pin 14 and reset on pin 15
## the second program is the binary bi0-directional counter
# import time
# import rp2
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def binaryCount():
#     set(y,0b1111)		## start at ob1111 because in PIO we can only DECREMENT, we will invert when we move to the LED PINS   
#     wrap_target()
#     label('readAgain')
#     mov(isr,null)		## clears the input shift register
#     in_(pins,2)			## references the button Pins, 01 is pin 14 and 10 is pin 15
#     nop()[31]			## each cycle is 0.5 milliseconds  
#     nop()[31]			##  both add up to 64 clock cycles which is 32 milliseconds
#     mov(x,isr)			##  the x register has the input pin 01 or 10 or the NULL 00
#     jmp(not_x,'readAgain') ## if nothing in x then we read again from label('readAgain')
    
#     mov(osr,y)  		## we move the y value of 0b1111 to the OSR to get it out of the way temporarily
#     set(y,0b0001)
#     jmp(x_not_y,'checkGreen')
#     mov(y,osr)
    
#     jmp(y_dec,'next')	## this gets the decrement going (which below will be inverted to make it a count up binary)
#     label('next')		##needed to do this inorder to use the jmp and the y-dec comm
    
#     wait(0,pin,0)
    
#     mov(pins,invert(y))
#     jmp('readAgain')
#     label('checkGreen')
    
#     #wait(0,pin,1)   ## this makes the green(pin15) turn off  0b0000 on button release, otherwise turn off on button press
    
#     set(y,0b0010)
#     wait(0,pin,1)  ## wait works here as well, it makes sense
#     jmp(x_not_y,'readAgain')
#     set(y,0b0000)
#     mov(pins,y) 
#     irq(rel(0)) 
#     wrap()
# but15=Pin(15,Pin.IN,Pin.PULL_DOWN)
# sm0=rp2.StateMachine(0,binaryCount,freq= 2000,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),out_base=Pin(16,Pin.OUT))
# sm0.active(1)

# # Set the IRQ handler to print the millisecond timestamp.
# sm0.irq(lambda p: print(time.ticks_ms()))
###~~~~~~~~~~~binary button controlled counter
## lesson 96 Paul McWhorter
## if 10 want to increment(pin 15), if 01 want to decrement (Pin14), y register is the  active count
import time
import rp2
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def binaryCount():
    set(y,0b1111)		## start at ob1111 because in PIO we can only DECREMENT, we will invert when we move to the LED PINS   
    wrap_target()
    label('readAgain')
    mov(isr,null)		## clears the input shift register
    in_(pins,2)			## references the button Pins, 01 is pin 14 and 10 is pin 15
    nop()[31]			## each cycle is 0.5 milliseconds  
    nop()[31]			##  both add up to 64 clock cycles which is 32 milliseconds
    mov(x,isr)			##  the x register has the input pin 01 or 10 or the NULL 00
    jmp(not_x,'readAgain') ## if nothing in x then we read again from label('readAgain')
    ## save the active count which is y in the osr register
    mov(osr,y)  		## we move the y value of 0b1111 to the OSR to get it out of the way temporarily
    set(y,0b0001)
    jmp(x_not_y,'increment')
    ## if end up here then in the 'decrement' portion
    ## can put the wait(0,pin,0) here or lines down 
    mov(y,osr)  ## retreive the active count
    jmp(y_dec,'next')	## this gets the decrement going (which below will be inverted to make it a count up binary)
    label('next')		##needed to do this inorder to use the jmp and the y-dec comm
    
    wait(0,pin,0)
    mov(pins,y)## this decrements with Pin 14 (red button)
    #mov(pins,invert(y))## this increments the red button pin 14v
    jmp('readAgain')
    label('increment')   
    wait(0,pin,1)   ## this makes the green(pin15) turn off  0b0000 on button release, otherwise turn off on button press
    set(y,0b0010)
    wait(0,pin,1)  ## wait works here as well, it makes sense
    jmp(x_not_y,'readAgain')
    mov(y,osr)
    mov(y,invert(y))
    jmp(y_dec,'inc')
    label('inc')
    mov(y,invert(y))
    
 #set(y,0b0000)
    mov(pins,y)
    
    irq(rel(0)) 
    wrap()
but15=Pin(15,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,binaryCount,freq= 2000,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),out_base=Pin(16,Pin.OUT))
sm0.active(1)

# Set the IRQ handler to print the millisecond timestamp.
sm0.irq(lambda p: print(time.ticks_ms()))
while True:
    pass