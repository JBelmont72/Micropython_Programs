'''
PW 100 two Statemachines with 2 servos

sm0.put(500)
sm0.exec('pull()')
second program is Lesson 99 with sweeping servo and time delay
wrap_target
set(pins,0)
mov(x,osr) mov(y,isr)
>>> bin(20000)
0b10011 10001 00000
>>> bin(1500)
0b10111 01110 0

'''
'''
import time
from machine import Pin
import rp2
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def servoSet():
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
sm0 = rp2.StateMachine(0,servoSet, freq=2000000, set_base=Pin(16))
sm0.active(1)
## 2d statemachine
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def servoSet2():
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
sm1 = rp2.StateMachine(1,servoSet2, freq=2000000, set_base=Pin(17))
sm1.active(1)

sm1.put(2000)
sm0.put(20000)
sm0.exec("pull()")
sm1.exec('pull()')
sm0.exec("mov(isr,osr)")
sm1.exec('mov(isr,osr)')

while True:
    for angle in range(0,180,1):
        pw=int(500+angle*2000/180)
        sm0.put(pw)
        sm1.put(2500-pw)
        
        
        sm0.exec("pull()")
    time.sleep(1)
    for angle in range(180,0,-1):
        pw=int(500+angle*2000/180)
        sm0.put(pw)
        sm1.put(2500-pw)
        sm0.exec("pull()")

'''
### run the two statemachines and two servos on the same function''

# import time
# from machine import Pin
# import rp2
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def servoSet():
#     wrap_target()
#     mov(x,osr)
#     mov(y,isr)
#     set(pins,0)
#     label('timeLoop')
#     jmp(x_not_y,'nxt')
#     set(pins,1)
#     label('nxt')
#     jmp(y_dec,'timeLoop')    
#     wrap()  
# sm0 = rp2.StateMachine(0,servoSet, freq=2000000, set_base=Pin(1))

# ## 2d statemachine\
# # @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)

# sm1 = rp2.StateMachine(4,servoSet, freq=2000000, set_base=Pin(0))
# sm1.active(1)
# sm0.active(1)
# sm1.put(20000)
# sm0.put(20000)
# sm0.exec("pull()")
# sm1.exec('pull()')
# sm0.exec("mov(isr,osr)")
# sm1.exec('mov(isr,osr)')

# while True:
#     for angle in range(0,180,1):
#         pw=int(500+angle*2000/180)
#         sm0.put(pw)
#         sm1.put(2500-pw)
        
#         sm1.exec('pull()')
#         sm0.exec("pull()")
#     time.sleep(1)
#     for angle in range(180,0,-1):
#         pw=int(500+angle*2000/180)
#         sm0.put(pw)
#         sm1.put(2500-pw)
#         sm0.exec("pull()")
#         sm1.exec('pull()')
''' 2 April 2025 put Period in y then ISR , put pulse width in x then OSR( will first use the isr and then clear it before proceeding to enter the period)
mov(x,osr) mov(y,isr)
>>> bin(20000)
0b10011 10001 00000 period 20,000
>>> bin(1500)
0b10111 01110 0   pulse 15000
'''  
import sys  
import time
from machine import Pin
import rp2
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def servoSet():
    ## put pulseWidth  in ISR
    # set(x,0b01)
    # in_(x,2)
    # set(x,0b01110)
    # in_(x,5)
    # set(x,0b11100)  ##the pulse width for 1500 90 deg is in x
    # in_(x,5)
    
    
    mov(isr,null)
    set(x,0b10111)
    in_(x,5)
    set(x,0b01110)
    in_(x,5)
    set(x,0b01)
    in_(x,2)
    
    
    mov(x,isr)## move pulse width to osr
    mov(osr,x)## move pulse width to osr
    mov(isr,null)
    set(y,0b10011)
    in_(y,5)    
    set(y,0b10001)
    in_(y,5)    
    set(y,0b00000)
    in_(y,5)    # period of 20,0000 in isr
    wrap_target()
    mov(y,isr) # move the period to y
    mov(x,osr) # move the pulse width to x
    set(pins,0)
    label('loop')
    jmp(x_not_y,'ON')
    set(pins,1)
    
    label('ON')
    jmp(y_dec,'loop')
    wrap()  
sm1 = rp2.StateMachine(1,servoSet, freq=2000000, set_base=Pin(2,Pin.OUT))
sm1.active(1)
try:
    while True:
        sm1.put(1500)
        sm1.exec('pull()')
        pass
except KeyboardInterrupt:
    sm1.active(0)
    sys.exit()