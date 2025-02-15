from BME_Class import BME_Temperature
from WiFiNetwork import WiFi
from Thingspeak import ThingSpeakApi
from time import sleep

#Sensor Initialization
sensor = BME_Temperature()

#ThingSpeak Initialization
field = 1
thingspeak = ThingSpeakApi(field)

#Network Initialization
network = WiFi()
ip = network.ConnectWiFi()

#Main Program
while True:
    temperature,h,pres,temp_f = sensor.Read()
    print(f"T={temperature}°C")
    thingspeak.WriteData(temperature)
    sleep(20)