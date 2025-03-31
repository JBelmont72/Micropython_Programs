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
    time.sleep_us(5)
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

########~~~~~~~
# from machine import Pin
# import time

# trig = Pin(11, Pin.OUT)
# echo = Pin(12, Pin.IN)
# trig.low()
# time.sleep_us(5)
# trig.high()
# time.sleep(1)
# trig.low()
# print("TRIG Pulse Done")

# if echo.value():
#     print("ECHO HIGH")
# else:
#     print("ECHO LOW")
#####~~~~~~~
# import machine
# import time

# # Pin configuration
# TRIG_PIN = 1  # GPIO11 (Physical pin 15 on Pico W)
# ECHO_PIN = 0  # GPIO12 (Physical pin 16 on Pico W)

# TRIG = machine.Pin(TRIG_PIN, machine.Pin.OUT)
# ECHO = machine.Pin(ECHO_PIN, machine.Pin.IN)

# # Timeout to prevent freezing
# TIMEOUT_US = 50000  # 30ms timeout for echo response (~5 meters max)

# def distance():
#     # Ensure TRIG is LOW before sending a pulse
#     TRIG.low()
#     time.sleep_us(5)

#     # Send a 10µs pulse to trigger the sensor
#     TRIG.high()
#     time.sleep_us(10)
#     TRIG.low()

#     # Wait for echo to go HIGH
#     start_time = time.ticks_us()
#     while ECHO.value() == 0:
#         if time.ticks_diff(time.ticks_us(), start_time) > TIMEOUT_US:
#             print("Timeout: No echo detected (HIGH)")
#             return -1

#     time1 = time.ticks_us()  # Echo pulse start time

#     # Wait for echo to go LOW
#     start_time = time.ticks_us()
#     while ECHO.value() == 1:
#         if time.ticks_diff(time.ticks_us(), start_time) > TIMEOUT_US:
#             print("Timeout: Echo pin stuck HIGH")
#             return -1

#     time2 = time.ticks_us()  # Echo pulse end time

#     # Calculate ping time and convert to distance
#     ping_time = time.ticks_diff(time2, time1) / 2  # Divide by 2 for round trip
#     distance_cm = 0.0343 * ping_time  # 343 m/s → 0.0343 cm/µs

#     # Return the distance
#     return distance_cm

# # Main loop
# while True:
#     dist = distance()
#     if dist == -1:
#         print("Measurement failed. Retrying...")
#     else:
#         print(f"Distance to Target: {dist:.2f} cm")

#     time.sleep_ms(250)  # Delay before next measurement
