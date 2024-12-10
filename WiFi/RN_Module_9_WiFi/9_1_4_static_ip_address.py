# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/

import network
import time

# Wi-Fi credentials
ssid = 'NETGEAR48'
password = 'waterypanda901'

# Static IP configuration
static_ip = '192.168.1.1'  # Replace with your desired static IP
subnet_mask = '255.255.255.0'
gateway_ip = '192.168.1.15'
dns_server = '192.168.1.1'

# Init Wi-Fi Interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to your network
wlan.connect(ssid, password)

# Wait for Wi-Fi connection
connection_timeout = 10
while connection_timeout > 0:
    if wlan.status() >= 3:
        break
    connection_timeout -= 1
    print('Waiting for Wi-Fi connection...')
    time.sleep(1)

# Set static IP address
wlan.ifconfig((static_ip, subnet_mask, gateway_ip, dns_server))

# Check if connection is successful
if wlan.status() != 3:
    raise RuntimeError('Failed to establish a network connection')
else:
    print('Connection successful!')
    network_info = wlan.ifconfig()
    print('IP address:', network_info[0])
    # print(subnet_mask)
    # print(static_ip)

    # print(dns_server)