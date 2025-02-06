'''


'''
import rp2
from machine import Pin
import time
 
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def pulse_program():
    wrap_target()
    pull(block)
    mov(x,osr)
    set(pins,1)[10-1]
    set(pins,0)
    wait(1,pin,0)
    label("land")
    mov(y,pins) # 1 clock cycle
    jmp(not_y,"moveOn") #1 clock cycle
    jmp(x_dec,"land") # 1 clock cycle
    label("moveOn")
    mov(isr,invert(x))
    push()
    wrap()
triggerPin = Pin(16,Pin.OUT)
echoPin = Pin(17, Pin.IN)
sm=rp2.StateMachine(0,pulse_program, freq=1000000, set_base=triggerPin,in_base=echoPin)
sm.active(1)
while True:
    sm.put(0xFFFFFFFF)
    print("Pulse Launched")
    clockCycles=sm.get()*3/2
    distance=clockCycles*.0342
    print("Distance to Target: ",distance)
    time.sleep(.25)