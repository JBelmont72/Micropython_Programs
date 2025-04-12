''' New Features Added:This is the Server code for the Pico W.
Listens for UDP messages and MQTT messages.
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

class MyTextFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # UDP Setup
        self.udp_ip = "192.168.1.253"  # Change to your Pico W IP
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
    frame = MyTextFrame()
    sys.exit(app.exec_())
    
    
################ this is the server code run on python text editor ######################
import sys
import socket
import paho.mqtt.client as mqtt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout

class MyTextFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

        # UDP Setup
        self.udp_ip = "192.168.1.253"  # Change to your Pico W IP
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
    frame = MyTextFrame()
    sys.exit(app.exec_())

