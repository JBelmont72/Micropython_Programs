'''
i will use a potentiometer to input values into the statemachien starting with put9VALUE AND RETREIVING FOR THE LED THE PWM GET(VALUE)
max number is 4,294,967,295
'''
# import time
# from machine import Pin, PWM,ADC
# import rp2   
# rPin=13
# rLed=PWM(rPin)
# potPin=26
# pot=ADC(potPin)
# rLed.freq(40000)
# rLed.duty_u16(0)
# @rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*4, out_shiftdir=rp2.PIO.SHIFT_RIGHT)
# def pioProg():        
#     wrap_target()            
#     pull()
#     mov(x,osr)     
#     mov(isr,x)
#     mov(pins,x)
#     push()         
# sm0 = rp2.StateMachine(0, pioProg,freq=2000, out_base=Pin(16))
# sm0.active(1)
# try:
#     while True:
#         for i in range(1023):
#             i =pot.read_u16()
#             print('PotVal: ',i)
#             sm0.put(i)      
#             a=sm0.get() 
#             rLed.duty_u16(a)
#             time.sleep(.10)
#             print(a) 
#         time.sleep(1)
#         sm0.active(0)
# except KeyboardInterrupt:
#     sm0.active(0)
#     print('All Done')
#     rLed.duty_u16(0)
    
    
import time
from machine import Pin, PWM,ADC
import rp2
@rp2.asm_pio(out_init=(rp2.PIO.OUT_LOW,)*6, out_shiftdir=rp2.PIO.SHIFT_RIGHT)


def pioProg():
    wrap_target()       ##not needed since I have a while loop
    pull()
    mov(x,osr)    
    mov(y,x)
    mov(isr,y)   
    out(pins,4)
    ## or could use mov(pins,y)
    push()   
    wrap()              ## not needed since I have a while loop
    
sm0 = rp2.StateMachine(0, pioProg,freq=2000, out_base=Pin(16))
sm0.active(1)   
try:
    while True:
        print('first: ',sm0.tx_fifo())
        print(sm0.rx_fifo())
        PutVal =int(input('enter a number please.'))
        print("the number you entered is: ",PutVal)
        time.sleep(.01) 
        print('second: ',sm0.tx_fifo())
        print(sm0.rx_fifo())
        sm0.put(PutVal)
        GetVal=sm0.get()
        time.sleep(.01)
        print('third ',sm0.tx_fifo())
        print(sm0.rx_fifo())
        print('GetVal: ',GetVal)   
except KeyboardInterrupt:
    print('')
    print('All done')
    sm0.active(0)    
    
sm0 = rp2.StateMachine(0, pioProg,freq=2000, out_base=Pin(16))
sm0.active(1)