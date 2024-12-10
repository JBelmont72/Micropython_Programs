'''PW 32 Weather Station'''


import network
import time
# import secrets
import urequests
 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
 
i2c=I2C(1,sda=Pin(2),scl=Pin(3), freq=400000)
dsp=SSD1306_I2C(128,64,i2c)
ssid = 'NETGEAR48'
password = 'waterypanda901'
wlan=network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)
# wlan.connect(secrets.SSID,secrets.PASSWORD)
while wlan.isconnected()==False:
    print('Connecting . . .')
print('Congratulations, You Have Connected')
#weather=urequests.get("https://api.openweathermap.org/data/2.5/weather?lat=0.478623&lon=33.164364&appid=0d631313b55e6e128285fd7882ba913f&units=imperial").json()
weather=urequests.get("https://api.openweathermap.org/data/2.5/weather?q=Jinja,Uganda&appid=0d631313b55e6e128285fd7882ba913f&units=imperial").json()
tm=time.localtime(weather['dt']+weather['timezone'])
print('Welcome to '+weather['name']+', '+weather['sys']['country'])
print('Local Time: '+str(tm[3])+':'+str(tm[4])+'  '+str(tm[1])+'/'+str(tm[2])+'/'+str(tm[0]))
sr=time.localtime(weather['sys']['sunrise']+weather['timezone'])
print('Sunrise at: '+str(sr[3])+':'+str(sr[4]))
ss=time.localtime(weather['sys']['sunset']+weather['timezone'])
print('Sunset at: '+str(ss[3]-12)+':'+str(ss[4])+' PM')
print('Current Temp: '+str(weather['main']['temp'])+' F')
print('Current Humidity: '+str(weather['main']['humidity'])+' %')
print('Current Barometric Pressure: '+str(weather['main']['pressure']*0.0009869233)+' ATM')
for i in range(len(weather['weather'])):
    print('Current Conditions: '+weather['weather'][i]['main']+', '+weather['weather'][i]['description'])
print('Wind: '+str(weather['wind']['speed'])+' MPH')
myTime=time.time()
while True:
    if time.time()-myTime>300:
       weather=urequests.get("https://api.openweathermap.org/data/2.5/weather?q=Jinja,Uganda&appid=0d631313b55e6e128285fd7882ba913f&units=imperial").json()
       tm=time.localtime(weather['dt']+weather['timezone'])
       ss=time.localtime(weather['sys']['sunset']+weather['timezone'])
       myTime=time.time()
       print('New Data Read')
    dsp.text('Welcome to '+weather['name'],0,0)
    sr=time.localtime(weather['sys']['sunrise']+weather['timezone'])
 
    dsp.text('Time: '+str(tm[3])+':'+str(tm[4]),0,16)
    dsp.text('Date: '+str(tm[1])+'/'+str(tm[2])+'/'+str(tm[0]),0,26)
    dsp.text('Sunrise: '+str(sr[3])+':'+str(sr[4]),0,36)
    dsp.text('Sunset: '+str(ss[3]-12)+':'+str(ss[4])+' PM',0,46)
    dsp.show()
    time.sleep(5)
    dsp.fill(0)
    dsp.text('Welcome to '+weather['name'],0,0)
    dsp.text('Weather: ',0,16)
    dsp.text('Temp: '+str(weather['main']['temp'])+' F',0,26)
    dsp.text('Humidity: '+str(weather['main']['humidity'])+' %',0,36)
    dsp.text('BP: '+str(weather['main']['pressure']*0.0009869233)+' ATM',0,46)
    dsp.text('Wind: '+str(weather['wind']['speed'])+' MPH',0,56)
    dsp.show()
    time.sleep(5)
    dsp.fill(0)
    dsp.text('Welcome to '+weather['name'],0,0)
    dsp.text('Conditions: ',0,16)
    row=26
    for i in range(len(weather['weather'])):
        dsp.text(weather['weather'][i]['main'],0,row)
        row=row+10
        dsp.text(weather['weather'][i]['description'],0,row)
        row=row+10
    dsp.show()
    time.sleep(5)
    dsp.fill(0)