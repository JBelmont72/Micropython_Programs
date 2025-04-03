'''PW103 pure  not altered. the other PW_103 has practice variations for PIO
incorporate IRQ interrupts on the Pi Pico PIO State Machines. The state machines will monitor the buttons, watching for button presses. When a button is pressed, an interrupt is set. That interrupt can then be used by that same state machine, a different state machine on the same PIO, or in the main micropython program. Our first example will be to toggle the LED in the main python program, based on the interrupt from the state machine. In the second example, one state machine monitors the button, and the second state machine controls the LED. 

'''
###controls leds from python program
# import rp2
# from machine import Pin
# import time
 
# # Define PIO program for SM0 to trigger an interrupt on button press
# @rp2.asm_pio()
# def button_irq():
#     wrap_target()
#     wait(1, pin, 0)  [31]  # Wait for the button press (low signal on GPIO 11)
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     irq(block, 0)      # Trigger interrupt 0
#     wait(0, pin, 0)    # Wait for the button release (high signal on GPIO 11)
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     nop() [31]
#     wrap()
# # Initialize State Machine 0 for the button (GPIO 11)
# button_pin = Pin(11, Pin.IN, Pin.PULL_DOWN)
# sm_button = rp2.StateMachine(0, button_irq, freq=2000, in_base=button_pin)
# # GPIO pin for the LED (GPIO 18)
# led_pin = Pin(18, Pin.OUT)
# # Interrupt handler for the button press
# def button_handler(sm):
#     led_pin.value(not led_pin.value())  # Toggle LED state
# # Attach the interrupt handler to the State Machine's IRQ
# sm_button.irq(button_handler)
# # Activate the state machine
# sm_button.active(1)
 
# # Keep the program running
# while True:
#     time.sleep(1)
##### controls leds  and INTERRUPTS from the statemachine

import rp2
from machine import Pin
import time
import sys
@rp2.asm_pio()
def button_irq():
    wrap_target()
    wait(1, pin, 0) [31]
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    irq(block,0)
    wait(0,pin,0)
    nop() [31]
    nop() [31]
    nop() [31]
    nop() [31]
    wrap()
 
@rp2.asm_pio(out_init=rp2.PIO.OUT_LOW)
def led_control():
    set(x,0b00000)
    wrap_target()
    wait(1, irq, 0)
    mov(x,invert(x))
    mov(pins,x)
    irq(clear, 0)
    wrap()
 
button_pin = Pin(14,Pin.IN,Pin.PULL_DOWN)
sm_button=rp2.StateMachine(0,button_irq, freq=2000, in_base=button_pin)
 
led_pin = Pin(16, Pin.OUT)
sm_led=rp2.StateMachine(1, led_control, freq=2000, out_base=led_pin)
sm_button.active(1)
sm_led.active(1)
while True:
    pass