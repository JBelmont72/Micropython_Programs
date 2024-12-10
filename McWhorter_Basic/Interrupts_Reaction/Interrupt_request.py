import machine
import utime


button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_DOWN)
count = 0

def button_press(pin):
    print("You press the button!")
    utime.sleep(1)

button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_press)

while True:
    count+=1
    print(count)
    utime.sleep(1)
  
'''
import machine
import utime
import urandom

led = machine.Pin(16, machine.Pin.OUT)
#button = machine.Pin(15, machine.Pin.IN,machine.Pin.PULL_DOWN)
#button = machine.Pin(15, machine.Pin.IN,machine.Pin.PULL_DOWN)
button = machine.Pin(15, machine.Pin.IN)

def button_press(pin):
    button.irq(handler=None)
    rection_time = utime.ticks_diff(utime.ticks_ms(), timer_light_off)
    print("Your reaction time was " + str(rection_time) + " milliseconds!")

led.value(1)
utime.sleep(urandom.uniform(2, 5))
led.value(0)
timer_light_off = utime.ticks_ms()
button.irq(trigger=machine.Pin.IRQ_FALLING, handler=button_press)
'''