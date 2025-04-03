'''
this is an alternate version to UDP_Ser_FingerCount.py
'''

#Picow Server side for finger count , receive count,calculate angle and move servo
import network
import usocket as socket
import time
import struct
import machine

# Setup Wi-Fi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('NETGEAR48', 'waterypanda901')

while not wlan.isconnected():
    time.sleep(1)

print("Connection Completed")
print('WiFi connected:', wlan.ifconfig())

# Setup UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")

# Initialize servo
servo = machine.PWM(machine.Pin(15))
servo.freq(50)
servo.duty_u16(0)

def set_servo_angle(angle):
    duty = int(6553/180*angle+1638)

    print(duty)
    # duty = int((angle / 180) * 1023)  # Map angle to duty cycle
    servo.duty_u16(duty)

while True:
    print('Waiting for a request from the client...')
    request, client_address = server_socket.recvfrom(1024)
    
    # Unpack the finger count
    finger_count = struct.unpack('i', request)[0]
    print(f"Finger Count: {finger_count}")

    # Calculate the servo angle
    angle = finger_count * 18
    set_servo_angle(angle)

    # Send the angle back to the client
    response = struct.pack('i', angle)
    server_socket.sendto(response, client_address)
    print(f'Sent angle {angle}° to {client_address}')



## Client MAC side for sending finger count to Pico server
# import socket
# import struct

# SERVER_IP = '192.168.1.29'  # Replace with your Pico W IP
# SERVER_PORT = 12345

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
#     finger_count = int(input("Enter finger count (0–10): ").strip())
    
#     if not (0 <= finger_count <= 10):
#         print("Invalid count. Enter a number between 0 and 10.")
#         continue

#     # Pack the finger count as a single integer
#     packed_data = struct.pack('i', finger_count)
#     client_socket.sendto(packed_data, (SERVER_IP, SERVER_PORT))
    
#     # Receive and unpack the server’s response
#     response, _ = client_socket.recvfrom(1024)
#     angle = struct.unpack('i', response)[0]
#     print(f"Server Response: Servo angle set to {angle} degrees")
