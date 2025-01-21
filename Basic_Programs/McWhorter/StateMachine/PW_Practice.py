'''
Move data inside the shift register:
in SOURCE count - Shift data into the ISR, where SOURCE can be X, Y, OSR or ISR, and count is 0...32
out DESTINATION count - Shift data out of the OSR, to DESTINATION X, Y, ISR
mov DESTINATION, SOURCE - Move data from SOURCE (X, Y, OSR or ISR) to DESTINATION (X, Y, OSR or ISR)
set DESTIANTION, data - write a 5-bit data value to DESTIANTION (X, Y)
Move data between the shift register and the main program:
pull - Load data from the TX FIFO into the OSR
push - Push data from the ISR to the RX FIFO, then clear the ISR
irq INDEX op - Modify the IRQ number index to be either cleared (op=0) or set (op=1)
'''
# import rp2
# from machine import Pin
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)

# def pioProg():   
#     wrap_target()
#     set(x,0b1111)[31]
#     label('bitLoop')
#     mov(pins,invert(x))
#     set(y,0b1111)
#     mov(pins,invert(x))
#     mov(isr,y)
#     in_(y,1)
#     mov(y,isr)
#     wait(0,pin,0)
#     label('loop')
#     nop()[31]
#     jmp(y_dec,'loop')[31]
#     nop()[31]
#     wait(1,pin,0)
#     jmp(x_dec,'bitLoop')  
#     #### out(pins,4)     ### out clears the osr and put the osr value to pins with an out, the osr is now empty, so this is a loop because the osr keeps getting freshly reloaed with  the value in x, the number is how many pins to be used
#     wrap()
# but13=Pin(13,Pin.IN,Pin.PULL_DOWN)
# sm0=rp2.StateMachine(0,pioProg,freq=2000,in_base=Pin(13,Pin.IN,Pin.PULL_DOWN),out_base=Pin(16,Pin.OUT))
# sm0.active(1)
# while True:
#     pass    
######~~~~~~~~~works two pins 4 leds
import rp2
from machine import Pin
@rp2.asm_pio(out_init=(rp2.PIO.OUT_HIGH,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    
    wrap_target()
    label('readAgain')
    mov(isr,null)
    in_(pins,2)
    nop()[31]
    nop()[31]
    mov(x,isr)
    jmp(not_x,'readAgain')
    set(y,0b01)
    jmp(x_not_y,'checkRed')
    set(y,0b1010)
    mov(pins,y)
    jmp('readAgain')
    label('checkRed')
    set(y,0b10)
    jmp(x_not_y,'readAgain')
    set(y,0b0101)
    mov(pins,y)
    jmp('readAgain')
    wrap()
butPin13 = Pin(13,Pin.IN,Pin.PULL_DOWN)
butPin14 =Pin(14,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,pioProg,freq=2000,in_base=Pin(13,Pin.IN,Pin.PULL_DOWN),out_base=Pin(16,Pin.OUT))
sm0.active(1)
while True:
    pass