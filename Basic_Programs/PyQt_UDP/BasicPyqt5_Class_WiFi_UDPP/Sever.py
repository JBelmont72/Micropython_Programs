## 1st UDP server 2d MQTT server 3d combined UDP and MQTT server 4th MQTT client and UPD client
  
# 
# 
# below is UPD for PicoW
## UDP Server:
## The Pico W will listen for UDP messages on port 12345.
## Ensure that  PyQt5 client sends messages to the Pico W's IP on this port.
# import network
# import socket

# ## Configure Wi-Fi
# SSID = "SpectrumSetup-41"  # Change to your Wi-Fi SSID

# PASSWORD = "leastdinner914"  # Change to your Wi-Fi password

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect(SSID, PASSWORD)

# while not wlan.isconnected():
#     pass

# print("Connected to Wi-Fi", wlan.ifconfig())

# ## Set Pico W's IP (for UDP server)
# PICO_IP = wlan.ifconfig()[0]  # Automatically gets assigned IP
# UDP_PORT = 12345  # Must match PyQt5 client

# ## UDP Server Setup
# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp_socket.bind((PICO_IP, UDP_PORT))

# print(f"Listening for UDP on {PICO_IP}:{UDP_PORT}")

# while True:
#     try:
#         data, addr = udp_socket.recvfrom(1024)
#         print(f"Received UDP from {addr}: {data.decode()}")
#     except Exception as e:
#         pass

####  MQTT server with subscriber on PicoW
## The Pico W will connect to your Mosquitto broker and listen for messages on the pico/commands topic.
## Your PyQt5 client will publish messages to the same topic.

# import network
# from umqtt.simple import MQTTClient

# # Configure Wi-Fi
# SSID = "your_SSID"
# PASSWORD = "your_PASSWORD"

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect(SSID, PASSWORD)

# while not wlan.isconnected():
#     pass

# print("Connected to Wi-Fi", wlan.ifconfig())

# # MQTT Setup
# MQTT_BROKER = "192.168.1.101"  # Change to your MQTT broker's IP
# MQTT_TOPIC = "pico/commands"

# # Initialize MQTT Client
# client = MQTTClient("pico", MQTT_BROKER)
# client.connect()

# def mqtt_callback(topic, msg):
#     print(f"Received MQTT: {msg.decode()}")

# client.set_callback(mqtt_callback)
# client.subscribe(MQTT_TOPIC)

# while True:
#     # Handle MQTT Messages
#     client.check_msg()
#########combined server UDP and MQTT on PicoW

   
## Configure Wi-Fi 

import secrets
import network
import socket
import machine
from umqtt.simple import MQTTClient

# Configure Wi-Fi
SSID = "SpectrumSetup-41"  # Change to your Wi-Fi SSID  
PASSWORD = "leastdinner914"  # Change to your Wi-Fi password

# SSID = "secrets.ssid_condo"
# PASSWORD = "secrets.password_condo"
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Connected to Wi-Fi", wlan.ifconfig())

# Set Pico W's IP (for UDP server)
PICO_IP = wlan.ifconfig()[0]  # Automatically gets assigned IP
UDP_PORT = 12345  # Must match PyQt5 client

# MQTT Setup

# MQTT_BROKER = "broker.hivemq.com" 
MQTT_BROKER = 'test.mosquitto.org'
# MQTT_BROKER = "192.168.1.101"  # Change to your MQTT broker's IP
MQTT_TOPIC = "pico/commands"

# Initialize MQTT Client
client = MQTTClient("pico", MQTT_BROKER)
client.connect()

def mqtt_callback(topic, msg):
    print(f"Received MQTT: {msg.decode()}")

client.set_callback(mqtt_callback)
client.subscribe(MQTT_TOPIC)

# UDP Server Setup
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((PICO_IP, UDP_PORT))

print(f"Listening for UDP on {PICO_IP}:{UDP_PORT}")

while True:
    # Handle MQTT Messages
    client.check_msg()
    
    # Handle UDP Messages
    try:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Received UDP from {addr}: {data.decode()}")
    except Exception as e:
        pass