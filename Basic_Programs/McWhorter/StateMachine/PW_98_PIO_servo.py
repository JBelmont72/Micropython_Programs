'''  PW pico lesson 98 Servo control

period of servo is 20 milliSecs(20,000 microSec), 0 degreees is 500 milliSec and 180 degrees is 2500millisec
for 90 degrees 1500 microSec 

need to save numbers in two placs statically y the ISR for the dynamic . but first use it for 
setting the period and then move the period over to OSR to store.  THis now frees up the ISR for 
the pulseLength.

#>>> bin(20000)
0b10011 10001 00000
#>>> bin(1500)
0b10111 01110 0
for the small servos
my large servos are:    # print(0b0110001110)   398
# print(0b00011111111)   255
#print(0b11110000)   240  low
# middle  bin(750)   '0b1011101110'
#print(0b10011111111)   1279  high okay with 1285
to command from the IDE REPL:
#>>> sm0.put(500)
##>>> sm0.exec('pull()')
'''
from machine import Pin
import rp2
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def servoSet():
    set(x,0b11111)
    in_(x,5)
    set(x,0b0100)
    in_(x,4)
    #set(x,0b00000)
    #in_(x,1)
    mov(osr,isr)
    
    mov(isr,null)
    set(y,0b10011)
    in_(y,5)
    set(y,0b10001)
    in_(y,5)
    set(y,0b00000)
    in_(y,5)
    
    wrap_target()
    mov(x,osr)
    mov(y,isr)
    set(pins,0)
    label('timeLoop')
    jmp(x_not_y,'nxt')
    set(pins,1)
    label('nxt')
    jmp(y_dec,'timeLoop')    
    wrap()
    
sm0 = rp2.StateMachine(0,servoSet, freq=2000000, set_base=Pin(20))
sm0.active(1)

###~~~~  this takes user input for the microseconds (converting to angle would be necessary for both the blue and black servos)