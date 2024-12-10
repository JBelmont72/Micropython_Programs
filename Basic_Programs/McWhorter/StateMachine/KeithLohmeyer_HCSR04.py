'''
Keith Lohmeyer
HC-SR-04
works fine in both VSCOde and thonny
'''
import time
from machine import Pin
import rp2
dist = 0
echo= Pin(15,Pin.IN)
trig = Pin(16,Pin.OUT)
# pwr =Pin(17,Pin.OUT)
# pwr.on()
## start at 300 and decrement and whenever the echo goes low
def get_cm(x):
    global dist
    dist = 300 - sm.get()
    # print(dist,time.ticks_ms())
    
@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW) 
def ping():
    label('loop')
    set(x,0b10010)     ## 300 in binary is 100101100, moved the 5 most signiticant digits into the ISR
    mov(isr,x)
    set(x,0b1100)       ## moved the 4 least signifiant digits  NOW has 300 in binary in the isr
    in_(x,4)            ## shifts into isr
    mov(x,isr)          ## mov isr back to x
    set(pins,0)[9]      ## set trig to low for 10 uSec, pins is for the OUTPUT pins
    set(pins,1)[9]      ## set trig pin to high for 10 uSec
    set(pins,0)         ## set trig to low
    wait(1,pin,0)       ## wait for echo input to go high, wait is for the INPUT pins
    label('cm')
    jmp(pin,'dec')[28]   ## while echo is high, jmp to dec
    ## if pin high want to jump after 28+1 clock cycles
    mov(isr,x) ## when echo goes 'low' send the isr value to x 
    push() ## push the isr value to fifo
    irq(rel(0))  ## trigger the irq to 'get' value
    
    ## looks like two loops('do_delay' and )
    label('do_delay')   ## jumped here from bottom if the 300 countdown goes to zero with no measurement
    mov(isr,invert(null))##this starts the timing loop again, if you invert NULL, you have all ones!
    in_(null,12)
## 12 bits = 4096 X 20 = 81920 cycles or about 80 milliseconds   2 **12 = 4096  
    mov(y,invert(isr)) 
    label('delay')
    jmp(y_dec,'delay')    [19] ## this decrements the y value that was set to 2**12 or 4096 (((worked without the [19])))
    
    jmp('loop')##After the 
    label('dec')
    jmp(x_dec,'cm')     [28] ## this tells the x_dec to cycle to 'cm' up to time out<300.(( and worked without the [28]))
    ###  if gets to zero, then it times out and moves to the next line down.
    jmp('do_delay')[19]   ## this ends the timing loop after 19+1 cycles , this 20 plus the 2**12 is 4096X20 = 81920 microseconds or ~82 milliseconds
sm =rp2.StateMachine(0,ping,freq=1000000,set_base=trig,jmp_pin=echo,in_base=echo)
sm.irq(get_cm)

sm.active(1)  
    
while True:
    time.sleep(.5)
    print(dist)   
    
        
        
