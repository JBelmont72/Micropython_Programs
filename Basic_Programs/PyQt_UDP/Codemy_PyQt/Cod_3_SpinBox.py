'''
PyQt5 lesson 3 spinBox

different spinBox arguements
    def setStepType(self, stepType: QAbstractSpinBox.StepType) -> None: ...
    def stepType(self) -> QAbstractSpinBox.StepType: ...
    def setDisplayIntegerBase(self, base: int) -> None: ...
    def displayIntegerBase(self) -> int: ...
    textChanged: typing.ClassVar[QtCore.pyqtSignal]
    valueChanged: typing.ClassVar[QtCore.pyqtSignal]
    def setValue(self, val: int) -> None: ...
    def event(self, e: typing.Optional[QtCore.QEvent]) -> bool: ...
    def fixup(self, str: typing.Optional[str]) -> str: ...
    def textFromValue(self, v: int) -> str: ...
    def valueFromText(self, text: typing.Optional[str]) -> int: ...
    def validate(self, input: typing.Optional[str], pos: int) -> typing.Tuple[QtGui.QValidator.State, str, int]: ...
    def setRange(self, min: int, max: int) -> None: ...
    def setMaximum(self, max: int) -> None: ...
    def maximum(self) -> int: ...
    def setMinimum(self, min: int) -> None: ...
    def minimum(self) -> int: ...
    def setSingleStep(self, val: int) -> None: ...
    def singleStep(self) -> int: ...
    def cleanText(self) -> str: ...
    def setSuffix(self, s: typing.Optional[str]) -> None: ...
    def suffix(self) -> str: ...
    def setPrefix(self, p: typing.Optional[str]) -> None: ...
    def prefix(self) -> str: ...
    def value(self) -> int: ...

'''
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Welcome to Jannie's Pizza")
        self.setLayout(qtw.QVBoxLayout())

        self.label = qtw.QLabel("Greetings! What's your name?")
        self.label.setFont(qtg.QFont('Zapfino', 16))
        self.layout().addWidget(self.label)

        self.name_entry = qtw.QLineEdit()
        # self.name_entry.setText('hello')
        self.name_entry.setPlaceholderText("Enter your name")
        self.layout().addWidget(self.name_entry)

        self.button = qtw.QPushButton("Next", clicked=self.go_to_pizza_window)
        self.layout().addWidget(self.button)

        self.show()

    def go_to_pizza_window(self):
        name = self.name_entry.text().strip()
        if name:
            self.pizza_window = PizzaWindow(name)
            self.pizza_window.show()
            self.close()  # or use self.hide() if you want it to still exist in memory

class PizzaWindow(qtw.QWidget):
    def __init__(self, name):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.setLayout(qtw.QVBoxLayout())
        ## create a label, font, and add to LAYOUT
        self.label = qtw.QLabel(f"Welcome {name}! Pick a topping for your pizza.")
        self.label.setFont(qtg.QFont('Zapfino', 16))
        self.layout().addWidget(self.label)
        ## create spinBox
        # self.my_spin=qtw.QSpinBox(self,value=10,maximum=100,minimum=0,singleStep=5, suffix = '#',prefix = '!!!!')
        self.my_spin = qtw.QDoubleSpinBox(self,value=10.11)
        self.my_spin.setFont(qtg.QFont('Arial',20))
        
        self.layout().addWidget(self.my_spin)
        ## creat button and add to layout
        # self.button = qtw.QPushButton("Press Me", clicked= self.press_it) ## clicked = lambda:press_it()
        # self.button = qtw.QPushButton("Press Me", clicked= lambda:self.press_it()) ## clicked = lambda:press_it()
        self.button = qtw.QPushButton("Press Me", clicked=lambda: self.press_it())

        
        self.layout().addWidget(self.button)
## 1st make label which will be used later , 2d make the combo.addition, 3d make a button so that when pressed will call the function and put the combo.addition text in the label!
    ## the combo.addItem is being displayed as the label text when button pressed.
        # self.show()
    def press_it(self):
        spin=self.my_spin.value()
        self.label.setText(f'You picked {spin} %')
    ## use below if I want to pass a value to the press_it()
    # def press_it(self, value):
    #     print(self.my_spin.value())        
    #     spin = f'{self.my_spin.value()} %'       
    #     self.label.setText(f'You picked {spin}, starting from {value}')
    #### if i want the passed value in press_it(47) to affect the count
    # def press_it(self, value):
    #     spin = self.my_spin.value()
        
    #     total = spin + value
    #     self.label.setText(f'You picked {spin}, boosted to {total}')
        

    
    
    
# Optional: Using functools.partial (cleaner alternative to lambda)
# You can also do the same thing more cleanly using functools.partial, like this:

# from functools import partial
# self.button = qtw.QPushButton("Press Me", clicked=partial(self.press_it, 42))
# No difference in behavior — just stylistic preference. partial() is nice when you're passing multiple arguments or want to avoid lambda.
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
