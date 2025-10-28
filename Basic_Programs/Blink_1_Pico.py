import machine
import time
# led=machine.Pin(2,machine.Pin.OUT)
led=machine.Pin('LED',machine.Pin.OUT)
# led = machine.Pin('LED',machine.Pin.OUT)    ## this is the on board LED
# led = machine.Pin(machine.Pin(14),machine.Pin.OUT) ##change the pin number as desired
blinkInterval=.2
while True:
    print('Look Sam,I\'m winking at you!!')
    led.value(True)
    time.sleep(1)
    led.value(False)
    time.sleep(1)
    led.value(True)
    time.sleep(blinkInterval)
    led.value(False)
    time.sleep(blinkInterval)
    led.value(True)
    time.sleep(blinkInterval * 2)
    led.value(False)
    time.sleep(blinkInterval *2)