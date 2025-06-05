'''
You've done a solid job converting your functional PyQt5 sine wave plotting program into a class-based version. However, there are several key issues and minor redundancies in your class-based version that affect functionality and correctness.

Here are the main problems and how to fix them:

✅ 1. Plotting x vs y is inconsistent in updatePlot()
You generate new x, but you use self.x (which is never updated) in setData():

Problem:

python
Copy
Edit
x = np.linspace(self.xStart, self.xStop, self.numPoints)
self.ySin = np.sin(self.frequency * self.x + self.count * self.incR / 100 * self.frequency)
# ...
self.plotSin.setData(self.x, self.ySin)  # <-- Still using self.x instead of local x
Fix:

Update self.x every time:

python
Copy
Edit
self.x = np.linspace(self.xStart, self.xStop, self.numPoints)
self.ySin = np.sin(self.frequency * self.x + self.count * self.incR / 100 * self.frequency)
# ...
self.plotSin.setData(self.x, self.ySin)
✅ 2. Missing update to frequency label text
Your frequency is updated with the slider, but the label is never updated.

Fix:

In updateFrequency():

python
Copy
Edit
def updateFrequency(self, value):
    self.frequency = value / 10
    self.sliderLabel.setText(f"Frequency: {self.frequency:.1f} Hz")
✅ 3. Redundant layout setting
You're setting the same layout multiple times:

Problem:

python
Copy
Edit
self.setLayout(mainLayout)
# ...
self.graphWidget.setLayout(mainLayout)  # ❌ This is wrong — graphWidget shouldn't set the main layout
self.setLayout(mainLayout)
Fix:

Just set it once in the main window:

python
Copy
Edit
self.setLayout(mainLayout)
Remove:

python
Copy
Edit
self.graphWidget.setLayout(mainLayout)  # ❌
✅ 4. Unnecessary re-plotting of initial values
You create initial ySin, ySin2, ySin3 but never plot them during __init__. They’re also not used afterward.

Fix (Optional):

You could initialize your plots here instead if you wanted to show the wave immediately:

python
Copy
Edit
self.plotSin.setData(self.x, ySin)
self.plotSin2.setData(self.x, ySin2)
self.plotSin3.setData(self.x, ySin3)
But since updatePlot() starts immediately, this is not strictly needed.

✅ 5. UI polish: Better window title usage
You're redundantly setting the title twice:

python
Copy
Edit
self.setWindowTitle('My Window')
...
self.setWindowTitle('The Magic of Sin Waves')
Fix:

Only set it once.

✅ 6. Minor: windowTitle='My Window' has no effect
You're passing windowTitle='My Window' when instantiating MainWindow, but your __init__ doesn't accept or use that kwarg.

Fix:

Just remove the argument:

python
Copy
Edit
w = MainWindow()
Or use:

python
Copy
Edit
class MainWindow(qtw.QWidget):
    def __init__(self, *args, windowTitle='The Magic of Sin Waves', **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle(windowTitle)
✅ Final Summary of Fixes

 Use self.x in updatePlot() (update it each time).
  Update sliderLabel in updateFrequency().
 Remove self.graphWidget.setLayout(...).
 Remove redundant or ineffective code like windowTitle kwarg or unused plot initializations.
 Improve clarity and naming where possible.


'''
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
