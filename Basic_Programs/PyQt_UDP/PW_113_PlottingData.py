'''
how Live Data can be plotted using a PyQt window. Our eventual goal is to bring in live data from the Raspberry Pi Pico W using UDP over WiFi, but to learn the concepts today, we will be generating a live sin wave to show how the plotting works. Here is the code we developed in this lesson:


'''
import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
 
numPoints = 200
xStart = 0
xStop = 4*np.pi
 
frequency = 1
Inc = (2*np.pi/numPoints)
 
count=0
incR=1
incG=2
 
x=np.linspace(xStart,xStop,numPoints)
ySin=np.sin(frequency*x)
ySin2 = np.sin(frequency*x + 2*np.pi/3)
ySin3 = np.sin(frequency*x + 4*np.pi/3)
 
def updatePlot():
    global numPoint,xStart,xStop,Inc,frequency,count
    xStart=xStart + Inc
    xStop=xStop + Inc
    x =np.linspace(xStart, xStop , numPoints)
    ySin=np.sin(frequency*x+count*incR/100*frequency)
    ySin2 = np.sin(frequency*x + 2*np.pi/3+count*incG/100*frequency)
    ySin3 = np.sin(frequency*x + 4*np.pi/3)
    
    plotSin.setData(x, ySin)
    plotSin2.setData(x, ySin2)
    plotSin3.setData(x, ySin3)
    
    count=count+1
 
def updateFrequency(value):
    global frequency, sliderLabel
    frequency = value/10
    sliderLabel.setText("Frequency: "+str(frequency)+" Hz")
 
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
graphWidget.setYRange(-1.25,1.25)
 
timer = QTimer()
timer.timeout.connect(updatePlot)
timer.start(100)
 
window.setLayout(layout)
window.show()
sys.exit(app.exec_())