'''


'''
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QDoubleSpinBox, QLabel
)   ####here i am importing SPECIFIC methods from QtWidgets and thus i don't have to specify qtw ( like specifying' machine' versus 'pin')
import PyQt5.QtGui as qtg
from PyQt5.QtCore import Qt

class LambdaTest(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Lambda + SpinBox Test")
        layout = QVBoxLayout()

        self.label = QLabel("Results will appear here.")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)

        # First Spin Box
        self.spin1 = QDoubleSpinBox()
        self.spin1.setRange(0.0, 100.0)
        self.spin1.setSingleStep(0.5)
        self.spin1.setValue(10.0)
        layout.addWidget(self.spin1)

        # Second Spin Box
        self.spin2 = QDoubleSpinBox()
        self.spin2.setRange(0.0, 100.0)
        self.spin2.setSingleStep(0.5)
        self.spin2.setValue(2.0)
        layout.addWidget(self.spin2)

        # Say Hello Button
        btn_hello = QPushButton("Say Hello")
        btn_hello.clicked.connect(lambda: self.say_hello("Sam"))
        layout.addWidget(btn_hello)

        # Double It Button
        btn_double = QPushButton("Double First Value")
        btn_double.clicked.connect(lambda: self.double_it())
        layout.addWidget(btn_double)

        # Multiply Button
        btn_multiply = QPushButton("Multiply Both Values")
        btn_multiply.clicked.connect(lambda: self.multiply())
        layout.addWidget(btn_multiply)

        self.setLayout(layout)
        self.show()

    def say_hello(self, name):
        message = f"Hello, {name}!"
        print(message)
        self.label.setText(message)

    def double_it(self):
        val = self.spin1.value()
        doubled = val * 2
        self.label.setText(f"{val} doubled is {doubled}")
        print(f"{val} doubled is {doubled}")
        self.spin1.setValue(doubled)

    def multiply(self):
        val1 = self.spin1.value()
        val2 = self.spin2.value()
        product = val1 * val2
        self.label.setText(f"{val1} × {val2} = {product}")
        print(f"{val1} × {val2} = {product}")

app = QApplication(sys.argv)
window = LambdaTest()
sys.exit(app.exec_())
