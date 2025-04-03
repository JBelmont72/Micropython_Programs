'''  PW pico lesson 98 Servo control

period of servo is 20 milliSecs(20,000 microSec), 0 degreees is 500 milliSec and 180 degrees is 2500millisec
for 90 degrees 1500 microSec 

need to save numbers in two places statically y the ISR for the dynamic . but first use it for 
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
x is pulse width, move to osr,   perIod to isr
'''
# from machine import Pin
# import rp2
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def servoSet():
#     set(x,0b11111)  ## this had the pulse width
#     in_(x,5)
#     set(x,0b11101)
#     in_(x,4)
#     #set(x,0b00000)
#     #in_(x,1)
#     mov(osr,isr)
    
#     mov(isr,null)   ## this has the period
#     set(y,0b10011)
#     in_(y,5)
#     set(y,0b10001)
#     in_(y,5)
#     set(y,0b00000)
#     in_(y,5)
    
#     wrap_target()
#     mov(x,osr)      ## move the pulse width to x
#     mov(y,isr)      ## move the period to y
#     set(pins,0)
#     label('timeLoop')
#     jmp(x_not_y,'nxt') ## while the count is greater than the pulse width, the pin still stays at zero
#     set(pins,1)     ## once the count gets to the pulse width eqauling the countdown of y which was the period    
#     label('nxt')        ## the pin (servo) becomes 1 then continues the 'timeloop' down to zero.
#     jmp(y_dec,'timeLoop')    
#     wrap()
    
# sm0 = rp2.StateMachine(0,servoSet, freq=2000000, set_base=Pin(0))
# sm0.active(1)
# while True:
#     pass
###~~~~  this takes user input for the microseconds (converting to angle would be necessary for both the blue and black servos)
# from machine import Pin
# import rp2
# @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def servoSet():## want the pulse width in the isr   and then move to osr, then period in isr
#     # 0b10011 10001 00000 ## x anbd osr have the period
    
#     set(x,0b10011)  ## this had the pulse width
#     in_(x,5)
#     set(x,0b11110)
#     in_(x,5)
#     set(x,0b0011)
#     in_(x,1)
#     mov(osr,isr) 
#     mov(isr,null)
#     set(y,0b10011) 
#     in_(y,5)
#     set(y,0b10001) 
#     in_(y,5)
#     set(y,0b00000)
#     in_(y,5)
#     wrap_target()
#     mov(x,osr)
#     mov(y,isr)
#     set(pins,0)
#     label('bitLoop')
#     jmp(x_not_y,'next')
#     set(pins,1)
#     label('next')
#     jmp(y_dec,'bitLoop')
#     wrap()     
# sm0 = rp2.StateMachine(0,servoSet, freq=2000000, set_base=Pin(0))
# sm0.active(1)
# while True:
#     pass
#>>> bin(20000)
# 0b10011 10001 00000
#>>> bin(1500)
# 0b10111 01110 0
########~~~~~~5 Jan 2025 basic servo prog
#>>> bin(20000)
# 0b10011 10001 00000
# #>>> bin(1500)
# 0b10111 01110 0
# for the small servos
# my large servos are:    # print(0b0110001110)   398
# print(0b00011111111)   255
#print(0b11110000)   240  low
# middle  bin(750)   '0b1011101110'
# import rp2
# from machine import Pin
# import time
# @rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,), out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def Servo():
#     wrap_target()
#     mov(isr,null)
#     set(y,0b10011)## moving 20,000 into isr then osr
#     in_(y,5)
#     set(y,0b10001)
#     in_(y,5)
#     set(y,0b00000)
#     in_(y,5)
#     mov(osr,isr)
#     mov(isr,null)
#     set(x,0b1000)
#     # set(x,0b10111)
#     in_(x,5)
#     set(x,0b01110)
#     in_(x,5)
#     set(x,0b00000)
#     in_(x,1)
#     mov(x,isr)
#     mov(y,osr)
#     set(pins,0)
#     label('decr_Y')
#     jmp(x_not_y,'loop')
#     set(pins,1)
#     label('loop')
#     jmp(y_dec,'decr_Y')
#     wrap()
# sm0=rp2.StateMachine(0,Servo,freq=2000000,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),set_base=Pin(0,Pin.OUT))
# sm0.active(1)
#####5 jan 2024 take above and make it take commands frompython
# import rp2
# from machine import Pin
# import time
# @rp2.asm_pio(set_init=(rp2.PIO.OUT_LOW,), out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def Servo():
#     wrap_target()
#     mov(y,isr)
#     mov(x,osr)
#     set(pins,0)
#     label('decr_Y')
#     jmp(x_not_y,'loop')
#     set(pins,1)
#     label('loop')
#     jmp(y_dec,'decr_Y')
#     wrap()
# sm0=rp2.StateMachine(0,Servo,freq=2000000,in_base=Pin(14,Pin.IN,Pin.PULL_DOWN),set_base=Pin(0,Pin.OUT))
# sm0.active(1)
# sm0.put(20000)
# sm0.exec('pull()')
# sm0.exec('mov(isr,osr)')


# while True:
#     for angle in range(0,180,1):
#         pw=int(500+angle*2000/180)
#         sm0.put(pw)
#         sm0.exec('pull()')
#     time.sleep(1)
#     for angle in range(180,0,-1):
#         pw=int(500+angle*(2000/180))
#         sm0.put(pw)
#         sm0.exec('pull()')
        
######make a servo class
# import rp2
# import time
# from machine import Pin
# class ServoState:
#     count=0
#     freq=2000000

#     @rp2.asm_pio(set_init=rp2.PIO.OUT_LOW, out_shiftdir=rp2.PIO.SHIFT_RIGHT)
#     def servoSet():
#         wrap_target()
#         mov(x,osr)
#         mov(y,isr)
#         set(pins,0)
#         label('decr_Y')
#         jmp(x_not_y,'loop')
#         set(pins,1)
#         label('loop')
#         jmp(y_dec,'decr_Y')
#         wrap()
#     def __init__(self,pin):
#         # self.sm = rp2.StateMachine(servoState.counter,servoState.servoSet, servoState.freq, set_base=servoPin)# instantiation
#         self.sm0=rp2.StateMachine(ServoState.count,ServoState.servoSet,ServoState.freq,set_base=Pin(pin))
#         self.sm0.active(1)
#         self.sm0.put(20000)
#         self.sm0.exec('pull()')
#         self.sm0.exec('mov(isr,osr)')
#         ServoState.count=ServoState.count+1
#         # print(str(ServoState.count)+'   '+str(ServoState.servoSet)+''+str(pin))
#     def ServoAngle(self,angle):
#         pw=int(500+angle*(2000/180))
#         self.sm0.put(pw)
#         self.sm0.exec('pull()')

            
# myServo=ServoState(0)
# while True:
#     for angle in range(0,180,1):
#         myServo.ServoAngle(angle)
#     time.sleep(1)
#     for angle in range(180,0,-1):
#         myServo.ServoAngle(angle)
####~~~~~~~~~~~~~       
'''20,000 is 0,10011,10001,00000
1,500 is 01,01110,11100
2500 is 010,01110,00100
500   is  ,01111,10100  '''
import rp2
from machine import Pin
import time
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def servo():
      ##the pulse width for 1500 90 deg is in x
    
    
    set(x,0b01)
    in_(x,2)
    set(x,0b01110)
    in_(x,5)
    set(x,0b11100)  ##the pulse width for 1500 90 deg is in x
    in_(x,5)
    mov(x,isr) ## the pulse width is in ISR
    mov(osr,x) ## the pulse width is also stored in OSR( not needed for this version))
    mov(isr,null)
      
    
    set(y,10011)
    in_(y,5)
    set(y,0b10001)
    in_(y,5)
    set(y,0b00000)
    in_(y,5) 
    wrap_target()
    mov(y,isr)  ## the period is in y and ISR
    mov(x,osr)
    set(pins,0)
    label('loop')
    jmp(x_not_y,'ON')
    set(pins,1)
    label("ON")
    jmp(y_dec,'loop')

     
    ## goes to here when y is decreased down to x (the pulsewidth) 
    
    wrap()
servoPin=Pin(0,Pin.OUT)
sm0=rp2.StateMachine(0,servo,2000000,set_base=Pin(2,Pin.OUT))
sm0.active(1)
x=0
while True:
    print(x)
    x+=1
    time.sleep(1)