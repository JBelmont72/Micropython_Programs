'''
improve PW_114 project by making the PyQt widget more virtual. The PyQt widget generates 3 sine waves, one for the Red color channel, one for the Green color channel, and one for the Blue color channel. The three sine waves are displayed on the widget. You are then given the opportunity in the widget to scale any of the three color channels. This allows you to calibrate your RGB LED in case any color channel is dominating. The widget also features a “Chase” mode where you can introduce phase injection into any of the color channels. This causes one or more of the color channels to “chase” the other ones. In this version, we preserve the phase as we turn the chase mode on or off. We also add buttons at the bottom of the widget to show the composite color being generated, as well as the individual R, G, and B color channels. This is the circuit schematic we are using on the Pi Pico side.

'''
## server on pico
import network
import usocket as socket
import secrets
import time
from machine import Pin,PWM
 
redLED=PWM(Pin(20))
greenLED=PWM(Pin(19))
blueLED=PWM(Pin(18))
 
redLED.freq(1000)
greenLED.freq(1000)
blueLED.freq(1000)
 
# Set up WiFi connection
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
print(secrets.SSID,secrets.PASSWORD)
wlan.connect(secrets.SSID,secrets.PASSWORD)
 
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
####~~~~~~~ Client side PyQt
import sys
import socket
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('192.168.88.71',12345)
client_socket.settimeout(1.0)
 
numPoints = 200
xStart = 0
xStop = 4*np.pi
frequency = 1
Inc = (2*np.pi/numPoints)
chaseMode = False
 
phaseR=0
phaseG=2*np.pi/3
phaseB=4*np.pi/3
 
incR=0
incG=.5
incB=1
 
ampR=1
ampG=1
ampB=1
 
x=np.linspace(xStart,xStop,numPoints)
ySin=255*np.sin(frequency*x)/2 + 255/2
ySin2 = 255*np.sin(frequency*x + 2*np.pi/3)/2+255/2
ySin3 = 255*np.sin(frequency*x + 4*np.pi/3)/2+255/2
 
def updatePlot():
    global numPoints,xStart,xStop,Inc,frequency,phaseR,phaseG,phaseB,incR,incG,incB,ampR,ampG,ampB
    xStart=xStart + Inc
    xStop=xStop + Inc
    x =np.linspace(xStart, xStop , numPoints)
    if chaseMode:
        phaseR=(phaseR+incR*Inc)
        phaseG=(phaseG+incG*Inc)
        phaseB=(phaseB+incB*Inc)
    
    ySin=(255*np.sin(frequency*x+phaseR)/2+255/2)*ampR
    ySin2 = (255*np.sin(frequency*x + phaseG)/2+255/2)*ampG
    ySin3 = (255*np.sin(frequency*x + phaseB)/2+255/2)*ampB
    
    plotSin.setData(x, ySin)
    plotSin2.setData(x, ySin2)
    plotSin3.setData(x, ySin3)
    
    currentRed=int(ySin[numPoints-1])
    currentGreen=int(ySin2[numPoints-1])
    currentBlue=int(ySin3[numPoints-1])
    
    compositeColor=QColor(currentRed,currentGreen,currentBlue)
    compositeButton.setStyleSheet("background-color: "+compositeColor.name()+"; border-radius: 50px; min-width: 100px; min-height: 100px; font-size: 20px; color: white;")
    redButton.setStyleSheet("background-color: rgb("+str(currentRed)+ ",0,0); border-radius: 50px; min-width: 100px; min-height: 100px; font-size: 20px; color: white;")
    greenButton.setStyleSheet("background-color: rgb(0,"+str(currentGreen)+ ",0); border-radius: 50px; min-width: 100px; min-height: 100px; font-size: 20px; color: white;")
    blueButton.setStyleSheet("background-color: rgb(0,0,"+str(currentBlue)+ "); border-radius: 50px; min-width: 100px; min-height: 100px; font-size: 20px; color: white;")
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
    global chaseMode
    if state:
        chaseMode=True
    if not state:
        chaseMode=False
 
app=QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("The Magic of Sin Waves")
window.setGeometry(100,100,800,600)
mainLayout = QHBoxLayout(window)
leftLayout = QVBoxLayout()
rightLayout = QVBoxLayout()
 
def updateAmplitudeRed(value):
    global ampR
    ampR = value/100
    
def updateAmplitudeGreen(value):
    global ampG
    ampG = value/100
    
def updateAmplitudeBlue(value):
    global ampB
    ampB = value/100
 
for color,label in [['red','RED'],['green','GREEN'],['blue','BLUE']]:
    labelWidget=QLabel(label)
    labelWidget.setStyleSheet("color: "+color+";font-size:20px;")
    leftLayout.addWidget(labelWidget)
    
    slider=QSlider(Qt.Vertical)
    slider.setMinimum(0)
    slider.setMaximum(100)
    slider.setValue(100)
    slider.setStyleSheet("Qslider::handle:vertical{background-color: " + color+";}")
    
    if color=='red':
        slider.valueChanged.connect(updateAmplitudeRed)
    if color=='green':
        slider.valueChanged.connect(updateAmplitudeGreen)
    if color=='blue':
        slider.valueChanged.connect(updateAmplitudeBlue)
    
    leftLayout.addWidget(slider)
 
sliderLabel=QLabel("Frequency: 1 Hz")
sliderLabel.setStyleSheet("font-size: 40px;")
rightLayout.addWidget(sliderLabel)
 
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(40)
slider.setValue(10)
slider.valueChanged.connect(updateFrequency)
rightLayout.addWidget(slider)
 
graphWidget =pg.PlotWidget()
plotSin=graphWidget.plot(x,ySin,pen=pg.mkPen('r',width=4))
plotSin2=graphWidget.plot(x,ySin2,pen=pg.mkPen('g',width=4))
plotSin3=graphWidget.plot(x,ySin3,pen=pg.mkPen('b',width=4))
graphWidget.setYRange(-10,265)
rightLayout.addWidget(graphWidget)
 
toggleButton=QCheckBox("Chase Mode")
toggleButton.stateChanged.connect(toggleChase)
rightLayout.addWidget(toggleButton)
 
buttonLayout=QHBoxLayout()
compositeButton=QPushButton("RGB")
redButton=QPushButton("Red")
greenButton=QPushButton("Green")
blueButton=QPushButton("Blue")
 
for button in [compositeButton,redButton,greenButton,blueButton]:
    button.setFixedSize(100,100)
    buttonLayout.addWidget(button)
 
rightLayout.addLayout(buttonLayout)
 
timer = QTimer()
timer.timeout.connect(updatePlot)
timer.start(100)
 
mainLayout.addLayout(leftLayout)
mainLayout.addLayout(rightLayout)
 
 
window.setLayout(mainLayout)
window.show()
sys.exit(app.exec_())
