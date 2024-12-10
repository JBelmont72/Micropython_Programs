'''
https://how2electronics.com/send-sensor-data-to-thingspeak-with-raspberry-pi-pico-w/
Send the DHT11 Humidity Temperature Sensor Data to Thingspeak Server using Raspberry Pi Pico W Board.
DHT11 has calibrated digital signal output.
The Raspberry Pi Pico W has a buck-boost converter IC. Hence you can power the Raspberry Pi Pico W via a Lipo Battery. The Lipo Battery Charger Module which consists of LTC4054 IC has been modified and specially designed for powering Raspberry Pi Pico W using Lipo Battery.

https://shop.pimoroni.com/products/pico-lipo-shim?variant=32369543086163

https://www.waveshare.com/wiki/Pico-UPS-B
https://shop.pimoroni.com/products/pimoroni-pico-lipo?variant=39335427080275

https://shop.pimoroni.com/products/pimoroni-pico-plus-2-w?variant=42182811942995

https://api.thingspeak.com/update?api_key=RG4961TZ9BKHMJ84&field1=0

GET https://api.thingspeak.com/update?api_key=RG4961TZ9BKHMJ84&field1=0

from dht import DHT22
dht22 = DHT22(Pin(12))
def readDht():
    dht22.measure()
    return dht22.temperature(), dht22.humidity()
    
    https://towardsdatascience.com/iot-made-easy-esp-micropython-mqtt-thingspeak-ce05eea27814
    rxtensive webpage with multiple devices button, dht11,,etc
'''

import machine
import urequests 
from machine import Pin
import network, time
from dht import DHT11
import random
import ujson as json 
HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'RG4961TZ9BKHMJ84'  
 
ssid = 'NETGEAR48'
password = 'waterypanda901'

api_key = 'RG4961TZ9BKHMJ84'
base_url = 'https://api.thingspeak.com/update'


# Configure Pico W as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
 
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 
 
while True:
    time.sleep(5) 
    pin = Pin(17, Pin.OUT, Pin.PULL_DOWN)
    
    sensor = DHT11(pin)
    sensor.measure()
    t  = sensor.temperature()
    h = sensor.humidity()
    # print("Temperature: {}".format(sensor.temperature))
    # print("Humidity: {}".format(sensor.humidity))
    print("Temperature: ",t)
    print("Humidity: ",h)
    
    dht_readings = {'field1':t, 'field3':h}
    ##GET https://api.thingspeak.com/update?api_key=RG4961TZ9BKHMJ84&field1=0 
    request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = dht_readings, headers = HTTP_HEADERS )  
    request.close() 
    print(dht_readings) 

    url = f"{base_url}?api_key={api_key}&field1={t}&field2={h}"
    response = urequests.get(url)
    print(response.text)
    time.sleep(1)

# while True:
#     print('Sending Data...',end='\r')
#     data1=random.randint(10,50)
#     data2=random.randint(50,100)
#     # URL = f'http://jsonplaceholder.typicode.com/albums/1'
#     URL =f'https://api.thingspeak.com/update?api_key=RG4961TZ9BKHMJ84&field1={data1} &field2={data2}'
#     response=urequests.get(URL)
    
    # # You can access .content multiple times of course
    # print(response.content)
    # print(response.json())

# It's mandatory to close response objects as soon as you finished
# working with them. On Pycopy platforms without full-fledged
# OS, not doing so may lead to resource leaks and malfunction.
 
    # print(response.status_code)
    # print(response.reason)
    # response.close()
    # time.sleep(15)



'''
### library for dht.py
import array
import micropython
import utime
from machine import Pin
from micropython import const
 
class InvalidChecksum(Exception):
    pass
 
class InvalidPulseCount(Exception):
    pass
 
MAX_UNCHANGED = const(100)
MIN_INTERVAL_US = const(200000)
HIGH_LEVEL = const(50)
EXPECTED_PULSES = const(84)
 
class DHT11:
    _temperature: float
    _humidity: float
 
    def __init__(self, pin):
        self._pin = pin
        self._last_measure = utime.ticks_us()
        self._temperature = -1
        self._humidity = -1
 
    def measure(self):
        current_ticks = utime.ticks_us()
        if utime.ticks_diff(current_ticks, self._last_measure) < MIN_INTERVAL_US and (
            self._temperature > -1 or self._humidity > -1
        ):
            # Less than a second since last read, which is too soon according
            # to the datasheet
            return
 
        self._send_init_signal()
        pulses = self._capture_pulses()
        buffer = self._convert_pulses_to_buffer(pulses)
        self._verify_checksum(buffer)
 
        self._humidity = buffer[0] + buffer[1] / 10
        self._temperature = buffer[2] + buffer[3] / 10
        self._last_measure = utime.ticks_us()
 
    @property
    def humidity(self):
        self.measure()
        return self._humidity
 
    @property
    def temperature(self):
        self.measure()
        return self._temperature
 
    def _send_init_signal(self):
        self._pin.init(Pin.OUT, Pin.PULL_DOWN)
        self._pin.value(1)
        utime.sleep_ms(50)
        self._pin.value(0)
        utime.sleep_ms(18)
 
    @micropython.native
    def _capture_pulses(self):
        pin = self._pin
        pin.init(Pin.IN, Pin.PULL_UP)
 
        val = 1
        idx = 0
        transitions = bytearray(EXPECTED_PULSES)
        unchanged = 0
        timestamp = utime.ticks_us()
 
        while unchanged < MAX_UNCHANGED:
            if val != pin.value():
                if idx >= EXPECTED_PULSES:
                    raise InvalidPulseCount(
                        "Got more than {} pulses".format(EXPECTED_PULSES)
                    )
                now = utime.ticks_us()
                transitions[idx] = now - timestamp
                timestamp = now
                idx += 1
 
                val = 1 - val
                unchanged = 0
            else:
                unchanged += 1
        pin.init(Pin.OUT, Pin.PULL_DOWN)
        if idx != EXPECTED_PULSES:
            raise InvalidPulseCount(
                "Expected {} but got {} pulses".format(EXPECTED_PULSES, idx)
            )
        return transitions[4:]
 
    def _convert_pulses_to_buffer(self, pulses):
        """Convert a list of 80 pulses into a 5 byte buffer
        The resulting 5 bytes in the buffer will be:
            0: Integral relative humidity data
            1: Decimal relative humidity data
            2: Integral temperature data
            3: Decimal temperature data
            4: Checksum
        """
        # Convert the pulses to 40 bits
        binary = 0
        for idx in range(0, len(pulses), 2):
            binary = binary << 1 | int(pulses[idx] > HIGH_LEVEL)
 
        # Split into 5 bytes
        buffer = array.array("B")
        for shift in range(4, -1, -1):
            buffer.append(binary >> shift * 8 & 0xFF)
        return buffer
 
    def _verify_checksum(self, buffer):
        # Calculate checksum
        checksum = 0
        for buf in buffer[0:4]:
            checksum += buf
        if checksum & 0xFF != buffer[4]:
            raise InvalidChecksum()

'''