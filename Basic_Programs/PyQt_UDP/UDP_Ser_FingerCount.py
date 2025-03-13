'''
this is the pico client for fingerCount in UPD format
'''
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
servo = machine.PWM(machine.Pin(16))
servo.freq(50)
##6553/180*angle+1638
def set_servo_angle(angle):
    duty = int(6553/180*angle+1638)

    print(duty)
    # duty = int((angle / 180) * 1023)  # Map angle to duty cycle
    servo.duty_u16(duty)

values =[]
def smooth_distance(new_value, values, size=1):
    # global values
    values.append(new_value)
    if len(values) > size:
        values.pop(0)
    return sum(values) / len(values)


while True:
    print('Waiting for a request from the client...')
    request, client_address = server_socket.recvfrom(1024)
    
    # Unpack the finger count
    Newfinger_count = struct.unpack('i', request)[0]
    
    finger_count =smooth_distance(Newfinger_count,values)

    
    
    
    
    print(f"Finger Count: {finger_count}")

    # Calculate the servo angle
    angle = finger_count * 18
    angle=int(angle)
    set_servo_angle(angle)

    # Send the angle back to the client
    response = struct.pack('i', angle)
    server_socket.sendto(response, client_address)
    print(f'Sent angle {angle}degrees to {client_address}')
