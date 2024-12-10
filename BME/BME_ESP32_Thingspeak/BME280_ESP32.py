
'''
https://microcontrollerslab.com/micropython-bme280-esp32-esp8266-temperature-humidity-pressure/



'''




import machine
import urequests 
from machine import Pin, SoftI2C
import network, time
import BME280  

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)    #initializing the I2C method

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'P06BZAQFY71S39OH' 

UPDATE_TIME_INTERVAL = 5000  # in ms 
last_update = time.ticks_ms() 

ssid='NETGEAR48'
password='waterypanda901'

# Configure ESP32 as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)

if not sta_if.isconnected():
    print('connecting to network...')
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

         bme_readings = {'field1':temperature, 'field2':pressure, 'field3':humidity} 
         request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = HTTP_HEADERS )  
         request.close() 
         print(bme_readings) 