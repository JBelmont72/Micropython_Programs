'''
chat 
https://microcontrollerslab.com/esp32-esp8266-adc-micropython-measure-analog-readings/
ADC Example for ESP32 and Raspberry Pi Pico
Reads analog voltage from a potentiometer connected to an ADC pin
and prints the raw ADC value and corresponding voltage to the console.'''


from machine import ADC, Pin
from time import sleep

# 1st is pico.  2 d is esp32 
# import machine
# #from time import sleep
# import utime
# potPin =28 # for pico

# myPot = machine.ADC(potPin)
# led_red = machine.Pin(15,machine.Pin.OUT)
# led_yellow = machine.Pin(17,machine.Pin.OUT)
# led_green = machine.Pin(18,machine.Pin.OUT)
# myInput = float(input("Input your Voltage"))
# if myInput >2:
    
#     while True:
#         led_red.value(1)
#         utime.sleep(1)
#         led_red.value(0)
#         break
               


# while True:
#     led_red.value(0)
#     led_yellow.value(0)
#     led_green.value(0)
#     potVal = myPot.read_u16()
#     print(potVal)
#     Voltage = 0.00005 * potVal
#     print(Voltage)
#     print(str(Voltage)+" Volts")
#     utime.sleep(0.5)
#     if Voltage >1.5:
#         led_red.value(1)
#         utime.sleep(1)
#         if Voltage >1.8:
#             led_red.value(0)
#             led_yellow.value(1)
#             utime.sleep(3)
#     if Voltage <1.0:
#         led_green.value(1)
#         utime.sleep(1.0)

# adc = ADC(Pin(32))
# adc.atten(ADC.ATTN_11DB)      # 0-3.3V range
# adc.width(ADC.WIDTH_12BIT)    # 12-bit resolution (0-4095)

# while True:
#     raw = adc.read()                    # read returns 0-4095 on ESP32
#     voltage = raw / 4095 * 3.3
#     print(raw, "{:.3f} V".format(voltage))
#     sleep(0.25)

'''
from machine import ADC, Pin
from time import sleep, ticks_us

# Create ADC object with Pin 32
adc = ADC(Pin(33))

# Set the ADC width to 12 bits (range: 0-4095)
adc.width(ADC.WIDTH_12BIT)  

# Call the ADC constructor directly with the correct settings
def init_adc():
    print(str(ticks_us()) + " [ Init ] ADC")
    adc = ADC(Pin(32))  # Re-initialize just for clarity, can be omitted
    # No attenuation setup needed as it defaults to 0-1V
    scale = 1
    offset = 0
    return adc, scale, offset

while True:
    print(str(ticks_us()) + " [ Reading ] ADC")
    raw = adc.read_u16()  # Read the ADC value (0-65535 for 16 bit)
    voltage = raw / 65535 * 3.3  # Scale to voltage from 0 to 3.3V
    print(raw, "{:.3f} V".format(voltage))
    sleep(0.5)

'''
from machine import ADC, Pin
from time import sleep

# Create ADC object for Pin 32
adc = ADC(Pin(32))

# Set the ADC width to 12 bits (range: 0-4095)
#adc.width(ADC.WIDTH_12BIT)

while True:
    # Read the ADC value (0-4095)
    raw = adc.read()	#this is 12 bit
    raw_u16=adc.read_u16()# this is 16 bit
    
    voltage = raw / 4095 * 3.3  # Scale to voltage (0-3.3V), this is 12 bit
    #print("Raw:", raw, "Voltage:", "{:.3f} V".format(voltage))
    print("Raw:", raw,"raw_16 ", raw_u16, "Voltage:", "{:.3f} V" .format(voltage),end='\r')
    sleep(1)
    

