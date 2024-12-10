# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/
'''
The response is an object of type Response. This object has several attributes that you can access and might be useful. For example:
• response.status_code: returns an integer value representing the status of the response;
• response.content: returns the actual content in bytes;
• response.text: returns the content converted to a string, using a character
encoding such as UTF-8;
• response.json(): returns the response as a JSON object (dictionary);
• response.headers(): access information about the response’s headers.

'''
import network
import requests


# Wi-Fi credentials
ssid = 'NETGEAR48'
password = 'waterypanda901'

# Connect to network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Connect to your network
wlan.connect(ssid, password)

# Make GET request
# response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Jinja,Uganda&appid=0d631313b55e6e128285fd7882ba913f&units=imperial").json()
response = requests.get("http://www.google.com")
# Get response code
response_code = response.status_code
# Get response content
response_content = response.content

# Print results
print('Response code: ', response_code)
# print('Response content:', response_content)
