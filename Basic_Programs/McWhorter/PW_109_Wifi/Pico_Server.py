'''
PW_109 this is the server on pico. (sends to Client.py) this is UPD 
(this video uses TCP to send back and forth
https://www.youtube.com/watch?v=9M9k5lLTT4c)
 send and receive data between the  Raspberry Pi Pico W, and your PC. We will be running  python on the PC, and we will exchange data using the UDP protocol. UDP is simple, and a very reliable way to send data packets back and forth. In this example, we will be demonstrating a simple Client Server relationship between the Pi Pico and PC using UDP over WiFi
'''
import network
import usocket as socket
import Secrets
import time

# Static IP configuration I added this to create a static ip address
static_ip = '127.0.0.1'  # Replace with your desired static IP
# static_ip = '192.168.1.1'  # Replace with your desired static IP
subnet_mask = '255.255.255.0'
gateway_ip = '192.168.1.15'
dns_server = '192.168.1.1'

# Init Wi-Fi Interface

 
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(Secrets.ssid,Secrets.password)
 

# Set static IP address I added this to create a static ip address
wlan.ifconfig((static_ip, subnet_mask, gateway_ip, dns_server))
# Wait for connection
while not wlan.isconnected():
    time.sleep(1)
print("Connection Completed")
print('WiFi connected')
print(wlan.ifconfig())
port =12345
# Set up UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")
print(wlan.ifconfig()[0])
 
while True:
    # bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
## 
    # message = bytesAddressPair[0]== request

    # address = bytesAddressPair[1]== client_address

    # clientMsg = "Message from Client:{}".format(message)
    # clientIP  = "Client IP Address:{}".format(address)
    
    # print(clientMsg)
    # print(clientIP)

   

    # # Sending a reply to client

    # UDPServerSocket.sendto(bytesToSend, address)
    
    
    
    print('Waiting for a request from the client...')
    # Receive request from client
    request, client_address = server_socket.recvfrom(1024)
    
    print("Client Request:",request.decode())
    print("FROM CLIENT",client_address)
   
   
#    msgFromServer       = "Hello UDP Client"

# bytesToSend         = str.encode(msgFromServer)

    
    # String to send
    data = "225,128,64"
    bytesToSend=str.encode(data)# my change
    # Send data to client
    server_socket.sendto(bytesToSend, client_address)# my Change
    # server_socket.sendto(data.encode(), client_address)
    print(f'Sent data to {client_address}')
    
    # Optional: Pause for a short period to prevent overwhelming the client
    time.sleep(1)
    