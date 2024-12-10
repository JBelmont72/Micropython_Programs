'''

this is for the server side on the Pico W
'''
import socket
import time
import network
wifi=network.WLAN(network.STA_IF)   ## this command creates the wifi network

# Static IP configuration
static_ip = '192.168.1.10'  # Replace with your desired static IP
subnet_mask = '255.255.255.0'
gateway_ip = '192.168.1.15'
dns_server = '192.168.1.1'


wifi.active(True)
## connect to the WiFi
wifi.connect('NETGEAR48','waterypanda901')
# wifi.connect(secrets.SSID,secrets.PASSWORD)

while wifi.isconnected() ==False:
    print('Waiting for connection....')
    time.sleep(.1)
 
 
# Set static IP address
wifi.ifconfig((static_ip, subnet_mask, gateway_ip, dns_server))
 
    
wifiInfo = wifi.ifconfig()
print(wifiInfo)

