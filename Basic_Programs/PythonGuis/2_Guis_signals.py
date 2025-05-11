'''
lesson 2 signals and slots
https://www.pythonguis.com/tutorials/pyqt-signals-slots-events/
'''
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
#         ##need this to call the parent class!!
#         # Your code will go here
        
#         # self.layout = qtw.QVBoxLayout()
#         # self.setLayout(self.layout)
        
#         self.setLayout(qtw.QVBoxLayout())
#         self.setFixedSize(800, 600)
#         first_layout= qtw.QHBoxLayout()
#         label =qtw.QLabel("Label:")
#         line_edit = qtw.QLineEdit('edit me')
#         but1=qtw.QPushButton("Press Me!") ## this is a signal and slot, when the button is pressed, it will call the press_it method
#         # but1.clicked.connect(self.press_it) ## this is a signal and slot, when the button is pressed, it will call the press_it method
#         # but1= qtw.QPushButton("Press Me!", clicked= lambda:self.setWindowTitle("Hello World")) ## this is a signal and slot, when the button is pressed, it will call the press_it method
#         but1= qtw.QPushButton("Press Me!", clicked= lambda:self.press_it()) ## this is a signal and slot, when the button is pressed, it will call the press_it method
#         # but1= qtw.QPushButton("Press Me!", clicked= lambda: print("Button 1 pressed")) ## this is a signal and slot, when the button is pressed, it will print "Button 1 pressed"
#         first_layout.addWidget(label)
#         first_layout.addWidget(line_edit)
#         first_layout.addWidget(but1)
#         self.layout().addLayout(first_layout)
#         button_2= qtw.QPushButton("Button 2")
#         self.layout().addWidget(button_2)   # this isadded to the main vertical layout
#         self.show()
        
#     def press_it(self):
#         print("Button 1 pressed")
#         if self.windowTitle() == "My Window":
#             self.setWindowTitle("Hello World")
#         else:
#             self.setWindowTitle("My Window")
#         # self.setWindowTitle("Hello World") ## this would reset the window title
#         # self.setWindowTitle("Hello World")## thias wopuld reset the window title
#             # self.setStyleSheet("background-color: red;") ## this would change the background color of the window to red
#             # self.setStyleSheet("background-color: blue;") ## this would change the background color of the window to blue
#             # self.setStyleSheet("background-color: green;") ## this would change the background color of the window to green
#             # self.setStyleSheet("background-color: yellow;") ## this would change the background color of the window to yellow
#             # self.setStyleSheet("background-color: purple;") ## this would change the background color of the window to purple
#             # self.setStyleSheet("background-color: orange;") ## this would change the background color of the window to orange
        


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes


##
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    toggled= qtc.pyqtSignal(bool) ## this is a signal that is emitted when the button is toggled
    clicked= qtc.pyqtSignal() ## this is a signal that is emitted when the button is clicked
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here
        self.setLayout(qtw.QVBoxLayout())
        self.setFixedSize(800, 600)
        first_layout= qtw.QHBoxLayout()
        button_1= qtw.QPushButton("Press Me!")
        button_1.setCheckable(True)
        button_1.setChecked(True)
        button_1.setAutoDefault(True)
        button_1.setDefault(True)
        button_1.setAutoRepeat(True)
        button_1.setStyleSheet("background-color: yellow;") ## 
        # button_1.clicked.connect(lambda: print("Button 1 pressed"))
        # button_1.clicked.connect(lambda: self.setWindowTitle)("Button 1 pressed")
        button_1.clicked.connect(lambda: self.setStyleSheet("background-color: red;")) ## this is a signal and slot, when the button is pressed, it will call the press_it method
        button_1.clicked.connect(self.the_button_was_toggled)
        button_1.clicked.connect( self.the_button_was_clicked)
        self.layout().addWidget(button_1)
        
        
        label =qtw.QLabel("Label:")
        line_edit = qtw.QLineEdit('edit me')
        but1=qtw.QPushButton("Press Me!") ## this is a signal and slot, when the button is pressed, it will call the press_it method
        but1.clicked.connect(lambda:self.setStyleSheet("background-color: blue;")) ## this is a signal and slot, when the button is pressed, it will call the press_it method
        but1.setStyleSheet('background-color: magenta')
        # but1.clicked.connect(self.press_it) ## this is a signal and slot, when the button is pressed, it will call the press_it method
        # but1= qtw.QPushButton("Press Me!", clicked= lambda:self.setWindowTitle("Hello World")) ## this is a signal and slot, when the button is pressed, it will call the press_it method
        first_layout.addWidget(label)
        first_layout.addWidget(line_edit)
        first_layout.addWidget(but1)
        self.layout().addLayout(first_layout)
        

        self.show()
    def the_button_was_clicked(self):   
        print("Button 1 pressed")
        if self.windowTitle() == "My Window":
            self.setWindowTitle("Hello World")
        else:
            self.setWindowTitle("My Window")
    def the_button_was_toggled(self,toggled):
        print("Button 1 toggled",toggled)
        
        # self.setWindowTitle("Hello World") ## this would reset the window title
        # self.setWindowTitle("Hello World")## thias wopuld reset the window title
            # self.setStyleSheet("background-color: red;") ## this would change the background color of the window to red
            # self.setStyleSheet("background-color: blue;") ## this would change the background color of the window to blue
            # self.setStyleSheet("background-color: green;") ## this would change the background color of the window to green
            # self.setStyleSheet("background-color: yellow;") ## this would change the background color of the window to yellow
            # self.setStyleSheet("background-color: purple;") ## this would change the background color of the window to purple
            # self.setStyleSheet("background-color: orange;") ## this would change the background color of the window to orange 

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes

