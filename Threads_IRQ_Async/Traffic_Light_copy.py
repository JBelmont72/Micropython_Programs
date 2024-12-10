'''import libraries
needed to define pins
no setup and no loop, defne pins and then call the function
define pins, then define a new function AND THEN CALL that function



'''
import machine
import time

red_pin = machine.Pin(16,machine.Pin.OUT)
yellow_pin= machine.Pin(17,machine.Pin.OUT)
green_pin = machine.Pin (18,machine.Pin.OUT)
#	Function to turn on the LEDs in a specific pattern
def traffic_light():
    red_pin.on()	#same as digitalWrite(HIGH in C++
    time.sleep(2)
    red_pin.off()
    green_pin.on()
    time.sleep(2)
    green_pin.off()
    time.sleep(1)
    yellow_pin.on()
    time.sleep(1)
    yellow_pin.off()
    
while True:    
    traffic_light()
    
    '''
import machine
import utime

led_red= machine.Pin(17,machine.Pin.OUT)
led_green = machine.Pin(18,machine.Pin.OUT)

while True:

    led_red.value(1)
    utime.sleep(0.5)
    led_red.value(0)
    utime.sleep(0.75)
while True:
    led_green.value(False)
    led_red.toggle()
    utime.sleep(0.1)
'''
    