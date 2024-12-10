'''

'''
import rp2
import network
import ubinascii
import machine
import urequests as requests
import time
# from secrets import secrets
import socket
import gc
import random
from imu import MPU6050
from machine import Pin, I2C
import time
import math
i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)
mpu=MPU6050(i2c)
# Initialize I2C


# Set country to avoid possible errors
rp2.country('DE')

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
# If you need to disable powersaving mode
# wlan.config(pm = 0xa11140)

# See the MAC address in the wireless chip OTP
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print('mac = ' + mac)

# Other things to query
# print(wlan.config('channel'))
# print(wlan.config('essid'))
# print(wlan.config('txpower'))

# Load login data from different file for safety reasons
ssid = 'NETGEAR48'
pw = 'waterypanda901'

wlan.connect(ssid, pw)

# Wait for connection with 10 second timeout
timeout = 10
while timeout > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    timeout -= 1
    print('Waiting for connection...')
    time.sleep(1)
    
# Handle connection error
# Error meanings
# 0  Link Down
# 1  Link Join
# 2  Link NoIp
# 3  Link Up
# -1 Link Fail
# -2 Link NoNet
# -3 Link BadAuth
if wlan.status() != 3:
    raise RuntimeError('Wi-Fi connection failed')
else:
    led = machine.Pin('LED', machine.Pin.OUT)
    for i in range(wlan.status()):
        led.on()
        time.sleep(0.2)
        led.off()
        time.sleep(0.2)
    print('Connected')
    status = wlan.ifconfig()
    print('ip = ' + status[0])
    
# Function to load in html page    
def get_html(html_name):
    with open(html_name, 'r') as file:
        html = file.read()
        
    return html

data=round(mpu.accel,1)

dice_val = 'Nothing'

# HTTP server with socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('Listening on', addr)

# Listen for connections
while True:
    try:
        cl, addr = s.accept()
        print('Client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
            
        response = get_html('index.html')
        data = round(mpu.accel,1)
        tapped = True       ## iam trying this
        # tapped = accelerometer.events['tap']
        response = response.replace('AccX', str(data[0]))
        response = response.replace('AccY', str(data[1]))
        response = response.replace('AccZ', str(data[2]))
        ## or try
        # response = response.replace('AccX', str(data[0]))
        # response = response.replace('AccY', str(data[1]))
        # response = response.replace('AccZ', str(data[2]))
        if tapped:
            dice_val = str(random.randint(1,6))
        response = response.replace('DiceVal', dice_val)
        
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
    except OSError as e:
        cl.close()
        print('Connection closed')