'''PW95
my attempt at binary counter on one pin(pin 14 which is 0b0001).  
0b1111 which we will invert  and use dec_ to make a count up binary counter. 
Reset to 0b000- with pin 15 ( y=0b0010), check PW 95 binary counter with reset

Lesson94 minute 27 discusses the jump command
jmp(not_x,not_y,x_not_y,x_dec,y_dec)
also: jmp(pin,'  ') jumps if pin is not zero, if a 1 then jumps
      jmp(not_osre, '')  jumps if the osr is empty
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
###~~~~~~~~~~~~~~~~~~~~~~

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

### dec 11th, 

# import rp2
# from machine import Pin
# import time
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     set(y,0b11111)
#     wrap_target()
#     label('readAgain')
#     mov(isr,null)
    
#     in_(pins,2)
#     nop()[31]#16 milliseconds
#     nop()[31]#32 delays of 1/2 millisecond
#     mov(x,isr)## storing isr in x, each new button press goes in the isr
#     jmp(not_x,'readAgain')     ## if zero then read again
#     mov(osr,y)## moving y to OSR so that it is safe and we can use the y for manipulations
#     set(y,0b0001)
#     jmp(x_not_y,'checkGreen')
#     ## this section means that re d pin14 was PRESSED, x is y here
#     ## need to retrieve the y from the osr so it can be used here
#     mov(y,osr)
#     ## y is the present active count
#     ## now want to decrement the y
#     jmp(y_dec,'nxt')
#     label('nxt') # y is now decremented
#     wait(1,pin,0)
#     nop()[31]
#     nop()[31]
#     wait(0,pin,0)
#     mov(pins,invert(y))## we now move the inverse of y because we want to count up in the leds
#     ## gone from ob1111 to ob1110 and then inverted to 0b0001 for first but push
#     jmp('readAgain')  
#     label('checkGreen')
#     set(y,0b0010)
#     jmp(x_not_y,'readAgain')## remember the x is the value fromthe pins   
#     set(y,0b11111)
#     mov(pins,invert(y))    
#     # mov(y,osr)
#     # mov(pins,y_dec)  
#     wrap()
# But14=Pin(14,Pin.IN,Pin.PULL_DOWN)
# But15=Pin(15,Pin.IN,Pin.PULL_DOWN)
# sm0=rp2.StateMachine(0,pioProg,in_base=Pin(14),freq=2000,out_base=Pin(16))
# # sm0=rp2.StateMachine.init()
# ## each clock cycle is 0.5 milliseconds at freq 2000
# sm0.active(1)
# while True:
#     pass
#######~~~~~~~~28 dec 2024 the below is same as above but a good reminder of my mistake noted below
### this count up or down (plus invert or not) and the bluue button pin 15 turns on a set value
# import rp2
# from time import sleep
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     set(y,0b1111)
#     wrap_target()
#     label('readAgain')
#     mov(osr,y) ## okay to have almost anywhere before it is first used. maintains active count
#     mov(isr,null)   
#     in_(pins,2)
#     nop()[31]
#     nop()[31]
#     mov(x,isr)
#     jmp(not_x,'readAgain')
#     # mov(osr,y)  ## osr maintains my current value of y 
#     set(y,0b0001)   # this sets us up to look at pin 14
#     jmp(x_not_y,'checkBlue') ## if x is not 0b0001, go down and check if it is 0b0010
    
#     mov(y,osr)
#     jmp(y_dec,'jump')   ## this was the problem
#     label('jump')
#     # jmp(y_dec,'jump') ## NOTE when i had this reversed, I was getting a complete instant count down and it failed.
#     wait(1,pin,0)
#     nop()[31]
#     nop()[31]
#     wait(0,pin,0)
#     mov(pins,y)
  
#     jmp('readAgain')
#     label('checkBlue')
#     set(y,0b0010)## i think i could delete this for this program but 
#     ##  maybe if i had a third pin 0b0011 i would need it
#     jmp(x_not_y,'readAgain')
#     set(y,0b1110)
#     mov(pins,invert(y))
#     wrap()
# blue15=Pin(15,Pin.IN,Pin.PULL_DOWN)
# red14=Pin(14,Pin.IN,Pin.PULL_DOWN)    
# sm1=rp2.StateMachine(0,pioProg,in_base=Pin(14),freq=2000,out_base=Pin(16,Pin.OUT))
# sm1.active(1)
# while True:
#     pass
######### used the above and modified it to an up down counter
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
########~~~~~~~
