'''
fair tutorial, the last program does not work, I need to revisit in future
https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-micropython/

interrupts and debouncing
If you are interfacing external devices that are time-sensitive, you should use interrupts
'''
'''

import machine
import utime


led_red= machine.Pin(16,machine.Pin.OUT)
button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_UP)
button.value(0)
print(button.value())
counter = 0
while True:
    if button.value()	==	0:
        led_red.value(1)
        print("Button  pressed!")
        print(button.value())
        counter +=1
        print("Counter ={}".format(counter))
        utime.sleep(.2)
    else:
        led_red.value(0)       
        print(button.value())
        print("NEW VALUE")
        utime.sleep(.2)
'''
# this worked but I was not able to turn the led off or add a ELIF or ELSE
# had to use time,   utime and sleep did not work because if the time.ticks_ms() method
'''
import machine
import time


led_red= machine.Pin(16,machine.Pin.OUT)
button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_UP)
button.value(1)
print(button.value())
counter = 0

debounce_time = 0

while True:
    if (( button.value() is	0)  and (time.ticks_ms() - debounce_time) > 300) :
        led_red.value(1)
        print("Button  pressed!")
        print(button.value())
        debounce_time =time.ticks_ms()
        counter +=1
        print("Counter ={}".format(counter))
'''
# works with the interrupt flag
'''
 import the Pin class and initialize a global variable called interrupt_flag to 0.
 We will use this variable to keep track of the occurrence of interrupts. Global variables in MicroPython can be accessed by all functions.
 Then we create a pin object of the Pin class.

define a function called callback() to handle interrupts. The code inside this function should not perform any complex task,
as it needs to hand over CPU usage to the main program quickly. We set the interrupt_flag variable as 1.
Note that we need to use the global keyword when we change a global variable inside a function.

handler : handler specifies the function which will be called when an interrupt occurs.
pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

In the while loop, we continuously check the value of the interrupt_flag variable.
If this value is detected as ‘1’, that means an interrupt has occurred.
We reset the variable to ‘0’ so that the variable can be set again when an interrupt occurs.
You might have noticed that the line “Interrupt has occurred” is printed in multiple lines with just a single button press.
This is similar to the button-bouncing case that we discussed earlier in this article.
We shall solve this problem in the next step.
'''
'''
from machine import Pin
import time

interrupt_flag=0
pin = Pin(15,Pin.IN,Pin.PULL_UP)

counter = 0

def callback(pin):
    global interrupt_flag
    interrupt_flag=1

pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)
while True:
    if interrupt_flag is 1:
        print("Interrupt has occured")
        counter += 1
        print("counter is:  {}".format(counter))
        interrupt_flag=0
'''

# Source: Electrocredible.com, Language: MicroPython
from machine import Pin
import time
interrupt_flag=0
debounce_time=0
pin = Pin(15, Pin.IN, Pin.PULL_UP)
led = Pin(16, Pin.OUT)
count=0

def callback(pin):
    global interrupt_flag, debounce_time
    if (time.ticks_ms()-debounce_time) > 500:
        interrupt_flag= 1
        debounce_time=time.ticks_ms()
        print(debounce_time)
pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

while True:
    if interrupt_flag is 1:
        interrupt_flag=0
        print("Interrupt Detected")
        led.toggle()
        print("LED value:  {}".format(led.value()))
        






