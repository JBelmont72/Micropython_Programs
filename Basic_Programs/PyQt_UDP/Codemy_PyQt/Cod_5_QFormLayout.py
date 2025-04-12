'''  first use oco_pilot, i asked for an example of QForm'''


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QFormLayout, QLabel, QLineEdit, QPushButton

# class FormExample(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QFormLayout Example")
        
#         # Create a QFormLayout
#         layout = QFormLayout()
        
#         # Add a label and a line edit
#         layout.addRow("Name:", QLineEdit())
        
#         # Create a custom widget (e.g., a button)
#         button = QPushButton("Click Me")
        
#         # Use setWidget to add the button to the second row
#         layout.setWidget(1, QFormLayout.FieldRole, button)
        
#         # Create a custom widget (e.g., a button)
#         button2 = QPushButton("Click Me Too!")
        
#         # Use setWidget to add the button to the second row
#         layout.setWidget(2, QFormLayout.FieldRole, button2)
        
#         # Set the layout for the main window
#         self.setLayout(layout)

# # Run the application
# app = QApplication(sys.argv)
# window = FormExample()
# window.show()
# sys.exit(app.exec_())

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
#  ## here i am importing all the methods from QtWidgets and thus have to specify qtw ( like specifying' machine' versus 'pin')

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Welcome to Jannie's Pizza")
#         self.setLayout(qtw.QVBoxLayout())

#         self.label = qtw.QLabel("Greetings! What's your name?")
#         self.label.setFont(qtg.QFont('Zapfino', 16))
#         self.layout().addWidget(self.label)

#         self.name_entry = qtw.QLineEdit()
#         self.name_entry.setPlaceholderText("Enter your name")
#         self.layout().addWidget(self.name_entry)

#         # self.button = qtw.QPushButton("Next", clicked=self.go_to_pizza_window)
#         self.button = qtw.QPushButton("Next", clicked=lambda:self.go_to_pizza_window())
#         self.layout().addWidget(self.button)

#         self.show()

#     def go_to_pizza_window(self):
#         name = self.name_entry.text().strip()
#         if name:
#             fingers =5          ## i added fingers just to reinforce sending arguemts to the second page
#             self.pizza_window = PizzaWindow(name,fingers) ## passing name to the PizzaWindow(name) constructor
#             self.pizza_window.show()
#             self.close()


# class PizzaWindow(qtw.QWidget):
#     def __init__(self, name,fingers):## if i was going to use this as a separate page, delete params
#         super().__init__()
#         self.name = name
#         self.fingers=fingers
#         self.setWindowTitle("Pizza Window")
#         self.setLayout(qtw.QVBoxLayout())

#         self.label = qtw.QLabel(f"Type something into the box, {self.name}")
#         self.label.setFont(qtg.QFont('Helvetica', 16))
#         self.layout().addWidget(self.label)

#         self.my_text = qtw.QTextEdit(
#             lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
#             lineWrapColumnOrWidth=75,
#             # placeholderText='Hello World',
#             placeholderText=f'Hello World, I have {self.fingers} fingers',
#             readOnly=False,
#             acceptRichText=True, ## rich text is text with formatting, bold,italic,colored, etc> I would paste it inot the box
#             # plainText = 'This is real text, does not dissapear',
#             # html ='<center><h1><em>Big Header Text!</em></h1></center><h2><em>my second line</em></h2>' ## this will add html, 
#             readOnly=False  ### this is the default. if True, can not overwrite or change
#         )
#         self.layout().addWidget(self.my_text)

#         self.my_button = qtw.QPushButton("Press Me", clicked=self.press_it)
#         self.layout().addWidget(self.my_button)

#     def press_it(self):
#         typed = self.my_text.toPlainText()
#         self.label.setText(f"{self.name}, you typed: {typed}")
#         # self.my_text.setPlainText('You clicked the button') ## this will set the text in the textBox widget that is placed in 'layout' created by:   self.my_text = qtw.QTextEdit(params)


# app = qtw.QApplication([])
# mw = MainWindow()
# app.exec_()

#######
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
#  ## here i am importing all the methods from QtWidgets and thus have to specify qtw ( like specifying' machine' versus 'pin')
class PizzaWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'judson'
        self.fingers=5
        ## add a title to the window
        self.setWindowTitle("Hello World")
        ## set a vertical limit to the window
        self.setMaximumHeight(500)
        ## set a horizontal limit to the window
        self.setMaximumWidth(500)               
        # self.setLayout(qtw.QVBoxLayout())##this was the original layout, but now we are using a form layout
        form_layout = qtw.QFormLayout() ## now We are name so we can reference it later and pass things into it
        self.setLayout(form_layout) ## WE WANT TO REFERENCE THE FORM LAYOUT, so we can pass items into it
        ## everything in a QFormLayout is in a row.
        ## each row has a label and a field
        ## the label is the first item in the row
        ## the field is the second item in the row
        ## the field can be a text box, a button, etc.
        ## the field can be a widget, a button, etc.
        ## note that below .addRow() to label and then added either the label or the QLineEdit and also a button
        label = qtw.QLabel(f"This is my cool box, {self.name}")
        label.setFont(qtg.QFont('Helvetica', 16))
        form_layout.addRow(label)
        ## add a text box   
        f_name = qtw.QLineEdit(self)
        f_name.setPlaceholderText("Enter your name")
        form_layout.addRow("First Name:", f_name)     
        l_name= qtw.QLineEdit(self)
        l_name.setPlaceholderText("Enter your last name")
        form_layout.addRow("Last Name:", l_name) 
        button= qtw.QPushButton("Click Me",clicked=self.press_it)
        form_layout.addRow(button)
        ## add a button
        button2= qtw.QPushButton("Click Me Too!",clicked=lambda:(print('hello world'),self.press_it()))       
        form_layout.addRow(button2)
            
  
        
        
        
        
        
        
        
        
        

        self.label = qtw.QLabel(f"Type something into the box, {self.name}")
        self.label.setFont(qtg.QFont('Helvetica', 16))
        self.layout().addWidget(self.label)

        self.my_text = qtw.QTextEdit(
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=75,
            # placeholderText='Hello World',
            placeholderText=f'Hello World, I have {self.fingers} fingers',
            readOnly=False,
            acceptRichText=True, ## rich text is text with formatting, bold,italic,colored, etc> I would paste it inot the box
            # plainText = 'This is real text, does not dissapear',
            # html ='<center><h1><em>Big Header Text!</em></h1></center><h2><em>my second line</em></h2>' ## this will add html, 
            # readOnly=False  ### this is the default. if True, can not overwrite or change
        )
        self.layout().addWidget(self.my_text)

        self.my_button = qtw.QPushButton("Press Me", clicked=self.press_it)
        self.layout().addWidget(self.my_button)
        self.show()## i had to add this since previously it was on the first page!!
    def press_it(self):
        typed = self.my_text.toPlainText()
        self.label.setText(f"{self.name}, you typed: {typed}")
        # self.my_text.setPlainText('You clicked the button') ## this will set the text in the textBox widget that is placed in 'layout' created by:   self.my_text = qtw.QTextEdit(params)
app = qtw.QApplication([])
mw = PizzaWindow()
app.exec_()

