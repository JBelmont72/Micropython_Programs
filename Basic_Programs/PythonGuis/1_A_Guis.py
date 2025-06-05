'''
this is the same as the 1_Guis.py file but with a different layout. I played with the layout and added a second horizontal layout to the first horizontal layout. I also added a stretchable space to the right of the second horizontal layout. I also added a second button to the main vertical layout. I also added a comment to explain what each line of code does.
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
#         # Create a button and set its text
#         button = qtw.QPushButton("Press Me!")

#         # Set the central widget of the Window.
#         # This is the widget that will be displayed in the window.
#         # The central widget is the main widget of the window.
#         # In this case, we are using a vertical box layout to arrange the button.
#         # The layout will automatically resize the button to fit the window.
#         self.setLayout(qtw.QVBoxLayout())   ## set the layout of the window to a vertical box layout!!
#         self.layout().addWidget(button)
#         # Create a horizontal layout to group more widgets
#         h_layout = qtw.QHBoxLayout()    ## this is creating my first horizontal layout!!
        
#         # Add widgets to the horizontal layout
#         label = qtw.QLabel("Label:")
#         line_edit = qtw.QLineEdit('edit me')
#         h_layout.addWidget(label)
#         h_layout.addWidget(line_edit)   ## add widgets to the horizontal layout named h_layout!!
#         ## add another layout and name it h2_layout !!!
#         h2_layout = qtw.QHBoxLayout()   ## this is creating my second horizontal layout!!
#         # Add widgets to the second horizontal layout
#         label2 = qtw.QLabel("Label 2:")
#         line_edit2 = qtw.QLineEdit('edit me too')
#         h2_layout.addWidget(label2)
#         h2_layout.addWidget(line_edit2)
#         ## option 1 is to add the second horizontal layout to the first horizontal layout
#         # Add the second horizontal layout to the first horizontal layout
#         h_layout.addLayout(h2_layout) ## this places the second horizontal layout inside the first horizontal layout next to the first horizontal layout
        
#         ## can i add the h2_layout directly to the main layout?
#         ## option 2 is to add the second horizontal layout to the main vertical layout
#         # self.layout().addLayout(h2_layout)  ## this adds the second horizontal layout to the main vertical layout,stacks the two horizontal layouts
        
#         # Add the horizontal layout to the main vertical layout
#         self.layout().addLayout(h_layout)
        
#         h2_layout.addStretch(1)  # Add stretchable space to the right of the horizontal layout
        
        
#         # Add another button to the main vertical layout
#         another_button = qtw.QPushButton("Another Button")
#         self.layout().addWidget(another_button)
#         # Set the window title
#         # self.setWindowTitle("Hello World")## thias wopuld reset the window title
#         # Set the window size
#         self.resize(800, 600)
#         # Set the window icon
#         # icon = qtg.QIcon("path/to/icon.png")  # Load an icon from a file
#         # self.setWindowIcon(icon)  # Set the window icon
#         # Set the window font
#         # font = qtg.QFont("Arial", 12)  # Create a font object with the desired font family and size
#         # self.setFont(font)  # Set the font for the window

#         # Your code ends here
#         self.show() ## put it here so the window shows.


# if __name__ == '__main__':
#     app = qtw.QApplication(sys.argv)
#     w = MainWindow(windowTitle='My Window')
#     sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes, app.exec_()  starrts the event loop

###~~~~~~~ my attempt, i have the 1st button in the main vertical layout, then h_layout= qtw.QHBoxLayout() added to the main verical layout:                self.layout().addLayout(h_layout) (can place any widgets in this h_layout). THen i added a second horizontal layout to the layout :  self.layout().addLayout(v_layout)  and finally added another button to the main vertical layout.

 
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here
        button= qtw.QPushButton("Press Me!")
        # Set the central widget of the Window.
        # This is the widget that will be displayed in the window.
        # The central widget is the main widget of the window.
        # In this case, we are using a vertical box layout to arrange the button.
        # The layout will automatically resize the button to fit the window.
        # Your code ends here   
        self.setLayout(qtw.QVBoxLayout())   ## set the layout of the window to a vertical box layout!!NOTE
        # self.setFixedSize(800, 600) ## set the size of the window
        self.setMaximumSize(400, 600) ## set the maximum size of the window
        self.setMinimumSize(200, 300)
        self.layout().addWidget(button) #NOTE
        # Create a horizontal layout to group more widgets
        h_layout= qtw.QHBoxLayout() #NOTE
        label_1= qtw.QLabel("Label:")
        line_edit_1= qtw.QLineEdit('edit me')
        h_layout.addWidget(label_1)
        h_layout.addWidget(line_edit_1)   ## add widgets to the horizontal layout named h_layout!!
        self.layout().addLayout(h_layout) ## NOTE this places the second horizontal layout inside the first horizontal layout next to the first horizontal layout
        
        v_layout= qtw.QHBoxLayout() ## this is creating my second horizontal layout!! NOTE second layout(the first button is in the main vertical layout)
        # Add widgets to the second vertical layout
        button_2= qtw.QPushButton("Button 2")
        label_2= qtw.QLabel("Label 2:")
        line_edit_2= qtw.QLineEdit('edit me too')
        v_layout.addWidget(label_2)
        v_layout.addWidget(line_edit_2)
        v_layout.addWidget(button_2)
        ## option 1 is to add the second vertical layout to the first horizontal layout
        # Add the second vertical layout to the first horizontal layout
        
        # h_layout.addLayout(v_layout)
        
        ## option 2 is to add the second vertical layout to the main vertical layout
        self.layout().addLayout(v_layout)  ## NOTE this adds the second vertical layout to the main vertical layout,stacks the two horizontal layouts
        # Add the horizontal layout to the main vertical layout
        # self.layout().addLayout(h_layout)
        button_2.setStyleSheet("font-size: 24px; font-weight: bold;")
        
        
        button_3= qtw.QPushButton("Another Button")
        self.layout().addWidget(button_3)
        
        
        self.show() ## put it here so the window shows.


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes
# print(len(locals()))  # Print the number of local variables to check the environment, checks number of namepacesbeing used
# ## can use aliases such as from Pyqt5 import QtWidgets as qtw, QtCore as qtc, QtGui as qtg