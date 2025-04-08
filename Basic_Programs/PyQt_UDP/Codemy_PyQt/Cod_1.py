'''
Codemy for PyQt5  Lesson 1

'''
###### step 1 create a basic window
# import PyQt5.QtWidgets as qtw
# print(qtw.__name__)
# class MainWIndow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()  ## class initialization      
#         self.show()
# app = qtw.QApplication([])  ## create an empty window
# mw =MainWIndow()
# app.exec_() ## runs the app
##########
# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg    ## need this since  'label' is a widget but fonts are gui s for example
# print(qtw.__name__)
# class MainWIndow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()  ## class initialization 
#         ## Add a title
#         self.setWindowTitle('Look Jannie! My PyQt5 Window.')
#         ## Set Layout can choose vertical, horizontal or grid
#         self.setLayout(qtw.QVBoxLayout())
#         ## Create a label for the layout
#         my_label =qtw.QLabel('Greetings to All! What\'s your Name')
#         ## Change the font size of label 
#         my_label.setFont(qtg.QFont('Zapfino',18))     ## Helvetica ,Arial , Phosphate
#         self.layout().addWidget(my_label)   ## this adds the QLabel (a widget) to 'layout' 
#         ## the label is a widget, but the font of the widget is GUI! so have to import QtGui above  and call if qtgui
        
          
#         # create an entry box
#         self.my_entry = qtw.QLineEdit()
#         self.my_entry.setObjectName('name_field')
#         self.my_entry.setPlaceholderText('Enter your Name please')
#         # self.my_entry.setText('Enter your name')## the text enty is optional can just have '  ' 
#         self.layout().addWidget(self.my_entry)
#         ## Create a button
#         # my_button =qtw.QPushButton('Press Me')   ## this just creates the button, next lines will also make it call a function
        
#         my_button = qtw.QPushButton('Press Me',clicked =lambda:press_it())
#         self.layout().addWidget(my_button) 
        
        
#         self.show()
#         def press_it():
#             ## i want to be able to erase the initial my_entry.setText('Enter your name') so that when the response to clicking the button does not show that message as part of the   my_label.setText(f'Hello {my_entry.text()}, Welcome')
#             ## add name to label
#             my_label.setText(f'Hello {self.my_entry.text()}, Welcome')
# #             ## clear entry box
#             self.my_entry.setText('')
# app = qtw.QApplication([])  ## create an empty window
# mw =MainWIndow()
# app.exec_() ## runs the app

############# this is same as above but uses a .placeholder instead of .setText
# Use .setPlaceholderText('Enter your name') instead of .setText('Enter your name'). A placeholder is just a greyed-out prompt that disappears when the user starts typing, and it doesn’t get counted as input.
# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg

# print(qtw.__name__)

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Look Jannie! My PyQt5 Window.')
#         self.setLayout(qtw.QVBoxLayout())

#         # Label
#         self.my_label = qtw.QLabel("Greetings to All! What's your Name")
#         self.my_label.setFont(qtg.QFont('Zapfino', 18))
#         self.layout().addWidget(self.my_label)

#         # Entry field
#         self.my_entry = qtw.QLineEdit()
#         self.my_entry.setObjectName('name_field')
#         self.my_entry.setPlaceholderText('Enter your name')  # <--- use this instead of setText
#         self.layout().addWidget(self.my_entry)

#         # Button
#         my_button = qtw.QPushButton('Press Me', clicked=self.press_it)
#         self.layout().addWidget(my_button)

#         self.show()

#     def press_it(self):
#         entered_name = self.my_entry.text()
#         if entered_name:  # Only respond if there's actual input
#             self.my_label.setText(f'Hello {entered_name}, Welcome')
#             self.my_entry.clear()

# app = qtw.QApplication([])
# mw = MainWindow()
# app.exec_()

### lambda practice
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QSlider, QLabel
)
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.color ='magenta'
        self.var = 'yellow'
        self.varOld = 'red'
        ## deleted all the window since it is inherited
        self.setWindowTitle('My very own Widget')
        self.setGeometry(100, 100, 800, 600)

        widgetBox = QVBoxLayout()
        buttonBox = QHBoxLayout()

        # Blue Button
        blueButton = QPushButton('Blue Button')
        blueButton.setStyleSheet('background-color: blue;color: white;')
        blueButton.clicked.connect(self.blueButtonpressed)
        buttonBox.addWidget(blueButton)

        # Red Button
        redButton = QPushButton('Red Button')
        redButton.setStyleSheet('background-color: red;color: white')
        redButton.clicked.connect(self.redButtonpressed)
        buttonBox.addWidget(redButton)

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
        ##  option 1
        self.offButton.clicked.connect(lambda: self.offButtonpressed())## this works the same as without any lambda function but allows more flexibililty,for example to log something or pass parameters!
        self.offButton.clicked.connect(lambda: self.offButtonpressed_with_param("Turning off"))
        buttonBox.addWidget(self.offButton)
        button = QPushButton("Say Hello")
        button.setStyleSheet('background-color: pink; color: magenta')
        ## option 2
        button.clicked.connect(lambda: self.say_something("Hello"))
        ## option 3
        self.some_value = 42
        button.clicked.connect(lambda: self.do_something("Click", self.some_value))
        ## option 4  Use lambda to do more than one thing (use a semicolon!)
        self.msg2 ='How Goes!'
        button.clicked.connect(lambda:(print('Boom'),self.say_something(self.msg2)))
        button.clicked.connect(lambda: (print("Clicked!"), self.say_something("Boom")))

        button.clicked.connect(lambda: (print("Turning off"), self.set_mode('off')))

        
        
        
        
        buttonBox.addWidget(button)
        widgetBox.addLayout(buttonBox)

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
        widgetBox.addStretch()

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
    def say_something(self,value):
        print(f'You said ,{value}')
    def do_something(self,msg, value):
        print(f'{msg} - {value}')
    def set_mode(self,value):
        
        self.var = self.color
        print(f"Mode is now {self.color}")

        print(f'You have changed the mode tp {value}')
app = QApplication(sys.argv)
mw = MainWindow()
sys.exit(app.exec_())