
COOL FUTURE PROJECT:   https://medium.com/@ilias.info.tel/display-opencv-camera-on-a-pyqt-app-4465398546f7
can display opencv in PYQT5!! 
in PyQt_UPP / UDP folder I have led_Client which has multiple programs to control leds remotely by UDP:
four programs for client on Python editor and server on PicoW
1. PicoW server encode/decode
2. Python client encode/decode
3. PicoW server STRUCT
4. Python client STRUCT binary coding
~~~~~~~~~~~~~~
In same subfoler of UDP i have 'servo_Client.py' :
'Using UDP to send servo commands from python client to the PicoW server!
Client Side Changes:
Send specific servo angle data (e.g., ANGLE:90).
Wait for acknowledgment from the Pico W after sending.
Control the time interval dynamically.
Server Side Changes:
Decode and parse the received data to extract the angle.
Move the servo to the requested angle.
Send an acknowledgment back to the client.
below I have four programs:
1-python client code ('utf_8')
2-PicoW server code ('utf-8')
3-python client struct
4-PicoW server code (struct)
At bottom is discussion of code versus struct 
~~~~~~~~~~~~~~~~~~~~~~~

PW_109... very basic UDP
~~~~~~~~~~~~~~~~~~~~~~
LED CONTROL using UDP. Can send even between picoWs ( the last sketch is the picoW client)!
/Users/judsonbelmont/Documents/SharedFolders/Pico/Micropython_Programs/Basic_Programs/PyQt_UDP/PW_110_Socket_Server.py.   I like the command and  command != last Command as way of minimizing messages being sent. 
And.  Else command = None added.
~~~~~~~~~~
Pyqt5_basic.py  is the first PyQt5
Pyqt_1.py and Pyqt5_basic.py show the building blocks for the PW_111_PyQt5.py with 3 led widgets and a slider
###########
Basic_Programs/PyQt_UDP/Class_WiFi_Tutorial.py  is great illustration of using class with PyQt5 and also incorporated UPD and MQTT!!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
