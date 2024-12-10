from  machine import Pin
from time import sleep

butPin = 14
button = Pin(butPin,Pin.IN,Pin.PULL_DOWN)

Led =17
led = Pin(Led, Pin.OUT)
led.value(0)
LED1=16
led1=Pin(LED1, Pin.OUT)
led1.value(0)

ledState =True
butValOld = 1
butValNew = 1


while True:
    butValNew = button.value()
    
    sleep(0.3)
    if((butValNew ==1) and  (butValOld == 0)):
        led.value(ledState)
        ledState = not ledState
        sleep(.5)
    print(f"New Button Val: ",butValNew, "\n\tOld Button Val: ",butValOld)
    butValOld =butValNew    
      
        
