'''
#1 is the PyQt5 client works and controls LEDs, 2 is the pico server, 3 is the client with UDP witout PyQt5, 4 is the client with UDP. and MQTT
#4 is the PyQt5 Class from PW_111_PyQt5.py



'''
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# import time
# ## client for python  in Python_Book_New
# import socket   ##client for PW110 in MIcropython_Programs/Basic_Programs/McWhorter/StateMachine/PIO_HCS04/PW_110_Socket_Server.py
# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('192.168.1.223', 12345)  # Adjust IP address and port as needed
 
# def greenButtonPressed():
#     print("green button clicked")
#     myColor='green'
#     client_socket.sendto(myColor.encode(), server_address)
#     data, addr = client_socket.recvfrom(1024)
#     print('Received data:', data.decode())
#     return myColor
# def yellowButtonPressed():
#     print("yellow button clicked")
#     myColor='yellow'
#     client_socket.sendto(myColor.encode(), server_address)
#     data, addr = client_socket.recvfrom(1024)
#     print('Received data:', data.decode())
#     return myColor
# def redButtonPressed():
#     print("red button clicked")
#     myColor='red'
#     client_socket.sendto(myColor.encode(), server_address)
#     data, addr = client_socket.recvfrom(1024)
#     print('Received data:', data.decode())
#     return myColor
# def offButtonPressed():
#     print("off button clicked")
#     myColor='off'
#     client_socket.sendto(myColor.encode(), server_address)
#     data, addr = client_socket.recvfrom(1024)
#     print('Received data:', data.decode())
#     return myColor
# def sliderValueChanged(val):
#     frequency=val/10
#     sliderLabel.setText("Frequency: "+str(frequency)+" Hz")
#     print("Frequency: ",frequency)
 
# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle("My Grand Widget")
# window.setGeometry(100,100,800,600)
 
# widgetBox=QVBoxLayout(window)
# buttonBox=QHBoxLayout()
 
# greenButton = QPushButton("Green Button")
# greenButton.setStyleSheet("background-color: green; color: white;")
# greenButton.clicked.connect(greenButtonPressed)
# buttonBox.addWidget(greenButton)

 
# yellowButton = QPushButton("Yellow Button")
# yellowButton.setStyleSheet("background-color: yellow; color: black;")
# yellowButton.clicked.connect(yellowButtonPressed)
# buttonBox.addWidget(yellowButton)
 
# redButton = QPushButton("Red Button")
# redButton.setStyleSheet("background-color: red; color: white;")
# redButton.clicked.connect(redButtonPressed)
# buttonBox.addWidget(redButton)
 
# offButton = QPushButton("Off Button")
# offButton.setStyleSheet("background-color: black; color: white;")
# offButton.clicked.connect(offButtonPressed)
# buttonBox.addWidget(offButton)
 
# slider = QSlider(Qt.Horizontal)
# slider.setMinimum(1)
# slider.setMaximum(40)
# slider.setValue(10)
# slider.setTickPosition(QSlider.TicksBelow)
# slider.setTickInterval(5)
# slider.valueChanged.connect(sliderValueChanged)
 
 
# sliderLabel=QLabel("Frequency: 1.0 HZ")
# sliderLabel.setAlignment(Qt.AlignCenter)
# sliderLabel.setStyleSheet("font-size: 24px;padding 2px;")
 
# widgetBox.addLayout(buttonBox)
# widgetBox.addWidget(sliderLabel)
# widgetBox.addWidget(slider)
# widgetBox.addStretch()
 
# window.setLayout(widgetBox)
# window.show()
# sys.exit(app.exec_())

################# below is the pico server with the leds
# PicoW Server
# import network
# import usocket as socket
# import secrets
# import time
# import machine
 
# greenLED=machine.Pin(16,machine.Pin.OUT)
# yellowLED=machine.Pin(18,machine.Pin.OUT)
# redLED=machine.Pin(17,machine.Pin.OUT)
# # Set up WiFi connection
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)

# print(secrets.ssid_home,secrets.password_home)
# wlan.connect(secrets.ssid_home,secrets.password_home)
# # print(secrets.SSID,secrets.PASSWORD)
# # wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')
# print(wlan.ifconfig())


# try:      ## this is to close a socket if already open
#     server_socket.close()
#     print('socket closed')
# except:
#     print('socket was already closed')
#     pass

# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Not always required on UDP but safe
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
# print(wlan.ifconfig()[0])
 
# while True:
#     print('Waiting for a request from the client...')
#     # Receive request from client
#     color, client_address = server_socket.recvfrom(1024)
#     color=color.decode()
#     print("Client Request:",color)
#     print("FROM CLIENT",client_address)


#     greenLED.value(color=='green')
#     yellowLED.value(color=='yellow')
#     redLED.value(color== 'red')
#     if color =='off':
#         greenLED.off()
#         yellowLED.off()
#         redLED.off()
'''         
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
'''
    # # Send data to client
    # data="LED "+color+" executed"
    # server_socket.sendto(data.encode(), client_address)
    # print(f'Sent data to {client_address}')
    
    # # Optional: Pause for a short period to prevent overwhelming the client
    # time.sleep(1)


    
#### below is the pico client, i will fold this into the PyQt5 class to make it a UDP client
'''
## client for python  in Python_Book_New
import socket   ##client for PW110 in MIcropython_Programs/Basic_Programs/McWhorter/StateMachine/PIO_HCS04/PW_110_Socket_Server.py
import time
 
# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.223', 12345)  # Adjust IP address and port as needed
 
while True:
    # Send request to the server
    myColor=input("Please Input Your Color (Green, Yellow, Red, Off )")
    myColor=myColor.lower()
    client_socket.sendto(myColor.encode(), server_address)
    
    # Receive data from the server
    data, addr = client_socket.recvfrom(1024)
    print('Received data:', data.decode())
'''
####### This is a working class that I want to make into the class structure for using UDP!
# import socket   ## this is the socket library for UDP
# import time
# # import network  
# import secrets


# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
#     QPushButton, QSlider, QLabel
# )
# from PyQt5.QtCore import Qt
# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('192.168.1.25', 12345)  # Adjust IP address and port as needed
# # # Set up WiFi connection
# # wlan = network.WLAN(network.STA_IF)
# # wlan.active(True)
# # wlan.connect(secrets.ssid_home,secrets.password_home)
# # # wlan.connect(secrets.SSID,secrets.PASSWORD)
# # # Wait for connection
# # while not wlan.isconnected():
# #     time.sleep(1)
# # print("Connection Completed")
# # print('WiFi connected')
# # print(wlan.ifconfig())


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.var = 'yellow'
#         self.varOld = 'red'
#         ## deleted all the window since it is inherited
#         self.setWindowTitle('My very own Widget')
#         self.setGeometry(100, 100, 800, 600)

#         widgetBox = QVBoxLayout() ##here i create a vertical layout for the widget
#         buttonBox = QHBoxLayout() ## Here i create a horizontal layout for the buttons

#         # Blue Button
#         blueButton = QPushButton('Blue Button')
#         blueButton.setStyleSheet('background-color: blue;color: white;')
#         blueButton.clicked.connect(self.blueButtonpressed)
#         buttonBox.addWidget(blueButton)

#         # Red Button
#         redButton = QPushButton('Red Button')
#         redButton.setStyleSheet('background-color: red;color: white')
#         redButton.clicked.connect(self.redButtonpressed)
#         buttonBox.addWidget(redButton)

#         # Yellow Button
#         yellowButton = QPushButton('Yellow Button')
#         yellowButton.setStyleSheet('background-color: yellow; color: magenta')
#         yellowButton.clicked.connect(self.yellowButtonpressed)
#         buttonBox.addWidget(yellowButton)

#         # Off Button
#         self.offButton = QPushButton('Off Button')
#         self.offButton.setStyleSheet('background-color: green; color: black')
#         # self.offButton.clicked.connect(self.offButtonpressed) ## this command works fine. tried to use lambda anonymous function instead below
#         # self.offButton.clicked.connect(lambda  self.offButtonpressed())  ### does not work:  This calls the method immediately (because of the parentheses), instead of passing a function reference.
# # Also, the syntax is invalid: lambda self.offButtonpressed() looks like you're trying to define the lambda’s argument as a function call, which isn’t allowed.
        
#         self.offButton.clicked.connect(lambda: self.offButtonpressed())## this works the same as without any lambda function but allows more flexibililty,for example to log something or pass parameters!
#         self.offButton.clicked.connect(lambda: self.offButtonpressed_with_param("Turning off"))


        
#         buttonBox.addWidget(self.offButton)

#         widgetBox.addLayout(buttonBox) ## here i add the buttonBOx to the widgetBox

#         # Slider Label and Slider
#         self.sliderLabel = QLabel("Frequency: 1.0 Hz")
#         self.sliderLabel.setAlignment(Qt.AlignCenter)
#         self.sliderLabel.setStyleSheet("font-size: 24px; padding: 2px;")

#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(1)
#         self.slider.setMaximum(40)
#         self.slider.setValue(10)
#         self.slider.setTickPosition(QSlider.TicksBelow)
#         self.slider.setTickInterval(5)
#         self.slider.valueChanged.connect(self.sliderValueChanged)

#         widgetBox.addWidget(self.sliderLabel)
#         widgetBox.addWidget(self.slider)
#         widgetBox.addStretch()

#         self.setLayout(widgetBox)
#         self.show()

#     def blueButtonpressed(self):
#         print('Blue button clicked')
#         self.var = 'green'
#         client_socket.sendto(self.var.encode(), server_address)
#         data, addr = client_socket.recvfrom(1024)
#         print('Received data:', data.decode())
#         self.varOld = self.var
#         self.var = 'green'
#         if self.varOld != self.var:
#             print('Blue button clicked')
#             self.varOld = self.var
#             client_socket.sendto(self.var.encode(), server_address)
            
#     def redButtonpressed(self):
#         print('Red button clicked')
#         self.var = 'red'
#         client_socket.sendto(self.var.encode(), server_address)
#         data, addr = client_socket.recvfrom(1024)
#         print('Received data:', data.decode())
#         self.varOld = self.var
#         if self.varOld != self.var:
#             print('Red button clicked')
#             self.varOld = self.var
#             client_socket.sendto(self.var.encode(), server_address)
      

#     def yellowButtonpressed(self):
#         print('Yellow button clicked')
#         self.var = 'yellow'
#         client_socket.sendto(self.var.encode(), server_address)
#         data, addr = client_socket.recvfrom(1024)
#         print('Received data:', data.decode())
#         self.varOld = self.var
#         if self.varOld != self.var:
#             print('Yellow button clicked')
#             self.varOld = self.var
#             client_socket.sendto(self.var.encode(), server_address)
      
#     def offButtonpressed(self):
#         print('Off button clicked')
#         self.var = 'off'
#         client_socket.sendto(self.var.encode(), server_address)
#         data, addr = client_socket.recvfrom(1024)
#         print('Received data:', data.decode())
#         self.varOld = self.var
#         self.var = 'off'
#         if self.varOld != self.var:
#             print('Off button clicked')
#             self.varOld = self.var
#             client_socket.sendto(self.var.encode(), server_address)
      

#     def sliderValueChanged(self, value):
#         frequency = value / 10
#         self.sliderLabel.setText(f'Frequency: {frequency:.1f} Hz')
#         print(f'Frequency: {frequency:.1f} Hz')
 
#     def offButtonpressed_with_param(self,param):
#         print(param)
#         client_socket.sendto(param.encode(), server_address)
#         data, addr = client_socket.recvfrom(1024)
#         print('Received data:', data.decode())
#         self.varOld = self.var
#         self.var = 'param'
# app = QApplication(sys.argv)
# mw = MainWindow()
# sys.exit(app.exec_())


## this is an improved version with exactly same functionality. 
## the if self.varOld != self.var: is to avoid duplicate messages sent
import socket
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel
)
from PyQt5.QtCore import Qt

# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.25', 12345)  # Adjust as needed


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.var = 'yellow'
        self.varOld = 'red'

        self.setWindowTitle('My very own Widget')
        self.setGeometry(100, 100, 800, 600)

        widgetBox = QVBoxLayout()
        buttonBox = QHBoxLayout()

        # Blue Button
        blueButton = QPushButton('Blue Button')
        blueButton.setStyleSheet('background-color: blue;color: white;')
        blueButton.clicked.connect(lambda: self.buttonPressed('green'))
        buttonBox.addWidget(blueButton)

        # Red Button
        redButton = QPushButton('Red Button')
        redButton.setStyleSheet('background-color: red;color: white')
        redButton.clicked.connect(lambda: self.buttonPressed('red'))
        buttonBox.addWidget(redButton)

        # Yellow Button
        yellowButton = QPushButton('Yellow Button')
        yellowButton.setStyleSheet('background-color: yellow; color: magenta')
        yellowButton.clicked.connect(lambda: self.buttonPressed('yellow'))
        buttonBox.addWidget(yellowButton)

        # Off Button
        self.offButton = QPushButton('Off Button')
        self.offButton.setStyleSheet('background-color: green; color: black')
        self.offButton.clicked.connect(lambda: self.offButtonpressed())
        self.offButton.clicked.connect(lambda: self.offButtonpressed_with_param("Turning off"))
        buttonBox.addWidget(self.offButton)

        widgetBox.addLayout(buttonBox)

        # Slider Label and Slider
        self.sliderLabel = QLabel("Frequency: 1.0 Hz")
        self.sliderLabel.setAlignment(Qt.AlignCenter)
        self.sliderLabel.setStyleSheet("font-size: 24px; padding: 2px;")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(40)
        self.slider.setValue(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(5)
        self.slider.valueChanged.connect(self.sliderValueChanged)

        widgetBox.addWidget(self.sliderLabel)
        widgetBox.addWidget(self.slider)
        widgetBox.addStretch()

        self.setLayout(widgetBox)
        self.show()

    def send_udp(self, message):
        client_socket.sendto(message.encode(), server_address)
        data, addr = client_socket.recvfrom(1024)
        print('Received data:', data.decode())

    def buttonPressed(self, color):
        print(f'{color.capitalize()} button clicked')
        self.var = color
        if self.varOld != self.var:
            self.varOld = self.var
            self.send_udp(self.var)

    def offButtonpressed(self):
        print('Off button clicked')
        self.var = 'off'
        if self.varOld != self.var:
            self.varOld = self.var
            self.send_udp(self.var)

    def offButtonpressed_with_param(self, param):
        print(param)
        self.send_udp(param)

    def sliderValueChanged(self, value):
        frequency = value / 10
        self.sliderLabel.setText(f'Frequency: {frequency:.1f} Hz')
        print(f'Frequency: {frequency:.1f} Hz')


app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())


# this pico server has an added static IP address to my Pico W when connecting to Wi-Fi (especially when using main.py without an interactive shell),  can use wlan.ifconfig() before connecting to the network.

# Here is the  updated program with the static IP added 
# Cautions with Static IP Address:  Make sure the static IP you assign (192.168.1.25) is within your router’s subnet and outside its DHCP range, or you may get IP conflicts.
# Keep your router’s DHCP settings in mind — if it uses .1.100–.1.200, you can use .1.25 safely.
# This change makes your Pico W reachable even if it's running main.py on boot, without needing to print or discover its IP.

# PicoW Server
import network
import usocket as socket
import secrets
import time
import machine
 
greenLED = machine.Pin(16, machine.Pin.OUT)
yellowLED = machine.Pin(18, machine.Pin.OUT)
redLED = machine.Pin(17, machine.Pin.OUT)

# Set up WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Set static IP configuration (adjust as needed)
# Format: (ip, subnet_mask, gateway, dns_server)
STATIC_IP = '192.168.1.25'
SUBNET_MASK = '255.255.255.0'
GATEWAY = '192.168.1.1'
DNS = '8.8.8.8'
wlan.ifconfig((STATIC_IP, SUBNET_MASK, GATEWAY, DNS))

print(secrets.ssid_home, secrets.password_home)
wlan.connect(secrets.ssid_home, secrets.password_home)
# print(secrets.SSID, secrets.PASSWORD)
# wlan.connect(secrets.SSID, secrets.PASSWORD)

# Wait for connection
while not wlan.isconnected():
    time.sleep(1)
print("Connection Completed")
print('WiFi connected')
print(wlan.ifconfig())

try:  # this is to close a socket if already open
    server_socket.close()
    print('socket closed')
except:
    print('socket was already closed')
    pass

# Set up UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Not always required on UDP but safe
server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")
print(wlan.ifconfig()[0])

while True:
    print('Waiting for a request from the client...')
    # Receive request from client
    color, client_address = server_socket.recvfrom(1024)
    color = color.decode()
    print("Client Request:", color)
    print("FROM CLIENT", client_address)

    greenLED.value(color == 'green')
    yellowLED.value(color == 'yellow')
    redLED.value(color == 'red')

    if color == 'off':
        greenLED.off()
        yellowLED.off()
        redLED.off()

    '''      
    if (color == "green"):
        greenLED.on()
        yellowLED.off()
        redLED.off()
    if (color == "yellow"):
        greenLED.off()
        yellowLED.on()
        redLED.off()
    if (color == "red"):
        greenLED.off()
        yellowLED.off()
        redLED.on()
    if (color == "off"):
        greenLED.off()
        yellowLED.off()
        redLED.off()
    '''

    # Send data to client
    data = "LED " + color + " executed"
    server_socket.sendto(data.encode(), client_address)
    print(f'Sent data to {client_address}')

    # Optional: Pause for a short period to prevent overwhelming the client
    time.sleep(1)

