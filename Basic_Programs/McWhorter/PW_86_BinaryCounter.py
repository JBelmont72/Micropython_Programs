'''
binary counter- two programs 
first one way and the second both ways
'''
# from machine import Pin
# import utime as time

# Pin1=16
# Pin2=17
# Pin4=18
# Pin8=19
# redPin=14
# led_1=Pin(Pin1,Pin.OUT)
# led_2=Pin(Pin2,Pin.OUT)
# led_4=Pin(Pin4,Pin.OUT)
# led_8=Pin(Pin8,Pin.OUT)
# UpBut=Pin(redPin,Pin.IN,Pin.PULL_DOWN)
# press =0
# tUp=time.ticks_ms() ## when redBut is 0
# tDown = time.ticks_ms() ## when redBut is 1
# ButValOld=0


# def countUp(pin):
#     global tUp,tDown,press,ButValOld
#     ButValNew=UpBut.value()
#     if ButValNew==0:
#         tUp=time.ticks_ms()
#     if ButValNew==1:
#         tDown=time.ticks_ms()
#     timeDiff=tDown-tUp
#     if ButValOld==0 and ButValNew==1 and timeDiff>50:
#         press =press +1
#         print("PRESSED ",press)
#         led_1.toggle()
#         if press%2==0:
#             led_2.toggle()
#         if press%4==0:
#             led_4.toggle()
#         if press%8== 0:
#             led_8.toggle()
        
#     ButValOld=ButValNew

# UpBut.irq(trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING,handler=countUp)
# try:    
#     while True: 
#         pass
# except KeyboardInterrupt:
#     led_1.value(0)
#     led_2.value(0)
#     led_4.value(0)
#     led_8.value(0)
#     print('all done')

##~~~~~~~~~~~~~~~~~~
## this has an up and down binary counter
from machine import Pin
import utime as time

Pin1=16
Pin2=17
Pin4=18
Pin8=19
redPin=14
bluePin=15
led_1=Pin(Pin1,Pin.OUT)
led_2=Pin(Pin2,Pin.OUT)
led_4=Pin(Pin4,Pin.OUT)
led_8=Pin(Pin8,Pin.OUT)
UpBut=Pin(redPin,Pin.IN,Pin.PULL_DOWN)
DownBut=Pin(bluePin,Pin.IN,Pin.PULL_DOWN)
press =0
tUp=time.ticks_ms() ## when redBut is 0
tDown = time.ticks_ms() ## when redBut is 1
ButValOld=0
tUp2=time.ticks_ms() ## when redBut is 0
tDown2 = time.ticks_ms() ## when redBut is 1
ButValOld2=0


def countUp(pin):
    global tUp,tDown,press,ButValOld
    ButValNew=UpBut.value()
    if ButValNew==0:
        tUp=time.ticks_ms()
    if ButValNew==1:
        tDown=time.ticks_ms()
    timeDiff=tDown-tUp
    if ButValOld==0 and ButValNew==1 and timeDiff>50:
        press =press +1
        print("PRESSED ",press)
        led_1.toggle()
        if press%2==0:
            led_2.toggle()
        if press%4==0:
            led_4.toggle()
        if press%8== 0:
            led_8.toggle()
        
    ButValOld=ButValNew
def countDown(pin):
    global tUp2,tDown2,press,ButValOld2
    ButValNew2=UpBut.value()
    if ButValNew2==0:
        tUp=time.ticks_ms()
    if ButValNew2==1:
        tDown=time.ticks_ms()
    timeDiff2=tDown2-tUp2
    if ButValOld2==0 and ButValNew2==1 and timeDiff2>50:
        press =press +1
        print("PRESSED ",press)
        led_1.toggle()
        if press%2==0:
            led_2.toggle()
        if press%4==0:
            led_4.toggle()
        if press%8== 0:
            led_8.toggle()
        
    ButValOld2=ButValNew2

UpBut.irq(trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING,handler=countUp)
DownBut.irq(trigger=Pin.IRQ_FALLING|Pin.IRQ_RISING,handler=countDown)
try:    
    while True: 
        pass
except KeyboardInterrupt:
    led_1.value(0)
    led_2.value(0)
    led_4.value(0)
    led_8.value(0)
    print('all done')

