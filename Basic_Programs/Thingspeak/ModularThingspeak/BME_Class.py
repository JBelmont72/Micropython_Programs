 
import machine
import urequests 
from machine import Pin, SoftI2C
import network, time
import BME280
import sys
class BME_Temperature:
    def __init__(self,scl,sda,freq=10000):
        self.i2c = SoftI2C(scl=Pin(scl), sda=Pin(sda), freq=freq)
    #self.i2c = SoftI2C(self.scl=Pin(22), self.sda=Pin(21), self.freq=10000)    #initializing the I2C method
        # self.i2c=I2C(self.scl,self.sda,freq=10000)
        self.bme = BME280.BME280(i2c=self.i2c)          #BME280 object created
    def Read(self):
        #self.i2c=I2C(scl=22,sda=21,freq=10000)
        # self.i2c=I2C(self.id,self.scl,self.sda,freq=10000)
        #bme = BME280.BME280(i2c=self.i2c, addr=0x76)
        #pres =self.bme.pressure
        # Read sensor data
        temp_c = self.bme.temperature
        hum = self.bme.humidity
        pres = self.bme.pressure
        print('Temperature: ', temp_c)
        # print('Temperature: ', temp_f)
        print('Humidity: ', hum)
        print('Pressure: ', pres)
        temp=temp_c.split('C')
        temp=float(temp[0])
        temp_f = temp*(1.8) + 32
        return temp_c,hum,pres,temp_f


def main():
    myValues=BME_Temperature(1,0)
    try:
        while True:
            t,h,p,temp_f=myValues.Read()
            print(t,h,p,temp_f)
            time.sleep(.5)      
    except Exception as e:
        # Handle any exceptions during sensor reading
        print('An error occurred:', e)
    finally:
        sys.exit()
if __name__=='__main__':
    main()

'''  

i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000)    #initializing the I2C method

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'XA19ARK93Z22UD33' 

UPDATE_TIME_INTERVAL = 5000  # in ms 
last_update = time.ticks_ms() 

ssid='SpectrumSetup-41'
password='leastdinner914'

# Configure ESP32 as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 

while True: 
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL: 
         bme = BME280.BME280(i2c=i2c)          #BME280 object created
         temperature = bme.temperature         #reading the value of temperature
         humidity = bme.humidity               #reading the value of humidity
         pressure = bme.pressure               #reading the value of pressure

         bme_readings = {'field1':temperature, 'field2':pressure, 'field3':humidity} 
         request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = HTTP_HEADERS )
         last_update=time.ticks_ms()
         request.close() 
         print(bme_readings)






# # Initialize I2C communication
# i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=10000)

# while True:
#     try:
#         # Initialize BME280 sensor
#         bme = BME280.BME280(i2c=i2c, addr=0x76)
#         # R_hum=bme.read_raw_humidity()
#         print('R_hum: ',R_hum)
#         # temp_c,hum,pres =bme.values      
#         # temp_c=temp_c[:-1]
#         # hum=hum[:-3]
#         # pres=pres[:-1]
#         # temp_c=float(temp_c)
#         # hum=float(hum)
#         # pres=float(pres)
        
        
#         pres =bme.pressure
#         # Read sensor data
#         temp_c = bme.temperature
#         hum = bme.humidity
#         pres = bme.pressure
        
#         # #Convert temperature to fahrenheit
#         # temp_f = (temp_c/100) * (9/5) + 32
#         # # temp_f = (bme.read_temperature()/100) * (9/5) + 32
#         # temp_f = str(round(temp_f, 2)) + 'F'
        
#         # Print sensor readings
#         print('Temperature: ', temp_c)
#         # print('Temperature: ', temp_f)
#         print('Humidity: ', hum)
#         print('Pressure: ', pres)
#         # print(type(temp_c))
#         # print(type(hum))
#     except Exception as e:
#         # Handle any exceptions during sensor reading
#         print('An error occurred:', e)

#     sleep(5)
'''
 