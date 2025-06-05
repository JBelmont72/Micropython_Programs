''' Pw 113 Plotting Data
first is a functional version, second is a QWidget class-based version,the third is a QMainWindow class-based version
Shows Live Data can be plotted using a PyQt window. Our eventual goal is to bring in live data from the Raspberry Pi Pico W using UDP over WiFi, but to learn the concepts today, we will be generating a live sin wave to show how the plotting works. Here is the code we developed in this lesson:
'''
#  PW 113 Plotting Data
# This code is a simple PyQt5 application that plots sine waves with adjustable frequency using the PyQtGraph library. The application features a slider to control the frequency of the sine waves and updates the plot in real-time.
# The code is structured into two main parts: the first part is a functional version, and the second part is a class-based version. The class-based version is more organized and allows for easier expansion in the future.
# The first part of the code creates a simple PyQt5 application that plots three sine waves with different phases. The frequency of the sine waves can be adjusted using a slider. The application uses the PyQtGraph library for plotting and updates the plot in real-time using a timer.
# The second part of the code is a more advanced version that uses classes to encapsulate the functionality. This version is more structured and allows for easier expansion in the future. It also includes better organization of the code and improved readability.
#  The use of global variables in the first part is replaced with instance variables in the class-based version, improving encapsulation and reducing potential issues with variable scope.
 
# import sys
# import numpy as np
# import pyqtgraph as pg
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
 
# numPoints = 200
# xStart = 0
# xStop = 4*np.pi
 
# frequency = 1
# Inc = (2*np.pi/numPoints)
 
# count=0
# incR=1
# incG=2
 
# x=np.linspace(xStart,xStop,numPoints)
# ySin=np.sin(frequency*x)
# ySin2 = np.sin(frequency*x + 2*np.pi/3)
# ySin3 = np.sin(frequency*x + 4*np.pi/3)
 
# def updatePlot():
#     global numPoint,xStart,xStop,Inc,frequency,count
#     xStart=xStart + Inc
#     xStop=xStop + Inc
#     x =np.linspace(xStart, xStop , numPoints)
#     ySin=np.sin(frequency*x+count*incR/100*frequency)
#     ySin2 = np.sin(frequency*x + 2*np.pi/3+count*incG/100*frequency)
#     ySin3 = np.sin(frequency*x + 4*np.pi/3)
    
#     plotSin.setData(x, ySin)
#     plotSin2.setData(x, ySin2)
#     plotSin3.setData(x, ySin3)
    
#     count=count+1
 
# def updateFrequency(value):
#     global frequency, sliderLabel
#     frequency = value/10
#     sliderLabel.setText("Frequency: "+str(frequency)+" Hz")
 
# app=QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle("The Magic of Sin Waves")
# window.setGeometry(100,100,800,600)
# layout = QVBoxLayout(window)
 
# sliderLabel=QLabel("Frequency: 1 Hz")
# sliderLabel.setStyleSheet("font-size: 40px;")
# layout.addWidget(sliderLabel)
 
# slider = QSlider(Qt.Horizontal)
# slider.setMinimum(1)
# slider.setMaximum(40)
# slider.setValue(10)
# slider.valueChanged.connect(updateFrequency)
# layout.addWidget(slider)
 
# graphWidget =pg.PlotWidget()
# layout.addWidget(graphWidget)
# plotSin=graphWidget.plot(x,ySin,pen=pg.mkPen('r',width=4))
# plotSin2=graphWidget.plot(x,ySin2,pen=pg.mkPen('g',width=4))
# plotSin3=graphWidget.plot(x,ySin3,pen=pg.mkPen('b',width=4))
# graphWidget.setYRange(-1.25,1.25)
 
# timer = QTimer()
# timer.timeout.connect(updatePlot)
# timer.start(100)
 
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())
###############
# The code below is a more advanced version of the above code, using classes and PyQt5
# and PyQtGraph. It is a more structured approach to creating the same functionality, with the added benefit of being able to easily add more features in the future.
#
import sys
import numpy as np
import pyqtgraph as pg
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Magic of Sin Waves")
        self.setGeometry(100, 100, 800, 600)

        # Parameters
        self.numPoints = 200
        self.xStart = 0
        self.xStop = 4 * np.pi
        self.frequency = 1
        self.Inc = (2 * np.pi / self.numPoints)
        self.count = 0
        self.incR = 1
        self.incG = 2

        # Layout
        self.layout = qtw.QVBoxLayout(self)## establish the main layout
        self.setLayout(self.layout)## set it to the main layout

        # Frequency label
        self.sliderLabel = qtw.QLabel("Frequency: 1.0 Hz")
        self.sliderLabel.setStyleSheet("font-size: 40px;")
        self.layout.addWidget(self.sliderLabel)

        # Slider
        self.slider = qtw.QSlider(qtc.Qt.Horizontal)
        self.slider.setMinimum(1)
        self.slider.setMaximum(40)
        self.slider.setValue(10)
        self.slider.valueChanged.connect(self.updateFrequency)
        self.layout.addWidget(self.slider)

        # Plotting
        self.graphWidget = pg.PlotWidget()
        self.layout.addWidget(self.graphWidget)
        self.graphWidget.setYRange(-1.25, 1.25)

        # Initial plot data
        self.x = np.linspace(self.xStart, self.xStop, self.numPoints)
        self.ySin = np.sin(self.frequency * self.x)
        self.ySin2 = np.sin(self.frequency * self.x + 2 * np.pi / 3)
        self.ySin3 = np.sin(self.frequency * self.x + 4 * np.pi / 3)

        # Create plots
        self.plotSin = self.graphWidget.plot(self.x, self.ySin, pen=pg.mkPen('r', width=4))
        self.plotSin2 = self.graphWidget.plot(self.x, self.ySin2, pen=pg.mkPen('g', width=4))
        self.plotSin3 = self.graphWidget.plot(self.x, self.ySin3, pen=pg.mkPen('b', width=4))

        # Timer
        self.timer = qtc.QTimer()
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(100)

        self.show()

    def updatePlot(self):
        self.xStart += self.Inc
        self.xStop += self.Inc
        self.x = np.linspace(self.xStart, self.xStop, self.numPoints)

        self.ySin = np.sin(self.frequency * self.x + self.count * self.incR / 100 * self.frequency)
        self.ySin2 = np.sin(self.frequency * self.x + 2 * np.pi / 3 + self.count * self.incG / 100 * self.frequency)
        self.ySin3 = np.sin(self.frequency * self.x + 4 * np.pi / 3)

        self.plotSin.setData(self.x, self.ySin)
        self.plotSin2.setData(self.x, self.ySin2)
        self.plotSin3.setData(self.x, self.ySin3)

        self.count += 1

    def updateFrequency(self, value):
        self.frequency = value / 10
        self.sliderLabel.setText(f"Frequency: {self.frequency:.1f} Hz")

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
# #  PW 113 Plotting Data
# # This code is a simple PyQt5 application that plots sine waves with adjustable frequency using the PyQtGraph library. The application features a slider to control the frequency of the sine waves and updates the plot in real-time.
# # The code is structured into two main parts: the first part is a functional version, and the second part is a class-based version. The class-based version is more organized and allows for easier expansion in the future.
# # Used QMainWindow  instead of QWidget
# import sys
# import numpy as np
# import pyqtgraph as pg
# from PyQt5.QtWidgets import (
#     QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider
# )
# from PyQt5.QtCore import Qt, QTimer

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("The Magic of Sin Waves")
#         self.setGeometry(100, 100, 800, 600)

#         # Central widget and layout
#         self.centralWidget = QWidget()
#         self.setCentralWidget(self.centralWidget)
#         self.layout = QVBoxLayout(self.centralWidget)

#         # Add label
#         self.sliderLabel = QLabel("Frequency: 1 Hz")
#         self.sliderLabel.setStyleSheet("font-size: 40px;")
#         self.layout.addWidget(self.sliderLabel)

#         # Add slider
#         self.slider = QSlider(Qt.Horizontal)
#         self.slider.setMinimum(1)
#         self.slider.setMaximum(40)
#         self.slider.setValue(10)
#         self.slider.valueChanged.connect(self.updateFrequency)
#         self.layout.addWidget(self.slider)

#         # Add graph
#         self.graphWidget = pg.PlotWidget()
#         self.layout.addWidget(self.graphWidget)

#         self.plotSin = self.graphWidget.plot(pen=pg.mkPen('r', width=4))
#         self.plotSin2 = self.graphWidget.plot(pen=pg.mkPen('g', width=4))
#         self.plotSin3 = self.graphWidget.plot(pen=pg.mkPen('b', width=4))
#         self.graphWidget.setYRange(-1.25, 1.25)

#         # Data setup
#         self.numPoints = 200
#         self.xStart = 0
#         self.xStop = 4 * np.pi
#         self.frequency = 1
#         self.Inc = (2 * np.pi / self.numPoints)
#         self.count = 0
#         self.incR = 1
#         self.incG = 2

#         self.x = np.linspace(self.xStart, self.xStop, self.numPoints)

#         # Start timer
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.updatePlot)
#         self.timer.start(100)

#     def updatePlot(self):
#         self.xStart += self.Inc
#         self.xStop += self.Inc
#         x = np.linspace(self.xStart, self.xStop, self.numPoints)
#         ySin = np.sin(self.frequency * x + self.count * self.incR / 100 * self.frequency)
#         ySin2 = np.sin(self.frequency * x + 2 * np.pi / 3 + self.count * self.incG / 100 * self.frequency)
#         ySin3 = np.sin(self.frequency * x + 4 * np.pi / 3)

#         self.plotSin.setData(x, ySin)
#         self.plotSin2.setData(x, ySin2)
#         self.plotSin3.setData(x, ySin3)
#         self.count += 1

#     def updateFrequency(self, value):
#         self.frequency = value / 10
#         self.sliderLabel.setText(f"Frequency: {self.frequency:.1f} Hz")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
