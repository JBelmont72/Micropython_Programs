from PicoSensor import Temperature
from WiFiNetwork import WiFi
from Thingspeak import ThingSpeakApi
from time import sleep

#Sensor Initialization
sensor = Temperature()

#ThingSpeak Initialization
field = 1
thingspeak = ThingSpeakApi(field)

#Network Initialization
network = WiFi()
ip = network.ConnectWiFi()

#Main Program
while True:
    temperature = sensor.ReadTemperature()
    print(f"T={temperature}°C")
    thingspeak.WriteData(temperature)
    sleep(20)