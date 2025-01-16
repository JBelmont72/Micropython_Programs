'''

'''
'''
import rp2
from machine import Pin
import time
 
# Define PIO program for the button to trigger an interrupt on SM0
@rp2.asm_pio()
def button_irq():
    wrap_target()
    label('readAgain')
    mov(isr,null) [31]
    in_(pins,3) [31]
    mov(x,isr) [31]
    jmp(not_x,'readAgain')
    set(y,0b001);
    jmp(x_not_y,'checkYellow')
    irq(block,0)
    wait(0,pin,0)
    jmp('readAgain')
    label('checkYellow')
    set(y,0b010)
    jmp(x_not_y,'checkRed')
    irq(block,1)
    wait(0,pin,1)
    jmp('readAgain')
    label('checkRed') 
    irq(block,2)
    wait(0,pin,2)
    wrap()
 
# Define PIO program for the LED control on SM1
@rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
def led_control1():
    set(x, 0b00000)         # Initialize X register to 0 (LED off initially)
    wrap_target()
    wait(1, irq, 0)   # Wait for interrupt 0 to be set
    mov(x, invert(x)) # Invert X register to toggle state
    mov(pins,x)
    irq(clear, 0)     # Clear the interrupt to allow the next press to be handled
    wrap()
@rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
def led_control2():
    set(x, 0b00000)         # Initialize X register to 0 (LED off initially)
    wrap_target()
    wait(1, irq, 1)   # Wait for interrupt 0 to be set
    mov(x, invert(x)) # Invert X register to toggle state
    mov(pins,x)
    irq(clear, 1)     # Clear the interrupt to allow the next press to be handled
    wrap()
@rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
def led_control3():
    set(x, 0b00000)         # Initialize X register to 0 (LED off initially)
    wrap_target()
    wait(1, irq, 2)   # Wait for interrupt 0 to be set
    mov(x, invert(x)) # Invert X register to toggle state
    mov(pins,x)
    irq(clear, 2)     # Clear the interrupt to allow the next press to be handled
    wrap()
'''
# # Initialize State Machine 0 for the button (GPIO 11)
# button_pin = Pin(13, Pin.IN, Pin.PULL_DOWN)
# button_pin2 = Pin(14, Pin.IN, Pin.PULL_DOWN)
# button_pin3 = Pin(15, Pin.IN, Pin.PULL_DOWN)
# sm_button = rp2.StateMachine(0, button_irq, freq=2000, in_base=button_pin)
 
# # Initialize State Machine 1 for the LED (GPIO 18)
# led_pin1 = Pin(16, Pin.OUT)
# sm_led1 = rp2.StateMachine(1, led_control1, freq=2000, out_base=led_pin1)
# # 
# led_pin2 = Pin(17, Pin.OUT)
# sm_led2 = rp2.StateMachine(2, led_control2, freq=2000, out_base=led_pin2)
 
# led_pin3 = Pin(18, Pin.OUT)
# sm_led3 = rp2.StateMachine(3, led_control3, freq=2000, out_base=led_pin3)
# # 
# # Activate both state machines
# sm_button.active(1)
# sm_led1.active(1)
# sm_led2.active(1)
# sm_led3.active(1)
# while True:
#     pass
# Keep the program running
###~~~~~~~~~~mine below
import time
from machine import Pin
import rp2

@rp2.asm_pio()
def button_irq():
    wrap_target()
    label('readAgain')
    mov(isr,null)[31]
    in_(pins,3)[31]
    mov(x,isr)## isr now has the 3 button pins info 01,1-,or 11
    jmp(not_x,'readAgain')
    set(y,0b001)     ## comparing to pin 13 which is the in base  button pin
    jmp(x_not_y,'checkYellow') ## if x is not y, we will check the second in base button pin 
    irq(block,0)    ## !! if x IS y then we are setting the irq to zero until it is cleared in the led_control_1 function
    wait(0,pin,0)   ##need to wait to see a zero on pin o to clear the interrupt, otherwise it will just keep cycling through led_control_1
    jmp('readAgain')
    label('checkYellow')         
    wrap()
    
#### this is handling interrupts in the state machine   
@rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
def led_control_1():
    set(x,0b00000)
    wrap_target()
    wait(1,irq,0)   ## WAIT FOR THE IRQ number 0 TO BE TRIGGERED (==1)
    nop()[31]
    mov(x,invert(x))    ## x is now 0b11111
    mov(pins,x)
    irq(clear,0)
    wrap()
    
## four statemachines,  one on button and 3 for the three leds   
button_pin=Pin(13,Pin.IN,Pin.PULL_DOWN)
sm_button = rp2.StateMachine(0,button_irq, freq=2000, in_base=Pin(button_pin))
led_pin=Pin(16,Pin.OUT)
sm_led_1=rp2.StateMachine(1,led_control_1,freq=2000,out_base=led_pin)
# led_pin=Pin(16,Pin.OUT)
# sm_led_2=rp2.StateMachine(1,led_control_2,freq=2000,out_base=led_pin)
# led_pin=Pin(16,Pin.OUT)
# sm_led_2=rp2.StateMachine(1,led_control_2,freq=2000,out_base=led_pin)

# def button_handler(sm):
#     led_pin.value(not led_pin.value())
# sm_button.irq(button_handler)
sm_button.active(1)
sm_led_1.active(1)
try:
    while True:
    
        pass 
except KeyboardInterrupt:
    led_pin.value(0)
    sm_button.active(0)
    sm_led_1.active(0)
    print('Done')