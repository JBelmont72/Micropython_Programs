from machine import Pin
import utime
import _thread
'''
https://dev.to/blues/your-first-steps-with-raspberry-pi-pico-and-visual-studio-code-4jbd
Nice tutorial on getting started with Micropython on BS Code
also links to "threads"
https://docs.python.org/3/library/threading.html

pushButton = Pin(16,Pin.IN)
ledRed = Pin(17,Pin.OUT)

#   Next we'll create a global variable that can be set and read by either thread of our program:
global button_pressed
button_pressed = False



'''

from machine import Pin
import utime
import _thread

button = Pin(16, Pin.IN)
led = Pin(17, Pin.OUT)

global button_pressed
button_pressed = False

def read_button():
    global button_pressed
    while True:
        if button.value() == 0:
            button_pressed = not button_pressed
            utime.sleep(0.5)

_thread.start_new_thread(read_button, ())

while True:
    if button_pressed == True:
        led.value(0)
    else:
        led.value(1)