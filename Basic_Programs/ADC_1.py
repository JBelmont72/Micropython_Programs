import machine
#from time import sleep
import utime
potPin =28

myPot = machine.ADC(potPin)
led_red = machine.Pin(15,machine.Pin.OUT)
led_yellow = machine.Pin(17,machine.Pin.OUT)
led_green = machine.Pin(18,machine.Pin.OUT)
myInput = float(input("Input your Voltage"))
if myInput >2:
    
    while True:
        led_red.value(1)
        utime.sleep(1)
        led_red.value(0)
        break
               


while True:
    led_red.value(0)
    led_yellow.value(0)
    led_green.value(0)
    potVal = myPot.read_u16()
    print(potVal)
    Voltage = 0.00005 * potVal
    print(Voltage)
    print(str(Voltage)+" Volts")
    utime.sleep(0.5)
    if Voltage >1.5:
        led_red.value(1)
        utime.sleep(1)
        
        if Voltage >1.8:
            led_red.value(0)
            led_yellow.value(1)
            utime.sleep(3)
    if Voltage <1.0:
        led_green.value(1)
        utime.sleep(1.0)
