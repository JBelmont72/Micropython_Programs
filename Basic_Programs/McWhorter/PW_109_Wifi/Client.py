'''
 send and receive data between the  Raspberry Pi Pico W, and your PC. We will be running  python on the PC, and we will exchange data using the UDP protocol. UDP is simple, and a very reliable way to send data packets back and forth. In this example, we will be demonstrating a simple Client Server relationship between the Pi Pico and PC using UDP over WiFi
'''
import socket
import time
 
# Set up UDP client
client_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = ('192.168.1.1', 12345)  # Adjust IP address and port as needed
 
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