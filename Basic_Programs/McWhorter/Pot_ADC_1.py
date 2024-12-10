import machine
import utime
potPin = 28
myPot= machine.ADC(potPin)
RedLed = 16
YellowLed =17
GreenLed =18
redLed = machine.Pin(RedLed,machine.Pin.OUT)
yellowLed = machine.Pin(YellowLed,machine.Pin.OUT)
greenLed = machine.Pin(GreenLed,machine.Pin.OUT)

#set up potentiometer on ADC GPIO 28
while True:
    potVal = myPot.read_u16()
    print(potVal)
    voltage = (3.3/65535)*potVal
    print("The voltage is eqaul to:  ",voltage)
    percent=(100/65535)*potVal
    print("Percent of PotVal is:  ",percent)
    utime.sleep(.5)
    if (percent < 70):
        redLed.value(1)
        yellowLed.value(0)
        greenLed.value(0)

    
    elif (percent >= 70 and percent <= 80):
        redLed.value(0)
        yellowLed.value(1)
        greenLed.value(0)
    elif (percent >80):
        redLed.value(0)
        yellowLed.value(0)
        greenLed.value(1)




'''
led_external=machine.Pin(17,machine.Pin.OUT)
button=machine.Pin(19,machine.Pin.IN)

while True:
    if button.value() ==1:
        led_external.value(1)
        x=button.value()
        print("x")
        utime.sleep(1)
    led_external.value(0)
    y = button.value()
    print("Value =  ", y)
    '''