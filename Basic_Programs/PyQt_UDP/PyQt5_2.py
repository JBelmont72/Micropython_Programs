''' PW111  PyQt5 essentials 

'''
import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
print(PyQt5.__name__)
import time

app = QApplication(sys.argv)    ## essential to set up an app, appllication OBJECT
## create a window of the browser screen, use 'window' to interact with the 'window OBJECT'
window = QWidget()
## have two objects so far
window.setWindowTitle('My very own Widget')
window.setGeometry(100,100,800,600)


window.show()
sys.exit(app.exec_())