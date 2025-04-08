'''lesson 4 codemay.com   Create Text Boxes PyQt5
  
 below is from Cod_3_Spin.py  great info on spinBox
        ## create spinBox
        # self.my_spin=qtw.QSpinBox(self,value=10,maximum=100,minimum=0,singleStep=5, suffix = '#',prefix = '!!!!')
        self.my_spin = qtw.QDoubleSpinBox(self,value=10.11)
        self.my_spin.setFont(qtg.QFont('Arial',20))       
        self.layout().addWidget(self.my_spin)
        ## creat button and add to layout
        # self.button = qtw.QPushButton("Press Me", clicked= self.press_it) ## clicked = lambda:press_it()
        # self.button = qtw.QPushButton("Press Me", clicked= lambda:self.press_it()) ## clicked = lambda:press_it()
        self.button = qtw.QPushButton("Press Me", clicked=lambda: self.press_it(42))       
        self.layout().addWidget(self.button)
## 1st make label which will be used later , 2d make the combo.addition, 3d make a button so that when pressed will call the function and put the combo.addition text in the label!
    ## the combo.addItem is being displayed as the label text when button pressed.
        # self.show()
    def press_it(self,value):
        spin=self.my_spin.value()
        self.label.setText(f'You picked {spin} %')
    # def press_it(self, value):
    #     print(self.my_spin.value())        
    #     spin = f'{self.my_spin.value()} %'       
    #     self.label.setText(f'You picked {spin}, starting from {value}')

# Optional: Using functools.partial (cleaner alternative to lambda)
# You can also do the same thing more cleanly using functools.partial, like this:

# from functools import partial
# self.button = qtw.QPushButton("Press Me", clicked=partial(self.press_it, 42))
# No difference in behavior — just stylistic preference. partial() is nice when you're passing multiple arguments or want to avoid lambda.
'''

# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg
# #  ## here i am importing all the methods from QtWidgets and thus have to specify qtw ( like specifying' machine' versus 'pin')

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
#             self.pizza_window = PizzaWindow(name)
#             self.pizza_window.show()
#             self.close()


# class PizzaWindow(qtw.QWidget):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name

#         self.setWindowTitle("Pizza Window")
#         self.setLayout(qtw.QVBoxLayout())

#         self.label = qtw.QLabel(f"Type something into the box, {self.name}")
#         self.label.setFont(qtg.QFont('Helvetica', 16))
#         self.layout().addWidget(self.label)

#         self.my_text = qtw.QTextEdit(
#             lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
#             lineWrapColumnOrWidth=75,
#             placeholderText='Hello World',
#             readOnly=False
#         )
#         self.layout().addWidget(self.my_text)

#         self.my_button = qtw.QPushButton("Press Me", clicked=self.press_it)
#         self.layout().addWidget(self.my_button)

#     def press_it(self):
#         typed = self.my_text.toPlainText()
#         self.label.setText(f"{self.name}, you typed: {typed}")


# app = qtw.QApplication([])
# mw = MainWindow()
# app.exec_()
##########~~~~~~~~2 d version of lesson 4 Codemy on textboxes below
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
#  ## here i am importing all the methods from QtWidgets and thus have to specify qtw ( like specifying' machine' versus 'pin')

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Welcome to Jannie's Pizza")
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel("Greetings! What's your name?")
        self.label.setFont(qtg.QFont('Zapfino', 16))
        self.layout().addWidget(self.label)

        self.name_entry = qtw.QLineEdit()
        self.name_entry.setPlaceholderText("Enter your name")
        self.layout().addWidget(self.name_entry)

        # self.button = qtw.QPushButton("Next", clicked=self.go_to_pizza_window)
        self.button = qtw.QPushButton("Next", clicked=lambda:self.go_to_pizza_window())
        self.layout().addWidget(self.button)

        self.show()

    def go_to_pizza_window(self):
        name = self.name_entry.text().strip()
        if name:
            self.pizza_window = PizzaWindow(name)
            self.pizza_window.show()
            self.close()


class PizzaWindow(qtw.QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name

        self.setWindowTitle("Pizza Window")
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel(f"Type something into the box, {self.name}")
        self.label.setFont(qtg.QFont('Helvetica', 16))
        self.layout().addWidget(self.label)

        self.my_text = qtw.QTextEdit(
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=75,
            placeholderText='Hello World',
            readOnly=False
        )
        self.layout().addWidget(self.my_text)

        self.my_button = qtw.QPushButton("Press Me", clicked=self.press_it)
        self.layout().addWidget(self.my_button)

    def press_it(self):
        typed = self.my_text.toPlainText()
        self.label.setText(f"{self.name}, you typed: {typed}")


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()

