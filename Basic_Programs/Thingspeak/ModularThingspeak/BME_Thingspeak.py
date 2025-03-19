'''
14Feb25

I will have a main.py with a pull down button that if goes high on startup will call this program
Named: BME_StartUp.py
'''
# import LCD_Class

from BME_Class import BME_Temperature
from WiFiNetwork import WiFi
from Thingspeak import ThingSpeakApi
from time import sleep
import machine

#Sensor Initialization
sensor = BME_Temperature(1,0)
field=4
#ThingSpeak Initialization
thingspeak = ThingSpeakApi(field)

#Network Initialization
network = WiFi()
ip = network.ConnectWiFi()
wdt = machine.WDT(timeout=8000)  # 8 seconds timeout, a watchdog

import urequests

url = "http://api.thingspeak.com/update?api_key=XA19ARK93Z22UD33&field1=23.87"
response = urequests.get(url)
print(f"Response code: {response.status_code}")
response.close()
#Main Program
try:
    while True:
        temperature, h, pres, temp_f = sensor.Read()
        field_data=temperature,h,pres,temp_f
        print(f"T={temperature}°C")
        sleep(1)
        #thingspeak.WriteData(field_data)
        thingspeak.WriteMultipleFields(field_data)
        wdt.feed()  # Resets the watchdog timer
except Exception as e:
        print(f"Error: {e}")
        machine.reset()  # Reset Pico on failure

## 18 March2025 will add the LCD_Class and moisture class
# import LCD_Class
# import MoistureClass
# from BME_Class import BME_Temperature
# from WiFiNetwork import WiFi
# from Thingspeak import ThingSpeakApi
# from time import sleep
# import machine
# from time import sleep, ticks_ms
# import gc

# # # Add this before your main loop
# # lcd_update_interval = 2000  # 2 seconds interval for updating the LCD
# # last_lcd_update = ticks_ms()

# #Sensor Initialization
# sensor = BME_Temperature(1,0)
# field=4
# #ThingSpeak Initialization
# thingspeak = ThingSpeakApi(field)

# #Network Initialization
# network = WiFi()
# ip = network.ConnectWiFi()
# wdt = machine.WDT(timeout=8000)  # 8 seconds timeout, a watchdog

# import urequests

# url = "http://api.thingspeak.com/update?api_key=YZRDGNJ7C9JZI3MP&field1=23.87"
# response = urequests.get(url)
# print(f"Response code: {response.status_code}")
# response.close()
# myLcd=LCD_Class.LCD(2,3)        
# myReading=MoistureClass.Moisture(26)
# myReading2 =MoistureClass.Moisture(27)


# #Main Program
# from time import sleep, ticks_ms

# # Add this before your main loop
# lcd_update_interval = 2000  # 2 seconds interval for updating the LCD
# last_lcd_update = ticks_ms()

# try:
#     while True:
#         moisture = myReading.Moisture_method()
#         moisture2 = myReading2.Moisture_method()
        
#         # Read sensor data
#         temperature, h, pres, temp_f = sensor.Read()
#         field_data = temperature, h, pres, temp_f, moisture, moisture2
#         MyInstance=myLcd.LCD_Method()
#         MyInstance.putstr(moisture)
#         # Update LCD without blocking
#         # if ticks_ms() - last_lcd_update > lcd_update_interval:
#         #     myLcd.clear()
#         # myLcd.putstr(f"Moisture1: {moisture}\nMoisture2: {moisture2}")
#         #     last_lcd_update = ticks_ms()
#         # print(f"Sending to ThingSpeak: {url}")
        
#         # Send data to ThingSpeak
#         thingspeak.WriteMultipleFields(field_data)

#         # After sending to ThingSpeak
#         gc.collect()
#         print(f"Free memory: {gc.mem_free()} bytes")

#         # Feed the watchdog timer to prevent reset
#         wdt.feed()
#         sleep(15)  # Short sleep to prevent CPU overload

# except Exception as e:
#     print(f"Error: {e}")
#     machine.reset()  # Reset on failure

#### 18 march 2025 9 PM
# import LCD_Class
# import MoistureClass
# from BME_Class import BME_Temperature
# from WiFiNetwork import WiFi
# from Thingspeak import ThingSpeakApi
# from time import sleep, ticks_ms
# import machine
# import gc
# import socket

# # --------------------------
# # Sensor Initialization
# # --------------------------
# sensor = BME_Temperature(1, 0)
# field = 4
# thingspeak = ThingSpeakApi(field)

# # --------------------------
# # Network Initialization
# # --------------------------
# network = WiFi()
# ip = network.ConnectWiFi()
# wdt = machine.WDT(timeout=8000)  # 8-second watchdog timer

# # --------------------------
# # LCD & Moisture Sensors
# # --------------------------
# myLcd = LCD_Class.LCD(2, 3)
# myReading = MoistureClass.Moisture(26)
# myReading2 = MoistureClass.Moisture(27)

# # --------------------------
# # LCD Update Interval
# # --------------------------
# lcd_update_interval = 2000  # 2 seconds for updating the LCD
# last_lcd_update = ticks_ms()

# import socket

# def test_wifi_connection():
#     try:
#         # Test DNS resolution
#         addr_info = socket.getaddrinfo("api.thingspeak.com", 80)
#         return True
#     except Exception as e:
#         print(f"⚠️ No internet: {e}")
#         return False

# --------------------------
# WiFi Connection Test


# --------------------------
# Main Program
# --------------------------
# try:
#     while True:
#         # ✅ Get moisture readings
#         moisture = myReading.Moisture_method()
#         moisture2 = myReading2.Moisture_method()
#         print(f"Moisture 1: {moisture} %, Moisture 2: {moisture2} %")

#         # ✅ Get BME280 sensor readings
#         temperature, h, pres, temp_f = sensor.Read()
#         field_data = temperature, h, pres, temp_f, moisture, moisture2

#         # ✅ Update LCD without blocking
#         if ticks_ms() - last_lcd_update > lcd_update_interval:
#             myLcd.clear()
#             myLcd.LCD_Method().putstr(f"M1: {moisture}\nM2: {moisture2}")
#             last_lcd_update = ticks_ms()

#         # ✅ Check WiFi connection before sending to ThingSpeak
#         if test_wifi_connection():
#             thingspeak.WriteMultipleFields(field_data)

#         # ✅ Free memory after sending data
#         gc.collect()
#         print(f"📉 Free memory: {gc.mem_free()} bytes")

#         # ✅ Feed the watchdog to avoid reset
#         wdt.feed()

#         # ✅ Sleep for 15 seconds (to respect ThingSpeak limits)
#         sleep(15)

# except Exception as e:
#     print(f"❗ Error: {e}")
#     machine.reset()  # 🔄 Reset on error
##########~~~ next try is below
# try:
#     while True:
#         # ✅ Get moisture readings
#         moisture = myReading.Moisture_method()
#         moisture2 = myReading2.Moisture_method()
#         print(f"Moisture 1: {moisture} %, Moisture 2: {moisture2} %")

#         # ✅ Get BME280 sensor readings
#         temperature, h, pres, temp_f = sensor.Read()
#         field_data = temperature, h, pres, temp_f, moisture, moisture2

#         # ✅ Update LCD without blocking
#         if ticks_ms() - last_lcd_update > lcd_update_interval:
#             myLcd.clear()
#             myLcd.LCD_Method().putstr(f"M1: {moisture}\nM2: {moisture2}")
#             last_lcd_update = ticks_ms()

#         # ✅ Check WiFi connection before sending to ThingSpeak
#         if test_wifi_connection():
#             thingspeak.WriteMultipleFields(field_data)

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

###~~~~
try:
    while True:
        # moisture = myReading.Moisture_method()
        # moisture2 = myReading2.Moisture_method()
        # print(f"Moisture 1: {moisture} %, Moisture 2: {moisture2} %")

        # Get BME280 sensor readings
        temperature, h, pres, temp_f = sensor.Read()
        field_data = temperature, h, pres, temp_f

        # ✅ Check WiFi connection before sending to ThingSpeak
        if test_wifi_connection():
            thingspeak.WriteMultipleFields(field_data)
        else:
            print("⚠️ No WiFi connection. Skipping data send.")

        # ✅ Free memory after sending data
        gc.collect()
        print(f"📉 Free memory: {gc.mem_free()} bytes")

        # ✅ Feed the watchdog to avoid reset
        wdt.feed()

        # ✅ Sleep for 15 seconds (to respect ThingSpeak limits)
        sleep(15)

except Exception as e:
    error_message = f"❗ Error: {e}\n"
    print(error_message)
    
    # Save the error to a file for debugging
    with open("error_log.txt", "w") as error_file:
        error_file.write(error_message)
        
    machine.reset()  # 🔄 Reset on error
