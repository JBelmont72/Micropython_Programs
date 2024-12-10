'''
https://bytesnbits.co.uk/simple-micropython-wifi-connection/

wlan connected
IP address = 192.168.1.24
subnet mask = 255.255.255.0
gateway  = 192.168.1.1
DNS server = 192.168.1.1
'''

## CONNECTING TO THE NETWORK
'''
import network
import utime

ssid = "NETGEAR48"
password = "waterypanda901"
## set WiFi to station interface, WLAN method call sets up the type of interface we want to create.
## In this instance we are creating a station interface which means that we want to connect to an existing Wi-Fi network
wlan = network.WLAN(network.STA_IF)
# activate the network interface
wlan.active(True)
# connect to wifi network
wlan.connect(ssid, password)

## need to wait for connection
max_wait = 10
# wait for connection
while max_wait > 0:
    """
        0   STAT_IDLE -- no connection and no activity,
        1   STAT_CONNECTING -- connecting in progress,
        -3  STAT_WRONG_PASSWORD -- failed due to incorrect password,
        -2  STAT_NO_AP_FOUND -- failed because no access point replied,
        -1  STAT_CONNECT_FAIL -- failed due to other problems,
        3   STAT_GOT_IP -- connection successful.
    """
    if wlan.status() < 0 or wlan.status() >= 3:
        # connection successful
        break
    max_wait -= 1
    print('waiting for connection... ' + str(max_wait))
    utime.sleep(1)
## check connection with ifconfig() method
# check connection
if wlan.status() != 3:
    # No connection
    raise RuntimeError('network connection failed')
else:
    # connection successful and the pico has been assigned a network IP address
    print('wlan connected')
    status = wlan.ifconfig()
    print('IP address = ' + status[0])
    print('subnet mask = ' + status[1])
    print('gateway  = ' + status[2])
    print('DNS server = ' + status[3])
'''    
    
'''USING ACCESS POINT MODE
If there is no available Wi-Fi network, or we want to make a direct connection to the Pi Pico we can set the Wi-Fi chip into access point mode.

'''
'''
import network
import time

ssid = 'MyPicoW'
password = '1234'

ap = network.WLAN(network.AP_IF)	## 'access point mode'
ap.config(essid=ssid, password=password)
##		ap.config(essid=ssid, password=password)
ap.active(True)

# wait for wifi to go active
wait_counter = 0
while ap.active() == False:
    print("waiting " + str(wait_counter))
    time.sleep(0.5)
    pass

print('WiFi active')
status = ap.ifconfig()
print('IP address = ' + status[0])
print('subnet mask = ' + status[1])
print('gateway  = ' + status[2])
print('DNS server = ' + status[3])
'''
'''		output: (not connected to internet but is its own access point
MPY: soft reboot
waiting 0
WiFi active
IP address = 192.168.4.1
subnet mask = 255.255.255.0
gateway  = 192.168.4.1
DNS server = 192.168.1.1

'''

##  https://publicapis.io/elonmush-api

##  https://publicapis.io/breaking-bad-quotes-api
###		ACCESSING WEB SERVICES
##  timeapi.io web service for current time and date
## this is a REST API where we send an HTTP GET request in the correct format
## for its retrurn block of JSON data. For this use import urequests library
import network
import utime
import urequests

ssid = "NETGEAR48"
password = "waterypanda901"
## set WiFi to station interface, WLAN method call sets up the type of interface we want to create.
## In this instance we are creating a station interface which means that we want to connect to an existing Wi-Fi network
wlan = network.WLAN(network.STA_IF)
# activate the network interface
wlan.active(True)
# connect to wifi network
wlan.connect(ssid, password)

## need to wait for connection
max_wait = 10
# wait for connection
while max_wait > 0:
    """
        0   STAT_IDLE -- no connection and no activity,
        1   STAT_CONNECTING -- connecting in progress,
        -3  STAT_WRONG_PASSWORD -- failed due to incorrect password,
        -2  STAT_NO_AP_FOUND -- failed because no access point replied,
        -1  STAT_CONNECT_FAIL -- failed due to other problems,
        3   STAT_GOT_IP -- connection successful.
    """
    if wlan.status() < 0 or wlan.status() >= 3:
        # connection successful
        break
    max_wait -= 1
    print('waiting for connection... ' + str(max_wait))
    utime.sleep(1)
## check connection with ifconfig() method
# check connection
if wlan.status() != 3:
    # No connection
    raise RuntimeError('network connection failed')
else:
    # connection successful and the pico has been assigned a network IP address
    print('wlan connected')
    status = wlan.ifconfig()
    print('IP address = ' + status[0])
    print('subnet mask = ' + status[1])
    print('gateway  = ' + status[2])
    print('DNS server = ' + status[3])
##  main loop
while True:
    start=utime.ticks_ms()
 
    
    ##response = urequests.get('https://timeapi.io/api/Time/current/zone?timeZone=Europe/London')
    print('request took '+str(utime.ticks_ms()-start) +'ms')
    print(response.content)
    print(response.json()['dateTime'])
    utime.sleep(5)