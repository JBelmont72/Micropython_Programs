'''  the basic necessary set-up for a widget

need :  window.show()
sys.exit(app.exec_())        in order for the window to display

'''
# import PyQt5          ###this only creates the window and nothing in it
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt
# print(PyQt5.__name__)
# import time

# app = QApplication(sys.argv)    ## essential to set up an app, appllication OBJECT
# ## create a window of the browser screen, use 'window' to interact with the 'window OBJECT'
# window = QWidget()
# ## have two objects so far
# window.setWindowTitle('My very own Widget')
# window.setGeometry(100,100,800,600)


# window.show()
# sys.exit(app.exec_())






## three levels here. first the window, then the widget box inside
###~~~~ below is the basic set including one widget (a bpushbutton)
import PyQt5
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 
print(PyQt5.__name__)
import time
def blueButtonpressed():
    print('Blue button clicked')
##step 1 create an object
app = QApplication(sys.argv)    ## essential to set up an app, appllication OBJECT
## step 2  create a window of the browser screen, use 'window' to interact with the 'window OBJECT'
window = QWidget()
## step 3 have two objects so far. 
window.setWindowTitle('My very own Widget')
window.setGeometry(100,100,800,600) ## at this point have a window but nothing inside. so next step is to create a widget box to put widgets in
## next CREATES THE NEXT LEVEL DOWN FROM THE WINDOW ABOVE
widgetBox=QVBoxLayout(window)
## Now build boxes inside the widgetBox. 
buttonBox=QHBoxLayout()     ## this goes inside the widgetBox, this creates the  buttonBox object.
# widgetBox.addLayout(buttonBox)  ## adds the buttonBox  to inside the widgetBox, this places the buttonBox
## the widgetBox at this point is empty, next create a button below
blueButton = QPushButton('Blue Button')
blueButton.setStyleSheet('background-color: blue;color: yellow;')## the format is very specific!!
blueButton.clicked.connect(blueButtonpressed)
## the blue buttton is created but now has to be added to the widgetBox
## the BUTTON is added to the BUTTONBOX, the ButtonBOx  is added to the WidgetBox
## and finally the widgetBox is added to the WINDOQ
buttonBox.addWidget(blueButton)
window.setLayout(widgetBox)     ## FU on this since sketch worked without this?
widgetBox.addLayout(buttonBox)## the buttonBox was made before but here it is positioned in the widget box
window.show()
sys.exit(app.exec_())
