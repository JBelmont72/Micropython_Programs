

Basic_Programs/PyQt_UDP/PW_112_PyQt_udpLeds.py ## works great!
#1 is the PyQt5 client works and controls LEDs, 2 is the pico server, 3 is the client with UDP without PyQt5, 4 is the client with UDP. and MQTT
#4 is the PyQt5 Class from PW_111_PyQt5.py

Basic_Programs/PyQt_UDP/PW_113_PlottingData.py
 Pw 113 Plotting Data
first is a functional version, second is a QWidget class-based version,the third is a QMainWindow class-based version
Shows Live Data can be plotted using a PyQt window. Our eventual goal is to bring in live data from the Raspberry Pi Pico W using UDP over WiFi, but to learn the concepts today, we will be generating a live sin wave to show how the plotting works. Here is the code we developed in this lesson:

Basic_Programs/PyQt_UDP/PW_113_Study.py just exploring some of the python functions used.

Basic_Programs/PyQt_UDP/PW_114_Leds.py works great
This project has a server running on the Raspberry Pi Pico, and a Client running on your desktop PC. First-  is the code for the server side for the Pi Pico.
Create a PyQt Window which  used 3 Sine Waves offset from each other by (2*Pi/). By offsetting the Sine Waves each by this amount creates 3 waves perfectly spaced across the domain. We then use the values from these sine waves to create the Red, Green and Blue values for the HSV color wheel. The x axis represents angle, in radians. Then the values of the sine wave represent the corresponding Red, Green, and Blue values. The program graphs the three waves on the PyQt widget, then passes the data via UDP over WiFi to the Pi Pico. The Pico then applies the values to the RGB LED.  We save the server side program on the Pi Pico as main.py, and power the project with the Breadboard Power Bank, meaning the Pi operates remote and untethered, and the LED is controlled by the desktop client software. This is a schematic of the Pi Pico circuit for the project.


PW_116.py https://toptechboy.com/control-dc-motor-with-raspberry-pi-pico-w-and-ta6586/





PW_117  motor  https://toptechboy.com/page/2/#google_vignette
In this video lesson I will show you how you can control a remote DC motor using your  Raspberry Pi Pico W. The Pi Pico is set up as a server, and is connected to a DC motor, and TA6586 Motor Controller. The motor is controlled by a client Python program running on your  desktop PC. On the client side we create a Graphical Widget, which will allow you to control both the speed and direction of the motor. the schematic for the Raspberry Pi Pico W side is shown below:In this video lesson I will show you how you can control a remote DC motor using your  Raspberry Pi Pico W. The Pi Pico is set up as a server, and is connected to a DC motor, and TA6586 Motor Controller. The motor is controlled by a client Python program running on your  desktop PC. On the client side we create a Graphical Widget, which will allow you to control both the speed and direction of the motor. the schematic for the Raspberry Pi Pico W side is shown below: