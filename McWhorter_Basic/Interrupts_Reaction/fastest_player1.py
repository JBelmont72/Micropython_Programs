'''Works great
two player reaction with fastest player
on the bottom is the sketch with two players but no fastest player determination
https://shop.sb-components.co.uk/blogs/posts/raspberry-pi-pico-reaction-game
good tutorial but I used the get started with micropython on RPI Pico book for reference
https://penguintutor.com/electronics/pico-power
very goo tutorial for powering the pico
'''


import machine
import utime
import urandom
interrupt_flag = 0
debounce_time = 0
reaction_time = 0

fastest_button = None

led = machine.Pin(16, machine.Pin.OUT)
#button = machine.Pin(15, machine.Pin.IN,machine.Pin.PULL_DOWN)
left_button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
right_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    right_button.irq(handler =None)
    left_button.irq(handler =None)
    
    global fastest_button
    fastest_button = pin
    
    #timer_reaction = utime.ticks_diff(utime.ticks_ms(),timer_start)
    #print("Your reaction time was "+ str(timer_reaction)+ " milliseconds")
print(right_button.value())
led.value(1)
utime.sleep(urandom.uniform(2,5))
led.value(0)
timer_start =utime.ticks_ms()
right_button.irq(trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_RISING, handler = button_handler)
left_button.irq(trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_RISING, handler = button_handler)
while fastest_button is None:
    utime.sleep(1)
if fastest_button is left_button:
    print("Left Player Wins!")
if fastest_button is right_button:
    print("Right Player Wins!")
print(left_button.value())


#	 below is above program without the fastest player designating script
'''
import machine
import utime
import urandom
interrupt_flag = 0
debounce_time = 0
reaction_time = 0



led = machine.Pin(16, machine.Pin.OUT)
#button = machine.Pin(15, machine.Pin.IN,machine.Pin.PULL_DOWN)
left_button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
right_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)

def button_handler(pin):
    right_button.irq(handler =None)
    left_button.irq(handler =None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(),timer_start)
    print("Your reaction time was "+ str(timer_reaction)+ " milliseconds")
print(right_button.value())
led.value(1)
utime.sleep(urandom.uniform(2,5))
led.value(0)
timer_start =utime.ticks_ms()
right_button.irq(trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_RISING, handler = button_handler)
left_button.irq(trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_RISING, handler = button_handler)
print(left_button.value())
'''