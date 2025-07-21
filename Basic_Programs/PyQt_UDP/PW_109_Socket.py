''' PW 109 pico server and python client

send and receive data between the Raspberry Pi Pico W, and your  PC. We will be running python on the PC, and we will exchange data using the UDP protocol. UDP is simple, and a very reliable way to send data packets back and forth. In this example, we will be demonstrating a simple Client Server relationship between the Pi Pico and PC using UDP over WiFi.
THis is interesting and can help trouble shooting

In terminal can use command   echo -n "test" | nc -u 192.168.1.31 12345
If the server prints the Client Request: test, you know the connection works!
'''
# # original PW109 server ## lesson 109 minute 10.  ##1 server side on pico Works
# import network
# import usocket as socket
# # import secrets
# import time
 
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48','waterypanda901')
# # wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')
# print(wlan.ifconfig())
# print(wlan.ifconfig()[0])
 
# # # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
# print(wlan.ifconfig()[0])
 
# while True:
#     print('Waiting for a request from the client...')
#     # Receive request from client
#     request, client_address = server_socket.recvfrom(1024)
#     print("Client Request:",request.decode())
#     print("FROM CLIENT",client_address)
    
#     # String to send
#     data = "225,128,64"
    
#     # Send data to client
#     server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
####~~~~
##original client from PW 109 that works with above***** does work when entered via terminal 


####~~~~~~. #1 Client side on Mac works with #1 Pico server above

# import network
# import usocket as socket
# import secrets
# import time
# # from WiFiNetwork_Socket import WiFi     ## class WiFi  ip =ConnectWiFi()
# ## server on pico
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48','waterypanda')
# wlan.connect(secrets.SSID,secrets.PASSWORD)

# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')

# # myWifi=WiFi()
# # ip =myWifi.ConnectWiFi()

# # wlan.ifconfig()=ip
# print(wlan.ifconfig())

# # print(ip)
 
# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # server_socket.bind((ip[0], 12345))
# server_socket.bind((wlan.ifconfig()[0], 12345))
# # server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
# # print(ip)
# print(wlan.ifconfig()[0])
 
# while True:
#     print('Waiting for a request from the client...')
#     # Receive request from client
#     request, client_address = server_socket.recvfrom(1024)
#     request =request.decode()
#     print("Client Request:",request.decode())
#     print("FROM CLIENT",client_address)
    
#     # String to send
#     data = "225,128,64"
    
#     # Send data to client
#     server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)

### Client side works fine 
import socket
import time
 
# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.10', 12345)  # Adjust IP address and port as needed
 
while True:
    # Send request to the server
    request_message = "SEND DATA"
    client_socket.sendto(request_message.encode(), server_address)
    
    # Receive data from the server
    data, addr = client_socket.recvfrom(1024)
    print('Received data:', data.decode())
    
    # Send acknowledgment back to server
    #ack_message = "Data received successfully"
    #client_socket.sendto(ack_message.encode(), addr)
    
    # Wait for 10 seconds before next request
    time.sleep(10)

#####~~~~~~ server on Pico with Struct the client side is in Python_Book_New and below!
# import network
# import usocket as socket
# # import secrets
# import time
# import struct
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('SpectrumSetup-41','leastdinner914')
# # wlan.connect('NETGEAR48','waterypanda901')
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
#     request, client_address = server_socket.recvfrom(1024)
#     request=struct.unpack('9s',request)
#     # print("Client Request:",request.decode())
#     print("FROM CLIENT",client_address)
#     print(f'From Client:  {request}')
    
    
    
    
#     # String to send
#     data = "225,128,64"
#     ## send data to client using struct
#     data=struct.pack('10s',data)
#     server_socket.sendto(data,client_address)
#     ## Send data to client
#     #server_socket.sendto(data.encode(), client_address)
    
#     # client_address ='192.168.1.12'
#     print(f'Sent data to {client_address}')
    
# # ## receive ack message from server
#     ack, client_address = server_socket.recvfrom(1024)
#     ack=ack.decode('utf-8')
#     print(ack)
    
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
    
### this is the picoW SERVER program to go with above CLIENT program using struct
# import network
# import usocket as socket
# # import secrets
# import time
 # import struct
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48','waterypanda901')
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
#     request, client_address = server_socket.recvfrom(1024)
#     request=struct.unpack('9s',request)
#     # print("Client Request:",request.decode())
#     print("FROM CLIENT",client_address)
#     print(f'From Client:  {request}')
#     # String to send
#     data = "225,128,64"
#     ## send data to client using struct
#     data=struct.pack('3i',data)
#     server_socket.sendto(data,client_address)
#     ## Send data to client
#     #server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
