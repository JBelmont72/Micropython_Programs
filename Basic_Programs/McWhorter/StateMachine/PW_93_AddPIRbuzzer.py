'''utilize wait for PIR 'put'   pull  and buzzer for push to get
when pir changes value the pull gets the value into the sm0
'''

import rp2
from machine import Pin
import time

myPin =16
PirPin=0
Pir=Pin(PirPin,Pin.IN,Pin.PULL_DOWN)
buzzer=Pin(myPin,Pin.OUT)
def handler(Get):
    
    print('Trespassing alert')
    for i in range(500):
            buzzer.toggle()
            time.sleep_ms(10)
    Get=0
    return Get
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*1,out_shiftdir=rp2.PIO.SHIFT_RIGHT)
def pioProg():
    #set(x,0b0000)   ## for a SIMPLE  switch having the set here was fine, but if need to change it, then needs to be in loop
    wrap_target()
    label('loop')
    pull()
    mov(x,osr)[31]
    #label('loop')
    
    wait(1,pin,0)
    nop()[31]
    nop()[31]
    mov(isr,x)
    push()
    #wait(0,pin,0)
    nop()[31]
    nop()[31]
    jmp('loop')
    wrap()
    
## if I use StateMachine.init() I get help with all the parameters and then delete the 'init'
#But15=Pin(15,Pin.IN,Pin.PULL_DOWN)
sm0=rp2.StateMachine(0,pioProg,in_base=Pin(0,Pin.IN,Pin.PULL_DOWN),freq=2000,out_base=Pin(16))
sm0.active(1)

while True:
    for i in range(50):
        print(i)
        PUT= Pir.value()
        print('PUT: ',PUT)
        time.sleep(.1)
        sm0.put(PUT)
        time.sleep(.4)
        Get=sm0.get()
        print('Get: ',Get)
        if Get ==1:
            handler(Get)
        time.sleep(1) 
            
            

'''
from machine import Pin
import utime as time

myPin =16
PirPin=0
Pir=Pin(PirPin,Pin.IN,Pin.PULL_DOWN)
buzzer=Pin(myPin,Pin.OUT)
'''
'''
while True:
    Val=Pir.value()
    if Val==1:
        
        print(Pir.value())
        print("Trespassing alert")
        

        for i in range(5000):
            buzzer.toggle()
            time.sleep_ms(1)
    elif Val==0:
        print('Value: ',Pir.value())
        time.sleep(1)
 
def handler(pin):
    print('Trespassing alert')
    for i in range(5000):
            buzzer.toggle()
            time.sleep_ms(1)
            
            
Pir.irq(trigger=Pin.IRQ_RISING,handler=handler)
while True:
    for i in range(50):
        print(i)
        time.sleep(1)
            
'''
