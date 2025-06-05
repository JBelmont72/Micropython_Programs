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
# server_address = ('192.168.1.32', 12345)  # Adjust IP address and port as needed
 
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
## PicoW Server
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

# print(secrets.ssid_condo,secrets.password_condo)
# wlan.connect(secrets.ssid_condo,secrets.password_condo)
# # print(secrets.SSID,secrets.PASSWORD)
# # wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')
# print(wlan.ifconfig())
 
# # Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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
    
#     if (color=="green"):
#         greenLED.on()
#         yellowLED.off()
#         redLED.off()
#     if (color=="yellow"):
#         greenLED.off()
#         yellowLED.on()
#         redLED.off()
#     if (color=="red"):
#         greenLED.off()
#         yellowLED.off()
#         redLED.on()
#     if (color=="off"):
#         greenLED.off()
#         yellowLED.off()
#         redLED.off()
    
#     # Send data to client
#     data="LED "+color+" executed"
#     server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
    
# #### below is the pico client, i folded this into the PyQt5 code above in #1
# '''
# ## client for python  in Python_Book_New
# import socket   ##client for PW110 in MIcropython_Programs/Basic_Programs/McWhorter/StateMachine/PIO_HCS04/PW_110_Socket_Server.py
# import time
 
# # Set up UDP client
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_address = ('192.168.1.223', 12345)  # Adjust IP address and port as needed
 
# while True:
#     # Send request to the server
#     myColor=input("Please Input Your Color (Green, Yellow, Red, Off )")
#     myColor=myColor.lower()
#     client_socket.sendto(myColor.encode(), server_address)
    
#     # Receive data from the server
#     data, addr = client_socket.recvfrom(1024)
#     print('Received data:', data.decode())
# '''
# ####### This is a working class that I want to make into the class structure for using UDP!
# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
#     QPushButton, QSlider, QLabel
# )
# from PyQt5.QtCore import Qt

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

#         # green Button
#         greenButton = QPushButton('green Button')
#         greenButton.setStyleSheet('background-color: green;color: white;')
#         greenButton.clicked.connect(self.greenButtonpressed)
#         buttonBox.addWidget(greenButton)

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

#     def greenButtonpressed(self):
#         print('green button clicked')
#         self.var = 'green'

#     def redButtonpressed(self):
#         print('Red button clicked')
#         self.var = 'red'

#     def yellowButtonpressed(self):
#         print('Yellow button clicked')
#         self.var = 'yellow'

#     def offButtonpressed(self):
#         print('Off button clicked')

#     def sliderValueChanged(self, value):
#         frequency = value / 10
#         self.sliderLabel.setText(f'Frequency: {frequency:.1f} Hz')
#         print(f'Frequency: {frequency:.1f} Hz')

#     def offButtonpressed_with_param(self,param):
#         print(param)

# app = QApplication(sys.argv)
# mw = MainWindow()
# sys.exit(app.exec_())
#### above is the working class that I want to make into the class structure for using UDP!
import socket
import time
import secrets


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel
)
from PyQt5.QtCore import Qt
# # Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.1.32', 12345)  # Adjust IP address and port as needed
 
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.var = 'yellow'
        self.varOld = 'red'
        ## deleted all the window since it is inherited
        self.setWindowTitle('My very own Widget')
        self.setGeometry(100, 100, 800, 600)

        widgetBox = QVBoxLayout() ##here i create a vertical layout for the widget
        buttonBox = QHBoxLayout() ## Here i create a horizontal layout for the buttons

        # green Button
        greenButton = QPushButton('green Button')
        greenButton.setStyleSheet('background-color: green;color: white;')
        greenButton.clicked.connect(self.greenButtonpressed)
        buttonBox.addWidget(greenButton)

        # Red Button
        redButton = QPushButton('Red Button')
        redButton.setStyleSheet('background-color: red;color: white')
        redButton.clicked.connect(self.redButtonpressed)
        buttonBox.addWidget(redButton)

        # Yellow Button
        yellowButton = QPushButton('Yellow Button')
        yellowButton.setStyleSheet('background-color: yellow; color: magenta')
        yellowButton.clicked.connect(self.yellowButtonpressed)
        buttonBox.addWidget(yellowButton)

        # Off Button
        self.offButton = QPushButton('Off Button')
        self.offButton.setStyleSheet('background-color: green; color: black')
        # self.offButton.clicked.connect(self.offButtonpressed) ## this command works fine. tried to use lambda anonymous function instead below
        # self.offButton.clicked.connect(lambda  self.offButtonpressed())  ### does not work:  This calls the method immediately (because of the parentheses), instead of passing a function reference.
# Also, the syntax is invalid: lambda self.offButtonpressed() looks like you're trying to define the lambda’s argument as a function call, which isn’t allowed.
        
        # self.offButton.clicked.connect(self.offButtonpressed)## this works the same as without any lambda function but allows more flexibililty,for example to log something or pass parameters!
        self.offButton.clicked.connect(lambda : self.offButtonpressed())## this works the same as without any lambda function but allows more flexibililty,for example to log something or pass parameters!
        self.offButton.clicked.connect(lambda: self.offButtonpressed())## this works the same as without any lambda function but allows more flexibililty,for example to log something or pass parameters!
        # self.offButton.clicked.connect(lambda: self.offButtonpressed_with_param("Turning off"))


        
        buttonBox.addWidget(self.offButton)

        widgetBox.addLayout(buttonBox) ## here i add the buttonBOx to the widgetBox

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

    def greenButtonpressed(self):
        print('green button clicked')
        self.var = 'green'
        client_socket.sendto(self.var.encode(), server_address)
        data, addr = client_socket.recvfrom(1024)
        print('Received data:', data.decode())
        return self.var

    def redButtonpressed(self):
        print('Red button clicked')
        self.var = 'red'
        client_socket.sendto(self.var.encode(), server_address)
        data, addr = client_socket.recvfrom(1024)
        print('Received data:', data.decode())
        return self.var

    def yellowButtonpressed(self):
        print('Yellow button clicked')
        self.var = 'yellow'
        client_socket.sendto(self.var.encode(), server_address)
        data, addr = client_socket.recvfrom(1024)
        print('Received data:', data.decode())
        return self.var

    def offButtonpressed(self):
        print('Off button clicked')
        self.var = 'off'
        client_socket.sendto(self.var.encode(), server_address)
        data, addr = client_socket.recvfrom(1024)
        print('Received data:', data.decode())
        return self.var

    def sliderValueChanged(self, value):
        frequency = value / 10
        self.sliderLabel.setText(f'Frequency: {frequency:.1f} Hz')
        print(f'Frequency: {frequency:.1f} Hz')

    def offButtonpressed_with_param(self,param):
        print(param)

app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())