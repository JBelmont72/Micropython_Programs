''' PW 109 pico server and python client

send and receive data between the Raspberry Pi Pico W, and your  PC. We will be running python on the PC, and we will exchange data using the UDP protocol. UDP is simple, and a very reliable way to send data packets back and forth. In this example, we will be demonstrating a simple Client Server relationship between the Pi Pico and PC using UDP over WiFi.ç
'''
import network
import usocket as socket
import secrets
import time
from WiFiNetwork_Socket import WiFi     ## class WiFi  ip =ConnectWiFi()
## server on pico
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48','waterypanda')
# wlan.connect(secrets.SSID,secrets.PASSWORD)

# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')

myWifi=WiFi()
ip =myWifi.ConnectWiFi()

# wlan.ifconfig()=ip
# print(wlan.ifconfig())

# print(ip)
 
# Set up UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((ip[0], 12345))
# server_socket.bind((wlan.ifconfig()[0], 12345))
# server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")
print(ip[0])
# print(wlan.ifconfig()[0])
 
while True:
    print('Waiting for a request from the client...')
    # Receive request from client
    request, client_address = server_socket.recvfrom(1024)
    print("Client Request:",request.decode())
    print("FROM CLIENT",client_address)
    
    # String to send
    data = "225,128,64"
    
    # Send data to client
    server_socket.sendto(data.encode(), client_address)
    print(f'Sent data to {client_address}')
    
    # Optional: Pause for a short period to prevent overwhelming the client
    time.sleep(1)

### Client side 
# import socket
# import time
 
# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('192.168.88.71', 12345)  # Adjust IP address and port as needed
 
# while True:
#     # Send request to the server
#     request_message = "SEND DATA"
#     client_socket.sendto(request_message.encode(), server_address)
    
#     # Receive data from the server
#     data, addr = client_socket.recvfrom(1024)
#     print('Received data:', data.decode())
    
#     # Send acknowledgment back to server
#     #ack_message = "Data received successfully"
#     #client_socket.sendto(ack_message.encode(), addr)
    
#     # Wait for 10 seconds before next request
#     time.sleep(10)˜