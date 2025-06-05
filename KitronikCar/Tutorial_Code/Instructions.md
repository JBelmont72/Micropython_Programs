Step 1  create a file `KitronikPicoMiniController.py` from https://kitronik.co.uk/5353
and load on the controller PicoW
Step 2
Kitronik Mini Controller for Pico

This repo contains the MicroPython library file for the Kitronik Mini Controller for Raspberry Pi Pico.

To use the library you can save the KitronikPicoMiniController.py file onto the Pico so it can be imported.

While this controller can be used with a standard Pico, it is better suited for use with a Pico W which is then connected to another device and used to control it.

To use this controller with a standard Pico you could control other devices or sensors by connecting them to the broken out GPIO pins.

When using this controller with a Pico W you can connect it to other wireless devices, such as another Pico W, to control them wirelessly using the Mini Controller
Step 3 
Mini Controller with Pico ARP Example

Also in this repo is an example of how to use the Mini Controller with a Pico W to control the Kitronik Autonomous Robotics Platform for Pico. The ARP buggy can have a second Pico W plugged in to it allowing the Mini Controller to drive the ARP buggy over Bluetooth.

To learn more about Bluetooth on the Raspberry Pi Pico W checkout this blog post.

 

The example code for this can be found in the Mini Controller with Pico ARP folder.

Both Pico Ws need a copy of the KitronikPicoWBluetooth.py file saved onto them.!!

The Pico W for this Mini Controller also needs a copy of the Pico Controller.py file saved onto it, as well as the KitronikPicoMiniController.py library from this repo.

Then the Pico W for the ARP buggy needs a copy of the Pico ARP.py file saved onto it, as well as the PicoAutonomousRobotics.py library.
the blue tooth program for both picos  
https://github.com/KitronikLtd/Kitronik-Pico-W-Bluetooth-MicroPython/blob/main/KitronikPicoWBluetooth.py
https://github.com/KitronikLtd/Kitronik-Pico-W-Bluetooth-MicroPython/blob/main/README.md