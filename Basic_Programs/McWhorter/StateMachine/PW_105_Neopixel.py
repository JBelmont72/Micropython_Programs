'''     1-ones     cycles      o-zeros 
'0'      1   2                   1 6   
'1'     1   5                     1 2 1
'''
import rp2
from machine import Pin
import time
@rp2.asm_pio(sideset_init=rp2.PIO.OUT_HIGH,
             out_shiftdir=rp2.PIO.SHIFT_LEFT,
             autopull=True,
             pull_thresh=24)
def ws2812():
    wrap_target()
    label("bitloop")
    out(x,1).side(0)
    jmp(not_x,"do_zero").side(1)
    nop().side(1)[5-1]
    nop().side(0)[2-1]
    jmp("bitloop").side(0)
    label("do_zero")
    nop().side(1)[2-1]
    jmp("bitloop").side(0)[6-1]
    wrap()
sm=rp2.StateMachine(0,ws2812,freq=8000000,sideset_base=Pin(0))
sm.active(1)
 
def write_neopixel(colors):
    for color in colors:
        grb=color[1]<<16 | color[0]<<8 | color[2]
        sm.put(grb,8)
        
    
NUM_LEDS =8
myColor=[0]*NUM_LEDS
# myColor=[[100,0,0],
#          [0,100,0],
#          [0,0,100],
#          [0,100,100],
#          [100,0,100],
#          [100,100,0],
#          [200,100,0],
#          [255,255,255]]
myColor=[[0,0,0]]
write_neopixel(myColor)