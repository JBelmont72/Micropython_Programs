'''PW95
my attempt at binary counter on one pin(pin 14 which is 0b0001).  
0b1111 which we will invert  and use dec_ to make a count up binary counter. 
Reset to 0b000- with pin 15 ( y=0b0010), check PW 95 binary counter with reset
'''
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