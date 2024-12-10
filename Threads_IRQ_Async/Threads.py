'''
Andreas Spiess #372  using two cores on pico
'barefoot" global variable
Also in the micropython handbook i have
first program- works well
seconjd program is with a 'baton" like in a relay race
'''
'''
import _thread
import utime
from machine import Pin
bPin = 18
bLed =Pin(bPin,Pin.OUT)
gPin=16
gLed = Pin(gPin,Pin.OUT )
rPin =17
rLed =Pin(rPin,Pin.OUT)
butPin =15
Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
BuzzPin=14
Buzzer=Pin(BuzzPin,Pin.OUT)
button_pressed=False
def Button_thread():
    global button_pressed
    while True:
        if Button.value() == 1:
            print('my press: ',Button.value())
            button_pressed=True
        utime.sleep(0.1)
_thread.start_new_thread(Button_thread,())
while True:
    print(Button.value(), button_pressed)
    if button_pressed==True:
        rLed.value(1)
        for i in range(1,10,1):
            Buzzer.value(1)
            utime.sleep(0.2)
            Buzzer.value(0)
            utime.sleep(0.2)
        button_pressed=False
    rLed.value(1)
    utime.sleep(2)
    gLed.value(1)
    rLed.value(0)
    utime.sleep(2)
    gLed.value(0)
    bLed.value(1)
    utime.sleep(1)
 '''   
    
    
# import _thread
# import utime
# from machine import Pin
# bPin = 18
# bLed =Pin(bPin,Pin.OUT)
# gPin=16
# gLed = Pin(gPin,Pin.OUT )
# rPin =17
# rLed =Pin(rPin,Pin.OUT)
# butPin =15
# Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
# BuzzPin=14
# Buzzer=Pin(BuzzPin,Pin.OUT)
# baton =_thread.allocate_lock()
# def ledRed_thread():
#     while True:
#         baton.acquire()
#         rLed.value(1)
#         utime.sleep(.5)
#         rLed.value(0)
#         utime.sleep(.5)
#         baton.release()
# _thread.start_new_thread(ledRed_thread,())

# while True:
#     baton.acquire()
#     gLed.value(1)
#     utime.sleep(.5)
#     gLed.value(0)
#     utime.sleep(.5)
#     baton.release()

'''
import machine
import utime
import urandom

led = machine.Pin(16,machine.Pin.OUT)
button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)

def button_handler(pin):
    print(pin)
    button.irq(handler = None)
    # timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    # print('Your reaction time was ' + str(timer_reaction) + "milliseconds!")

led.value(1)
#buttonVal= button.value()
utime.sleep(urandom.uniform(1,5))
led.value(0)
utime.sleep(.01)

# timer_start =utime.ticks_ms()
button.irq(trigger = machine.Pin.IRQ_RISING|machine.Pin.IRQ_FALLING, handler = button_handler)

'''

# import machine
# import utime
# import urandom
# butPin  = 15
# led = machine.Pin(16,machine.Pin.OUT)
# button = machine.Pin(butPin,machine.Pin.IN,machine.Pin.PULL_DOWN)

# def button_handler(pin):
#     print(pin)
#     # button.irq(handler = None)
#     # timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
#     # print('Your reaction time was ' + str(timer_reaction) + "milliseconds!")

# led.value(1)
# #buttonVal= button.value()
# utime.sleep(urandom.uniform(1,5))
# led.value(0)
# utime.sleep(.01)

# # timer_start =utime.ticks_ms()
# button.irq(trigger = machine.Pin.IRQ_RISING|machine.Pin.IRQ_FALLING, handler = button_handler)


# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/
'''
from machine import Pin

button = Pin(15, Pin.IN, Pin.PULL_DOWN)
counter = 0  # Initialize the button press count

def button_pressed(pin):
    global counter # Declare variable as global
    counter +=1
    print("Button Pressed! Count: ", counter)

# Attach the interrupt to the button's rising edge
button.irq(trigger=Pin.IRQ_RISING, handler=button_pressed)
'''
'''

import machine
import utime
import urandom

led = machine.Pin(16,machine.Pin.OUT)
button= machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)

def button_handler(pin):
    button.irq(handler = None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(),timer_start)
    print("Your reaction time was " + str(timer_reaction) + " milliseconds")
led.value(1)
utime.sleep(urandom.uniform(5,10))
led.value(0)
timer_start = utime.ticks_ms()
button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
            
            
'''

# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/

from machine import Pin, Timer
from time import sleep

# LED pin
led_pin = 14
led = Pin(led_pin, Pin.OUT)

# Callback function for the timer
def toggle_led(timer):
    print(led.value())
    led.value(not led.value())  # Toggle the LED state (ON/OFF)

# Create a periodic timer, the period is milliseconds
blink_timer = Timer()
blink_timer.init(mode=Timer.PERIODIC, period=1000, callback=toggle_led)  # Timer repeats every half second

# Main loop (optional)
while True:
    try:
        print('Main Loop is running')
        sleep(.2)
    except KeyboardInterrupt:
        print('Close Program')
        led.value(0)
        blink_timer.deinit()
        break


'''
## reaction game
import machine
import utime
import urandom

led = machine.Pin(16,machine.Pin.OUT)
button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)

# led.value(1)
# utime.sleep(urandom.uniform(3,8))
# led.value(0)
# button.irq(trigger = machine.Pin.IRQ_RISING, handler= button_handler)


def button_handler(pin):
    button.irq(handler = None)
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print('Your reaction time was ' + str(timer_reaction) + "milliseconds!")

led.value(1)
#buttonVal= button.value()
utime.sleep(urandom.uniform(3,8))
led.value(0)
timer_start =utime.ticks_ms()
button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)

'''
