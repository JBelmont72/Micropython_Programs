'''
In this video lesson I will show you how you can control a remote DC motor using your  Raspberry Pi Pico W. The Pi Pico is set up as a server, and is connected to a DC motor, and TA6586 Motor Controller. The motor is controlled by a client Python program running on your  desktop PC. On the client side we create a Graphical Widget, which will allow you to control both the speed and direction of the motor. the schematic for the Raspberry Pi Pico W side is shown below:

'''
# # server on pico
# import network
# import usocket as socket
# # import secrets
# import time
# from machine import Pin, PWM
# icPin1=Pin(16,Pin.OUT)
# icPin2=Pin(17,Pin.OUT)
# fPWM=PWM(icPin1)
# rPWM=PWM(icPin2)
# fPWM.freq(1000)
# rPWM.freq(1000)
 
# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48','waterypanda901')
# # wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')
# print(wlan.ifconfig())
 
# Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
 
# while True:
#     print('Waiting for a request from the client...')
#     # Receive request from client
#     request, client_address = server_socket.recvfrom(1024)
#     request=request.decode()
#     print("Client Request:",request)
#     print("FROM CLIENT",client_address)
#     cmdArray=request.split(',')
#     motorState=cmdArray[0]
#     speed=int(cmdArray[1])
#     rPWM.duty_u16(0)
#     fPWM.duty_u16(0)
#     if motorState == 'O':
#         rPWM.duty_u16(0)
#         fPWM.duty_u16(0)
#     if motorState == 'F':
#         rPWM.duty_u16(0)
#         fPWM.duty_u16(int(speed/100*65535))
#     if motorState == 'R':
#         fPWM.duty_u16(0)
#         rPWM.duty_u16(int(speed/100*65535))
#     # String to send
#     data =request +" CMD PROCESSES+D"
    
#     # Send data to client
#     server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
 
# server on pico
# import network
# import usocket as socket
# # import secrets
# from machine import Pin,PWM
# import time
# ##left motor
# icPin1=Pin(20,Pin.OUT)
# icPin2=Pin(19,Pin.OUT)
# # icPin1=Pin(14,Pin.OUT)
# # icPin2=Pin(15,Pin.OUT)
# fPWM=PWM(icPin1)
# rPWM=PWM(icPin2)
# fPWM.freq(1000)
# rPWM.freq(1000)
# ## right motor
# RicPin1=Pin(6,Pin.OUT)
# RicPin2=Pin(7,Pin.OUT)
# # icPin1=Pin(14,Pin.OUT)
# # icPin2=Pin(15,Pin.OUT)
# RfPWM=PWM(RicPin1)
# RrPWM=PWM(RicPin2)
# RfPWM.freq(1000)
# RrPWM.freq(1000)

# wlan = network.WLAN(network.STA_IF)
# wlan.active(True)
# wlan.connect('NETGEAR48','waterypanda901')
# # wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# # Wait for connection
# while not wlan.isconnected():
#     time.sleep(1)
# print("Connection Completed")
# print('WiFi connected')
# print(wlan.ifconfig())
 
# ##Set up UDP server
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_socket.bind((wlan.ifconfig()[0], 12345))
# print("Server is Up and Listening")
 
# while True:
#     print('Waiting for a request from the client...')
#     # Receive request from client
#     request, client_address = server_socket.recvfrom(1024)
#     request=request.decode()
#     print("Client Request:",request)
#     print("FROM CLIENT",client_address)
#     cmdArray=request.split(',')
#     motorState=cmdArray[0]
#     speed=int(cmdArray[1])
#     rPWM.duty_u16(0)
#     fPWM.duty_u16(0)
#     RrPWM.duty_u16(0)
#     RfPWM.duty_u16(0)
#     if motorState == 'O':
#         rPWM.duty_u16(0)
#         fPWM.duty_u16(0)
#         RrPWM.duty_u16(0)
#         RfPWM.duty_u16(0)
#     if motorState == 'F':
#         rPWM.duty_u16(0)
#         fPWM.duty_u16(int(speed/100*65535))
#         RrPWM.duty_u16(0)
#         RfPWM.duty_u16(int(speed/100*65535))
#     if motorState == 'R':
#         fPWM.duty_u16(0)
#         rPWM.duty_u16(int(speed/100*65535))
#         RfPWM.duty_u16(0)
#         RrPWM.duty_u16(int(speed/100*65535))
#     # String to send
#     data =request +" CMD PROCESSES+D"
    
#     # Send data to client
#     server_socket.sendto(data.encode(), client_address)
#     print(f'Sent data to {client_address}')
    
#     # Optional: Pause for a short period to prevent overwhelming the client
#     time.sleep(1)
 
 # client side
import socket
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
speedF=0
speedR=0
motorStatus='O'
 
# Set up UDP client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1)
server_address = ('192.168.1.25', 12345)  # Adjust IP address and port as needed
 
app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle("Big Boss Motor Controller")
window.setGeometry(100,100,800,600)
mainLayout=QHBoxLayout(window)
leftLayout=QVBoxLayout()
rightLayout=QVBoxLayout()
 
def updateMotor():
    global motorStatus,speedF,speedR
    try:
        print(motorStatus)
        if motorStatus=='F':
            cmd=motorStatus+','+str(speedF)
        if motorStatus=='R':
            cmd=motorStatus+','+str(speedR)
        if motorStatus=='O':
            cmd=motorStatus+','+str(0)
 
        client_socket.sendto(cmd.encode(), server_address)
        data, addr = client_socket.recvfrom(1024)
        print('Received data:', data.decode())
        
    except:
        print("Server Did Not Respond, Try Again")
 
 
def updateForSpeed(value):
    global speedF
    speedF=value
    print(speedF)
def updateRevSpeed(value):
    global speedR
    speedR=value
    print(speedR)
def motorGo():
    global motorStatus
    motorStatus = 'F'
    print("GO")
def motorRev():
    global motorStatus
    motorStatus = 'R'
    print("REV")
def motorStop():
    global motorStatus
    motorStatus = 'O'
    print("STOP")
 
 
sliderLabelF=QLabel("Forward Speed")
sliderLabelF.setStyleSheet("font-size: 20px;")
leftLayout.addWidget(sliderLabelF)
 
sliderF=QSlider(Qt.Vertical)
sliderF.setMinimum(0)
sliderF.setMaximum(100)
sliderF.setValue(0)
sliderF.valueChanged.connect(updateForSpeed)
sliderF.setStyleSheet("QSlider::handle:vertical {background-color: rgb(0,255,0);}")
leftLayout.addWidget(sliderF)
 
sliderLabelR=QLabel("Forward Speed")
sliderLabelR.setStyleSheet("font-size: 20px;")
leftLayout.addWidget(sliderLabelR)
 
sliderR=QSlider(Qt.Vertical)
sliderR.setMinimum(0)
sliderR.setMaximum(100)
sliderR.setValue(0)
sliderR.valueChanged.connect(updateRevSpeed)
sliderR.setStyleSheet("QSlider::handle:vertical {background-color: rgb(0,0,255);}")
leftLayout.addWidget(sliderR)
 
greenButton=QPushButton("GO")
greenButton.setStyleSheet("background-color: rgb(0,255,0); border-radius: 50px; min-height: 100px; font-size: 20px; color: black;")
blueButton=QPushButton("REVERSE")
blueButton.setStyleSheet("background-color: rgb(0,0,255); border-radius: 50px; min-height: 100px; font-size: 20px; color: white;")
redButton=QPushButton("STOP")
redButton.setStyleSheet("background-color: rgb(255,0,0); border-radius: 50px; min-height: 100px; font-size: 20px; color: black;")
 
greenButton.clicked.connect(motorGo)
rightLayout.addWidget(greenButton)
 
blueButton.clicked.connect(motorRev)
rightLayout.addWidget(blueButton)
 
redButton.clicked.connect(motorStop)
rightLayout.addWidget(redButton)
 
timer =QTimer()
timer.timeout.connect(updateMotor)
timer.start(200)
 
mainLayout.addLayout(leftLayout)
mainLayout.addLayout(rightLayout)
window.setLayout(mainLayout)
window.show()
sys.exit(app.exec_())