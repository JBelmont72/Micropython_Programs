'''
https://www.youtube.com/watch?v=4CdzTqiLKec
turn this into classes
'''
# Raspberry Pi Pico
# DHT22 (AM2302) Temperature and Humidity Sensor
# 📝 Code:


import machine
import time
import urequests
import network
import ujson
import dht

#ThingSpeak settings
THINGSPEAK_API_KEY = "TXD92FQJN6C8APJD"
THINGSPEAK_URL = "http://api.thingspeak.com/update"

#Wi-Fi settings
WIFI_SSID = "Your_WiFi_SSID"
WIFI_PASSWORD = "Your_WiFi_Password"

###DHT22 (AM2302) sensor on GPIO 4
dht_sensor = dht.DHT22(machine.Pin(4))

#Function to read room temperature and humidity
def read_room_temperature_humidity():
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temperature, humidity

#Function to send data to ThingSpeak
def send_data_to_thingspeak(temperature, humidity):
    data = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": temperature,
        "field2": humidity,
    }
    response = urequests.post(THINGSPEAK_URL, data=ujson.dumps(data), headers={"Content-Type": "application/json"})
    response.close()

#Initialize the Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

#Wait for the Wi-Fi connection to establish
while not wifi.isconnected():
    time.sleep(1)

print("Connected to Wi-Fi")

if __name__== "__main__":
    try:
        while True:
            temperature, humidity = read_room_temperature_humidity()
            send_data_to_thingspeak(temperature, humidity)
            print("Data sent to ThingSpeak")
            time.sleep(15)  # Send data every 15 seconds (adjust the interval as needed)
    except KeyboardInterrupt:
        pass