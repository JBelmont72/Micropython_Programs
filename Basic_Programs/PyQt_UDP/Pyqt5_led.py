'''


'''
import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
print(PyQt5.__name__)
import time
var='yellow'
varOld='red'

def blueButtonpressed():
    global var
    print('Blue button clicked')
    var ='blue'
    return var
def redButtonpressed():
    global var
    print('Red button clicked')
    var = 'red'
    return var
def yellowButtonpressed():
    global yellow
    print('Yellow button clicked')
    var = 'yellow'
def offButtonpressed():
    print('Off button clicked')

def sliderValueChanged(value):
    frequency=value/10
    sliderLabel.setText('Frequency: '+str(frequency)+ ' Hz')
    print('Frequency: ',frequency)
   

       
    
app = QApplication(sys.argv)    ## essential to set up an app, appllication OBJECT
## create a window of the browser screen, use 'window' to interact with the 'window OBJECT'
window = QWidget()
## have two objects so far
window.setWindowTitle('My very own Widget')
window.setGeometry(100,100,800,600)## x,y,width,height
## next CREATES THE NEXT LEVEL DOWN FROM THE WINDOW ABOVE
widgetBox=QVBoxLayout(window)
## Now build boxes inside the widgetBox. 
buttonBox=QHBoxLayout()     ## this goes inside the widgetBox, this creates the  buttonBox object.
# widgetBox.addLayout(buttonBox)  ## adds the buttonBox  to inside the widgetBox, this places the buttonBox
## the widgetBox at this point is empty, next create a button below
blueButton = QPushButton('Blue Button')
blueButton.setStyleSheet('background-color: blue;color: white;')## the format is very specific!!
blueButton.clicked.connect(blueButtonpressed)
## the blue buttton is created but now has to be added to the widgetBox
## the BUTTON is added to the BUTTONBOX, the ButtonBOx  is added to the WidgetBox
## and finally the widgetBox is added to the WINDOQ
buttonBox.addWidget(blueButton)
## do the same for additional buttons
redButton=QPushButton('Red Button')
redButton.setStyleSheet('background-color: red;color: white')
redButton.clicked.connect(redButtonpressed)
buttonBox.addWidget(redButton)
yellowButton=QPushButton('Yellow Button')
yellowButton.setStyleSheet('background-color:yellow; color:magenta')
yellowButton.clicked.connect(yellowButtonpressed)
buttonBox.addWidget(yellowButton)
offButton=QPushButton('Off Button')   ## fourth lowest level
offButton.setStyleSheet('background-color:green;color:black')
offButton.clicked.connect(offButtonpressed)     ##desired action a method of the fourth highest level
buttonBox.addWidget(offButton)  ## third highest level
widgetBox.addLayout(buttonBox)  ## second highest level
### buttonBosx does not have a specified position so is in the center. Below we will add an arbitrary 'push' to raise the widgetBox
## bottom to top__ Button ,,,buttonBOx,,,widgetBox,,,Window

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(40)
slider.setValue(10)
slider.setTickPosition(QSlider.TicksBelow)
slider.setTickInterval(5)
slider.valueChanged.connect(sliderValueChanged)


sliderLabel=QLabel("Frequency: 1.0 HZ")
sliderLabel.setAlignment(Qt.AlignCenter)
sliderLabel.setStyleSheet("font-size: 24px;padding 2px:")



widgetBox.addWidget(sliderLabel)
widgetBox.addWidget(slider)

widgetBox.addStretch()## this raises the widgetBOx to the top

window.setLayout(widgetBox) ## highset level
window.show()





sys.exit(app.exec_())

