'''
Basic_Programs/McWhorter/PW_109_Wifi/UDP_Client.py 
'''
import socket
import time

 

msgFromClient       = "Hello UDP Server"

bytesToSend         = str.encode(msgFromClient)

serverAddressPort   = ("127.0.0.1", 20001)

bufferSize          = 1024

 

# Create a UDP socket at client side

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Send  request to server using created UDP socket

UDPClientSocket.sendto(bytesToSend, serverAddressPort)



msgFromServer = UDPClientSocket.recvfrom(bufferSize)



msg = "Message from Server {}".format(msgFromServer[0])

print(msg)
