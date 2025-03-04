'''PW 110
print(wlan.ifconfig()[0])

A simple client server project on the Raspberry Pi Pico W. The Pico is configures as the server, and your desktop pc or laptop is configures to be the client. You will be running python on your PC. The project requests the user on the PC to specify a desired color. The color is then sent to the Pico, the Server. Then the Pico sets that color to ‘ON’. The pi pico is powered by a breadboard power bank, and there is no need for any connections to the pico. You can pick up the breadBoard Power Bank HERE [Affiliate Link]. Below is the schematic for the Server Side of the project:
PW_110_CLient.py in python_book_new Folder
'''
## PicoW Server
# import network
# import usocket as socket
# # import secrets
# import time
# import machine
 
# greenLED=machine.Pin(16,machine.Pin.OUT)
# yellowLED=machine.Pin(18,machine.Pin.OUT)
# redLED=machine.Pin(17,machine.Pin.OUT)
# # Set up WiFi connection
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# print('NETGEAR48','waterypanda914')
# wlan.connect('NETGEAR48','waterypanda914')
# # print(secrets.SSID,secrets.PASSWORD)
# # wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')
# print(wlan.ifconfig())
 
# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
# print(wlan.ifconfig()[0])
 
# while True:
#     print('Waiting for a request from the client...')
#     # Receive request from client
#     color, client_address = server_socket.recvfrom(1024)
#     color=color.decode()
#     print("Client Request:",color)
#     print("FROM CLIENT",client_address)
    
#     if (color=="green"):
#         greenLED.on()
#         yellowLED.off()
#         redLED.off()
#     if (color=="yellow"):
#         greenLED.off()
#         yellowLED.on()
#         redLED.off()
#     if (color=="red"):
#         greenLED.off()
#         yellowLED.off()
#         redLED.on()
#     if (color=="off"):
#         greenLED.off()
#         yellowLED.off()
#         redLED.off()
    
#     # Send data to client
#     data="LED "+color+" executed"
#     server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
###~~~~~~~ struct version of picoW server with socket
# import network
# import usocket as socket
# # import secrets
# import time
# import machine
# import struct
 
# greenLED=machine.Pin(16,machine.Pin.OUT)
# yellowLED=machine.Pin(18,machine.Pin.OUT)
# redLED=machine.Pin(17,machine.Pin.OUT)
# # Set up WiFi connection
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# print('NETGEAR48','waterypanda914')
# wlan.connect('NETGEAR48','waterypanda914')
# # print(secrets.SSID,secrets.PASSWORD)
# # wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')
# print(wlan.ifconfig())
 
# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
# print(wlan.ifconfig()[0])
 
# while True:
#     print('Waiting for a request from the client...')
#     # Receive request from client
#     color, client_address = server_socket.recvfrom(1024)
#     color =struct.unpack('')
#     # color=color.decode()
#     print("Client Request:",color)
#     print("FROM CLIENT",client_address)
    
#     if (color=="green"):
#         greenLED.on()
#         yellowLED.off()
#         redLED.off()
#     if (color=="yellow"):
#         greenLED.off()
#         yellowLED.on()
#         redLED.off()
#     if (color=="red"):
#         greenLED.off()
#         yellowLED.off()
#         redLED.on()
#     if (color=="off"):
#         greenLED.off()
#         yellowLED.off()
#         redLED.off()
    
#     # Send data to client
#     data="LED "+color+" executed"
#     server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
    
## client side     
'''


import socket
import time
 
# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.88.71', 12345)  # Adjust IP address and port as needed
 
while True:
    # Send request to the server
    myColor=input("Please Input Your Color (Green, Yellow, Red, Off )")
    myColor=myColor.lower()
    client_socket.sendto(myColor.encode(), server_address)
    
    # Receive data from the server
    data, addr = client_socket.recvfrom(1024)
    print('Received data:', data.decode())


'''
### March3, 2025 with struct  Chat

import network
import usocket as socket
import time
import machine
import struct

# LED setup
greenLED = machine.Pin(16, machine.Pin.OUT)
yellowLED = machine.Pin(18, machine.Pin.OUT)
redLED = machine.Pin(17, machine.Pin.OUT)

# Connect to Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NETGEAR48', 'waterypanda901')
# wlan.connect('NETGEAR48-2.4-LOFT', 'waterypanda901')w

while not wlan.isconnected():
    time.sleep(1)

print("Connection Completed")
print('WiFi connected:', wlan.ifconfig())

# Set up UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")
print(wlan.ifconfig()[0])

while True:
    print('Waiting for a request from the client...')
    
    # Receive and unpack the client request
    request, client_address = server_socket.recvfrom(1024)
    length = len(request)
    color = struct.unpack(f'{length}s', request)[0].decode().strip()
    
    print(f"Client Request: {color}")
    print("FROM CLIENT:", client_address)

    # Control LEDs
    if color == "green":
        greenLED.on()
        yellowLED.off()
        redLED.off()
    elif color == "yellow":
        greenLED.off()
        yellowLED.on()
        redLED.off()
    elif color == "red":
        greenLED.off()
        yellowLED.off()
        redLED.on()
    elif color == "off":
        greenLED.off()
        yellowLED.off()
        redLED.off()

    # Send response to client
    response = f"LED {color} executed"
    packed_response = struct.pack(f'{len(response)}s', response.encode())
    server_socket.sendto(packed_response, client_address)
    print(f'Sent data to {client_address}')
  
###### the client side 
# import network
# import usocket as socket
# import time
# import struct

# # Set up WiFi connection
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48', 'waterypanda914')

# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")˜
# print('WiFi connected:', wlan.ifconfig())

# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('<PICO_W_IP_ADDRESS>', 12345)

# while True:
#     command = input("Enter LED color (green, yellow, red, off): ")
    
#     # Pack the command and send it
#     packed_command = struct.pack(f'{len(command)}s', command.encode())
#     client_socket.sendto(packed_command, server_address)
    
#     # Receive and unpack response from server
#     response, _ = client_socket.recvfrom(1024)
#     length = len(response)
#     unpacked_response = struct.unpack(f'{length}s', response)[0].decode()
#     print("Server Response:", unpacked_response)
    
#     time.sleep(1)


