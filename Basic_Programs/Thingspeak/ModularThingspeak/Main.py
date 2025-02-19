'''
14Feb25
'''
from BME_Class import BME_Temperature
from WiFiNetwork import WiFi
from Thingspeak import ThingSpeakApi
from time import sleep
import machine

#Sensor Initialization
sensor = BME_Temperature(1,0)
field=4
#ThingSpeak Initialization
thingspeak = ThingSpeakApi(field)

#Network Initialization
network = WiFi()
ip = network.ConnectWiFi()
wdt = machine.WDT(timeout=8000)  # 8 seconds timeout, a watchdog

import urequests

url = "http://api.thingspeak.com/update?api_key=YZRDGNJ7C9JZI3MP&field1=23.87"
response = urequests.get(url)
print(f"Response code: {response.status_code}")
response.close()
#Main Program
try:
    while True:
        temperature, h, pres, temp_f = sensor.Read()
        field_data=temperature,h,pres,temp_f
        print(f"T={temperature}°C")
        sleep(1)
        #thingspeak.WriteData(field_data)
        thingspeak.WriteMultipleFields(field_data)
        wdt.feed()  # Resets the watchdog timer
except Exception as e:
        print(f"Error: {e}")
        machine.reset()  # Reset Pico on failure