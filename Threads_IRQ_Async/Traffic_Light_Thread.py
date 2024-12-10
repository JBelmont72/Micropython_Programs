import machine
import time

import _thread

button = machine.Pin(19,machine.Pin.IN,machine.Pin.PULL_DOWN)
buzzer =machine.Pin(22,machine.Pin.OUT)

red_pin = machine.Pin(16,machine.Pin.OUT)
yellow_pin= machine.Pin(17,machine.Pin.OUT)
green_pin = machine.Pin (18,machine.Pin.OUT)

global button_pressed
button_pressed = False

def button_reader_thread():
    global_button_pressed
    while True:
        if button.value()	== 1:
            button_pressed = True
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
    