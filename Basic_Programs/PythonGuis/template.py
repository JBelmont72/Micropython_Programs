'''
Alan D Moore Codes tutorial template
This template is designed to help you create a structured and organized code file for your project. It includes sections for imports, constants, functions, and the main execution block.
His github repositiory https://github.com/alandmoore/PyQt-Videos-Examples/blob/master/HelloWorldqt/template.py
default command line arguements for any QT program
https://doc.qt.io/qt-5/qapplication.html#QApplication
'''
## Hello World
# from PyQt5.QtWidgets import *

# app = QApplication([])

# w = QWidget(windowTitle='hello world')
# w.show()

# app.exec_()
######## template.py
# import sys
# from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg

# class MainWindow(qtw.QWidget):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Your code will go here

#         # Your code ends here
#         self.show()


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)## first line always run, pass in gthe command line arguements from the QT libfrary
#     ## this is the default arguements but to make work right, need to pass sys.argv into the QApplication.
#     w = MainWindow()
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
#####~~~~~~~~~~work with the above template
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here

        # Your code ends here
        self.show() ## put it here so the window shows.


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes




# print(len(locals()))  # Print the number of local variables to check the environment, checks number of namepacesbeing used
# ## can use aliases such as from Pyqt5 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
# ## QtCore for low-level core functionality, QtGui for graphics and user interface elements, and QtWidgets for higher-level widgets and controls.
# # Import necessary PyQt5 modules
# ## he following imports are commonly used in PyQt5 applications:
# from PyQt5 import QtCore as qtc  # Import Qt core functionalities
# from PyQt5 import QtWidgets as qtw  
# from PyQt5 import QtGui as qtg
# import sys# for command line arguements and also for executing (needed for linux to know if commands to exit succeeded  )

# # from PyQt5.QtWidgets import *
# # from PyQt5.QtCore import Qt  # Import necessary PyQt5 modules i needed for Qt functionalities
# # from PyQt5.QtGui import QIcon  # Import QIcon if you need to use icons in your application
# # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel  # Import necessary PyQt5 modules
# # from PyQt5.QtCore import Qt  # Import Qt core functionalities
# print(len(locals()))  # Print the number of local variables to check the environment after imports
# from PyQt5.QtGui import QFont  # Import QFont if you need to set custom fonts
# print(len(locals()))  # Print the number of local variables to check the environment after imports

# # app = QApplication([])  # Create a QApplication instance    
# app =qtw.QApplication([]) ## passing command arguements , for this need 'command line arguements' for this need import sys
# # w=QWidget(windowTitle= 'Hello World')  # Create a QWidget instance

# w=qtw.QTabWidget(windowTitle = 'Hello WOrld')
# w.setWindowTitle("Alan D Moore Codes")  # Set the window title
# w.resize(800, 600)  # Set the window size
# # Create a layout for the main window
# # layout = QVBoxLayout()  # Create a vertical box layout
# layout = qtw.QHBoxLayout()
# # Add a label to the layout
# # label = QLabel("Welcome to Alan D Moore Codes!")  # Create a QLabel instance
# label=qtw.QLabel('Welcome')
# # label.setAlignment(Qt.AlignCenter)  # Center the label text
# # label.setAlignment(Qt.AlignLeft)  # Align the label text to the left


# label.setStyleSheet("font-size: 24px; font-weight: bold;")  # Set the label style
# layout.addWidget(label)  # Add the label to the layout

# w.show()  # Show the main window
# # app.exec_()  # Start the application event loop
# ## change above to 
# sys.exit(app.exec_())## need sys to get exit status to know if program worked successfully. 
###~~~~~~~~~~
print(len(locals()))  # Print the number of local variables to check the environment, checks number of namepacesbeing used
## can use aliases such as from Pyqt5 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg
## QtCore for low-level core functionality, QtGui for graphics and user interface elements, and QtWidgets for higher-level widgets and controls.
# Import necessary PyQt5 modules
## he following imports are commonly used in PyQt5 applications:
from PyQt5 import QtCore as qtc  # Import Qt core functionalities
from PyQt5 import QtWidgets as qtw  
from PyQt5 import QtGui as qtg
import sys# for command line arguements and also for executing (needed for linux to know if commands to exit succeeded  )
import os
print(os.path)
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt  # Import necessary PyQt5 modules i needed for Qt functionalities
# from PyQt5.QtGui import QIcon  # Import QIcon if you need to use icons in your application
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel  # Import necessary PyQt5 modules
# from PyQt5.QtCore import Qt  # Import Qt core functionalities
print(len(locals()))  # Print the number of local variables to check the environment after imports
from PyQt5.QtGui import QFont  # Import QFont if you need to set custom fonts
print(len(locals()))  # Print the number of local variables to check the environment after imports
class MainWindow(qtw.QWidget):## NOTE this creates a subclass( or child of parent?) with all the functionality of the QWidget class   
    pass
app =qtw.QApplication(sys.argv) 
w=MainWindow(windowTitle='Hello World') ## w is an object of the MainWindow subclass
# w=qtw.QWidget(windowTitle='I skipped the subclass')## here i made a direct object of the QWidget class!
w.show()
sys.exit(app.exec_())










# app = QApplication([])  # Create a QApplication instance    
app =qtw.QApplication([]) ## passing command arguements , for this need 'command line arguements' for this need import sys
# w=QWidget(windowTitle= 'Hello World')  # Create a QWidget instance



w=qtw.QTabWidget(windowTitle = 'Hello WOrld')
w.setWindowTitle("Alan D Moore Codes")  # Set the window title
w.resize(800, 600)  # Set the window size
# Create a layout for the main window
# layout = QVBoxLayout()  # Create a vertical box layout
layout = qtw.QHBoxLayout()
# Add a label to the layout
# label = QLabel("Welcome to Alan D Moore Codes!")  # Create a QLabel instance
label=qtw.QLabel('Welcome')
# label.setAlignment(Qt.AlignCenter)  # Center the label text
# label.setAlignment(Qt.AlignLeft)  # Align the label text to the left


label.setStyleSheet("font-size: 24px; font-weight: bold;")  # Set the label style
layout.addWidget(label)  # Add the label to the layout




w.show()  # Show the main window
# app.exec_()  # Start the application event loop
## change above to 
sys.exit(app.exec_())## need sys to get exit status to know if program worked successfully. 


####################
#     return main_window, app # Return the main window and application instance   
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())