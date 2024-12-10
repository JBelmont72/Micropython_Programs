# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/
###     https://github.com/RuiSantosdotme/RPi-Pico-W-MicroPython-eBook/tree/main
'''
The following example creates a station interface and an access point interface and checks if they are active
in this case False
'''


import network

sta_if = network.WLAN(network.STA_IF)
print(sta_if.active())

ap_if = network.WLAN(network.AP_IF)
print(ap_if.active())
