'''
Name WiFiNetwork.py 

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
import secrets
# import secrets_Loft
# import secrets_Condo
from time import sleep
class WiFi:
    def __init__(self):
        # self.ssid = secrets_Loft.ssid
        self.ssid = secrets.ssid_Home
        #self.ssid = self.password
        #self.ssid = self.password
        # self.ssid = 'SpectrumSetup-41'
        # self.password = secrets_Loft.password
        self.password = secrets.password_Home
        # self.password = 'leastdinner914'
    
    def ConnectWiFi(self):
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        #wlan.connect(Secrets_Condo.ssid,Secrets_Condo.password)
        wlan.connect(self.ssid, self.password)
        sleep(1)
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
