'''
https://shop.sb-components.co.uk/blogs/posts/raspberry-pi-pico-reaction-game

'''

import machine

import utime

import urandom
timer_start = 0
pressed = False

led = machine.Pin(16, machine.Pin.OUT)

button = machine.Pin(15, machine.Pin.IN,machine.Pin.PULL_DOWN)
pressed = False
def button_handler(pin):
    #global pressed
    button.irq(handler = None)
    '''
    if  pressed == False:
        pressed=True
        print("HI")'''
    print(pin)
led.value(1)

utime.sleep(urandom.uniform(2, 4))

led.value(0)
button.irq(trigger=machine.Pin.IRQ_RISING,handler=button_handler)


''''''




'''
def button_handler(pin):

    global pressed

    if  not pressed:

    pressed=True

    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)

    print("Your reaction time was " + str(timer_reaction) + " milliseconds!")

led.value(1)

utime.sleep(urandom.uniform(2,4))

led.value(0)

timer_start = utime.ticks_ms()

button.irq(trigger=machine.Pin.IRQ_RISING,handler=button_handler)

'''