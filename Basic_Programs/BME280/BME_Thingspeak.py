'''
from https://microdigisoft.com/weather-monitoring-with-raspberry-pi-pico-w-bme280-and-thingspeak/
works well 11 Feb 2025
RG4961TZ9BKHMJ84
'''

# import machine
# import urequests 
# from machine import Pin, SoftI2C
# import network, time
# import BME280  
# i2c = SoftI2C(scl=Pin(1), sda=Pin(0), freq=10000)    #initializing the I2C method
# THINGSPEAK_WRITE_API_KEY = 'RG4961TZ9BKHMJ84'
#     #  'https://api.thingspeak.com/update'
# HTTP_HEADERS = {'Content-Type': 'application/json'} 
# # api_key = 'RG4961TZ9BKHMJ84'
# # base_url = 'https://api.thingspeak.com/update' = 'YOUR_THINGSPEAK_API_KEY' 

# UPDATE_TIME_INTERVAL = 5000  # in ms 
# last_update = time.ticks_ms() 

# # ssid='Your SSID'
# # password='Your Password'
# ssid = 'SpectrumSetup-41'
# password = 'leastdinner914'
# # Configure ESP32 as Station
# sta_if=network.WLAN(network.STA_IF)
# sta_if.active(True)

# if not sta_if.isconnected():
#     print('connecting to network...')
#     sta_if.connect(ssid, password)
#     while not sta_if.isconnected():
#      pass
# print('network config:', sta_if.ifconfig()) 

# while True: 
#     if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL: 
#          bme = BME280.BME280(i2c=i2c)          #BME280 object created
#          temperature = bme.temperature         #reading the value of temperature
#          humidity = bme.humidity               #reading the value of humidity
#          pressure = bme.pressure               #reading the value of pressure
#         #  print(temperature,humidity,pressure)
#          bme_readings = {'field1':temperature, 'field2':pressure, 'field3':humidity}
#         #  bme_readings=ujson.dumps(bme_readings) 
#          request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = HTTP_HEADERS )  
#          request.close() 
#          print(bme_readings)
#          last_update=time.ticks_ms()
         
''' from micropython_Programs  Basic_Programs, BME280 

from https://microdigisoft.com/weather-monitoring-with-raspberry-pi-pico-w-bme280-and-thingspeak/
works well 11 Feb 2025
'''
import machine
import urequests 
from machine import Pin, SoftI2C
import network, time
import BME280  
i2c = SoftI2C(scl=Pin(1), sda=Pin(0), freq=10000)    #initializing the I2C method
THINGSPEAK_WRITE_API_KEY = 'RG4961TZ9BKHMJ84'
    #  'https://api.thingspeak.com/update'
HTTP_HEADERS = {'Content-Type': 'application/json'} 
# api_key = 'RG4961TZ9BKHMJ84'
# base_url = 'https://api.thingspeak.com/update' = 'YOUR_THINGSPEAK_API_KEY' 

UPDATE_TIME_INTERVAL = 10000  # in ms 
last_update = time.ticks_ms() 

# ssid='Your SSID'
# password='Your Password'
ssid = 'SpectrumSetup-41'
password = 'leastdinner914'
# Configure ESP32 as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)

if not sta_if.isconnected():
    #print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 

while True: 
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL: 
         bme = BME280.BME280(i2c=i2c)          #BME280 object created
         temperature = bme.temperature         #reading the value of temperature
         humidity = bme.humidity               #reading the value of humidity
         pressure = bme.pressure               #reading the value of pressure
         #print(type(temperature))
         temp=temperature.split('C')
         temp=float(temp[0])
         temp_f = temp*(1.8) + 32
         #temperature=temperature.split('C')
         #print(temperature[0])
         bme_readings = {'field1':temperature, 'field2':pressure, 'field3':humidity,'field4':temp_f} 
         request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = HTTP_HEADERS )  
         request.close() 
         print(bme_readings)
         last_update=time.ticks_ms()