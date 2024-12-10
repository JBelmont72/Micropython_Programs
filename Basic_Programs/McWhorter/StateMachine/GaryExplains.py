'''
tutorial is Gary Explains and he uses examples from this github-
https://github.com/raspberrypi/pico-micropython-examples/tree/master/pio
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