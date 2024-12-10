# Rui Santos & Sara Santos - Random Nerd Tutorials  page 372
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/

import network
from time import sleep
# Wi-Fi credentials
ssid = 'NETGEAR48' 
password = 'waterypanda901'

# Init Wi-Fi Interface Creates a station interface
wlan = network.WLAN(network.STA_IF)
## activates the station interface
wlan.active(True)

# Connect to your network
wlan.connect(ssid, password)
'''
The code first checks the connection status, and if it’s wlan.status() >= 3 (this means it has even connected to the network or failed to connect), the loop exits. It waits for a maximum of 10 seconds (10 attempts defined in the connection_timeout variable).
The method wlan.status(), as the name suggests, checks the status of the Wi-Fi connection of the Raspberry Pi. This method returns an integer with the following meaning:
• 0: WLAN is not enabled
• 1: WLAN is currently scanning for networks
• 2: WLAN is connecting to a network
• 3: WLAN is connected to a network
• 4: WLAN failed to connect to a network
Then, we check if it’s connected or not (we know that status = 3 means it’s connected). If wlan.status() is different than 3, we know it failed to establish a connection.

'''
# Wait for Wi-Fi connection
connection_timeout = 10
while connection_timeout > 0:
    if wlan.status() >= 3:
        break
    connection_timeout -= 1
    print('Waiting for Wi-Fi connection...')
    sleep(1)

# Check if connection is successful
if wlan.status() != 3:
    raise RuntimeError('Failed to establish a network connection')
else:
    print('Connection successful!')
    network_info = wlan.ifconfig()
    print('IP address:', network_info[0])
    # print('IP address:', network_info)
    ## alternatively, I used the isconnected()  method to see if i am connected. true or false
    IsConnected=wlan.isconnected()
    print(IsConnected)
'''
In case we succeed, we can get the network information using theifconfig()method. This method returns a tuple with the following information:
• network_info[0]: The IP address assigned to the Pico on the network.
• network_info[1]: The subnet mask.
• network_info[2]: The gateway IP address.
• network_info[3]: The DNS (Domain Name System) server IP address.
We just need the IP address, so we just get the first element of the array (network_info[0]).

The isconnected() method
Instead of checking the connection status, the wlan object supports a method called isconnected() that returns True if the board is connected to the network or False otherwise. You can use that approach instead of checking wlan.status().


'''