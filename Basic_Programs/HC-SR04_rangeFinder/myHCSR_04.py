'''
https://github.com/rsc1975/micropython-hcsr04
https://randomnerdtutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/

'''
from machine import Pin, time_pulse_us
from utime import sleep_us
import time
# __version__ = '0.2.1'
# __author__ = 'Roberto Sánchez'
# __license__ = "Apache License 2.0. https://www.apache.org/licenses/LICENSE-2.0"

# class HCSR04:
#     """
#     Driver to use the untrasonic sensor HC-SR04.
#     The sensor range is between 2cm and 4m.

#     The timeouts received listening to echo pin are converted to OSError('Out of range')

#     """
#     # echo_timeout_us is based in chip range limit (400cm)
#     def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
#         """
#         trigger_pin: Output pin to send pulses
#         echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
#         echo_timeout_us: Timeout in microseconds to listen to echo pin. 
#         By default is based in sensor limit range (4m)
#         """
#         self.echo_timeout_us = echo_timeout_us
#         # Init trigger pin (out)
#         self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
#         self.trigger.value(0)

#         # Init echo pin (in)
#         self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

#     def _send_pulse_and_wait(self):
#         """
#         Send the pulse to trigger and listen on echo pin.
#         We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
#         """
#         self.trigger.value(0) # Stabilize the sensor
#         sleep_us(5)
#         self.trigger.value(1)
#         # Send a 10us pulse.
#         sleep_us(10)
#         self.trigger.value(0)
#         try:
#             pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
#             # time_pulse_us returns -2 if there was timeout waiting for condition; and -1 if there was timeout during the main measurement. It DOES NOT raise an exception
#             # ...as of MicroPython 1.17: http://docs.micropython.org/en/v1.17/library/machine.html#machine.time_pulse_us
#             if pulse_time < 0:
#                 MAX_RANGE_IN_CM = const(500) # it's really ~400 but I've read people say they see it working up to ~460
#                 pulse_time = int(MAX_RANGE_IN_CM * 29.1) # 1cm each 29.1us
#             return pulse_time
#         except OSError as ex:
#             if ex.args[0] == 110: # 110 = ETIMEDOUT
#                 raise OSError('Out of range')
#             raise ex

#     def distance_mm(self):
#         """
#         Get the distance in milimeters without floating point operations.
#         """
#         pulse_time = self._send_pulse_and_wait()

#         # To calculate the distance we get the pulse_time and divide it by 2 
#         # (the pulse walk the distance twice) and by 29.1 becasue
#         # the sound speed on air (343.2 m/s), that It's equivalent to
#         # 0.34320 mm/us that is 1mm each 2.91us
#         # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
#         mm = pulse_time * 100 // 582
#         return mm

#     def distance_cm(self):
#         """
#         Get the distance in centimeters with floating point operations.
#         It returns a float
#         """
#         pulse_time = self._send_pulse_and_wait()

#         # To calculate the distance we get the pulse_time and divide it by 2 
#         # (the pulse walk the distance twice) and by 29.1 becasue
#         # the sound speed on air (343.2 m/s), that It's equivalent to
#         # 0.034320 cm/us that is 1cm each 29.1us
#         cms = (pulse_time / 2) / 29.1
#         return cms
    
#####   #################

from machine import Pin, time_pulse_us
from utime import sleep_us
trigger_pin=16
echo_pin=17
echo_timeout_us=500*2*30 ## can make longer distance up to about 1,000,000 microseconds
trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
echo = Pin(echo_pin, mode=Pin.IN, pull=None)
tHigh=time.ticks_us()
tLow=time.ticks_us()
while True:

    # Send the pulse to trigger and listen on echo pin.
    # We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.

    trigger.value(0) # Stabilize the sensor
    sleep_us(5)
    trigger.value(1)
    # Send a 10us pulse.
    sleep_us(10)
    trigger.value(0)
    try:
        # pulse_time = time_pulse_us(echo, 1, echo_timeout_us)
        # time_pulse_us returns -2 if there was timeout waiting for condition; and -1 if there was timeout during the main measurement. It DOES NOT raise an exception
        # ...as of MicroPython 1.17: http://docs.micropython.org/en/v1.17/library/machine.html#machine.time_pulse_us
        echoVal=echo.value(0)
        if echoVal==0:
            tLow =time.ticks_us()
        if echoVal== 1:
            tHigh=time.ticks_us()
        pulse_time=time.ticks_diff(tLow,tHigh)
        
        
        if pulse_time < 0:
            MAX_RANGE_IN_CM = const(500) # it's really ~400 but I've read people say they see it working up to ~460
            pulse_time = int(MAX_RANGE_IN_CM * 29.1) # 1cm each 29.1us
            # print( 'pulse time: ',pulse_time)
            # sleep_us(1000)
        cms = (pulse_time / 2) / 29.1
        print(cms)
        sleep_us(100000)
    except OSError as ex:
        if ex.args[0] == 110: # 110 = ETIMEDOUT
            raise OSError('Out of range')
        raise ex




#     def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
#         """
#         trigger_pin: Output pin to send pulses
#         echo_pin: Readonly pin to measure the distance. The pin should be protected with 1k resistor
#         echo_timeout_us: Timeout in microseconds to listen to echo pin. 
#         By default is based in sensor limit range (4m)
#         """
#         self.echo_timeout_us = echo_timeout_us
#         # Init trigger pin (out)
#         self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
#         self.trigger.value(0)

#         # Init echo pin (in)
#         self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

#     def _send_pulse_and_wait(self):
#         """
#         Send the pulse to trigger and listen on echo pin.
#         We use the method `machine.time_pulse_us()` to get the microseconds until the echo is received.
#         """
#         self.trigger.value(0) # Stabilize the sensor
#         sleep_us(5)
#         self.trigger.value(1)
#         # Send a 10us pulse.
#         sleep_us(10)
#         self.trigger.value(0)
#         try:
#             pulse_time = time_pulse_us(self.echo, 1, self.echo_timeout_us)
#             # time_pulse_us returns -2 if there was timeout waiting for condition; and -1 if there was timeout during the main measurement. It DOES NOT raise an exception
#             # ...as of MicroPython 1.17: http://docs.micropython.org/en/v1.17/library/machine.html#machine.time_pulse_us
#             if pulse_time < 0:
#                 MAX_RANGE_IN_CM = const(500) # it's really ~400 but I've read people say they see it working up to ~460
#                 pulse_time = int(MAX_RANGE_IN_CM * 29.1) # 1cm each 29.1us
#             return pulse_time
#         except OSError as ex:
#             if ex.args[0] == 110: # 110 = ETIMEDOUT
#                 raise OSError('Out of range')
#             raise ex

#     def distance_mm(self):
#         """
#         Get the distance in milimeters without floating point operations.
#         """
#         pulse_time = self._send_pulse_and_wait()

#         # To calculate the distance we get the pulse_time and divide it by 2 
#         # (the pulse walk the distance twice) and by 29.1 becasue
#         # the sound speed on air (343.2 m/s), that It's equivalent to
#         # 0.34320 mm/us that is 1mm each 2.91us
#         # pulse_time // 2 // 2.91 -> pulse_time // 5.82 -> pulse_time * 100 // 582 
#         mm = pulse_time * 100 // 582
#         return mm

#     def distance_cm(self):
#         """
#         Get the distance in centimeters with floating point operations.
#         It returns a float
#         """
#         pulse_time = self._send_pulse_and_wait()

#         # To calculate the distance we get the pulse_time and divide it by 2 
#         # (the pulse walk the distance twice) and by 29.1 becasue
#         # the sound speed on air (343.2 m/s), that It's equivalent to
#         # 0.034320 cm/us that is 1cm each 29.1us
#         cms = (pulse_time / 2) / 29.1
#         return cms
    
    
#     machine.time_pulse_us(pin, pulse_level, timeout_us=1000000, /)
# Time a pulse on the given pin, and return the duration of the pulse in microseconds. The pulse_level argument should be 0 to time a low pulse or 1 to time a high pulse.

# If the current input value of the pin is different to pulse_level, the function first (*) waits until the pin input becomes equal to pulse_level, then (**) times the duration that the pin is equal to pulse_level. If the pin is already equal to pulse_level then timing starts straight away.

# The function will return -2 if there was timeout waiting for condition marked (*) above, and -1 if there was timeout during the main measurement, marked (**) above. The timeout is the same for both cases and given by timeout_us (which is in microseconds).