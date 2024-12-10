'''create a HTTP server
2d Core program for wifi
https://core-electronics.com.au/guides/raspberry-pi-pico-w-create-a-simple-http-server/

create a simple HTTP server using a Raspberry Pi Pico W. This server will be accessible from within a local WiFi network and can be used to read sensors and control hardware - in our case we'll drive an LED and read the state of a button.
'''

# Hardware Test
# Blink and LED (GP15) slowly/quickly while a button (GP16) is not-pressed/pressed
# from machine import Pin
# from time import sleep_ms

# led = Pin(16, Pin.OUT)
# button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# while True:
#     if button.value() == 0: # button pressed
#         delay = 100 # short delay
#     else:
#         delay = 1000 # long delay
    
#     led.toggle()
#     sleep_ms(delay)

# Simple HTTP Server Example
# Control an LED and read a Button using a web browser

import time
import network
import socket
from machine import Pin



# Static IP configuration
static_ip = '192.168.1.10'  # Replace with your desired static IP
subnet_mask = '255.255.255.0'
gateway_ip = '192.168.1.15'
dns_server = '192.168.1.1'

led = Pin(17, Pin.OUT)
ledState = 'LED State Unknown'

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

ssid = 'NETGEAR48'
password = 'waterypanda901'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
'''
html = """<!DOCTYPE html>
<html>
<head> <title>Pico W</title> </head>
<body> <h1>Pico W HTTP Server</h1>
<p>Hello, World!</p>
<p>%s</p>
</body>
</html>
'''

## more elaborate html with buttons added!!
# replace the "html" variable with the following to create a more user-friendly control panel
html = """<!DOCTYPE html><html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:,">
<style>html { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center;}
.buttonGreen { background-color: #4CAF50; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
.buttonRed { background-color: #D11D53; border: 2px solid #000000;; color: white; padding: 15px 32px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; }
text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
</style></head>
<body><center><h1>Control Panel</h1></center><br><br>
<form><center>
<center> <button class="buttonGreen" name="led" value="on" type="submit">LED ON</button>
<br><br>
<center> <button class="buttonRed" name="led" value="off" type="submit">LED OFF</button>
</form>
<br><br>
<br><br>
<p>%s<p></body></html>
"""







# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Set static IP address
wlan.ifconfig((static_ip, subnet_mask, gateway_ip, dns_server))

    
# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('Connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
    
# Open socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.bind(addr)
s.listen(1)
print('listening on', addr)

# Listen for connections, serve client
while True:
    try:       
        cl, addr = s.accept()
        print('client connected from', addr)
        request = cl.recv(1024)
        print("request:")
        print(request)
        request = str(request)
        led_on = request.find('led=on')
        led_off = request.find('led=off')
        
        print( 'led on = ' + str(led_on))
        print( 'led off = ' + str(led_off))
        
        if led_on == 8:
            print("led on")
            led.value(1)
        if led_off == 8:
            print("led off")
            led.value(0)
        
        ledState = "LED is OFF" if led.value() == 0 else "LED is ON" # a compact if-else statement
        
        if button.value() == 1: # button not pressed
            print("button NOT pressed")
            buttonState = "Button is NOT pressed"
        else:
            print("button pressed")
            buttonState = "Button is pressed"
        
        # Create and send response
        stateis = ledState + " and " + buttonState
        response = html % stateis
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.send(response)
        cl.close()
        
    except OSError as e:
        cl.close()
        print('connection closed')