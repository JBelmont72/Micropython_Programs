import machine
import time



button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)
buzzer =machine.Pin(22,machine.Pin.OUT)

red_pin = machine.Pin(16,machine.Pin.OUT)
yellow_pin= machine.Pin(17,machine.Pin.OUT)
green_pin = machine.Pin (18,machine.Pin.OUT)

global button_pressed
button_pressed = False

def button_reader_thread():
    global button_pressed
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
try:    
    while True:    
        traffic_light()
        time.sleep(10)
except KeyboardInterrupt:
    red_pin.value(0)
    green_pin.value(0)
    yellow_pin.value(0)
    print('Bye')

    