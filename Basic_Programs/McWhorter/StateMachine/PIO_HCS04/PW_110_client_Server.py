'''PW 110

A simple client server project on the Raspberry Pi Pico W. The Pico is configures as the server, and your desktop pc or laptop is configures to be the client. You will be running python on your PC. The project requests the user on the PC to specify a desired color. The color is then sent to the Pico, the Server. Then the Pico sets that color to ‘ON’. The pi pico is powered by a breadboard power bank, and there is no need for any connections to the pico. You can pick up the breadBoard Power Bank HERE [Affiliate Link]. Below is the schematic for the Server Side of the project:
'''
## PicoW Server
import network
import usocket as socket
import secrets
import time
import machine
 
greenLED=machine.Pin(18,machine.Pin.OUT)
yellowLED=machine.Pin(19,machine.Pin.OUT)
redLED=machine.Pin(20,machine.Pin.OUT)
# Set up WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print(secrets.SSID,secrets.PASSWORD)
wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# Wait for connection
while not wlan.isconnected():
    time.sleep(1)
print("Connection Completed")
print('WiFi connected')
print(wlan.ifconfig())
 
# Set up UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")
print(wlan.ifconfig()[0])
 
while True:
    print('Waiting for a request from the client...')
    # Receive request from client
    color, client_address = server_socket.recvfrom(1024)
    color=color.decode()
    print("Client Request:",color)
    print("FROM CLIENT",client_address)
    
    if (color=="green"):
        greenLED.on()
        yellowLED.off()
        redLED.off()
    if (color=="yellow"):
        greenLED.off()
        yellowLED.on()
        redLED.off()
    if (color=="red"):
        greenLED.off()
        yellowLED.off()
        redLED.on()
    if (color=="off"):
        greenLED.off()
        yellowLED.off()
        redLED.off()
    
    # Send data to client
    data="LED "+color+" executed"
    server_socket.sendto(data.encode(), client_address)
    print(f'Sent data to {client_address}')
    
    # Optional: Pause for a short period to prevent overwhelming the client
    time.sleep(1)
    
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
