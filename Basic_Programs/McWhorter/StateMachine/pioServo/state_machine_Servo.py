'''Lesson 98 PW is setting up the timing cycle, manually setting the pulse width from 500 to2500 microseconds in 20,000 microsecond period

500 is 0111110100
2500 is 0100111000100
sm0.put(500)
sm0.exec('pull()')
second program is Lesson 99 with sweeping servo and time delay

create a linear equation to convert desired degrees of servo motion into microseconds
Range is 0 degrees which is 500 uSec and 180 deg which is 25000 u sec and period of 20 millisec or 20,000 u Sec
(0,500)  and (180,2500) are point we cabn use,  m=1200/180
y =1200/180 *x +500  uSec Pulse Width = 1200/180 * angle in degrees + 500
PW=120/18 *angle+500
'''
'''
import time
from machine import Pin
import rp2   ## the   @ is  'decorator' and alerts that we are programming the state machine
@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,), out_shiftdir=rp2.PIO.SHIFT_RIGHT)  # defines the number of GPIO pins to use,
def servoSet():
#    set(x,0b10111)
    set(x,0b01001)
    in_(x,5)
#    set(x,0b01110)
    set(x,0b11000)
    in_(x,5)
 #   set(x,0b00000)
    set(x,0b00100)
 #   in_(x,1)
    in_(x,3)
    mov(osr,isr)
    mov(isr,null)
    set(y,0b10011)## 
    in_(y,5)
    set(y,0b10001)
    in_(y,5)
    set(y,0b00000)
    in_(y,5)
    wrap_target() 
    mov(y,isr)		## getting fresh values for x and y from osr and isr at beginning of each cycle
    mov(x,osr)
    set(pins,0)
    label('timeLoop')
    jmp(x_not_y,'nxt')  ## when x is not = to y( like at the start of each period) there is cycling with y decrementing 
    set(pins,1)
    label('nxt')
    jmp(y_dec,'timeLoop')
    
    wrap()
### sm0 is instantiating the satemenachine object, using SM 0 put can go all the way to SM 7    
sm0 = rp2.StateMachine(0, servoSet,freq=2000000, set_base=Pin(16))
sm0.active(1)
'''
'''
while True:
    for i in range(180):
        PW =int(120/18 * i +500)
        sm0.put(PW)
        sm0.exec('pull()')
    for i in range(180,-1):
        PW =int(120/18 * i +500)
        sm0.put(PW)
        sm0.exec('pull()')
'''        
      
import time
from machine import Pin
import rp2   ## the   @ is  'decorator' and alerts that we are programming the state machine
@rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,), out_shiftdir=rp2.PIO.SHIFT_RIGHT)  # defines the number of GPIO pins to use,
def servoSet():

    wrap_target() 
    mov(y,isr)		## getting fresh values for x and y from osr and isr at beginning of each cycle
    mov(x,osr)
    set(pins,0)
    label('timeLoop')
    jmp(x_not_y,'nxt')  ## when x is not = to y( like at the start of each period) there is cycling with y decrementing 
    set(pins,1)
    label('nxt')
    jmp(y_dec,'timeLoop')
    
    wrap()

##sm0 is instantiating the satemachine object, using SM 0 put can go all the way to SM 7    
sm0 = rp2.StateMachine(0, servoSet,freq=2000000, set_base=Pin(16))
sm0.active(1)
sm0.put(20000)
sm0.exec('pull()')
sm0.exec('mov(isr,osr)') ## this gets the period of 20,000 microSec into the ISR
while True:
    for angle in range(0,180,1):
        PW=int(500 + angle*2000/180)
        sm0.put(PW)
        sm0.exec('pull()')

    for angle in range(180,0,-1):
        PW=int(500 + angle*2000/180)
        sm0.put(PW)
        sm0.exec('pull()')