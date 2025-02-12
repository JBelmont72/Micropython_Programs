'''
shilleh bme280 Plus thinkspeak
'''

from machine import Pin, I2C
import network
import urequests
import time
from time import sleep
import BME280
#import constants


sdaPINbme=Pin(0)
sclPINbme=Pin(1)
i2c=I2C(0,sda=sdaPINbme, scl=sclPINbme, freq=400000)
# bme = BME280(i2c=i2c)
bme = BME280.BME280(i2c=i2c, addr=0x76)

##i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=400000) 
# ssid='NETGEAR48'
# ssid='NETGEAR48_2.4_Loft'
# password = 'waterypanda901'
# ssid = constants.INTERNET_NAME
# password = constants.INTERNET_PASSWORD
ssid = 'SpectrumSetup-41'
password = 'leastdinner914'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
# while not wlan.isconnected():
#     print('connecting...')
#     pass


max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    print(status)



api_key = 'RG4961TZ9BKHMJ84'
base_url = 'https://api.thingspeak.com/update'

# def read_sensor():
#     bme = bme280.BME280(i2c=i2c)
#     temperature, pressure, humidity = [float(i) for i in bme.values]
#     return temperature, pressure, humidity



# Send data to ThingSpeak
while True:
    # temperature, pressure, humidity = read_sensor()
    
    t = bme.temperature
    h = bme.humidity
    p = bme.pressure
    print(t,h,p)
    # temp_c = bme.temperature
    # hum = bme.humidity
    # pres = bme.pressure
    # t,p,h = bme.read_compensated_data()
    temperature=float(t/100)
    # pressure= float(p)
    pressure= float(p // 100)
    
    hi =h// 1024
    # hd = h * 100 // 1024 - hi * 100
    humidity =float(hi)
    print(temperature,pressure,humidity)
    url = f"{base_url}?api_key={api_key}&field1={temperature}&field2={pressure}&field3={humidity}"
    response = urequests.get(url)
    print(response.text)
    time.sleep(2)

#####
'''
from machine import Pin, I2C
from time import sleep
import bme280    


sdaPINbme=Pin(14)
sclPINbme=Pin(15)
i2c=machine.I2C(1,sda=sdaPINbme, scl=sclPINbme, freq=400000)
bme = bme280.BME280(i2c=i2c)

while True:
    t, p, h = bme.read_compensated_data()
    temperature=t/100
    p = p // 256
    pressure = p // 100
    hi = h // 1024
    hd = h * 100 // 1024 - hi * 100
    print ("{}C".format(temperature), "{}hPa".format(pressure),
    "{}.{:02d}%".format(hi, hd))
    sleep(1.0)
'''