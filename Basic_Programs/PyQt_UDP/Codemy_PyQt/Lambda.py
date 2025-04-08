'''  this is lambda practice   I also have good examples in Cod_1.py  where I have multiple versions for button control '''


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QDoubleSpinBox, QLabel
)

class LambdaTest(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda Test")
        layout = QVBoxLayout()

        self.name = 'Sam'
        self.num = 10
        self.num2 = 2

        # buttonBox=QHBoxLayout()     ## this goes inside the widgetBox, this creates the  buttonBox object.
# widgetBox.addLayout(buttonBox)  ## adds the buttonBox  to inside the widgetBox, this places the buttonBox
## the widgetBox at this point is empty, next create a button below. NOTE that below we add 'widgetBox.addLayout(buttonBox) near end!!!!
## what this does is add the 'buttonBox' to inside the widgetBox(which has already been added to the 'window') You can see this a few lines up where 'widgetBox=QVBoxLayout(window)' appears
        blueButton = QPushButton('Blue Button')
        blueButton.setStyleSheet('background-color: blue;color: white;')## the format is very specific!!
        blueButton.clicked.connect(self.say_hello)##this worked but could not pass a value
        # blueButton.clicked.connect((lambda:self.say_hello('name'))) ## this works and can pass a value!!
        
        ## the blue buttton is created but now has to be added to the widgetBox
        ## the BUTTON is added to the BUTTONBOX, the ButtonBOx  is added to the WidgetBox
        ## and finally the widgetBox is added to the WINDOQ
        layout.addWidget(blueButton)



        # Label for showing spin box changes
        self.label = QLabel("Change the value in the spin box")
        layout.addWidget(self.label)

        # QDoubleSpinBox setup
        self.my_spin = QDoubleSpinBox()
        self.my_spin.setDecimals(2)
        self.my_spin.setSingleStep(0.1)
        self.my_spin.setValue(10.11)
        # self.my_spin.valueChanged.connect(self.spin_box_changed)      ## this works
        # self.my_spin.valueChanged.connect(lambda :self.spin_box_changed)## note this does not work! look in Notes_PyQt.md
        self.my_spin.valueChanged.connect(lambda val: self.spin_box_changed(val))## works

        layout.addWidget(self.my_spin)

        # Button 1 - Say Hello
        btn_hello = QPushButton("Say Hello")
        btn_hello.clicked.connect(lambda: self.say_hello(self.name))
        layout.addWidget(btn_hello)

        # Button 2 - Double a number
        btn_double = QPushButton("Double It")
        btn_double.clicked.connect(lambda: self.double_it(self.num))
        layout.addWidget(btn_double)

        # Button 3 - Multiply two numbers
        btn_multiply = QPushButton("Multiply 10 × 2")
        btn_multiply.clicked.connect(lambda: self.multiply(self.num, self.num2))
        layout.addWidget(btn_multiply)

        self.setLayout(layout)
        self.show()

    def say_hello(self, name):
        print(f"Hello, {name}!")

    def double_it(self, number):
        print(f"Double of {number} is {number * 2}")
        self.num += number

    def multiply(self, a, b):
        print(f"{a} × {b} = {a * b}")
        self.num +=b

    def spin_box_changed(self, newVal):
        oldVal = self.num  # just for demonstration
        print(f"SpinBox changed from {oldVal} to {newVal}")
        self.label.setText(f"Old value: {oldVal}, New value: {newVal:.2f}")
        self.num = newVal  # update num to the new value
  


app = QApplication(sys.argv)
window = LambdaTest()
sys.exit(app.exec_())


'''
class QDoubleSpinBox(QAbstractSpinBox):

    def __init__(self, parent: typing.Optional[QWidget] = ...) -> None: ...

    def setStepType(self, stepType: QAbstractSpinBox.StepType) -> None: ...
    def stepType(self) -> QAbstractSpinBox.StepType: ...
    textChanged: typing.ClassVar[QtCore.pyqtSignal]
    valueChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setValue(self, val: float) -> None: ...
    def fixup(self, str: typing.Optional[str]) -> str: ...
    def textFromValue(self, v: float) -> str: ...
    def valueFromText(self, text: typing.Optional[str]) -> float: ...
    def validate(self, input: typing.Optional[str], pos: int) -> typing.Tuple[QtGui.QValidator.State, str, int]: ...
    def setDecimals(self, prec: int) -> None: ...
    def decimals(self) -> int: ...
    def setRange(self, min: float, max: float) -> None: ...
    def setMaximum(self, max: float) -> None: ...
    def maximum(self) -> float: ...
    def setMinimum(self, min: float) -> None: ...
    def minimum(self) -> float: ...
    def setSingleStep(self, val: float) -> None: ...
    def singleStep(self) -> float: ...
    def cleanText(self) -> str: ...
    def setSuffix(self, s: typing.Optional[str]) -> None: ...
    def suffix(self) -> str: ...
    def setPrefix(self, p: typing.Optional[str]) -> None: ...
    def prefix(self) -> str: ...
    def value(self) -> float: ...

Improve and clean up the double_it() and multiply() logic so they actually update the values.
Add a second QDoubleSpinBox to control both values dynamically.
Display the updated result in a label.
'''
# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QPushButton,
#     QDoubleSpinBox, QLabel
# )
# from PyQt5.QtCore import Qt

# class LambdaTest(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Lambda + SpinBox Test")
#         self.setGeometry(10, 100, 400, 400)
        
        
#         self.widgetBox=QVBoxLayout()## will work on these later to segregate gui sections
#         self.buttonBox=QVBoxLayout() 
      
#         layout = QVBoxLayout()
        
#         self.label = QLabel("Results will appear here.")
#         self.label.setAlignment(Qt.AlignCenter)
#         layout.addWidget(self.label)
        
#         # First Spin Box
#         self.spin1 = QDoubleSpinBox()
#         self.spin1.setRange(0.0, 100.0)
#         self.spin1.setSingleStep(0.5)
#         self.spin1.setValue(10.0)
#         layout.addWidget(self.spin1)

#         # Second Spin Box
#         self.spin2 = QDoubleSpinBox()
#         self.spin2.setRange(0.0, 100.0)
#         self.spin2.setSingleStep(0.5)
#         self.spin2.setValue(2.0)
#         layout.addWidget(self.spin2)

#         # Say Hello Button
#         btn_hello = QPushButton("Say Hello")
#         btn_hello.clicked.connect(lambda: self.say_hello("Sam"))
#         layout.addWidget(btn_hello)

#         # Double It Button
#         btn_double = QPushButton("Double First Value")
#         btn_double.clicked.connect(lambda: self.double_it())
#         layout.addWidget(btn_double)

#         # Multiply Button
#         btn_multiply = QPushButton("Multiply Both Values")
#         btn_multiply.clicked.connect(lambda: self.multiply())
#         layout.addWidget(btn_multiply)

#         self.setLayout(layout)
#         self.buttonBox.addStretch()
#         self.show()

#     def say_hello(self, name):
#         message = f"Hello, {name}!"
#         print(message)
#         self.label.setText(message)

#     def double_it(self):
#         val = self.spin1.value()
#         doubled = val * 2
#         self.label.setText(f"{val} doubled is {doubled}")
#         print(f"{val} doubled is {doubled}")
#         self.spin1.setValue(doubled)

#     def multiply(self):
#         val1 = self.spin1.value()
#         val2 = self.spin2.value()
#         product = val1 * val2
#         self.label.setText(f"{val1} × {val2} = {product}")
#         print(f"{val1} × {val2} = {product}")

# app = QApplication(sys.argv)
# window = LambdaTest()
# sys.exit(app.exec_())

