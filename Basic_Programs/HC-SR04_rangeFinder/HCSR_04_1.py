## at the bottom I have the program from myEngineeringStuffs
##  I arranged it so I could convert into assemoly language



# # Complete project details at https://RandomNerdTutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/
# from hcsr04 import HCSR04
# from time import sleep
# from machine import Pin
# # ESP32 Pico
# sensor = HCSR04(trigger_pin=16, echo_pin=15, echo_timeout_us=10000)

# # ESP8266
# #sensor = HCSR04(trigger_pin=12, echo_pin=14, echo_timeout_us=10000)

# while True:
#     distance = sensor.distance_cm()
#     print('Distance:', distance, 'cm')
#     sleep(1)
###~~~~~~~~~~


#myEngineeringStuffs
# from machine import Pin, I2C
# import utime


# trig_pin = Pin(16, Pin.OUT)
# echo_pin = Pin(15, Pin.IN)


# def ultraSonic():
#    trig_pin.low()
#    utime.sleep_us(2)
#    trig_pin.high()
#    utime.sleep_us(5)
#    trig_pin.low()
#    while echo_pin.value() == 0:
#        pulseOff = utime.ticks_us()
#    while echo_pin.value() == 1:
#        pulseOn = utime.ticks_us()
       
#    time_used = pulseOn - pulseOff
#    distance = (time_used * 0.0343) / 2
#    distance = "{:.1f}".format(distance)
#    return str(distance)


# print("Process started...")

# while True:
#     print("Distance in cm : "+ str(ultraSonic()))
#     utime.sleep(1)
    
#####~~~~~~~~ This works fine
from machine import Pin, I2C
import utime


trig_pin = Pin(11, Pin.OUT)
echo_pin = Pin(12, Pin.IN)

## i took the below function and put it in the While True loop
# def ultraSonic():
#    trig_pin.low()
#    utime.sleep_us(2)
#    trig_pin.high()
#    utime.sleep_us(5)
#    trig_pin.low()
#    while echo_pin.value() == 0:
#        pulseOff = utime.ticks_us()
#    while echo_pin.value() == 1:
#        pulseOn = utime.ticks_us()
       
#    time_used = pulseOn - pulseOff
#    distance = (time_used * 0.0343) / 2
#    distance = "{:.1f}".format(distance)
#    return str(distance)
pulseOn=utime.ticks_us()
pulseOff=utime.ticks_us()

print("Process started...")

while True:
    trig_pin.low()
    utime.sleep_us(2)
    trig_pin.high()
    utime.sleep_us(5)
    trig_pin.low()
    while echo_pin.value() == 0:
       pulseOff = utime.ticks_us()
    while echo_pin.value() == 1:
       pulseOn = utime.ticks_us()
       
    echoVal=echo_pin.value()
    if echoVal == 0:
       pulseOff = utime.ticks_us()
    if echoVal == 1:
       pulseOn = utime.ticks_us()
       
    time_used = pulseOn - pulseOff
    distance = (time_used * 0.0343) / 2
    distance = "{:.5f}".format(distance)



    print("Process started...")
    print("Distance in cm : "+ str(distance))
    utime.sleep(1)