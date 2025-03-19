'''


'''
import LCD_Class
import MoistureClass
from BME_Class import BME_Temperature
from WiFiNetwork import WiFi
from Thingspeak import ThingSpeakApi
from time import sleep,ticks_ms
import machine


#Sensor Initialization
sensor = BME_Temperature(1,0)
field=6
#ThingSpeak Initialization
thingspeak = ThingSpeakApi(field)

#Network Initialization
network = WiFi()
ip = network.ConnectWiFi()
wdt = machine.WDT(timeout=8000)  # 8 seconds timeout, a watchdog
#### the next 5 lines are not used because this is apready called in Thingspeak.py class
# import urequests
# url = "http://api.thingspeak.com/update?api_key=XA19ARK93Z22UD33&field1=23.87"
# response = urequests.get(url)
# print(f"Response code: {response.status_code}")
# response.close()
#Main Program

# # LCD & Moisture Sensors
# --------------------------
myLcd = LCD_Class.LCD(2, 3)
myReading = MoistureClass.Moisture(26)
myReading2 = MoistureClass.Moisture(27)

# --------------------------
# LCD Update Interval
# --------------------------
lcd_update_interval = 2000  # 2 seconds for updating the LCD
last_lcd_update = ticks_ms()


try:
    while True:
        temperature, h, pres, temp_f = sensor.Read()
        myMoisture1=myReading.Moisture_method()
        myMoisture2=myReading2.Moisture_method()
        print(myMoisture1)
        field_data=temperature,h,pres,temp_f,myMoisture1,myMoisture2
        print(f"T={temperature}°C")
        sleep(1)
        #thingspeak.WriteData(field_data)
        thingspeak.WriteMultipleFields(field_data)
        wdt.feed()  # Resets the watchdog timer
except Exception as e:
        print(f"Error: {e}")
        machine.reset()  # Reset Pico on failure




#######


# try:
#     while True:
#         moisture = myReading.Moisture_method()
#         moisture2 = myReading2.Moisture_method()
#         print(f"Moisture 1: {moisture} %, Moisture 2: {moisture2} %")

#         # Get BME280 sensor readings
#         temperature, h, pres, temp_f = sensor.Read()
#         field_data = temperature, h, pres, temp_f, moisture, moisture2

#         # ✅ Check WiFi connection before sending to ThingSpeak
#         if test_wifi_connection():
#             thingspeak.WriteMultipleFields(field_data)
#         else:
#             print("⚠️ No WiFi connection. Skipping data send.")

#         # ✅ Free memory after sending data
#         gc.collect()
#         print(f"📉 Free memory: {gc.mem_free()} bytes")

#         # ✅ Feed the watchdog to avoid reset
#         wdt.feed()

#         # ✅ Sleep for 15 seconds (to respect ThingSpeak limits)
#         sleep(15)

# except Exception as e:
#     error_message = f"❗ Error: {e}\n"
#     print(error_message)
    
#     # Save the error to a file for debugging
#     with open("error_log.txt", "w") as error_file:
#         error_file.write(error_message)
        
#     machine.reset()  # 🔄 Reset on error

########


# import LCD_Class
# import MoistureClass
# from BME_Class import BME_Temperature
# from WiFiNetwork import WiFi
# from Thingspeak import ThingSpeakApi
# from time import sleep, ticks_ms
# import machine
# import gc
# import socket
# import urequests

# # --------------------------
# # Sensor Initialization
# # --------------------------
# sensor = BME_Temperature(1, 0)
# field = 4
# thingspeak = ThingSpeakApi(field)


# #Network Initialization
# network = WiFi()
# ip = network.ConnectWiFi()
# wdt = machine.WDT(timeout=8000)  # 8 seconds timeout, a watchdog

# import urequests

# url = "http://api.thingspeak.com/update?api_key=XA19ARK93Z22UD33&field1=23.87"
# response = urequests.get(url)
# print(f"Response code: {response.status_code}")
# response.close()

# # --------------------------
# # Network Initialization
# # --------------------------
# # network = WiFi()
# # ip = network.ConnectWiFi()
# # wdt = machine.WDT(timeout=8000)  # 8-second watchdog timer

# # --------------------------
# # LCD & Moisture Sensors
# # # --------------------------
# # myLcd = LCD_Class.LCD(2, 3)
# # myReading = MoistureClass.Moisture(26)
# # myReading2 = MoistureClass.Moisture(27)

# # --------------------------
# # LCD Update Interval
# # --------------------------
# # lcd_update_interval = 2000  # 2 seconds for updating the LCD
# # last_lcd_update = ticks_ms()


# # --------------------------
# # WiFi Connection Test
# # --------------------------
# def test_wifi_connection():
#     try:
#         addr_info = socket.getaddrinfo("www.thingspeak.com", 80)
#         print("✅ Internet is available.")
#         return True
#     except Exception as e:
#         print(f"⚠️ No internet connection: {e}")
#         return False


# # --------------------------
# # Main Program
# # --------------------------
# try:
#     while True:
#         # ✅ Get moisture readings
#         # moisture = myReading.Moisture_method()
#         # moisture2 = myReading2.Moisture_method()
#         # print(f"Moisture 1: {moisture} %, Moisture 2: {moisture2} %")

#         # ✅ Get BME280 sensor readings
#         temperature, h, pres, temp_f = sensor.Read()
#         # field_data = temperature, h, pres, temp_f, moisture, moisture2
#         field_data = temperature, h, pres, temp_f

#         # # ✅ Update LCD without blocking
#         # if ticks_ms() - last_lcd_update > lcd_update_interval:
#         #     myLcd.clear()
#         #     myLcd.LCD_Method().putstr(f"M1: {moisture}\nM2: {moisture2}")
#         #     last_lcd_update = ticks_ms()

#         # ✅ Check WiFi connection before sending to ThingSpeak
#         if test_wifi_connection():
#             thingspeak.WriteMultipleFields(field_data)

#         # ✅ Free memory after sending data
#         # gc.collect()
#         # print(f"📉 Free memory: {gc.mem_free()} bytes")

#         # ✅ Feed the watchdog to avoid reset
#         wdt.feed()

#         # ✅ Sleep for 15 seconds (to respect ThingSpeak limits)
#         sleep(15)

# except Exception as e:
#     print(f"❗ Error: {e}")
#     # machine.reset()  # 🔄 Reset on error
