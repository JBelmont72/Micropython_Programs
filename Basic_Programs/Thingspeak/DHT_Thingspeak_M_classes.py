''''M Classes'  send data to cloud using Pico thingspeak  REST API
https://www.youtube.com/watch?v=4CdzTqiLKec
very good
APIkey
RG4961TZ9BKHMJ84
'''
import machine
import time
import urequests
import network
import ujson
import dht

##ThingSpeak settings


# base_url = 'https://api.thingspeak.com/update'
THINGSPEAK_API_KEY = "RG4961TZ9BKHMJ84"
THINGSPEAK_URL = "http://api.thingspeak.com/update"

##Wi-Fi settings
WIFI_SSID = "NETGEAR48"
WIFI_PASSWORD = "waterypanda901"

##DHT11 ( sensor on GPIO 17
dht_sensor = dht.DHT11(machine.Pin(17))

##Function to read room temperature and humidity
def read_room_temperature_humidity():
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    return temperature, humidity

##Function to send data to ThingSpeak
def send_data_to_thingspeak(temperature, humidity):
    data = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": temperature,
        "field2": humidity,
    }
    response = urequests.post(THINGSPEAK_URL, data=ujson.dumps(data), headers={"Content-Type": "application/json"})
    response.close()

##Initialize the Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

####Wait for the Wi-Fi connection to establish
while not wifi.isconnected():
    time.sleep(1)

print("Connected to Wi-Fi")
status = wifi.ifconfig()
print(status)
if __name__== "__main__":    
    try:
        while True:
            temperature, humidity = read_room_temperature_humidity()
            send_data_to_thingspeak(temperature, humidity)
            print("Data sent to ThingSpeak")
            print(temperature,humidity)
            
            
            time.sleep(15)  # Send data every 15 seconds (adjust the interval as needed)
    except KeyboardInterrupt:
        pass
    
    