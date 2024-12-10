# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-w-micropython-ebook/
##      https://github.com/RuiSantosdotme/RPi-Pico-W-MicroPython-eBook/tree/main
##  this will scan for nearby networks
##      The network information is separated by commas and is in the following order: SSDI, BSSID, RSSI, channel
##  (b'NETGEAR48', b'\x14?\xc3\x8as\xe3', 6, -61, 5, 6)
##      (b'', b'\xf6y\n@\x9c\x00', 11, -86, 5, 3)
##  -86 is rssi the signal strenght, the last 2 numbers are unknown value
import network

# Init Wi-Fi interface
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

# Scan for Wi-Fi networks
networks = wlan.scan()

# Print Wi-Fi networks
print("Available WiFi Networks:")
for network_info in networks:
    print(network_info)
