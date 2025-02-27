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
    in_(pins,1) # 1 Cycle THese two lines were absent and program hung up
    mov(y,isr)  # 1 Cycle
    #mov(y,pins) # 1 clock cycle Was this Problem that the pins had to go to ISR first
    jmp(not_y,"moveOn") #1 clock cycle
    jmp(x_dec,"land") # 1 clock cycle
    label("moveOn")
    mov(isr,invert(x))
    push()
    wrap()
triggerPin = Pin(1,Pin.OUT)
echoPin = Pin(0, Pin.IN)
sm=rp2.StateMachine(0,pulse_program, freq=1000000, set_base=triggerPin,in_base=echoPin)
sm.active(1)
while True:
    sm.put(0xFFFFFFFF)
    print("Pulse Launched")
    clockCycles=sm.get()*3/2
    distance=clockCycles*.0342
    print("Distance to Target: ",distance)
    time.sleep(.25)
