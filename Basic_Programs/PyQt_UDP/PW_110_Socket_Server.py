'''PW 110
print(wlan.ifconfig()[0])

A simple client server project on the Raspberry Pi Pico W. The Pico is configures as the server, and your desktop pc or laptop is configures to be the client. You will be running python on your PC. The project requests the user on the PC to specify a desired color. The color is then sent to the Pico, the Server. Then the Pico sets that color to ‘ON’. The pi pico is powered by a breadboard power bank, and there is no need for any connections to the pico. You can pick up the breadBoard Power Bank HERE [Affiliate Link]. Below is the schematic for the Server Side of the project:
PW_110_CLient.py in python_book_new Folder
1- the pico server
2- the struct form of pico server 
4- is the pythonside client that I use 
5- client python side with wifi connection, if ran on a pico etc. 
Trroubleshooting help:  
In terminal can use command   echo -n "test" | nc -u 192.168.1.29 12345
If the server prints Client Request: test, you know the connection works!


'''
# ## PicoW Server
# import network
# import usocket as socket
# import secrets
# import time
# import machine
 
# greenLED=machine.Pin(16,machine.Pin.OUT)
# yellowLED=machine.Pin(18,machine.Pin.OUT)
# redLED=machine.Pin(17,machine.Pin.OUT)
# # Set up WiFi connection
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)

# print(secrets.ssid_home,secrets.password_home)
# wlan.connect(secrets.ssid_home,secrets.password_home)
# # print(secrets.ssid_condo,secrets.password_condo)
# # wlan.connect(secrets.ssid_condo,secrets.password_condo)
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
## this is the client side for the picoW server above
####  2  client for python  in Python_Book_New
import socket   ##client for PW110 in MIcropython_Programs/Basic_Programs/McWhorter/StateMachine/PIO_HCS04/PW_110_Socket_Server.py
import time
 
# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.31', 12345)  # Adjust IP address and port as needed
 
while True:
    # Send request to the server
    myColor=input("Please Input Your Color (Green, Yellow, Red, Off )")
    myColor=myColor.lower()
    client_socket.sendto(myColor.encode(), server_address)
    
    # Receive data from the server
    data, addr = client_socket.recvfrom(1024)
    print('Received data:', data.decode())
    
    
    
    
    
    
    
# ### 3  ~~~~~~~ struct version of picoW server with socket
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
# print('secrets.ssid_condo','secrets.password_condo')
# wlan.connect('secrets.ssid_condo','.secrets.password_condo')
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
    
#     #     # Receive and unpack the client request
#     # request, client_address = server_socket.recvfrom(1024)
#     # length = len(request)
#     # color = struct.unpack(f'{length}s', request)[0].decode().strip()
#    ## note: want the 0 index of the 'request' to decode and strip!
    
    
#     request, client_address = server_socket.recvfrom(1024)
#     color=struct.unpack(f'{len(request)}s',request)[0].decode().strip()

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


import socket   #4 client on python txt editor
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
### March3, 2025 with struct  this works and uses the client .py that follows

###### the client side /Users/judsonbelmont/Documents/SharedFolders/Python/Python_Book_New/UDP/UDP_C_PW110.py
## i would copy below on python editor
# import socket
# import struct

# # Server details
# SERVER_IP = '192.168.1.223'  # Replace with your Pico W's IP address
# SERVER_PORT = 12345

# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     command = input("Enter LED color (green, yellow, red, off): ").strip().lower()
    
#     if command not in {"green", "yellow", "red", "off"}:
#         print("Invalid command. Please enter 'green', 'yellow', 'red', or 'off'.")
#         continue

#     # Pack the command and send it
#     packed_command = struct.pack(f'{len(command)}s', command.encode())
#     client_socket.sendto(packed_command, (SERVER_IP, SERVER_PORT))
    
#     # Receive and unpack response from server
#     response, _ = client_socket.recvfrom(1024)
#     length = len(response)
#     unpacked_response = struct.unpack(f'{length}s', response)[0].decode()
#     print("Server Response:", unpacked_response)



# ## below would be the client if I needed a wifi conneciton

# import network
# import usocket as socket
# import time
# import struct

# # Set up WiFi connection
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48', 'waterypanda901')

# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected:', wlan.ifconfig())

# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('192.168.1.223', 12345)

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
    
## try to run the above from a picoW as the client but use buttons for the input    
import network
import usocket as socket
import time
import struct
from machine import Pin

# Button pin assignments
gPin, yPin, rPin, offPin = 13, 14, 15, 12
greenBut = Pin(gPin, Pin.IN, Pin.PULL_DOWN)
yellowBut = Pin(yPin, Pin.IN, Pin.PULL_DOWN)
redBut = Pin(rPin, Pin.IN, Pin.PULL_DOWN)
offBut = Pin(offPin, Pin.IN, Pin.PULL_DOWN)

# WiFi setup
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('SpectrumSetup-41', 'leastdinner914')
# wlan.connect('NETGEAR48', 'waterypanda901')

while not wlan.isconnected():
    time.sleep(1)
print("Connection Completed")
print('WiFi connected:', wlan.ifconfig())

# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.223', 12345)
last_command = None  # Store the last command to prevent redundant sending

while True:
    # Read button values
    if greenBut.value():
        command = 'green'
    elif yellowBut.value():
        command = 'yellow'
    elif redBut.value():
        command = 'red'
    elif offBut.value():
        command = 'off'
    else:
        command = None  # No button pressed

    # Send command only if it's new
    if command and command != last_command:
        ## below is with struct
        # packed_command = struct.pack(f'{len(command)}s', command.encode())
        ## to change from struct to utf-8
        packed_command=command.encode()
        client_socket.sendto(packed_command, server_address)
        
        # Receive acknowledgment
        response, _ = client_socket.recvfrom(1024)
        ## next is non struct decode
        print('Server Response:',respnse.decode())
        ## below is struct decode
        length = len(response)
        unpacked_response = struct.unpack(f'{length}s', response)[0].decode()
        print("Server Response:", unpacked_response)

        last_command = command  # Update last command
        time.sleep(0.1)  # Debounce

    time.sleep(0.1)  # Small delay to reduce CPU usage

