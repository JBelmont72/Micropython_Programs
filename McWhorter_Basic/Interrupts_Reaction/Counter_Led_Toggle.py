import machine
import utime


led_red= machine.Pin(16,machine.Pin.OUT)
button = machine.Pin(15,machine.Pin.IN,machine.Pin.PULL_DOWN)
print(button.value())
counter = 0
while True:
    if button.value()	==	1:
        led_red.value(1)
        print("Button  pressed!")
        print(button.value())
        counter +=1
        print("Counter ={}".format(counter))
        utime.sleep(.2)
    else:
        led_red.value(0)       
        print(button.value())
        print("NEW VALUE")
        utime.sleep(.2)
