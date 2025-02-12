import BME280
from machine import Pin, I2C
from time import sleep
from BME280 import BME280
 

class BME_Temperature:
    import BME280
    def __init__(self,id,scl,sda):
        self.id =id
        self.scl=scl
        self.sda=sda
        # self.i2c=I2C(self.id,self.scl,self.sda,freq=10000)
    def Read(self):
        self.i2c=I2C(id=0,scl=1,sda=0,freq=10000)
        # self.i2c=I2C(self.id,self.scl,self.sda,freq=10000)
        bme = BME280.BME280(i2c=self.i2c, addr=0x76)
        pres =bme.pressure
        # Read sensor data
        temp_c = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        print('Temperature: ', temp_c)
        # print('Temperature: ', temp_f)
        print('Humidity: ', hum)
        print('Pressure: ', pres)
        return temp_c,hum,pres

myValues=BME_Temperature(0,1,0)
while True:
    t,h,p=myValues.Read()
    print(t,h,p)
    sleep(.5)      


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
 