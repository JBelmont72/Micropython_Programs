'''Client and server.py in this folder are the same as below but separated. Run the Server on PicoW.
https://www.tutorialexample.com/understand-pyqt-qhboxlayout-addstretch-with-examples-for-beginners-pyqt-tutorial/
Here we create two buttons with QPushButton class, then add these two buttons into QHBoxLayout using hbox.addWidget(), finally, we use self.setLayout(hbox) to set layout of our window frame is QHBoxLayout.

important explantion at bottom about the UPD and MQTT operation to send communication!!
'''
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QHBoxLayout, QVBoxLayout

# class YuTextFrame(QWidget):

#     def __init__(self):
#         super().__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle('YuText')  
        
#         #
#         btn_search = QPushButton('Find', self)
#         btn_search.setStyleSheet("background-color:red;color:yellow;")
#         btn_search.clicked.connect(Find)
        
#         btn_select = QPushButton('Select', self)
#         btn_select.setStyleSheet("background-color:green;color: yellow")
#         btn_select.clicked.connect(Select)
#         #
#         hbox = QHBoxLayout()
#         hbox.addWidget(btn_select)
#         hbox.addWidget(btn_search)
        
#         self.setLayout(hbox)
#         self.setGeometry(300,300,400,300)
#         self.show()
#     def Find(self):
#         print('You found me!')
#     def Select(self):
#         print('You selected me!')

# if __name__ == '__main__':

#     app = QApplication(sys.argv)
#     frame = YuTextFrame()
#     sys.exit(app.exec_())
    
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class YuTextFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('YuText')  

        # Create and style buttons
        btn_search = QPushButton('Find', self)
        btn_search.setStyleSheet("background-color:red;color:yellow;")
        btn_search.clicked.connect(self.Find)  # Connect to class method

        btn_select = QPushButton('Select', self)
        btn_select.setStyleSheet("background-color:green;color: yellow")
        btn_select.clicked.connect(self.Select)  # Connect to class method

        # Layout setup
        hbox = QHBoxLayout()
        hbox.addWidget(btn_select)
        hbox.addWidget(btn_search)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def Find(self):
        print('You found me!')

    def Select(self):
        print('You selected me!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = YuTextFrame()
    sys.exit(app.exec_())

############ MQTT and UPD combined  PyQt5 program to support both UDP and MQTT communication when clicking the buttons.
''' New Features Added: CLIENT
UDP Messaging: Sends "Find" or "Select" over UDP to a Pico W.
MQTT Messaging: Publishes "Find" or "Select" to an MQTT topic.
⚡ How It Works:
Clicking Find → Sends "Find" via UDP & MQTT.
Clicking Select → Sends "Select" via UDP & MQTT.
📌 Setup Notes:
Change self.udp_ip to your Pico W's IP.
Set self.mqtt_broker to your MQTT broker's IP.
'''
import sys
import socket
import paho.mqtt.client as mqtt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class YuTextFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # UDP Setup
        self.udp_ip = "192.168.1.100"  # Change to your Pico W IP
        self.udp_port = 12345
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # MQTT Setup
        # Replace with your MQTT broker IP or domain
        self.mqtt_broker = "test.mosquitto.org"  # Change to your MQTT broker URL or IP
        self.mqtt_topic = "pico/commands"
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(self.mqtt_broker, 1883, 60)

    def initUI(self):
        self.setWindowTitle('YuText')

        btn_search = QPushButton('Find', self)
        btn_search.setStyleSheet("background-color:red;color:yellow;")
        btn_search.clicked.connect(self.Find)

        btn_select = QPushButton('Select', self)
        btn_select.setStyleSheet("background-color:green;color: yellow")
        btn_select.clicked.connect(self.Select)

        hbox = QHBoxLayout()
        hbox.addWidget(btn_select)
        hbox.addWidget(btn_search)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def Find(self):
        print('You found me!')
        self.send_udp("Find")
        self.send_mqtt("Find")

    def Select(self):
        print('You selected me!')
        self.send_udp("Select")
        self.send_mqtt("Select")

    def send_udp(self, message):
        try:
            self.udp_socket.sendto(message.encode(), (self.udp_ip, self.udp_port))
            print(f"UDP message sent: {message}")
        except Exception as e:
            print(f"UDP error: {e}")

    def send_mqtt(self, message):
        try:
            self.mqtt_client.publish(self.mqtt_topic, message)
            print(f"MQTT message sent: {message}")
        except Exception as e:
            print(f"MQTT error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = YuTextFrame()
    sys.exit(app.exec_())

'''Explanation:
Set MQTT Broker:
You can replace self.mqtt_broker = "test.mosquitto.org" with any broker of your choice:
HiveMQ: self.mqtt_broker = "broker.hivemq.com"
Mosquitto: self.mqtt_broker = "test.mosquitto.org"
Or even a local broker IP address: self.mqtt_broker = "192.168.1.101"
Connect to the Broker:
The client connects to the broker using self.mqtt_client.connect(self.mqtt_broker, 1883, 60) where 1883 is the default port for MQTT.
Brokers You Can Use:
HiveMQ: broker.hivemq.com
Mosquitto: test.mosquitto.org
Public Brokers: There are many free public brokers available, and you can find their addresses online.
Private Brokers: If you have your own broker (e.g., on your local network), use its IP or domain.
Just replace self.mqtt_broker with the appropriate broker address, and you should be all set to use either HiveMQ or Mosquitto. Let me know if you need further adjustments!
'''
import sys
import socket
import paho.mqtt.client as mqtt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
## final version of python client(UPD)  /  publisher(MQTT))
class YuTextFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # UDP Setup
        self.udp_ip = "192.168.1.100"  # Change to your Pico W IP
        self.udp_port = 12345
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # MQTT Setup
        # Replace with your MQTT broker IP or domain
        self.mqtt_broker = "test.mosquitto.org"  # Change to your MQTT broker URL or IP
        self.mqtt_topic = "pico/commands"
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(self.mqtt_broker, 1883, 60)

    def initUI(self):
        self.setWindowTitle('YuText')

        btn_search = QPushButton('Find', self)
        btn_search.setStyleSheet("background-color:red;color:yellow;")
        btn_search.clicked.connect(self.Find)

        btn_select = QPushButton('Select', self)
        btn_select.setStyleSheet("background-color:green;color: yellow")
        btn_select.clicked.connect(self.Select)

        hbox = QHBoxLayout()
        hbox.addWidget(btn_select)
        hbox.addWidget(btn_search)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def Find(self):
        print('You found me!')
        self.send_udp("Find")
        self.send_mqtt("Find")

    def Select(self):
        print('You selected me!')
        self.send_udp("Select")
        self.send_mqtt("Select")

    def send_udp(self, message):
        try:
            self.udp_socket.sendto(message.encode(), (self.udp_ip, self.udp_port))
            print(f"UDP message sent: {message}")
        except Exception as e:
            print(f"UDP error: {e}")

    def send_mqtt(self, message):
        try:
            self.mqtt_client.publish(self.mqtt_topic, message)
            print(f"MQTT message sent: {message}")
        except Exception as e:
            print(f"MQTT error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = YuTextFrame()
    sys.exit(app.exec_())



########``` below was the first combined client python  UDP/MQTT combined`
import sys
import socket
import paho.mqtt.client as mqtt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class YuTextFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        # UDP Setup
        self.udp_ip = "192.168.1.100"  # Change to your Pico W IP
        self.udp_port = 12345
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # MQTT Setup
        self.mqtt_broker = "192.168.1.101"  # Change to your MQTT broker IP
        self.mqtt_topic = "pico/commands"
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(self.mqtt_broker, 1883, 60)

    def initUI(self):
        self.setWindowTitle('YuText')  

        btn_search = QPushButton('Find', self)
        btn_search.setStyleSheet("background-color:red;color:yellow;")
        btn_search.clicked.connect(self.Find)

        btn_select = QPushButton('Select', self)
        btn_select.setStyleSheet("background-color:green;color: yellow")
        btn_select.clicked.connect(self.Select)

        hbox = QHBoxLayout()
        hbox.addWidget(btn_select)
        hbox.addWidget(btn_search)

        self.setLayout(hbox)
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def Find(self):
        print('You found me!')
        self.send_udp("Find")
        self.send_mqtt("Find")

    def Select(self):
        print('You selected me!')
        self.send_udp("Select")
        self.send_mqtt("Select")

    def send_udp(self, message):
        try:
            self.udp_socket.sendto(message.encode(), (self.udp_ip, self.udp_port))
            print(f"UDP message sent: {message}")
        except Exception as e:
            print(f"UDP error: {e}")

    def send_mqtt(self, message):
        try:
            self.mqtt_client.publish(self.mqtt_topic, message)
            print(f"MQTT message sent: {message}")
        except Exception as e:
            print(f"MQTT error: {e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = YuTextFrame()
    sys.exit(app.exec_())
########combined server/ subscriber  mqtt upd  version  for PicoW
 '''Server-Side Implementation for Pico W
This script handles:
UDP Communication: Listens for messages from the PyQt5 client.
MQTT Communication: Subscribes to the pico/commands topic on the Mosquitto broker.
📌 Setup Instructions
Wi-Fi Configuration: Set SSID and PASSWORD to your network.
UDP Settings:
The Pico W automatically gets an IP from Wi-Fi.
The script binds to this IP and listens on UDP_PORT = 12345.
Ensure your PyQt5 client's self.udp_ip matches the Pico W’s assigned IP.
MQTT Settings:
Set MQTT_BROKER = "192.168.1.101" to match your Mosquitto broker.
Your PyQt5 client should use the same broker IP.
'''
import secrets
import network
import socket
import machine
from umqtt.simple import MQTTClient

# Configure Wi-Fi
SSID = "secrets.ssid_condo"
PASSWORD = "secrets.password_condo"
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
###### the above combined UPD MQTT pico side server for pico and subscriber for MQTT
## below is UPD for PicoW
# UDP Server:
# The Pico W will listen for UDP messages on port 12345.
# Ensure that  PyQt5 client sends messages to the Pico W's IP on this port.
import network
import socket

# Configure Wi-Fi
SSID = "your_SSID"
PASSWORD = "your_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Connected to Wi-Fi", wlan.ifconfig())

# Set Pico W's IP (for UDP server)
PICO_IP = wlan.ifconfig()[0]  # Automatically gets assigned IP
UDP_PORT = 12345  # Must match PyQt5 client

# UDP Server Setup
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind((PICO_IP, UDP_PORT))

print(f"Listening for UDP on {PICO_IP}:{UDP_PORT}")

while True:
    try:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Received UDP from {addr}: {data.decode()}")
    except Exception as e:
        pass

####  MQTT server with subscriber on PicoW
# The Pico W will connect to your Mosquitto broker and listen for messages on the pico/commands topic.
# Your PyQt5 client will publish messages to the same topic.
import network
from umqtt.simple import MQTTClient

# Configure Wi-Fi
SSID = "your_SSID"
PASSWORD = "your_PASSWORD"

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    pass

print("Connected to Wi-Fi", wlan.ifconfig())

# MQTT Setup
MQTT_BROKER = "192.168.1.101"  # Change to your MQTT broker's IP
MQTT_TOPIC = "pico/commands"

# Initialize MQTT Client
client = MQTTClient("pico", MQTT_BROKER)
client.connect()

def mqtt_callback(topic, msg):
    print(f"Received MQTT: {msg.decode()}")

client.set_callback(mqtt_callback)
client.subscribe(MQTT_TOPIC)

while True:
    # Handle MQTT Messages
    client.check_msg()

'''
 it's not an issue for your PyQt5 client to send both UDP and MQTT messages simultaneously from the Python browser side. The client will handle both protocols independently, and there’s no conflict since they operate in different layers:
UDP is a connectionless protocol. When you send a message via UDP, it’s just a one-way transmission to the specified IP and port.
MQTT is a messaging protocol that operates on a broker-client model. The client connects to the broker and publishes messages to a topic.
In your code, the send_udp and send_mqtt functions are called independently when the Find or Select buttons are clicked. So, when you press a button, the client sends the UDP message to the Pico W and the MQTT message to the broker.
Here’s a bit more detail on how they function:
UDP: Sends the message to the Pico W's IP directly. The Pico W receives it through its UDP server.
MQTT: Publishes the message to the broker (e.g., Mosquitto). The Pico W can subscribe to the MQTT topic to receive these messages.
Why It Works Fine:
Independence: UDP and MQTT are separate processes. They do not interfere with each other since the UDP socket operates through a different channel than the MQTT client.
Concurrency: Python handles both operations simultaneously (since both send_udp and send_mqtt are non-blocking by default), so you don’t have to worry about them blocking each other.
Important Considerations:
Pico W: The Pico W will only receive messages from either UDP or MQTT, depending on how you've set it up (it cannot handle both at the same time for the same action).
If you want the Pico W to handle both UDP and MQTT, you must set it up to listen for both (as shown in the previous server-side code with client.check_msg() for MQTT and recvfrom for UDP).
Network Traffic: As long as your network can handle the traffic and both protocols are properly configured, sending messages over both protocols shouldn’t be a problem.'''