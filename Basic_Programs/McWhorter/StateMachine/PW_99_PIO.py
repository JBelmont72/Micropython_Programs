'''
PW 99 pico turorial
SWEEPING SERVO POSITION USING THE PIO STATE MACHINE ON THE RASPBERRY PI PICO PIO STATE MACHINE
 use the Raspberry Pi Pico PIO State Machine to sweep a servo through its full range of motion. 
'''



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
# sm0 = rp2.StateMachine(0,servoSet, freq=2000000, set_base=Pin(0))
# sm0.active(1)
# sm0.put(20000)
# sm0.exec("pull()")
# sm0.exec("mov(isr,osr)")
# while True:
#     for angle in range(0,180,1):
#         pw=int(500+angle*2000/180)
#         sm0.put(pw)
#         sm0.exec("pull()")
#     time.sleep(5)
#     for angle in range(180,0,-1):
#         pw=int(500+angle*2000/180)
#         sm0.put(pw)
#         sm0.exec("pull()")
#####~~~~~~~~~~29 dec 2024
import rp2
from machine import Pin
from time import sleep

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
## isr will have the period of 20,000 and osr the PW
def servoSet():
    wrap_target()
    mov(x,isr)
    mov(y,osr)
    set(pins,0)
    label('bitLoop')
    jmp(x_not_y,'PW')
    set(pins,1)
    label('PW')
    jmp(x_dec,'bitLoop')    
    wrap()
   
    
sm1=rp2.StateMachine(1,servoSet,freq=2000000,set_base=Pin(0))
sm1.active(1)
sm1.put(20000)
sm1.exec('pull()')## pulls into the OSR
sm1.exec('mov(isr,osr)')## moves the period of 20,000 to the isr
while True:
    for angle in range(0,180,1):
        pw=int(500+angle*2000/180)
        sm1.put(pw)
        sm1.exec('pull()')## now loads the OSR with the pulse width sequentially
    sleep(1)
    for angle in range(180,0,-1):
        pw=int(500+angle*(2000/180))
        sm1.put(pw)
        sm1.exec('pull()')
        
        
