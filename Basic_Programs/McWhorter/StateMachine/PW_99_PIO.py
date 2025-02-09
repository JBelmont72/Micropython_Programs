'''
PW 99 pico turorial
SWEEPING SERVO POSITION USING THE PIO STATE MACHINE ON THE RASPBERRY PI PICO PIO STATE MACHINE
 use the Raspberry Pi Pico PIO State Machine to sweep a servo through its full range of motion. 
 
 two point for calculaitng th linear equation (0,500) (180 ,2500)
 m=(y2-y1)/(x2-x1)    m=(2000/180)
 y-500=(1200/180)times (X)
 y=1200/180  times X +500  the y is the pulse width of how long the voltage is high to the servo during each period
 PulseWIdth = (1200/180) times ANGLE +500
 
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
# import rp2
# from machine import Pin
# from time import sleep

# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# ## isr will have the period of 20,000 and osr the PW
# def servoSet():
#     wrap_target()
#     mov(x,isr)
#     mov(y,osr)
#     set(pins,0)
#     label('bitLoop')
#     jmp(x_not_y,'PW')
#     set(pins,1)
#     label('PW')
#     jmp(x_dec,'bitLoop')    
#     wrap()
   
    
# sm1=rp2.StateMachine(1,servoSet,freq=2000000,set_base=Pin(0))
# sm1.active(1)
# sm1.put(20000)
# sm1.exec('pull()')## pulls into the OSR
# sm1.exec('mov(isr,osr)')## moves the period of 20,000 to the isr
# while True:
#     for angle in range(0,180,1):
#         pw=int(500+angle*2000/180)
#         sm1.put(pw)
#         sm1.exec('pull()')## now loads the OSR with the pulse width sequentially
#     sleep(1)
#     for angle in range(180,0,-1):
#         pw=int(500+angle*(2000/180))
#         sm1.put(pw)
#         sm1.exec('pull()')
 
'''20,000 is 0,10011,10001,00000
1,500 is 01,01110,11100
2500 is 010,01110,00100
500   is  ,01111,10100  
i will enter the period first becasue I wnat it in the OSR  since I will be entering the Pulse width later directly into the OSR
'''       
import rp2
from machine import Pin
import time 
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def servo():
    set(y,0b01)     #Pulse width  is in ISR and move it to OSR and then will be X in the program
                    ## i want the period  in the isr because I will be changing the pulse width by pulling it into the osr , it willbe in y and decremented
    in_(y,2)
    set(y,0b01110)  # i
    in_(y,5)
    set(y,0b11100)
    in_(y,5)
    mov(osr,isr)
    mov(isr,null)
    set(x,0b10011)## period goes to osr and then y`
    in_(x,5)
    set(x,0b10001)
    in_(x,5)
    set(x,0b00000)
    in_(x,5)
    mov(y,isr)
    wrap_target()
    mov(x,osr)
    mov(y,isr)
    set(pins,0)
    label('loop')
    jmp(x_not_y,'decrement')
    
    set(pins,1)
    label('decrement')
    jmp(y_dec,'loop')  
    wrap() 
servoPin=Pin(0,Pin.OUT)       
sm0=rp2.StateMachine(0,servo,2000000,set_base=Pin(0,Pin.OUT))
sm0.active(1)
# sm0.put(20000)
# sm0.exec("pull()")
# sm0.exec("mov(isr,osr)")
while True:
    pass
    # sm0.put(2500)
    # sm0.exec('pull()')
    # time.sleep(1)
    # sm0.put(500)
    # sm0.exec('pull()')
    # time.sleep(1)
    
    # for angle in range(0,180,1):
    #     pw=int(500+angle*2000/180)
    #     sm0.put(pw)
    #     sm0.exec('pull()')## now loads the OSR with the pulse width sequentially
    # time.sleep(1)
    # for angle in range(180,0,-1):
    #     pw=int(500+angle*(2000/180))
    #     sm0.put(pw)
    #     sm0.exec('pull()')