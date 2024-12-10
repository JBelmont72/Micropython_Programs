'''first of the Core series - works fine! 
https://core-electronics.com.au/guides/raspberry-pi-pico-w-connect-to-the-internet/

Part 2: Timeserver and json support

This is the data returned by a time-server (http://date.jsontest.com). 
The date/time returned is from timezone GMT+0. 
If you follow the link to that server you will see the data is presented on a webpage in .json format. 
We could query this website in the same way as Example 1, but it's far more useful to make use of the limited json support offered by the urequests package. 
Printing r.json() interprets the requested data as json format and loads it into a useful dictionary. For example, we can extract just the time component by reading r.json()['time']

'''
# A simple example that:
# - Connects to a WiFi Network defined by "ssid" and "password"
# - Performs a GET request (loads a webpage)
# - Queries the current time from a server

import network   # handles connecting to WiFi
import urequests # handles making and servicing network requests

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Fill in your network name (ssid) and password here:
ssid = 'NETGEAR48'
password = 'waterypanda901'
wlan.connect(ssid, password)


# Example 1. Make a GET request for google.com and print HTML
# Print the html content from google.com
# print("1. Querying google.com:")
# r = urequests.get("http://www.google.com")
# print(r.content)
# r.close()

# Example 2. urequests can also handle basic json support! Let's get the current time from a server
print("\n\n2. Querying the current GMT+0 time:")
r = urequests.get("http://date.jsontest.com") # Server that returns the current GMT+0 time.
print(r.json())