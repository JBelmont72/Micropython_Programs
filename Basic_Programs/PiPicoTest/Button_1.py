import machine
import utime


led_red= machine.Pin(15,machine.Pin.OUT)
button = machine.Pin(14,machine.Pin.IN)
print(button.value())

x=3
y = 4
def addition(x,y):
    c=x+y
    return c



while True:
    if button.value()== 1:
        led_red.value(False)
        print("Button pressed!", button.value())
        print(button.value())
        utime.sleep(1)
    led_red.value(True)       
    print(button.value())
    print("NEW VALUE")
    SUM= (addition(x,y))
    print(SUM)
    
