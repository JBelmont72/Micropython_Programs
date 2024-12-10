'''
note that there are different DHT11 modules with its own one-wire communiction (not the more widespread dallas one wire), as
well as I2c newer modules.


'''
## this works and is from https://docs.micropython.org/en/latest/esp8266/tutorial/dht.html
# import dht
# import machine
# import time

# print("Starting DHT11.")
# d = dht.DHT11(machine.Pin(17))


# while True:
#     print("Measuring.")
#     time.sleep(5)
#     retry = 0
#     while retry < 3:
#         try:
#             d.measure()
#             break
#         except:
#             retry = retry + 1
#             print(".", end = "")

#     print("")

#     if retry < 3:
#         print("Temperature: %3.1f °C" % d.temperature())
#         print("   Humidity: %3.1f %% RH" % d.humidity())

#     time.sleep(5)



# interesting- the DHT11 is a sensor and would be an "INPUT" but here it
# is designated an OUTPUT, so that vlotage can be sent to it


# The sensor uses a one wire protocol so in the DHT library module a request for data is sent and data is returned over the same pin. I assume that the pin is changed between input and output in the library. In Arduino we use an external pull down resistor on the data pin so I guess using the internal pull down makes the circuit easier
#  I used the built-in temp sensor on the pico W:

# adcPin = 4
# sensor = machine.ADC(adcPin)
# adcVal = sensor.read_u16()
# voltage = (3.3/65535) * adcVal
# temperature = 27 - (voltage - 0.706)/0.001721

# The error was, '  File "<stdin>", line 12, in <module>'. The line was 'sensor.measure()'. So I placed a 'time.sleep(1)' after the 'sensor=DHT11(myPin)'.
###  this works different pin instantiation
# from machine import Pin
# import utime as time
# from dht import DHT11

# dataPin  =17

# myPin = Pin(dataPin,Pin.OUT,Pin.PULL_UP)
# # now create a DHT11 object called sensor, and pass to it the 'MyPin'

# sensor = DHT11(myPin)
# time.sleep(.250)
# while True:
#     sensor.measure()
#     time.sleep(.250)
#     tempC = sensor.temperature()
#     hum = sensor.humidity()
#     print(tempC,hum)
#     time.sleep(1)
    

    

# from machine import Pin
# from time import sleep
# import dht 

### example with 3 different object instantiations!!
import dht
import machine
import time
dataPin =17
## option 1
# sensor = dht.DHT11(machine.Pin(dataPin))    ## works
## option 2   the following 2 commands work equally well!!
#myPin = machine.Pin(dataPin,machine.Pin.OUT,machine.Pin.PULL_UP)
##  now create a DHT11 object called sensor, and pass to it the 'MyPin'
# sensor = dht.DHT11(myPin)
###################
## option # 3
sensor = dht.DHT11(dataPin)
while True:
  try:
    time.sleep(5)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    temp_f = temp * (9/5) + 32.0
    print('Temperature: %3.1f C' %temp)
    print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%' %hum)
  except OSError as e:
    print('Failed to read sensor.')
