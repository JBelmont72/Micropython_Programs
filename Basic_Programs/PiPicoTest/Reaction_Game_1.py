import machine
import utime
import urandom

led = machine.Pin(16,machine.Pin.OUT)
button = machine.Pin(19,machine.Pin.IN)

ledYellow = machine.Pin(17,machine.Pin.OUT)
ledPurple = machine.Pin(28,machine.Pin.OUT)
ledPurple.value(0)
ledYellow.value(0)

def button_handler(pin):
    button.irq(handler = None)
    print("This in the button_handler method")
    timer_reaction = utime.ticks_diff(utime.ticks_ms(), timer_start)
    print('Your reaction time was ' + str(timer_reaction) + "milliseconds!")

led.value(1)
#buttonVal= button.value()
utime.sleep(urandom.uniform(3,8))
led.value(0)
timer_start =utime.ticks_ms()
button.irq(trigger = machine.Pin.IRQ_FALLING, handler = button_handler)

            
