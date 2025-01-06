'''
PW 101 creating  PIO class
each PIO machine share 32 lines of code. so the four statemanchines
on each block share the 32 lines. thus statemachinee 0 through 3 use the same code.
THis means if I used statemachines in both blocks, the code would be copied into each of the PIO BLOCKS

we want to interact with the servo through an object that is instantiated by a class


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
# sm0 = rp2.StateMachine(0,servoSet, freq=2000000, set_base=Pin(1))
# sm1 = rp2.StateMachine(1,servoSet, freq=2000000, set_base=Pin(0))
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

import time
from machine import Pin
import rp2

class servoState:
    counter =0
    freq=2000000
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

    def __init__(self,servoPin):
        self.sm = rp2.StateMachine(servoState.counter,servoState.servoSet, servoState.freq, set_base=servoPin)# instantiation
        self.sm.active(1)
        self.sm.put(20000)
        self.sm.exec('pull()')
        self.sm.exec('mov(isr,osr)')
        print('statemachine: '+str(servoState.counter) +'  '+str(servoPin)+ 'created') 
        servoState.counter=servoState.counter +1
        
    def servoAngle(self,angle):
        pw=int(500+angle*2000/180)
        self.sm.put(pw)
        self.sm.exec("pull()")
        
myServo1=servoState(0)
myServo2=servoState(1)



while True:
    
    for angle in range(0,180,2):
        myServo1.servoAngle(angle)
        myServo2.servoAngle(180-angle)
    for angle in range(180,0,-2):
        myServo1.servoAngle(angle)
        myServo2.servoAngle(180-angle)
        
        