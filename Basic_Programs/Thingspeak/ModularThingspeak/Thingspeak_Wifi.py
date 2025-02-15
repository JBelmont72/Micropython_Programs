'''
Indistrail IT and Automation Youtube
https://www.halvorsen.blog/documents/technology/iot/pico/pico_thingspeak.php
excellent tutorial
HTTP_HEADERS = {'Content-Type': 'application/json'} 


https://api.thingspeak.com/update?api_key=xxxxxx&field1=20
https://api.thingspeak.com/update?api_key="YZRDGNJ7C9JZI3MP"field1=20
'''
import network
import urequests
import random
from time import sleep
ssid = 'SpectrumSetup-41'
password = 'leastdinner914'
def ConnectWiFi():
    wlan=network.WLAN(network.STA_IF)
    wlan.active(True)
    while wlan.isconnected()==False:
        print('Waiting for connection...')
        sleep(1)
    ip=   wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
## COnnect to internet
ip=ConnectWiFi()
print(ip)
## thingspeak initialization   
THINGSPEAK_WRITE_API_KEY = 'YZRDGNJ7C9JZI3MP'
server = 'http://api.thingspeak.com/'
field = 1
while True:
    temperature = random.uniform(55,90)
    temperature =round(temperature,1)
    print(f"T= {temperature} C")
    url=f"{server}/update?api_key={THINGSPEAK_WRITE_API_KEY}&{field}={temperature}"
    request= urequests.post(url)
    request.close()
    sleep(2)
