'''
 Create a PyQt Window which  used 3 Sine Waves offset from each other by (2*Pi/). By offsetting the Sine Waves each by this amount creates 3 waves perfectly spaced across the domain. We then use the values from these sine waves to create the Red, Green and Blue values for the HSV color wheel. The x axis represents angle, in radians. Then the values of the sine wave represent the corresponding Red, Green, and Blue values. The program graphs the three waves on the PyQt widget, then passes the data via UDP over WiFi to the Pi Pico. The Pico then applies the values to the RGB LED.  We save the server side program on the Pi Pico as main.py, and power the project with the Breadboard Power Bank, meaning the Pi operates remote and untethered, and the LED is controlled by the desktop client software. This is a schematic of the Pi Pico circuit for the project.
This project has a server running on the Raspberry Pi Pico, and a Client running on your desktop PC. First-  is the code for the server side for the Pi Pico.
'''
import network
import usocket as socket
import secrets
import time
from machine import Pin,PWM
## This code for the server which is the pico 
redLED=PWM(Pin(20))
greenLED=PWM(Pin(19))
blueLED=PWM(Pin(18))
 
redLED.freq(1000)
greenLED.freq(1000)
blueLED.freq(1000)
 
# Set up WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print(secrets.ssid_loft,secrets.password_loft)
wlan.connect(secrets.ssid_loft,secrets.password_loft)
# print(secrets.SSID,secrets.PASSWORD)
# wlan.connect(secrets.SSID,secrets.PASSWORD)
 
# Wait for connection
while not wlan.isconnected():
    time.sleep(1)
print("Connection Completed")
print('WiFi connected')
print(wlan.ifconfig())
 
# Set up UDP server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((wlan.ifconfig()[0], 12345))
print("Server is Up and Listening")
print(wlan.ifconfig()[0])
 
while True:
    print('Waiting for a request from the client...')
    # Receive request from client
    myColor, client_address = server_socket.recvfrom(1024)
    myColor=myColor.decode()
    print("Client Request:",myColor)
    print("FROM CLIENT",client_address)
    colorArray=myColor.split(',')
    r=int(colorArray[0])
    g=int(colorArray[1])
    b=int(colorArray[2])
    print(r,g,b)
    redLED.duty_u16(int((r/255)*65535))
    greenLED.duty_u16(int((g/255)*65535))
    blueLED.duty_u16(int((b/255)*65535))
    print("Client Request: ",myColor)
    print("From Client",client_address)
    data="LED "+myColor+" executed"
    server_socket.sendto(data.encode(), client_address)
    print("Data Sent")
######~~~~~~~~below is the python code for the browser
import sys
import socket
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.88.71',12345)
client_socket.settimeout(1.0)
 
numPoints = 200
xStart = 0
xStop = 4*np.pi
 
frequency = 1
Inc = (2*np.pi/numPoints)
 
count=0
incR=0
incG=0
 
x=np.linspace(xStart,xStop,numPoints)
ySin=255*np.sin(frequency*x)/2 + 255/2
ySin2 = 255*np.sin(frequency*x + 2*np.pi/3)/2+255/2
ySin3 = 255*np.sin(frequency*x + 4*np.pi/3)/2+255/2
 
def updatePlot():
    global numPoint,xStart,xStop,Inc,frequency,count
    xStart=xStart + Inc
    xStop=xStop + Inc
    x =np.linspace(xStart, xStop , numPoints)
    ySin=255*np.sin(frequency*x+count*incR/100*frequency)/2+255/2
    ySin2 = 255*np.sin(frequency*x + 2*np.pi/3+count*incG/100*frequency)/2+255/2
    ySin3 = 255*np.sin(frequency*x + 4*np.pi/3)/2+255/2
    
    plotSin.setData(x, ySin)
    plotSin2.setData(x, ySin2)
    plotSin3.setData(x, ySin3)
    
    count=count+1
    
    myColor=str(int(ySin[numPoints-1]))+","+str(int(ySin2[numPoints-1]))+","+str(int(ySin3[numPoints-1]))
    client_socket.sendto(myColor.encode(),server_address)
    try:
        data, addr =client_socket.recvfrom(1024)
        print('Received data: ',data.decode())
    except socket.timeout:
        print("Request timed out. No Response from Server")
    except Exception as e:
        print("An Error Occured")
def updateFrequency(value):
    global frequency, sliderLabel
    frequency = value/10
    sliderLabel.setText("Frequency: "+str(frequency)+" Hz")
def toggleChase(state):
    global incR,incG
    if state==0:
        incR=0
        incG=0
    if state==2:
        incR=1
        incG=2
 
app=QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("The Magic of Sin Waves")
window.setGeometry(100,100,800,600)
layout = QVBoxLayout(window)
 
sliderLabel=QLabel("Frequency: 1 Hz")
sliderLabel.setStyleSheet("font-size: 40px;")
layout.addWidget(sliderLabel)
 
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(40)
slider.setValue(10)
slider.valueChanged.connect(updateFrequency)
layout.addWidget(slider)
 
graphWidget =pg.PlotWidget()
layout.addWidget(graphWidget)
plotSin=graphWidget.plot(x,ySin,pen=pg.mkPen('r',width=4))
plotSin2=graphWidget.plot(x,ySin2,pen=pg.mkPen('g',width=4))
plotSin3=graphWidget.plot(x,ySin3,pen=pg.mkPen('b',width=4))
graphWidget.setYRange(-10,265)
 
toggleButton=QCheckBox("Chase Mode")
toggleButton.stateChanged.connect(toggleChase)
layout.addWidget(toggleButton)
 
timer = QTimer()
timer.timeout.connect(updatePlot)
timer.start(100)
 
window.setLayout(layout)
window.show()
sys.exit(app.exec_())