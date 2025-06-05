'''
pythonguis.com

remember any widget can be a window. a pushbutton can be the whole window for example
'''

## NOTE Below is the template from Alan D Moore that i like
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)## positional arguements, keyword arguemants, this calls the parent arguements and methods
        ##need this to call the parent class!!
        # Your code will go here
        # Create a button and set its text
        button = qtw.QPushButton("Press Me!")

        # Set the central widget of the Window.
        # This is the widget that will be displayed in the window.
        # The central widget is the main widget of the window.
        # In this case, we are using a vertical box layout to arrange the button.
        # The layout will automatically resize the button to fit the window.
        self.setLayout(qtw.QVBoxLayout())
        self.layout().addWidget(button)
        # Create a horizontal layout to group more widgets
        h_layout = qtw.QHBoxLayout()
        
        # Add widgets to the horizontal layout, first create the widgets,then add them to h_layout(created above)
        label = qtw.QLabel("Label:")
        line_edit = qtw.QLineEdit('edit me')
        h_layout.addWidget(label)
        h_layout.addWidget(line_edit)
        ## Create another layout and name it h2_layout
        h2_layout = qtw.QHBoxLayout()
        # create 2 widgets and Add widgets to the second horizontal layout
        label2 = qtw.QLabel("Label 2:")
        line_edit2 = qtw.QLineEdit('edit me too')
        h2_layout.addWidget(label2)
        h2_layout.addWidget(line_edit2)
        # Add the second horizontal layout to the first horizontal layout
        h_layout.addLayout(h2_layout)## this places the second horizontal layout inside the first horizontal layout next to the first horizontal layout
        ### in 1_A_guis.py i added the second horizontal layout to the main vertical layout just to see what would happen
        # Add the horizontal layout to the main vertical layout!!!
        self.layout().addLayout(h_layout)## earlier i added a button (  self.layout().addWidget(button)  ) to the main vertical layout, now i am adding the horizontal layout to the main vertical layout
        
        h2_layout.addStretch(1)  # Add stretchable space to the right of the horizontal layout
        
        
        # Add another button to the main vertical layout
        another_button = qtw.QPushButton("Another Button")
        self.layout().addWidget(another_button)
        # Set the window title
        # self.setWindowTitle("Hello World")## thias wopuld reset the window title
        # Set the window size
        self.resize(800, 600)
        # Set the window icon
        # icon = qtg.QIcon("path/to/icon.png")  # Load an icon from a file
        # self.setWindowIcon(icon)  # Set the window icon
        # Set the window font
        # font = qtg.QFont("Arial", 12)  # Create a font object with the desired font family and size
        # self.setFont(font)  # Set the font for the window

        # Your code ends here
        self.show() ## put it here so the window shows.


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow(windowTitle='My Window')
    sys.exit(app.exec_())   ## exit status tells if the program exited with or without mistakes, app.exec_()  starrts the event loop
'''we create an instance of QApplication, passing in sys.argv, which is Python list containing the command line arguments passed to the application.

PYTHON
app = QApplication(sys.argv)
If you know you won't be using command line arguments to control Qt you can pass in an empty list instead, e.g.

PYTHON
app = QApplication([])


Next we create an instance of a QWidget using the variable name w    w = MainWindow(windowTitle='My Window')  
In Qt all top level widgets are windows -- that is, they don't have a parent and are not nested within another widget or layout. This means you can technically create a window using any widget you like.

Widgets without a parent are invisible by default. So, after creating the window object, we must always call .show() to make it visible. You can remove the .show() and run the app, but you'll have no way to quit it!   
'''

''''
JBelmont72: why do we not use   # Set the central widget of the Window.
        self.setCentralWidget(button)

GitHub.copilot-chat.github.copilot.editor: The reason you are not using `self.setCentralWidget(button)` in this code is because the class you are working with likely inherits from `QWidget` instead of `QMainWindow`. Let me explain the difference:

### 1. **`QMainWindow` vs `QWidget`**
   - **`QMainWindow`**: This class is designed for creating main application windows. It has a built-in concept of a "central widget," which is set using `self.setCentralWidget()`. This central widget is the main area of the window, and additional features like toolbars, menus, and status bars can be added around it.
   - **`QWidget`**: This is a more general-purpose widget class. It does not have the concept of a "central widget." Instead, you directly set a layout (e.g., `QVBoxLayout`) and add child widgets to that layout.

### 2. **Your Code**
In your code, you are using `self.setLayout(qtw.QVBoxLayout())` to set a layout for the window and then adding the button to that layout. This approach is typical when working with `QWidget` because `QWidget` does not support `setCentralWidget()`.

If your class inherits from `QMainWindow`, you would use `self.setCentralWidget(button)` to set the button as the main widget of the window. However, in that case, you wouldn't use `setLayout()` because `QMainWindow` does not allow setting a layout directly.

### 3. **When to Use `setCentralWidget()`**
You would use `self.setCentralWidget()` if:
   - Your class inherits from `QMainWindow`.
   - You want to set a single widget (like a button or a layout container) as the main content of the window.

### Example Comparison

#### Using `QWidget` (Your Current Approach):
```python
import PyQt5.QtWidgets as qtw

class MyWidget(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setLayout(qtw.QVBoxLayout())
        button = qtw.QPushButton("Press Me!")
        self.layout().addWidget(button)
        self.resize(800, 600)
```

#### Using `QMainWindow` with `setCentralWidget()`:
```python
import PyQt5.QtWidgets as qtw

class MyMainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        button = qtw.QPushButton("Press Me!")
        self.setCentralWidget(button)
        self.resize(800, 600)
```

### Key Takeaway
- Use `setLayout()` if your class inherits from `QWidget`.
- Use `setCentralWidget()` if your class inherits from `QMainWindow`.
'''