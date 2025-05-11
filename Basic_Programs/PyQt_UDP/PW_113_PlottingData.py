'''PW_113.py
This program demonstrates how to plot live data using PyQt and pyqtgraph.
We will be using a QTimer to update the plot at regular intervals. The plot will show a sine wave, and we will be able to change the frequency of the sine wave using a QSlider. The QSlider will emit a signal when its value changes, and we will connect this signal to a slot that updates the frequency of the sine wave.
We will also be using a QLabel to display the current frequency of the sine wave. The QLabel will be updated whenever the QSlider value changes. We will use a QVBoxLayout to arrange the widgets vertically, and we will set the layout for the main window.
We will also be using a QHBoxLayout to arrange the widgets horizontally. We will add a QSlider, a QLabel, and a QVBoxLayout to the main window. The QVBoxLayout will contain the graph widget, which will be used to plot the sine wave. We will use pyqtgraph to create the graph widget and plot the sine wave.
We will also be using a QTimer to update the plot at regular intervals. The QTimer will emit a signal when its timeout occurs, and we will connect this signal to a slot that updates the plot. The QTimer will be started with a timeout interval of 100 milliseconds.
We will also be using a QSlider to change the frequency of the sine wave. The QSlider will emit a signal when its value changes, and we will connect this signal to a slot that updates the frequency of the sine wave. The QSlider will be set to a range of 1 to 40, and its initial value will be set to 10. The frequency of the sine wave will be calculated by dividing the value of the QSlider by 10.
Show Live Data can be plotted using a PyQt window. Our eventual goal is to bring in live data from the Raspberry Pi Pico W using UDP over WiFi, but to learn the concepts today, we will be generating a live sin wave to show how the plotting works. Here is the code we developed in this lesson:
to process live data from the UDP server. The UDP server will be running on the Raspberry Pi Pico W, and the client will be running on the computer. The client will send color commands to the server when buttons are pressed. The server will control the state of three LEDs (green, yellow, and red) based on the received color command.
#         self.offButton.setStyleSheet('background-color: black; color: white')
#         self.offButton.clicked.connect(self.offButtonpressed)
#         buttonBox.addWidget(self.offButton)
we will need numpy and pyqtgraph to plot the data. Pyqtgraph is a pure-python graphics library built on PyQt and numpy. It is designed to be fast, flexible, and easy to use. It is used for plotting data in real-time, and it can handle large datasets efficiently. We will also need PyQt5 to create the GUI.


'''
# import sys    ## woorking non_class version
# import numpy as np
# import pyqtgraph as pg
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
 
# numPoints = 200
# xStart = 0
# xStop = 4*np.pi # 2*pi is one full cycle of a sine wave
# ## one option to generate x is to use a for loop, but this is not efficient
# ## this is how we would use a for loop to generate x
# x=np.zeros(numPoints)
# for i in range(numPoints):
#     x[i] = xStart + i*(xStop-xStart)/numPoints
#     print(x[i])
# # print(x) 
# frequency = 1
# Inc = (2*np.pi/numPoints)
 
# count=0
# incR=1
# incG=2
 
# # x=np.linspace(xStart,xStop,numPoints) ## this is a more efficient way to generate x
# # x = np.arange(xStart, xStop, Inc) ## this is another way to generate x
# ySin=np.sin(frequency*x)
# # ySin2=np.sin(frequency*x) ## this is a phase shift of 2*pi/3, divide by 3 to get the phase shift-- green
# # ySin3=np.sin(frequency*x)
# # ySin2 = np.sin(frequency*x + 2*np.pi/3) # this is a phase shift of 2*pi/3, divide by 3 to get the phase shift-- green
# ySin3 = np.sin(frequency*x + 4*np.pi/3) # this is a phase shift of 4*pi/3
# ySin2 = np.sin(frequency*x + 2*np.pi/3+count*incG/100*frequency)
# # ySin3 = np.sin(frequency*x + 4*np.pi/3)
# # ySin2 = np.sin(frequency*x + 2*np.pi/3+count*incG/100*frequency)
# # ySin3 = np.sin(frequency*x + 4*np.pi/3)
# # ySin2 = np.sin(frequency*x + 2*np.pi/3)
 
# def updatePlot():
#     ## this function will be called every 100 milliseconds
#     global numPoint,xStart,xStop,Inc,frequency,count
#     xStart=xStart + Inc
#     xStop=xStop + Inc
#     x =np.linspace(xStart, xStop , numPoints)
#     ySin=np.sin(frequency*x+count*incR/100*frequency)###red 'count*incR/100' is the phase shift and is a fixed offset
#     ySin2 = np.sin(frequency*x + 2*np.pi/3+count*incG/100*frequency) ##green the higher the frequensy, the faster the wave moves
#     ySin3 = np.sin(frequency*x + 4*np.pi/3)###blue
#     ## green and red chase blue
#     # ysin2 = np.sin(frequency*x + 2*np.pi/3)
    
#     # ySin=np.sin(frequency*x*count)
    
#     plotSin.setData(x, ySin)
#     plotSin2.setData(x, ySin2)
#     plotSin3.setData(x, ySin3)
    
#     count=count+1## here we are incrementing the count by 1 to make the green and red sine waves move
 
# def updateFrequency(value):
#     global frequency, sliderLabel
#     frequency = value/10
#     sliderLabel.setText("Frequency: "+str(frequency)+" Hz")
 
# app=QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle("The Magic of Sine Waves")
# window.setGeometry(100,100,800,600)
# layout = QVBoxLayout(window)## create a vertical layout inside the window
# # layout.setContentsMargins(10,10,10,10)
# # layout.setSpacing(10)
# # layout.setAlignment(Qt.AlignTop)
# # layout.setAlignment(Qt.AlignLeft)
# # layout.setAlignment(Qt.AlignRight)
 
# sliderLabel=QLabel("Frequency: 1 Hz")
# sliderLabel.setStyleSheet("font-size: 60px;")
# layout.addWidget(sliderLabel)
 
# slider = QSlider(Qt.Horizontal)
# slider.setMinimum(1)## use integer values
# slider.setMaximum(40)
# slider.setValue(10)
# slider.valueChanged.connect(updateFrequency)
# layout.addWidget(slider)
 
# graphWidget =pg.PlotWidget()
# layout.addWidget(graphWidget)
# plotSin=graphWidget.plot(x,ySin,pen=pg.mkPen('r',width=4))  # mkPen is used to set the color and width of the line
# plotSin2=graphWidget.plot(x,ySin2,pen=pg.mkPen('g',width=4))
# plotSin3=graphWidget.plot(x,ySin3,pen=pg.mkPen('b',width=4))
# graphWidget.setYRange(-1.25,1.25)
 
# timer = QTimer()
# timer.timeout.connect(updatePlot)
# timer.start(100)
 
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())
############### class version below 2d version
# Revised & Fully Functional PyQt5 + PyQtGraph Class Version
# import sys
# import numpy as np
# import pyqtgraph as pg
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc


# class MainWindow(qtw.QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # --- Initialize parameters ---
#         self.numPoints = 200
#         self.xStart = 0
#         self.xStop = 4 * np.pi  # 2*pi is one full cycle of a sine wave
#         self.frequency = 1
#         self.Inc = (2 * np.pi / self.numPoints)
#         self.count = 0
#         self.incR = 1
#         self.incG = 2

#         # Generate initial x values (for loop version - not the most efficient, but shows stepwise generation)
#         self.x = np.zeros(self.numPoints)
#         for i in range(self.numPoints):
#             self.x[i] = self.xStart + i * (self.xStop - self.xStart) / self.numPoints
#             print(self.x[i])
#         # Alternative: self.x = np.linspace(self.xStart, self.xStop, self.numPoints)

#         # --- Setup UI ---
#         self.setWindowTitle("The Magic of Sine Waves")
#         self.setGeometry(100, 100, 800, 600)

#         central_widget = qtw.QWidget()
#         self.setCentralWidget(central_widget)
#         layout = qtw.QVBoxLayout(central_widget)

#         # --- Slider Label ---
#         self.sliderLabel = qtw.QLabel("Frequency: 1 Hz")
#         self.sliderLabel.setStyleSheet("font-size: 60px;")
#         layout.addWidget(self.sliderLabel)

#         # --- Frequency Slider ---
#         slider = qtw.QSlider(qtc.Qt.Horizontal)
#         slider.setMinimum(1)  # Integer values for frequency slider
#         slider.setMaximum(40)
#         slider.setValue(10)
#         slider.valueChanged.connect(self.updateFrequency)
#         layout.addWidget(slider)

#         # --- Graph Setup ---
#         self.graphWidget = pg.PlotWidget()
#         layout.addWidget(self.graphWidget)
#         ySin = np.sin(self.frequency * self.x)
#         ySin2 = np.sin(self.frequency * self.x + 2 * np.pi / 3 + self.count * self.incG / 100 * self.frequency)
#         ySin3 = np.sin(self.frequency * self.x + 4 * np.pi / 3)

#         # Store plot objects for updating
#         self.plotSin = self.graphWidget.plot(self.x, ySin, pen=pg.mkPen('r', width=4))  # Red wave
#         self.plotSin2 = self.graphWidget.plot(self.x, ySin2, pen=pg.mkPen('g', width=4))  # Green wave
#         self.plotSin3 = self.graphWidget.plot(self.x, ySin3, pen=pg.mkPen('b', width=4))  # Blue wave
#         self.graphWidget.setYRange(-1.25, 1.25)

#         # --- Timer Setup ---
#         self.timer = qtc.QTimer()
#         self.timer.timeout.connect(self.updatePlot)
#         self.timer.start(100)  # Call updatePlot every 100 milliseconds

#         self.show()

#     def updatePlot(self):
#         # Shift x window forward
#         self.xStart += self.Inc
#         self.xStop += self.Inc
#         self.x = np.linspace(self.xStart, self.xStop, self.numPoints)

#         # Compute sine wave values with phase shifts
#         ySin = np.sin(self.frequency * self.x + self.count * self.incR / 100 * self.frequency)  # Red
#         ySin2 = np.sin(self.frequency * self.x + 2 * np.pi / 3 + self.count * self.incG / 100 * self.frequency)  # Green
#         ySin3 = np.sin(self.frequency * self.x + 4 * np.pi / 3)  # Blue

#         # Update plot data
#         self.plotSin.setData(self.x, ySin)
#         self.plotSin2.setData(self.x, ySin2)
#         self.plotSin3.setData(self.x, ySin3)

#         # Increment count to animate motion
#         self.count += 1

#     def updateFrequency(self, value):
#         # Update frequency based on slider
#         self.frequency = value / 10
#         self.sliderLabel.setText(f"Frequency: {self.frequency:.1f} Hz")


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     mw = MainWindow()
#     sys.exit(app.exec_())

'''
Replaced global variables with instance variables.
Moved graph data like count, xStart, etc., into self.
Used self.plotSin instead of qtw.plotSin (which was incorrect).
Maintained your helpful comments (with slight revisions where appropriate).
Ensured all widgets and variables are instance-scoped for proper object-oriented encapsulation.
| Issue                                          | Fix                                               |
| ---------------------------------------------- | ------------------------------------------------- |
| `global` variables inside methods              | Converted to instance variables (`self`)          |
| `qtw.plotSin` used wrongly                     | Corrected to `self.plotSin`, etc.                 |
| `xStart`, `xStop`, `count` undefined in method | Moved to `self`                                   |
| `sliderLabel` out of scope                     | Stored as `self.sliderLabel`                      |
| UI layout and widget ownership                 | Properly handled with `QMainWindow` and `QWidget` |


'''
## below is the class version with animated buttons
# Revised & Fully Functional PyQt5 + PyQtGraph Class Version (With Start/Stop)
'''
Below version fully refactors second version into a clean class-based PyQt5 program that:

Uses only class attributes (no global variables).
Keeps your original comments, revised as needed.
Adds Start and Stop buttons to control the animation.
Fixes all current issues like:
Unused count being a local variable.
sliderLabel, plotSin, etc. being incorrectly referenced.
QMainWindow missing a proper central widget.
Makes the code modular and readable.


Improvements & Notes:
Global variables removed: Everything is encapsulated inside the class.
Count is now a class attribute (self.count) and properly updated.
Used QMainWindow with a proper centralWidget and layout.
Plot handles (plotSin, etc.) are stored as instance attributes, not incorrectly via qtw.plotSin.
Start/Stop buttons use animation control via QTimer.
Future enhancements could include:
A combo box to select different waveforms (sine, square, triangle),
A button to export the plot to an image/PDF,

Real-time frequency adjustments while the wave is running,
A combo box to select different waveforms (sine, square, triangle),
Export to image/PDF,
Live FFT (Fast Fourier Transform) display.

'''

import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer

class SineWavePlotter(QMainWindow):
    def __init__(self):
        super().__init__()  # initialize parent class

        self.setWindowTitle("The Magic of Sine Waves")
        self.setGeometry(100, 100, 800, 600)

        self.numPoints = 200
        self.xStart = 0
        self.xStop = 4 * np.pi  # 2*pi is one full cycle of a sine wave
        self.Inc = (2 * np.pi / self.numPoints)
        self.frequency = 1
        self.count = 0
        self.incR = 1
        self.incG = 2

        self.x = np.zeros(self.numPoints)
        for i in range(self.numPoints):
            self.x[i] = self.xStart + i * (self.xStop - self.xStart) / self.numPoints
            print(self.x[i])

        # Initialize sine wave data
        self.ySin = np.sin(self.frequency * self.x)
        self.ySin2 = np.sin(self.frequency * self.x + 2 * np.pi / 3)
        self.ySin3 = np.sin(self.frequency * self.x + 4 * np.pi / 3)

        self.initUI()

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.updatePlot)
        self.timer.start(100)

    def initUI(self):
        # Main layout
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        layout = QVBoxLayout(centralWidget)

        # Frequency display label
        self.sliderLabel = QLabel("Frequency: 1 Hz")
        self.sliderLabel.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.sliderLabel)

        # Frequency slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(1)  # use integer values
        self.slider.setMaximum(40)
        self.slider.setValue(10)
        self.slider.valueChanged.connect(self.updateFrequency)
        layout.addWidget(self.slider)

        # Start/Stop buttons
        buttonLayout = QHBoxLayout()
        self.startButton = QPushButton("Start")
        self.stopButton = QPushButton("Stop")
        self.startButton.clicked.connect(self.startAnimation)
        self.stopButton.clicked.connect(self.stopAnimation)
        buttonLayout.addWidget(self.startButton)
        buttonLayout.addWidget(self.stopButton)
        layout.addLayout(buttonLayout)

        # Plot widget setup
        self.graphWidget = pg.PlotWidget()
        layout.addWidget(self.graphWidget)

        self.plotSin = self.graphWidget.plot(self.x, self.ySin, pen=pg.mkPen('r', width=4))
        self.plotSin2 = self.graphWidget.plot(self.x, self.ySin2, pen=pg.mkPen('g', width=4))
        self.plotSin3 = self.graphWidget.plot(self.x, self.ySin3, pen=pg.mkPen('b', width=4))

        self.graphWidget.setYRange(-1.25, 1.25)

    def updatePlot(self):
        # This function will be called every 100 milliseconds
        self.xStart += self.Inc
        self.xStop += self.Inc
        self.x = np.linspace(self.xStart, self.xStop, self.numPoints)

        # 'count*self.incR/100' is the phase shift and is a fixed offset
        self.ySin = np.sin(self.frequency * self.x + self.count * self.incR / 100 * self.frequency)  # red
        self.ySin2 = np.sin(self.frequency * self.x + 2 * np.pi / 3 + self.count * self.incG / 100 * self.frequency)  # green
        self.ySin3 = np.sin(self.frequency * self.x + 4 * np.pi / 3)  # blue

        # green and red chase blue

        self.plotSin.setData(self.x, self.ySin)
        self.plotSin2.setData(self.x, self.ySin2)
        self.plotSin3.setData(self.x, self.ySin3)

        self.count += 1  # incrementing the count to animate green and red sine waves

    def updateFrequency(self, value):
        self.frequency = value / 10
        self.sliderLabel.setText(f"Frequency: {self.frequency} Hz")

    def startAnimation(self):
        if not self.timer.isActive():
            self.timer.start(100)

    def stopAnimation(self):
        if self.timer.isActive():
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = SineWavePlotter()
    win.show()
    sys.exit(app.exec_())


