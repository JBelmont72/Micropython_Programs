
''' 94 two button PIO counter
At bottom I made a three button controlled LED program
in_base: Unknown | None = None,
    out_base: Unknown | None = None,
    set_base: Unknown | None = None,
    jmp_pin: Unknown | None = None,
    sideset_base: Unknown | None = None,
    in_shiftdir: Unknown | None = None,
    out_shiftdir: Unknown | None = None,
    push_thresh: Unknown | None = None,
    pull_thresh: Unknown | None = None
) -> None
Configure the state machine instance to run the given program.

The program is added to the instruction memory of this PIO instance. If the instruction memory already contains this program, then its offset is reused so as to save on instruction memory.

freq is the frequency in Hz to run the state machine at. Defaults to the system clock frequency.

The clock divider is computed as system clock frequency / freq, so there can be slight rounding errors.

The minimum possible clock divider is one 65536th of the system clock: so at the default system clock frequency of 125MHz, the minimum value of freq is 1908. To run state machines at slower frequencies, you'll need to reduce the system clock speed with machine.freq().

in_base is the first pin to use for in() instructions.

out_base is the first pin to use for out() instructions.

set_base is the first pin to use for set() instructions.

jmp_pin is the first pin to use for jmp(pin, ...) instructions.

sideset_base is the first pin to use for side-setting.

in_shiftdir is the direction the ISR will shift, either PIO.SHIFT_LEFT or PIO.SHIFT_RIGHT.

out_shiftdir is the direction the OSR will shift, either PIO.SHIFT_LEFT or PIO.SHIFT_RIGHT.

push_thresh is the threshold in bits before auto-push or conditional re-pushing is triggered.

pull_thresh is the threshold in bits before auto-pull or conditional re-pulling is triggered.

when button on pin 14 is pushed, the value is 0001  (in_(pins,2),
if x from mov(x,isr) is 01, then we exit the readAgainloop and see the y,0b0101.
mov this to the pins and all set for RED, button14.
On the other hand if after we set y to 0b0001, the x value from isr,pins namely ""in_(pins,2)"" is NOT 0b0001, then we jump to
'CheckGreen'
since we know that the value of the input pin (pin15 in this case) is not 0b0001, we check to see if it is 0b0010,
So we set y to 0b0010 and do the read again. This time it passes though all the commands down to y being reset to 0b1010 and then moved to the output pins.

'''
'''Lesson 94 this will use two buttons to switch between values for the leds
wait is a blocking function
but 14 is red and if pressed is 01bits  and but 15 is blue and when pressed is 10 bits
first  we move 2 pins into the isr register with in_(pins,2)
and then mov the isr to x with mov(x,isr)

if bits 00 --readAgain
if bits 01  - Red, but 14  go to block B and set led 0101
if bits 10  - Green but 15 go to block of code A and set LED to 1010


'''
# import rp2
# import time
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def wait_pin_low():    
#     wrap_target()
#     label('readAgain')
    
    
# import rp2
# from machine import Pin

# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def butWatch():
#     wrap_target()
#     label('readAgain')
#     mov(isr,null)
#     in_(pins,2)
#     nop()[31]#0.5 millisec  32 clock cycles is 16 milliseconds
#     nop()[31]#0.5 millisec  32 clock cycles is 16 milliseconds
#     mov(x,isr)
#     jmp(not_x,'readAgain')## if x is zero the program jumps back up to readAgain	1
#     set(y,0b0001)     ## 0001 is the red button (14)								2
#     jmp(x_not_y,'checkGreen')        ## if x is not y then jump,  means that the button push is not pushed.	3
#     ###  since X is NOT Y, we want this section to do what is associated with the Red Button PUSH (which we already set as 0b0001)
#     ### now that we know that the red button (ob0001) was pressed, we set the y register for what we are going to want the PINS to do
#     set(y,0b0101)		##4
    
#     mov(pins,y)
    
#     label('checkGreen') ## note that if x is not zero and x is not y, then x is red
#     set(y,0b0010)
#     jmp(x_not_y,'readAgain')    ## i question if this is necessary
#     set(y,0b1010)
#     mov(pins,y)
#     wrap()
   
# ## if I use StateMachine.init() I get help with all the parameters and then delete the 'init'
# But15=Pin(15,Pin.IN,Pin.PULL_DOWN)
# But14=Pin(14,Pin.IN,Pin.PULL_DOWN)
# ##sm0=rp2.StateMachine(0,butWatch,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),freq=2000,out_base=Pin(16))
# sm0=rp2.StateMachine(0,butWatch,in_base=But14,freq=2000,out_base=Pin(16))
# sm0.active(1)
'''
from machine import Pin
import time
import rp2
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def butWatch():
    wrap_target()
    label('readAgain')
    mov(isr,null)
    in_(pins,2)
    mov(x,isr)
    nop()[31]
    nop()[31]
    jmp(not_x,'readAgain')##green will be 10 and 0101   red will be 01 and 1010
    set(y,0b0001)
    jmp(x_not_y,'checkGreen')
    set(y,0b1010)
    mov(pins,y)
    label('checkGreen')
    set(y,0b0010)
    jmp(x_not_y,'readAgain')
    set(y,0b0101)
    mov(pins,y)
    wrap()
    
    
    
    
But15 =Pin(15,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,butWatch,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),freq=2000,out_base=Pin(16))
sm0.active(1)
'''
###~~~~
'''
import time
import rp2
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def butWatch():
    wrap_target()
    label('readAgain')
    mov(isr,null)
    in_(pins,2)
    nop()[31]
    nop()[31]
    mov(x,isr)
    jmp(not_x,'readAgain')
    set(y,0b0001)   # but 14, red 01  0b1010   but15 green 10 0b0101
    jmp(x_not_y,'checkGreen')
    set(y,0b0000)
    mov(pins,y)
    label('checkGreen')
    set(y,0b0010)
    jmp(x_not_y,'readAgain')
    label('counter')
    set(y,0b1111)
    mov(pins,y)
    jmp(y_dec,'counter')  
    wrap()
but15=Pin(15,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,butWatch,freq= 2000,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),out_base=Pin(16,Pin.OUT))
'''
 ## three buttons to control 4 leds   
import rp2
from machine import Pin

@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*5,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def butWatch():
    wrap_target()
    label('readAgain')
    mov(isr,null)
    in_(pins,2)
    nop()[31]#0.5 millisec  32 clock cycles is 16 milliseconds
    nop()[31]#0.5 millisec  32 clock cycles is 16 milliseconds
    mov(x,isr)
    jmp(not_x,'readAgain')## if x is zero the program jumps back up to readAgain	1
    set(y,0b0001)     ## 0001 is the red button (14)								2
    jmp(x_not_y,'checkGreen')        ## if x is not y then jump,  means that the button push is not pushed.	3
    ###  since X is NOT Y, we want this section to do what is associated with the Red Button PUSH (which we already set as 0b0001)
    ### now that we know that the red button (ob0001) was pressed, we set the y register for what we are going to want the PINS to do
    set(y,0b0101)		##4
    
    mov(pins,y)
    
    label('checkGreen') ## note that if x is not zero and x is not y, then x is red
    set(y,0b0010)
    jmp(x_not_y,'checkBut3')
    set(y,0b1010)
    mov(pins,y)
    label('checkBut3')
    set(y,0b0011)
    jmp(x_not_y,'readAgain')
    set(y,0b11111)
    mov(pins,y)
    wrap()
    
But13 =Pin(13,Pin.IN,Pin.PULL_DOWN)   
## if I use StateMachine.init() I get help with all the parameters and then delete the 'init'
But15=Pin(15,Pin.IN,Pin.PULL_DOWN)
But14=Pin(14,Pin.IN,Pin.PULL_DOWN)
##sm0=rp2.StateMachine(0,butWatch,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),freq=2000,out_base=Pin(16))
sm0=rp2.StateMachine(0,butWatch,in_base=But14,freq=2000,out_base=Pin(16))
sm0.active(1)