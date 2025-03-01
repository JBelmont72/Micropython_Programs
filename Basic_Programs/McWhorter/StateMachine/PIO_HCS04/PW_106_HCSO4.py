'''Echolocation
the trigger pulse generation and the timing with micropython is unreliable if multiple functions are performed.
The approach recommended os to use the state machine.
dimensional analysis  speed of sound is 1234.8 km/hr (1000m/ km)(100 cm/m)(1 hr/3600)(1 sec/1,000,000 u sec)=0.0343 cm/ u sec
d = rate x time
'''
import machine
import time
 
TRIG_PIN = 1
ECHO_PIN = 0
 
TRIG = machine.Pin(TRIG_PIN,machine.Pin.OUT)
ECHO = machine.Pin(ECHO_PIN,machine.Pin.IN)
 
def distance():
    TRIG.low()
    time.sleep_us(2)
    TRIG.high()
    time.sleep_us(10)
    TRIG.low()
    while (ECHO.value()==0):    ## the echo pin is low and time passes 
        pass                    ## until the echo pin goes high 10 u sec after the trig pin goes low 
    time1=time.ticks_us()       ## when the echo pin goes high, the beginning of pingTime begins
    while (ECHO.value()==1):    ## ping is occurring until the return of the ping sends the echo value to 0
        pass
    time2=time.ticks_us()       ## once the echo pin goes low, that is the end of the pingtime
    pingTime=time.ticks_diff(time2,time1)/2 ## this is the same as (time2-time1)/2 but addresses the rare rollover of the clock
    d=.0343*pingTime
    return d
while True:
    dist=distance()
    print("Distance to Target: ",dist," cm")
    time.sleep_ms(250)