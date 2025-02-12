'''

'''
# import network
# from time import sleep

# ssid = 'SpectrumSetup-41'
# password = 'leastdinner914'

# def ConnectWiFi():
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     wlan.connect(ssid, password)
#     while wlan.isconnected() == False:
#         print('Waiting for connection...')
#         sleep(1)
#     print(wlan.ifconfig())

# ConnectWiFi()


import network
import secrets_Condo

from time import sleep

class WiFi:
    def __init__(self):
        self.ssid = self.password
        # self.ssid = 'SpectrumSetup-41'
        self.password = self.password
        # self.password = 'leastdinner914'
    
    def ConnectWiFi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(self.ssid, self.password)
        while wlan.isconnected() == False:
            print('Waiting for connection...')
            sleep(1)
        ip = wlan.ifconfig()[0]
        print(f'Pico Connected on IP {ip}')
        return ip
    
    
def main():
    myWifi=WiFi()
    while True:
        ip=myWifi.ConnectWiFi()
        print(ip)
        sleep(1)
    
if __name__=='__main__':
    main()