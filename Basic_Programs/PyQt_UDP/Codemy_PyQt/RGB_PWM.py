'''
PyQt5 interface that:
Uses spin boxes with a range of 0–255 for R, G, and B values.
Adds sliders for the same values alongside the spin boxes.
Shows a live preview of the color using a QLabel with background color.
This can also be found in Notes_PyQt5.md
'''
# import sys  ### Program 1  beginning at line 423 is a discussion of alternative means to accompish this
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
#     QLabel, QSlider, QSpinBox
# )
# from PyQt5.QtCore import Qt

# class RGBController(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("RGB LED Controller")

#         layout = QVBoxLayout()
#         self.setLayout(layout)

#         self.color_preview = QLabel()
#         self.color_preview.setFixedHeight(100)
#         self.color_preview.setStyleSheet("background-color: rgb(0, 0, 0);")
#         layout.addWidget(self.color_preview)

#         self.r_spin, self.g_spin, self.b_spin = QSpinBox(), QSpinBox(), QSpinBox()
#         self.r_slider, self.g_slider, self.b_slider = QSlider(Qt.Horizontal), QSlider(Qt.Horizontal), QSlider(Qt.Horizontal)

#         for spin, slider, color in zip(
#             [self.r_spin, self.g_spin, self.b_spin],
#             [self.r_slider, self.g_slider, self.b_slider],
#             ['Red', 'Green', 'Blue']
#         ):
#             spin.setRange(0, 255)
#             slider.setRange(0, 255)
#             spin.setValue(128)
#             slider.setValue(128)

#             # Sync spin box and slider
#             spin.valueChanged.connect(slider.setValue)
#             slider.valueChanged.connect(spin.setValue)
#             slider.valueChanged.connect(self.update_color_preview)

#             row = QHBoxLayout()
#             row.addWidget(QLabel(color))
#             row.addWidget(spin)
#             row.addWidget(slider)
#             layout.addLayout(row)

#         self.update_color_preview()

#     def update_color_preview(self):
#         r = self.r_spin.value()
#         g = self.g_spin.value()
#         b = self.b_spin.value()
#         self.color_preview.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")


# app = QApplication(sys.argv)
# window = RGBController()
# window.show()
# sys.exit(app.exec_())

# What You’ll Learn Through This:
# How to synchronize a slider with a spin box.
# How to dynamically update UI elements (like color previews).
# How to use RGB to represent color with a QLabel.
# Would you like to add PWM output later to send these values to a Pico W or just continue building the UI for now?

# build the UI   a complete PyQt5 UI that lets you:
# Adjust Red, Green, and Blue values using both QSpinBox and QSlider
# Preview the resulting RGB color in a QLabel that updates in real time

# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
#     QLabel, QSpinBox, QSlider
# )
# from PyQt5.QtCore import Qt

# class RGBController(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("RGB LED Controller")
#         self.setGeometry(100, 100, 400, 300)

#         main_layout = QVBoxLayout()
#         self.color_preview = QLabel()
#         self.color_preview.setFixedHeight(100)
#         self.color_preview.setStyleSheet("background-color: rgb(0, 0, 0); border: 1px solid black;")
#         main_layout.addWidget(self.color_preview)

#         # Create layouts for Red, Green, Blue controls
#         self.red_spin, self.red_slider = self.create_rgb_control("Red", main_layout)
#         self.green_spin, self.green_slider = self.create_rgb_control("Green", main_layout)
#         self.blue_spin, self.blue_slider = self.create_rgb_control("Blue", main_layout)

#         self.setLayout(main_layout)
#         self.update_color()

#     def create_rgb_control(self, label_text, parent_layout):
#         layout = QHBoxLayout()
#         label = QLabel(label_text)
#         label.setFixedWidth(40)

#         spin_box = QSpinBox()
#         spin_box.setRange(0, 255)
#         spin_box.setValue(0)

#         slider = QSlider(Qt.Horizontal)
#         slider.setRange(0, 255)
#         slider.setValue(0)

#         # Sync spin box and slider
#         spin_box.valueChanged.connect(slider.setValue)
#         slider.valueChanged.connect(spin_box.setValue)

#         # Update preview when value changes
#         spin_box.valueChanged.connect(self.update_color)

#         layout.addWidget(label)
#         layout.addWidget(spin_box)
#         layout.addWidget(slider)
#         parent_layout.addLayout(layout)

#         return spin_box, slider

#     def update_color(self):
#         r = self.red_spin.value()
#         g = self.green_spin.value()
#         b = self.blue_spin.value()
#         self.color_preview.setStyleSheet(f"background-color: rgb({r}, {g}, {b}); border: 1px solid black;")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = RGBController()
#     window.show()
#     sys.exit(app.exec_())

# Next:  hook up the RGB values to control a physical RGB LED via serial or Wi-Fi using your Pico W.
# Add a "Send to LED" button if you'd like to simulate actual control logic.
# Would you like to add that next or maybe save and recall preset colors?
######~~~~~~~~~~~~~~~~~~~~~~~~~~~
# What’s Next?
# You can hook up the RGB values to control a physical RGB LED via serial or Wi-Fi using your Pico W.
# Add a "Send to LED" button if you'd like to simulate actual control logic.
# Would you like to add that next or maybe save and recall preset colors?


# Next: add a 'send to Led ' button to send the three values chosen

# Updated PyQt5 UI with a "Send to LED" button that, when clicked, will print the current RGB values to the console (simulating sending the data to a real LED controller, like a Pico W):
# ✅ Additions:
# A QPushButton labeled "Send to LED"
# A method send_to_led() that grabs the current RGB values and prints them
# 🧠 You can later replace the print statement with a real communication method (e.g., serial, MQTT, or socket).
# ✅ Updated Code:

# import sys
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
#     QLabel, QSpinBox, QSlider, QPushButton
# )
# from PyQt5.QtCore import Qt

# class RGBController(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("RGB LED Controller")
#         self.setGeometry(100, 100, 400, 350)

#         main_layout = QVBoxLayout()

#         # Color Preview
#         self.color_preview = QLabel()
#         self.color_preview.setFixedHeight(100)
#         self.color_preview.setStyleSheet("background-color: rgb(0, 0, 0); border: 1px solid black;")
#         main_layout.addWidget(self.color_preview)

#         # Create RGB controls
#         self.red_spin, self.red_slider = self.create_rgb_control("Red", main_layout)
#         self.green_spin, self.green_slider = self.create_rgb_control("Green", main_layout)
#         self.blue_spin, self.blue_slider = self.create_rgb_control("Blue", main_layout)

#         # Send to LED Button
#         send_button = QPushButton("Send to LED")
#         send_button.clicked.connect(self.send_to_led)
#         main_layout.addWidget(send_button)

#         self.setLayout(main_layout)
#         self.update_color()

#     def create_rgb_control(self, label_text, parent_layout):
#         layout = QHBoxLayout()
#         label = QLabel(label_text)
#         label.setFixedWidth(40)

#         spin_box = QSpinBox()
#         spin_box.setRange(0, 255)
#         spin_box.setValue(0)

#         slider = QSlider(Qt.Horizontal)
#         slider.setRange(0, 255)
#         slider.setValue(0)

#         # Sync values
#         spin_box.valueChanged.connect(slider.setValue)
#         slider.valueChanged.connect(spin_box.setValue)
#         spin_box.valueChanged.connect(self.update_color)

#         layout.addWidget(label)
#         layout.addWidget(spin_box)
#         layout.addWidget(slider)
#         parent_layout.addLayout(layout)

#         return spin_box, slider

#     def update_color(self):
#         r = self.red_spin.value()
#         g = self.green_spin.value()
#         b = self.blue_spin.value()
#         self.color_preview.setStyleSheet(f"background-color: rgb({r}, {g}, {b}); border: 1px solid black;")

#     def send_to_led(self):
#         r = self.red_spin.value()
#         g = self.green_spin.value()
#         b = self.blue_spin.value()
#         print(f"Sending to LED: R={r}, G={g}, B={b}")
#         # Later: replace this with actual code to send to the Pico W

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = RGBController()
#     window.show()
#     sys.exit(app.exec_())
#############~~~~~~~~~~~~~~~~~~~~~~~~~
# Options to consider in future;
# Replace the print with UDP or MQTT message sending?
# Store these RGB values as a preset and recall later?
# Add a live color name label (like "Orange", "Purple", etc.)?

# Next below add both UPD and MQTT sending, and a pico W server /subscriber separate programs for the  MQTT and UPD(please keep the server programs separate for readability) 

# ✅ PyQt5 RGB Controller (UDP + MQTT)
# This GUI app:
# Lets you set RGB values (0–255) via spin boxes and sliders.
# Shows a live color preview.
# Sends RGB values when "Send to LED" is clicked via both UDP and MQTT.

### rgb_gui_controller.py       MQTT publisher and UPD client combined
# import sys
# import socket
# import json
# import paho.mqtt.client as mqtt
# from PyQt5.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout,
#     QLabel, QSlider, QSpinBox, QPushButton
# )
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QColor

# MQTT_BROKER = "192.168.1.100"  # change to your MQTT broker IP
# MQTT_TOPIC = "led/rgb"
# UDP_IP = "192.168.1.101"       # Pico W IP for UDP
# UDP_PORT = 5005

# class RGBController(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("RGB LED Controller (UDP + MQTT)")
#         layout = QVBoxLayout()

#         self.color_preview = QLabel("Color Preview")
#         self.color_preview.setStyleSheet("background-color: #000; color: white; font-size: 18px;")
#         self.color_preview.setAlignment(Qt.AlignCenter)
#         layout.addWidget(self.color_preview)

#         self.rgb = {"R": 0, "G": 0, "B": 0}
#         self.spinners = {}

#         for color in ["R", "G", "B"]:
#             row = QHBoxLayout()
#             label = QLabel(color)
#             spin = QSpinBox()
#             slider = QSlider(Qt.Horizontal)
#             spin.setRange(0, 255)
#             slider.setRange(0, 255)

#             spin.valueChanged.connect(lambda val, c=color: self.update_color(c, val))
#             slider.valueChanged.connect(lambda val, c=color: self.update_color(c, val))
#             spin.valueChanged.connect(slider.setValue)
#             slider.valueChanged.connect(spin.setValue)

#             self.spinners[color] = spin
#             row.addWidget(label)
#             row.addWidget(spin)
#             row.addWidget(slider)
#             layout.addLayout(row)

#         send_btn = QPushButton("Send to LED")
#         send_btn.clicked.connect(self.send_rgb_values)
#         layout.addWidget(send_btn)

#         self.setLayout(layout)
#         self.mqtt_client = mqtt.Client()
#         self.mqtt_client.connect(MQTT_BROKER)

#     def update_color(self, channel, value):
#         self.rgb[channel] = value
#         color = QColor(self.rgb["R"], self.rgb["G"], self.rgb["B"])
#         self.color_preview.setStyleSheet(f"background-color: {color.name()}; color: white;")

#     def send_rgb_values(self):
#         message = json.dumps(self.rgb)
#         # MQTT
#         self.mqtt_client.publish(MQTT_TOPIC, message)
#         print(f"[MQTT] Sent: {message}")

#         # UDP
#         udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         udp_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))
#         udp_socket.close()
#         print(f"[UDP] Sent: {message}")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = RGBController()
#     window.show()
#     sys.exit(app.exec_())
    
################ MicroPython - Pico W UDP Server
######!!!!!!!!!!! pico_udp_server.py below
# import socket
# import json
# import machine

# led_r = machine.PWM(machine.Pin(15))
# led_g = machine.PWM(machine.Pin(14))
# led_b = machine.PWM(machine.Pin(13))
# for led in (led_r, led_g, led_b):
#     led.freq(1000)

# def set_rgb(r, g, b):
#     led_r.duty_u16(int(r / 255 * 65535))
#     led_g.duty_u16(int(g / 255 * 65535))
#     led_b.duty_u16(int(b / 255 * 65535))

# addr = socket.getaddrinfo('0.0.0.0', 5005)[0][-1]
# udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# udp.bind(addr)
# print("UDP server listening...")

# while True:
#     data, addr = udp.recvfrom(1024)
#     try:
#         rgb = json.loads(data.decode())
#         print("Received:", rgb)
#         set_rgb(rgb["R"], rgb["G"], rgb["B"])
#     except:
#         print("Invalid data")
########~~~~~~~~~~~~~~~~~~
### MicroPython - Pico W MQTT Subscriber below
# pico_mqtt_subscriber.py
# import network
# import time
# import json
# import machine
# from umqtt.simple import MQTTClient

# WIFI_SSID = 'YOUR_WIFI_SSID'
# WIFI_PASS = 'YOUR_WIFI_PASS'
# MQTT_BROKER = '192.168.1.100'
# MQTT_TOPIC = b'led/rgb'

# led_r = machine.PWM(machine.Pin(15))
# led_g = machine.PWM(machine.Pin(14))
# led_b = machine.PWM(machine.Pin(13))
# for led in (led_r, led_g, led_b):
#     led.freq(1000)

# def set_rgb(r, g, b):
#     led_r.duty_u16(int(r / 255 * 65535))
#     led_g.duty_u16(int(g / 255 * 65535))
#     led_b.duty_u16(int(b / 255 * 65535))

# def on_message(topic, msg):
#     print("MQTT received:", msg)
#     try:
#         rgb = json.loads(msg.decode())
#         set_rgb(rgb["R"], rgb["G"], rgb["B"])
#     except:
#         print("Failed to parse message")

# # Connect to Wi-Fi
# sta = network.WLAN(network.STA_IF)
# sta.active(True)
# sta.connect(WIFI_SSID, WIFI_PASS)
# while not sta.isconnected():
#     time.sleep(1)
# print("Connected to WiFi")

# # MQTT client
# client = MQTTClient("pico", MQTT_BROKER)
# client.set_callback(on_message)
# client.connect()
# client.subscribe(MQTT_TOPIC)
# print("Subscribed to", MQTT_TOPIC)

# while True:
#     client.check_msg()
#     time.sleep(0.1)
### Would you like help flashing these to your Pico W or testing from the PyQt5 GUI?


##### below is a look at the first program above using lambda functions and looking at alternatives for calling the update rgb function::

# Why is self.update_color_preview() called without arguments?
# Your current method is defined as:
# python
# Copy
# Edit
# def update_color_preview(self):
#     r = self.r_spin.value()
#     g = self.g_spin.value()
#     b = self.b_spin.value()
#     self.color_preview.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")
# It gets the values from the spin boxes directly. That’s why you can call it without any arguments.
# ✅ Yes, You Could Use a Lambda to Pass Values
# If you want update_color_preview to accept r, g, b values directly (instead of reading from spin boxes), you could rewrite it like this:
# python
# Copy
# Edit
# def update_color_preview(self, r, g, b):
#     self.color_preview.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")
# Then connect the slider like so:
# python
# Copy
# Edit
# slider.valueChanged.connect(lambda val, s=spin, c=color: self.update_color_preview(
#     self.r_spin.value(),
#     self.g_spin.value(),
#     self.b_spin.value()
# ))
# But here's the twist: this doesn’t actually give you a new r, g, or b value at the moment the slider changes, because lambda captures the current values when it's created, not when it's run (unless you design it carefully).
# So here's a better version using lambda that ensures updated values are passed when the slider is moved:
# python
# Copy
# Edit
# slider.valueChanged.connect(lambda val, s=spin: self.update_color_preview(
#     self.r_spin.value(),
#     self.g_spin.value(),
#     self.b_spin.value()
# ))
# This works fine because it captures the current spin values at the time of the call. You don't need the val unless you’re debugging or displaying it somewhere.
# 🚨 When is this lambda useful?
# This lambda approach makes more sense if:
# You want to separate the model (spin values) from the preview logic.
# You might have another widget (like RGB input fields) calling the same function with arbitrary values.
# You want to reuse the preview function for testing or animation.
# But if you always pull from the spin boxes or sliders, your original method is totally fine—and simpler.
# ✅ TL;DR
# ✔️ Yes, you can use a lambda to pass values explicitly to update_color_preview(r, g, b)
# But if the values always come from the widgets, the no-argument version is cleaner.
# Use lambda when:
# You're feeding r, g, b from different sources.
# You want to be more explicit or flexible
# rewrite your PyQt5 RGBController the first program in this folder  so that:
# The update_color_preview() method accepts RGB values as parameters.
# We use lambda functions in signal connections to pass current values to it.
# Instead of this:

# slider.valueChanged.connect(self.update_color_preview)
# We’ll use:

# slider.valueChanged.connect(lambda _: self.update_color_preview(
#     self.r_spin.value(),
#     self.g_spin.value(),
#     self.b_spin.value()
# ))
# This calls the function with the latest values.

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QSlider, QSpinBox
)
from PyQt5.QtCore import Qt

class RGBController(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RGB LED Controller")

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.color_preview = QLabel()
        self.color_preview.setFixedHeight(100)
        self.color_preview.setStyleSheet("background-color: rgb(0, 0, 0);")
        layout.addWidget(self.color_preview)

        self.r_spin, self.g_spin, self.b_spin = QSpinBox(), QSpinBox(), QSpinBox()
        self.r_slider, self.g_slider, self.b_slider = QSlider(Qt.Horizontal), QSlider(Qt.Horizontal), QSlider(Qt.Horizontal)

        for spin, slider, color in zip(
            [self.r_spin, self.g_spin, self.b_spin],
            [self.r_slider, self.g_slider, self.b_slider],
            ['Red', 'Green', 'Blue']
        ):
            spin.setRange(0, 255)
            slider.setRange(0, 255)
            spin.setValue(128)
            slider.setValue(128)

            # Sync spin box and slider
            spin.valueChanged.connect(slider.setValue)
            slider.valueChanged.connect(spin.setValue)

            # Use lambda to pass current values to the function
            slider.valueChanged.connect(lambda _, s=spin: self.update_color_preview(
                self.r_spin.value(),
                self.g_spin.value(),
                self.b_spin.value()
            ))

            row = QHBoxLayout()
            row.addWidget(QLabel(color))
            row.addWidget(spin)
            row.addWidget(slider)
            layout.addLayout(row)

        # Call once to set initial color
        self.update_color_preview(
            self.r_spin.value(),
            self.g_spin.value(),
            self.b_spin.value()
        )

    def update_color_preview(self, r, g, b):
        self.color_preview.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")


app = QApplication(sys.argv)
window = RGBController()
window.show()
sys.exit(app.exec_())
# Above used lambda _, s=spin: — the _ is needed because valueChanged passes a parameter (the new value), but we don’t actually need it here.
# The method is now more flexible—it doesn’t depend on UI widgets directly.
# This pattern is useful when you want clean separation between UI state and logic, or when you plan to reuse the color function elsewhere.
## ihad another question:I do not understand # Use lambda to pass current values to the function
#             slider.valueChanged.connect(lambda _, s=spin: self.update_color_preview(
#                 self.r_spin.value(),
#                 self.g_spin.value(),
#                 self.b_spin.value()
#             )) where the 'spin' is being passed the the self.update_color_preview(...), why the _,s=spin rather than just spin?


# slider.valueChanged.connect(lambda _, s=spin: self.update_color_preview(
#     self.r_spin.value(),
#     self.g_spin.value(),
#     self.b_spin.value()
# ))

# 1. slider.valueChanged.connect(...)
# This connects a signal (valueChanged) to a function (in this case, an anonymous lambda function).
# valueChanged emits an integer (the new slider value). That’s why the lambda must accept one argument, even if we don’t use it.
# 2. lambda _, s=spin:
# _ = the value emitted from the signal (valueChanged gives an int).
# s=spin = a default argument capturing the current spin in the loop.
# Why is s=spin needed?
# Because without it, all the lambdas would use the last spin object from the loop, due to late binding in Python closures. 😱
# This way, each lambda "freezes" the current spin at the time it was created.
# Even if we’re not using s, we must bind it to ensure the lambda holds the correct spin box per iteration. So, yes—we’re not passing s to update_color_preview, but we still bind it for the sake of proper behavior in the loop.
# 3. What if we wrote this instead?
# python
# Copy
# Edit
# slider.valueChanged.connect(lambda: self.update_color_preview(...))
# That would throw an error: valueChanged sends an argument (the new int value), and this lambda doesn’t accept any parameters.
# 4. So why not just use lambda _: ...?
# That works if you're not inside a loop. But when inside a loop (like we are), the reference to spin will always point to the last spin box unless you do s=spin.
# You could simplify if you're not looping:
# python
# Copy
# Edit
# slider.valueChanged.connect(lambda _: self.update_color_preview(...))
# ✅ Works, but in a loop, this becomes unsafe without the s=spin trick.
# ✅ TL;DR:
# Code	Meaning
# lambda _:	Accepts the signal’s value, ignores it.
# lambda _, s=spin:	Accepts signal's value, and freezes the current spin.
# s=spin	Captures the current spin in the loop (late binding fix).
# s not used	It's okay—we're not using it, just capturing the loop value safely.
