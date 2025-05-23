'''
IRQ pio interrupts
PW lesson 103
first is a recap of PW_87
second is the PW102 servo library
third is the IRQ lesson 103
a SM using a IRQ can trigger interrupts on other statemachines or in Python
'''
# import rp2
# from machine import Pin
# import time
# import sys
# ##recap pioprog from PW_87
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():
#     # wrap_target()
#     set(x,0b111111)## not used in the sm0.exec(put(value))
#     wrap_target()  ## if the wrap target is here, then the osr is reloaded each time trhough the cycle
#     # mov(osr,x)      ### moves x to osr ## i found that i could comment this out, i think I'm just skipping loading the OSR
#     # wrap_target()## if the wrap_target is left here. the osr is loaded with x only one time!! it flashes the first time throughthe loop
#     # mov(x,osr)
#     mov(pins,x)
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
    
    
#     mov(pins,invert(x))   
#     # out(pins,6)     ### out clears the osr and put the osr value to pins with an out, the osr is now empty, so this is a loop because the osr keeps getting freshly reloaed with  the value in x, the number is how many pins to be used
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
    
    
#     wrap()
# led=Pin(16,Pin.OUT)   
# sm0=rp2.StateMachine(0,pioProg,freq =2000,out_base=Pin(16,Pin.OUT))
# sm0.active(1)
# sm0.put(0b1111)
# sm0.exec('pull()')

# try:
#     while True:
#         pass
# except:
#     sm0.active(0)
#     print('Off')
# finally:
#     sys.exit
####
'''
## set up an interrupt when the button pressed which will toggle the led
import time
from machine import Pin
import rp2
class servoState:
    counter=0
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
        self.sm = rp2.StateMachine(servoState.counter,servoState.servoSet, freq=2000000, set_base=Pin(servoPin))
        self.sm.active(1)
        self.sm.put(20000)
        self.sm.exec("pull()")
        self.sm.exec("mov(isr,osr)")
        print("State Machine: "+str(servoState.counter)+" created")
        servoState.counter=servoState.counter+1
    def servoAngle(self,angle):
        pw=int(500+angle*2000/180)
        self.sm.put(pw)
        self.sm.exec("pull()")
myServo1=servoState(20)
myServo2=servoState(21)
myServo3=servoState(22)
myServo4=servoState(23)
myServo5=servoState(24)
myServo6=servoState(25)
myServo7=servoState(26)
myServo8=servoState(27)
while True:
    for angle in range(0,180,1):
        myServo1.servoAngle(angle)
        myServo7.servoAngle(180-angle)
    time.sleep(5)
    for angle in range(180,0,-1):
        myServo1.servoAngle(angle)
        myServo7.servoAngle(180-angle)
    time.sleep(5)
'''
## in statemachine need to clear the interrupt, in python,it is cleared automatically
## 8 interrupts on each PIO block, Note in python can only use interrupt ZERO
import time
from machine import Pin
import rp2

@rp2.asm_pio()
def button_irq():
    wrap_target()
    wait(1,pin,0)
    nop()[31]   
    nop()[31]   
    nop()[31]   
    nop()[31]   
  
    irq(block,0)
    wait(0,pin,0)
    nop()[31]   
    nop()[31]   
    nop()[31]   
    nop()[31]         
    wrap()
button_pin=Pin(14,Pin.IN,Pin.PULL_DOWN)
sm_button = rp2.StateMachine(0,button_irq, freq=2000000, in_base=Pin(button_pin))
led_pin=Pin(16,Pin.OUT)
## this is handling interrupts in python
def button_handler(sm):
    led_pin.value(not led_pin.value())
sm_button.irq(button_handler)
sm_button.active(1)
while True:
    pass 
  
    
### three buttons and three leds controlled by interuupts
# import time
# from machine import Pin
# import rp2

# @rp2.asm_pio()
# def button_irq():
#     wrap_target()
#     wait(1,pin,0)
#     nop()[31]   
#     nop()[31]   
#     nop()[31]   
#     nop()[31]   
  
#     irq(block,0)
#     wait(0,pin,0)
#     nop()[31]   
#     nop()[31]   
#     nop()[31]   
#     nop()[31]         
#     wrap()
    
# #### this is handling interrupts in the state machine   
# @rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
# def led_control():
#     set(x,0b00000)
#     wrap_target()
#     wait(1,irq,0)   ## WAIT FOR THE IRQ number 0 TO BE TRIGGERED (==1)
#     mov(x,invert(x))    ## x is now 0b11111
#     mov(pins,x)
#     irq(clear,0)
#     wrap()
    
    
# button_pin=Pin(14,Pin.IN,Pin.PULL_DOWN)
# sm_button = rp2.StateMachine(0,button_irq, freq=2000, in_base=Pin(button_pin))
# led_pin=Pin(16,Pin.OUT)
# sm_led=rp2.StateMachine(1,led_control,freq=2000,out_base=led_pin)
# # def button_handler(sm):
# #     led_pin.value(not led_pin.value())
# # sm_button.irq(button_handler)
# sm_button.active(1)
# sm_led.active(1)
# while True:
#     pass 
###~~~~~~~~7 Feb 2025 same as above , i tried adding  the out_init, outShift in the decorator and the out_base pins in the state machine instantiator
# import rp2 
# from machine import Pin
# import time
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*3,out_shiftdir=rp2.PIO.SHIFT_RIGHT)


# def But_irq():

#     wrap_target()
#     wait(0,pin,0)
    
#     set(y,0b111)
#     mov(pins,y)
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     nop()[31]
#     irq(block, 0)
#     wait(1,pin,0)## the pin is instantiates and can call the irq method in 'smButton.irq( trigger is the  and the handler is the 'button_handler ()' function
    
#     nop()[31]
#     nop()[31]
#     mov(pins,invert(y))
#     nop()[31]
#     nop()[31]
#     wrap()
    
# Button=Pin(14,Pin.IN,Pin.PULL_DOWN)
# smButton=rp2.StateMachine(0,But_irq,freq=2000,in_base=Button,out_base=Pin(17,Pin.OUT))## creates an instance of Statemachine the instantiates the 'pin' in the Satemachine program (But_irq)
# smButton.active(1)
# led_pin= Pin(16,Pin.OUT)

# def button_handler(pin):
#     led_pin.value(not led_pin.value())
#     print(time.ticks_ms())
# smButton.irq(button_handler)    #when the interrupt occurs in  the SM program, it will alert/trigger the smButton.irq interrupt, then the handler is called which is the button_handler and toggles the led
# # smButton.irq(lambda p: print(time.ticks_ms()))
# while True:
#     pass

###~~~~~~~~~~~~~~~~9 feb 2025 three buttons and 3 interrupts

