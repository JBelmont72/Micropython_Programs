# import machine
# import utime
# import urandom

# led = machine.Pin(17,machine.Pin.OUT)
# red_button = machine.Pin(15,machine.Pin.IN)
# green_button = machine.Pin(18,machine.Pin.IN)

# fastest_button =None


# def button_handler(pin):
#     red_button.irq(handler = None)
#     green_button.irq(handler = None)
#     print("This in the button_handler method")
    
#     global fastest_button
#     fastest_button = pin
#     '''
#     timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
#     print('Your reaction time was ' + str(timer_reaction) + "milliseconds!")
#     '''
# led.value(1)
# #buttonVal= button.value()
# utime.sleep(urandom.uniform(3,8))
# led.value(0)
# timer_start =utime.ticks_ms()
# green_button.irq(trigger =machine.Pin.IRQ_RISING, handler = button_handler)
# red_button.irq(trigger = machine.Pin.IRQ_RISING, handler = button_handler)
# while fastest_button is None:
#     utime.sleep(1)
    
# if fastest_button is green_button:
#     print("Green Player wins!")
# elif fastest_button is red_button:
#     print("Red Player wins!")




# red_button.irq(trigger = machine.Pin.IRQ_FALLING, handler = button_handler)

# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/
#############################
# from machine import Pin, Timer
# from time import sleep

# # LED pin
# led_pin = 14
# led = Pin(led_pin, Pin.OUT)

# # Callback function for the timer
# def toggle_led(timer):
#     print(led.value())
#     led.value(not led.value())  # Toggle the LED state (ON/OFF)

# # Create a periodic timer, the period is milliseconds
# blink_timer = Timer()
# blink_timer.init(mode=Timer.PERIODIC, period=1000, callback=toggle_led)  # Timer repeats every half second

# # Main loop (optional)
# while True:
#     try:
#         print('Main Loop is running')
#         sleep(.2)
#     except KeyboardInterrupt:
#         print('Close Program')
#         led.value(0)
#         blink_timer.deinit()
#         break
##############################

# import machine
# import utime
# import urandom

# led = machine.Pin(16,machine.Pin.OUT)
# button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)

# def button_handler(pin):
#     print(pin)
#     button.irq(handler = None)
#     timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
#     print('Your reaction time was ' + str(timer_reaction) + "milliseconds!")

# led.value(1)
# #buttonVal= button.value()
# utime.sleep(urandom.uniform(1,5))
# led.value(0)
# utime.sleep(.01)

# timer_start =utime.ticks_ms()

# # Attach the interrupt to the button's rising edge
# button.irq(trigger = machine.Pin.IRQ_RISING|machine.Pin.IRQ_FALLING, handler = button_handler)
# # while True:
# #     pass
# while True:
#     try:
#         pass
#         # print('Main Loop is running')
#         utime.sleep(.2)
#     except KeyboardInterrupt:
#         print('Close Program')
#         led.value(0)
#         # blink_timer.deinit()
#         break

import machine
import utime
import urandom

led = machine.Pin(16,machine.Pin.OUT)
button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)
counter =0

def count(pin):
    global counter
    counter +=1
    print(counter)
    
button.irq(trigger=machine.Pin.IRQ_RISING,handler=count)

while True:
    try:
        utime.sleep(0.02)
        pass
    except KeyboardInterrupt:
        print('Final count: ',counter)
        utime.sleep(.1)
        print('Closing Program')
        break

