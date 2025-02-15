'''works 11 feb 2025
'''
## Rui Santos & Sara Santos - Random Nerd Tutorials
## Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/
## this works as is
## note libray is loaded as BME280.py  Capitals! and connected to 3.3 volts
# from machine import Pin, I2C
# from time import sleep
# import BME280 

# # Initialize I2C communication
# i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=10000)

# while True:
#     try:
#         # Initialize BME280 sensor
#         bme = BME280.BME280(i2c=i2c, addr=0x76)

#         # temp_c,hum,pres =bme.values      
#         # temp_c=temp_c[:-1]
#         # hum=hum[:-3]
#         # pres=pres[:-1]
#         # temp_c=float(temp_c)
#         # hum=float(hum)
#         # pres=float(pres)
        
        
#         pres =bme.pressure
#         # Read sensor data
#         temp_c = bme.temperature
#         hum = bme.humidity
#         pres = bme.pressure
        
#         # #Convert temperature to fahrenheit
#         # temp_f = (temp_c/100) * (9/5) + 32
#         # # temp_f = (bme.read_temperature()/100) * (9/5) + 32
#         # temp_f = str(round(temp_f, 2)) + 'F'
        
#         # Print sensor readings
#         print('Temperature: ', temp_c)
#         # print('Temperature: ', temp_f)
#         print('Humidity: ', hum)
#         print('Pressure: ', pres)
#         # print(type(temp_c))
#         # print(type(hum))
#     except Exception as e:
#         # Handle any exceptions during sensor reading
#         print('An error occurred:', e)

#     sleep(5)

import ujson
THINGSPEAK_API_KEY='aaaaaaa'
t=float(3.555)
h= int(10)
data = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": t,
        "field2": h,
    }

print(data)
data1 =ujson.dumps(data)
print(data1)

from machine import Pin, I2C
from time import sleep
import BME280 

# Initialize I2C communication
i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=10000)

while True:
    try:
        # Initialize BME280 sensor
        bme = BME280.BME280(i2c=i2c, addr=0x76)

        # temp_c,hum,pres =bme.values      
        # temp_c=temp_c[:-1]
        # hum=hum[:-3]
        # pres=pres[:-1]
        # temp_c=float(temp_c)
        # hum=float(hum)
        # pres=float(pres)
        
        
        pres =bme.pressure
        # Read sensor data
        temp_c = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        
        # #Convert temperature to fahrenheit
        # temp_f = (temp_c/100) * (9/5) + 32
        # # temp_f = (bme.read_temperature()/100) * (9/5) + 32
        # temp_f = str(round(temp_f, 2)) + 'F'
        
        # Print sensor readings
        print('Temperature: ', temp_c)
        # print('Temperature: ', temp_f)
        print('Humidity: ', hum)
        print('Pressure: ', pres)
        data = {
        "field1": temp_c,
        "field2": hum,
        "field3":pres,
    }

        print(data)
        data1 =ujson.dumps(data)
        print(data1)
        
        
        # print(type(temp_c))
        # print(type(hum))
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('An error occurred:', e)

    sleep(5)
   