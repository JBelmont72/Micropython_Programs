'''Works great WITH LCD!
two player reaction with fastest player  WITH LCD
on the bottom is the sketch with two players but no fastest player determination
https://shop.sb-components.co.uk/blogs/posts/raspberry-pi-pico-reaction-game
good tutorial but I used the get started with micropython on RPI Pico book for reference
https://penguintutor.com/electronics/pico-power
very goo tutorial for powering the pico

https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico

'''

import utime
import urandom

from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
#i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=4000)
i2c = I2C(1, sda=Pin(26), scl=Pin(27), freq=4000)
#I2C_ADDR = i2c.scan()[0]
I2C_ADDR = 0x27
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)





interrupt_flag = 0
debounce_time = 0
reaction_time = 0

fastest_button = None

led = machine.Pin(16, machine.Pin.OUT)
#button = machine.Pin(15, machine.Pin.IN,machine.Pin.PULL_DOWN)
left_button = machine.Pin(14, machine.Pin.IN,machine.Pin.PULL_DOWN)
right_button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
'''
while True:
    lcd.clear()
    lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
    lcd.putstr("Tom's Hardware")
    sleep(2)
    lcd.blink_cursor_off()
    lcd.clear()
    lcd.putstr("Backlight Test")
    for i in range(10):
        lcd.backlight_on()
        sleep(0.2)
        lcd.backlight_off()
        sleep(0.2)
    lcd.backlight_on()
    lcd.hide_cursor()
    for i in range(20):
        lcd.putstr(str(i))
        sleep(0.4)
        lcd.clear()
'''








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
    lcd.clear()
    #lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
    lcd.putstr("Left Player Wins")
    lcd.putstr("Your reaction time was "+ str(timer_reaction)+ " milliseconds")
    print("Left Player Wins!")
    sleep(2)
if fastest_button is right_button:
    lcd.clear()
    #lcd.putstr("I2C Address:"+str(hex(I2C_ADDR))+"\n")
    lcd.putstr("Your reaction time was "+ str(timer_reaction)+ " milliseconds")
    lcd.putstr("Right Player Wins")
    
    print("Right Player Wins!")
    sleep(2)
    lcd.clear()
print(left_button.value())

'''another way is to put the print statemints in the def button+press callback function like this:
def button_press(pin):
    left_button.irq(handler=None)
    right_button.irq(handler=None)
    rection_time = utime.ticks_diff(utime.ticks_ms(), timer_light_off)
    if pin == left_button:
        print("Left player is winner!")
    elif pin == right_button:
        print("Right player is winner!")
    print("Your reaction time was " + str(rection_time) + " milliseconds!")

led.value(1)
utime.sleep(urandom.uniform(5, 10))
led.value(0)
timer_light_off = utime.ticks_ms()
right_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)
left_button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)


'''
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