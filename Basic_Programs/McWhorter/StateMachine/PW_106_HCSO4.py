'''

'''
import machine
import time
 
TRIG_PIN = 16
ECHO_PIN = 17
 
TRIG = machine.Pin(TRIG_PIN,machine.Pin.OUT)
ECHO = machine.Pin(ECHO_PIN,machine.Pin.IN)
 
def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    while (ECHO.value()==0):
        pass
    time1=time.ticks_us()
    while (ECHO.value()==1):
        pass
    time2=time.ticks_us()
    pingTime=time.ticks_diff(time2,time1)/2
    d=.0343*pingTime
    return d
while True:
    dist=distance()
    print("Distance to Target: ",dist," cm")
    time.sleep_ms(250)