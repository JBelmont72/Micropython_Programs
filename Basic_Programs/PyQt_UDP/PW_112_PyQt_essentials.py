'''



'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import time
 
def greenButtonPressed():
    print("green button clicked")
def yellowButtonPressed():
    print("yellow button clicked")
def redButtonPressed():
    print("red button clicked")
def offButtonPressed():
    print("off button clicked")
def sliderValueChanged(val):
    frequency=val/10
    sliderLabel.setText("Frequency: "+str(frequency)+" Hz")
    print("Frequency: ",frequency)
 
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("My Grand Widget")
window.setGeometry(100,100,800,600)
 
widgetBox=QVBoxLayout(window)
buttonBox=QHBoxLayout()
 
greenButton = QPushButton("Green Button")
greenButton.setStyleSheet("background-color: green; color: white;")
greenButton.clicked.connect(greenButtonPressed)
buttonBox.addWidget(greenButton)
 
yellowButton = QPushButton("Yellow Button")
yellowButton.setStyleSheet("background-color: yellow; color: black;")
yellowButton.clicked.connect(yellowButtonPressed)
buttonBox.addWidget(yellowButton)
 
redButton = QPushButton("Red Button")
redButton.setStyleSheet("background-color: red; color: white;")
redButton.clicked.connect(redButtonPressed)
buttonBox.addWidget(redButton)
 
offButton = QPushButton("Off Button")
offButton.setStyleSheet("background-color: black; color: white;")
offButton.clicked.connect(offButtonPressed)
 
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(40)
slider.setValue(10)
slider.setTickPosition(QSlider.TicksBelow)
slider.setTickInterval(5)
slider.valueChanged.connect(sliderValueChanged)
 
 
sliderLabel=QLabel("Frequency: 1.0 HZ")
sliderLabel.setAlignment(Qt.AlignCenter)
sliderLabel.setStyleSheet("font-size: 24px;padding 2px;")
 
widgetBox.addLayout(buttonBox)
widgetBox.addWidget(sliderLabel)
widgetBox.addWidget(slider)
widgetBox.addStretch()
 
window.setLayout(widgetBox)
window.show()
sys.exit(app.exec_())