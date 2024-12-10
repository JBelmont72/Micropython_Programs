'''
https://www.halvorsen.blog/documents/technology/iot/pico/pico_thingspeak.php



api_key = 'RG4961TZ9BKHMJ84'
base_url = 'https://api.thingspeak.com/update'
api_key = 'RG4961TZ9BKHMJ84'
https://api.thingspeak.com/update?api_key=RG4961TZ9BKHMJ84&field1=20
'''

'''
import machine
import time

adcpin = 4
sensor = machine.ADC(adcpin)
  
def ReadTemperature():
 	adc_value = sensor.read_u16()
 	volt = (3.3/65535) * adc_value
 	temperature = 27 - (volt - 0.706)/0.001721
 	return round(temperature, 1)
  
while True:
 	temperature = ReadTemperature()
 	print(temperature)
 	time.sleep(5)
  
  
###########


from machine import ADC
import machine
import time

adcpin = 4
sensor = machine.ADC(adcpin)
class Temperature:
    def __init__(self):
        adcpin = 4
        self.sensor = ADC(adcpin)
        
    def ReadTemperature(self):
        adc_value = self.sensor.read_u16()
        volt = (3.3/65535)*adc_value
        temperature = 27 - (volt - 0.706)/0.001721
        return round(temperature, 1)
  
while True:
 	temperature = ReadTemperature()
 	print(temperature)
 	time.sleep(5)
'''
## write to thingspeak
import network
import urequests
import random
from time import sleep

#Network Initialization
ssid = "NETGEAR48"
password = "waterypanda901"

def ConnectWiFi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

#Connect to Network
ip = ConnectWiFi()

#ThingSpeak Initialization
server = "http://api.thingspeak.com/"
api_key = 'RG4961TZ9BKHMJ84'
field = 1

#Main Program
try:
    while True:
        temperature = random.uniform(20, 25) #Random Number between 20 and 25
        temperature = round(temperature, 1)
        print(f"T = {temperature}°C")
        sleep(1)
        url = f"{server}/update?api_key={api_key}&field{field}={temperature}"
        request = urequests.post(url)
        request.close()
        sleep(1)

except KeyboardInterrupt:
    print('all done')
    