'''
CODEMY 2 COMBO BOXES
/Users/judsonbelmont/Documents/SharedFolders/Pico/Micropython_Programs/Basic_Programs/PyQt_UDP/Codemy_PyQt/Cod_2_ComboBox.py
first two are same. the third has a sign in window that then goes to the pizza topping selection list
'''

# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg

# print(qtw.__name__)

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle('Look Jannie! My Pizzeria')
#         self.setLayout(qtw.QVBoxLayout())

#         # Label
#         self.my_label = qtw.QLabel("Pick topping for your pizza")
#         # self.my_label = qtw.QLabel("Greetings to All! What's your Name")
#         self.my_label.setFont(qtg.QFont('Zapfino', 18))
#         self.layout().addWidget(self.my_label)
#         ## NEW ADDITION OF COMBO BOX
#         self.my_combo = qtw.QComboBox(self)
#         ## add items to the Combo Box
#         self.my_combo.addItem('Pepperoni', 1)
#         self.my_combo.addItem('Cheese', 'new item')
#         self.my_combo.addItem('Peppers',qtw.QWidget)
#         self.my_combo.addItem('Hamburger')
#         # my_combo = qtw.QComboBox(self)
#         # ## add items to the Combo Box
#         # my_combo.addItem('Pepperoni', 1)
#         # my_combo.addItem('Cheese', 'new item')
#         # my_combo.addItem('Peppers',qtw.QWidget)
#         # my_combo.addItem('Hamburger')
#         ## put combo box on screeen
#         self.layout().addWidget(self.my_combo)
        
        
#         # # Entry field
#         # self.my_entry = qtw.QLineEdit()
#         # self.my_entry.setObjectName('name_field')
#         # self.my_entry.setPlaceholderText('Enter your name')  # <--- use this instead of setText
#         # self.layout().addWidget(self.my_entry)

#         # Button
#         my_button = qtw.QPushButton('Press Me', clicked=self.press_it)
#         self.layout().addWidget(my_button)

#         self.show()

#     # def press_it(self):
#     #     ## add name to label for the pizza
#     #     self.my_label.setText('You Picked ',self.my_combo.currenText())
#     # def press_it(self):
#     #     picked = self.my_combo.currentText()
#     #     self.my_label.setText(f'You Picked {picked}')    
#     def press_it(self):
#         topping = self.my_combo.currentText()
#         extra_info = self.my_combo.currentData()
#         self.my_label.setText(f'You Picked {topping} ({extra_info})')

#         # entered_name = self.my_entry.text()
#         # if entered_name:  # Only respond if there's actual input
#         #     self.my_label.setText(f'Hello {entered_name}, Welcome')
#         #     self.my_entry.clear()

# app = qtw.QApplication([])
# mw = MainWindow()
# app.exec_()

###### Revised version

import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

print(qtw.__name__)

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Look Jannie! My Pizzeria')
        self.setLayout(qtw.QVBoxLayout())

        # Label
        self.my_label = qtw.QLabel("Pick topping for your pizza")
        self.my_label.setFont(qtg.QFont('Zapfino', 18))
        self.layout().addWidget(self.my_label)

        # Combo Box
        self.my_combo = qtw.QComboBox(self)
        self.my_combo.addItem('Pepperoni', 1)
        self.my_combo.addItem('Cheese', 'new item')
        self.my_combo.addItem('Peppers', qtw.QWidget)
        self.my_combo.addItem('Hamburger')
        self.layout().addWidget(self.my_combo)

        # Button
        my_button = qtw.QPushButton('Press Me', clicked=self.press_it)
        self.layout().addWidget(my_button)

        self.show()

    def press_it(self):
        picked = self.my_combo.currentText()
        self.my_label.setText(f'You Picked {picked}')

app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
####
# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Welcome to Jannie's Pizza")
#         self.setLayout(qtw.QVBoxLayout())

#         self.label = qtw.QLabel("Greetings! What's your name?")
#         self.label.setFont(qtg.QFont('Zapfino', 16))
#         self.layout().addWidget(self.label)

#         self.name_entry = qtw.QLineEdit()
#         # self.name_entry.setText('hello')
#         self.name_entry.setPlaceholderText("Enter your name")
#         self.layout().addWidget(self.name_entry)

#         self.button = qtw.QPushButton("Next", clicked=self.go_to_pizza_window)
#         self.layout().addWidget(self.button)

#         self.show()

#     def go_to_pizza_window(self):
#         name = self.name_entry.text().strip()
#         if name:
#             self.pizza_window = PizzaWindow(name)
#             self.pizza_window.show()
#             self.close()  # or use self.hide() if you want it to still exist in memory

# class PizzaWindow(qtw.QWidget):
#     def __init__(self, name):
#         super().__init__()

#         self.setWindowTitle("Pick Your Toppings")
#         self.setLayout(qtw.QVBoxLayout())
#         ## create a label, font, and add to LAYOUT
#         self.label = qtw.QLabel(f"Welcome {name}! Pick a topping for your pizza.")
#         self.label.setFont(qtg.QFont('Zapfino', 16))
#         self.layout().addWidget(self.label)
#         ## create a comboBox, addItems, add to LAYOUT
#         # self.combo = qtw.QComboBox(self)
#         self.combo = qtw.QComboBox(self,editable=True, insertPolicy=qtw.QComboBox.InsertAtBottom)
#         self.combo.addItem('Pepperoni', 1)
#         self.combo.addItem('Cheese', 'Classic')
#         self.combo.addItem('Peppers', 'Spicy')
#         self.combo.addItem('Hamburger', 'Savory')
#         # self.combo.addItems(['Meatballs', 'Shrimp' ,'Hot Peppers]')
#         self.combo.insertItem(2,'Third Cheese Medley')
#         self.combo.insertItems(3,['four meats','five spice special']) 
#         self.layout().addWidget(self.combo)
#         ## creat buitton and add to layout
#         self.button = qtw.QPushButton("Press Me", clicked=self.show_selection)
#         self.layout().addWidget(self.button)
# ## 1st make label which will be used later , 2d make the combo.addition, 3d make a button so that when pressed will call the function and put the combo.addition text in the label!
#     ## the combo.addItem is being displayed as the label text when button pressed.
#     def show_selection(self):
#         topping = self.combo.currentText()
#         extra_info = self.combo.currentData()
#         self.label.setText(f'You Picked {topping} ({extra_info})')
#     # def show_selection(self):
#     #     topping = self.combo.currentText()
#     #     self.label.setText(f'You Picked {topping}!')

# app = qtw.QApplication([])
# mw = MainWindow()
# app.exec_()
