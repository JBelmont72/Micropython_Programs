'''my main.py to startup other files'''


from machine import Pin
from time import sleep
import sys
ButPin =14
Button = Pin(ButPin,Pin.IN,Pin.PULL_DOWN)
print(Button.value())

led = Pin('LED', Pin.OUT)
print('Blinking LED Example')
if Button.value()==1:
    for i in range(5):
        Button.value()
        
        print(Button.value())
        led.value(not led.value())
        sleep(0.5)
    
    import BME_Startup
    Button.value(0)
else:
    sys.exit()