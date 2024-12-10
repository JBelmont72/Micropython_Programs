import machine
import time

# led = machine.Pin('LED',machine.Pin.OUT)
led = machine.Pin(machine.Pin(17),machine.Pin.OUT)

while True:
    led.value(True)
    time.sleep(1)
    led.value(False)
    time.sleep(1)