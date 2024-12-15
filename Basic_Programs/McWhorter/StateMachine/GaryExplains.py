'''
tutorial is Gary Explains and he uses examples from this github-
https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio
'''
'''
import time
import rp2
from machine import Pin

# Define the blink program.  It has one GPIO to bind to on the set instruction, which is an output pin.
# Use lots of delays to make the blinking visible by eye.

@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,)*4, out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def blink():
    wrap_target()
    set(pins, 0b1111)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0b0000)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()

# Instantiate a state machine with the blink program, at 2000Hz, with set bound to Pin(25) (LED on the Pico board)
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(16))

# Run the state machine for 3 seconds.  The LED should blink.
sm.active(1)
time.sleep(3)
sm.active(0)
'''
'''
import time
from machine import Pin
import rp2
@rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    pull()
    set(x,31)
    label('bitloop')
    out(pins,1)[31]
    nop()[31]
    jmp(x_dec,'bitloop')
    wrap()
sm0=rp2.StateMachine.init(0,blink,freq=2000,out_shiftdir=rp2.PIO.SHIFT_RIGHT,out_base=Pin(16))
sm0.active(1)
while True:
    sm0.put(0x00000001)
    
'''  
''' 
import time
from machine import Pin
import rp2
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def bounce():
    pull()
    mov(isr,osr)
    push()
sm0=rp2.StateMachine(0,bounce,freq=2000,set_base=Pin(16))
sm0.put(31)
print('Num of words in TX: ',sm0.tx_fifo())
print('Num of wrods in the RX fifo: ',sm0.rx_fifo())
sm0.active(1)
time.sleep(1)
sm0.active(0)
print('Num of words in TX: ',sm0.tx_fifo())
print('Num of wrods in the RX fifo: ',sm0.rx_fifo())
a =sm0.get()
sm0.active(1)
print('Num of words in TX: ',sm0.tx_fifo())
print('Num of wrods in the RX fifo: ',sm0.rx_fifo())
print(a)
sm0.active(0)
'''
'''
## this program doubles numbers and displays on LEDs
import time
from machine import Pin
import rp2
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*6,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def double_pull():
    wrap_target()
    pull()
    in_(osr,8)
    set(x,0)
    in_(x,1)
    mov(y,isr)
    mov(pins,y)
    push()
    wrap()
sm0=rp2.StateMachine(0,double_pull,freq=2000,out_shiftdir=rp2.PIO.SHIFT_RIGHT,out_base=Pin(16))
sm0.active(1)
while True:
    a = int(input('enter number'))
    sm0.put(a)
    print('number entered: ',a)
    time.sleep(.2)
    print('number doubled is: ',sm0.get())
'''
## this doubl_pull function worked and I used the osr to y to in_ instead of above
# def double_pull():
#     wrap_target()
#     pull()
#     mov(y,osr)
#     in_(y,8)
#     set(y,null)
#     set(x,0)
#     in_(x,1)
#     mov(y,isr)
#     mov(pins,y)
#     push()
#     wrap()
'''

'''



# minute 26 pull data from statemachine and flash for the x value number of times
import time
from machine import Pin
import rp2
@rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
def blink_pull():
    wrap_target()
    set(x,31)
    label('bitloop')
    out(pins,1)[31]
    nop()[31]
    jmp(x_dec,'bitloop')
    wrap()
sm0=rp2.StateMachine(0,blink_pull,freq=2000,out_shiftdir=rp2.PIO.SHIFT_RIGHT,out_base=Pin(16))
sm0.active(1)