'''
class version of PW111
ERRORS in first version_ not corrected:
1. ❌ window = QWidget() creates a separate window, which you don't need inside your MainWindow.
✅ You're already inheriting from QWidget with class MainWindow(QWidget):, so just work with self directly.
❌ window.setLayout(widgetBox) — this refers to the wrong window.
✅ Fix: Remove all references to window and use self instead.
2. ❌ Unused or mis-scoped variables like sliderLabel and slider
You use self.sliderLabel in the method sliderValueChanged(), but you defined it as sliderLabel (no self.), so it's not accessible in other methods.
✅ Fix: define them with self. so they become part of the class.
3. ❌ sliderValueChanged() is missing an argument
This method is connected to a signal that passes a value (valueChanged). So it needs to accept a value parameter.
The valueChanged signal automatically passes the slider value to the connected slot (function), so sliderValueChanged must accept one argument.
'''
####~~~~~~~ working version of three buttons and slider
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel
)
from PyQt5.QtCore import Qt

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

        # Blue Button
        blueButton = QPushButton('Blue Button')
        blueButton.setStyleSheet('background-color: blue;color: white;')
        blueButton.clicked.connect(self.blueButtonpressed)
        buttonBox.addWidget(blueButton)## add the button to the buttonBox

        # Red Button
        redButton = QPushButton('Red Button')
        redButton.setStyleSheet('background-color: red;color: white')
        redButton.clicked.connect(self.redButtonpressed)
        buttonBox.addWidget(redButton) ## add the button to the buttonBox

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
        
        self.offButton.clicked.connect(lambda: self.offButtonpressed())## this works the same as without any lambda function but allows more flexibililty,for example to log something or pass parameters!
        self.offButton.clicked.connect(lambda: self.offButtonpressed_with_param("Turning off"))


        
        buttonBox.addWidget(self.offButton)

        widgetBox.addLayout(buttonBox) ## here i add the buttonBOx to the widgetBox!!NOTE that the buttonBox is added to the widgetBox and not the other way around

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
        widgetBox.addStretch()## important to add stretch to the layout so that the widgets are raised to the top of the window

        self.setLayout(widgetBox)
        self.show()

    def blueButtonpressed(self):
        print('Blue button clicked')
        self.var = 'blue'

    def redButtonpressed(self):
        print('Red button clicked')
        self.var = 'red'

    def yellowButtonpressed(self):
        print('Yellow button clicked')
        self.var = 'yellow'

    def offButtonpressed(self):
        print('Off button clicked')

    def sliderValueChanged(self, value):
        frequency = value / 10
        self.sliderLabel.setText(f'Frequency: {frequency:.1f} Hz')
        print(f'Frequency: {frequency:.1f} Hz')

    def offButtonpressed_with_param(self,param):
        print(param)

app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())
