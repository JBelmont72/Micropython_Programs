'''importing the LCD class THat i have in the moisture_lcd.py program
https://peppe8o.com/capacitive-soil-moisture-sensor-with-raspberry-pi-pico-wiring-code-and-calibrating-with-micropython/
https://newbiely.com/tutorials/arduino-micropython/arduino-micropython-soil-moisture-sensor

Choosinbg the right sensor
https://www.youtube.com/watch?v=IGP38bz-K48
Moisture:the moisture is 43386  on pin26
the moisture is 63903  on pin27
Moisture:  43546 % 
Moisture:  64351 % 
the moisture is 43546  on pin26
the moisture is 64351  on pin27
Moisture:  43514 % 
Moisture:  64303 % 

64399oisture:  64511 % 
the moisture is 18180  on pin26
the moisture is 64511  on pin27
Moisture:  18228 % 
Moisture:  64175 % 
the moisture is 18228  on pin26
the moisture is 64175  on pin27
Moisture:  18212 % 
Moisture:  64399 % 
the moisture is 18212  on pin26
the moisture is 64399  on pin27
Moisture:  18436 %
'''
# from machine import ADC
# adc = ADC(27)
# adc2=ADC(26)
# print(adc.read_u16())
# print(adc2.read_u16())


from machine import Pin,ADC
import time
from machine import Pin, SoftI2C,ADC
from pico_i2c_lcd import I2cLcd
from time import sleep
import sys
from LCD_Class import LCD

class Moisture:
    def __init__(self,pin):
        self.pin=pin
        self.adc=ADC(pin)
    def Moisture_method(self):
        # moisture=90.44
        moisture=self.adc.read_u16()
        # conversion_factor = 100 / (65535)
        print("Moisture: ", round(moisture, 1), "% ")
        return str(moisture)

def main():
    myLcd=LCD(2,3)        
    myReading=Moisture(26)
    myReading2 =Moisture(27)        
    while True:
        moisture=myReading.Moisture_method()
        moisture2=myReading2.Moisture_method()
        print(f'the moisture is {str(moisture)}  on pin26')
        print(f'the moisture is {str(moisture2)}  on pin27')
        moisture =str(moisture) 
        moisture2 =str(moisture2) 
        i=myLcd.LCD_Method()
        j=myLcd.LCD_Method()
        # myLcd.LCD_Method.putstr(moisture)
        i.putstr(moisture +'  pin26')
        sleep(1)
        i.clear()
        j.putstr(moisture2 + ' pin27')
        sleep(1)
        j.clear()
if __name__=='__main__':
    main()       



# adc = ADC(26)
# conversion_factor = 100 / (65535)
# myLCD=LCD(0,1)
# while True:
#     moisture=100.3
#     # moisture = 130 - (adc.read_u16() * conversion_factor)
#     print("Moisture: ", round(moisture, 1), "% ")
#     lcd =myLCD.LCD_Method()
#     # lcd=myLCD.LCD_Method("Moisture: {:.1f}%  ".format(moisture,), 1)
#     lcd.putstr('its working')
#     sleep(2)
#     lcd.clear()
#     lcd.putstr(str(moisture))
#     sleep(2)
#     lcd.clear()
    # if moisture >= 70 :
    #     led_onboard.value(0)
    #     sleep(30)
    # elif moisture < 70 :
    #     led_onboard.toggle()
    #     utime.sleep_ms(500)








# from machine import Pin, SoftI2C,ADC
# from pico_i2c_lcd import I2cLcd
# from time import sleep
# import sys
# from LCD_Class import LCD
# try:
#         message_scrolling = "This is a scrolling message with more than 16 characters"
#         message1="My LCD Class"
#         while True:        
#             myLcd=LCD(0,1)
#             lcdInstance = myLcd.LCD_Method()
            
#             lcdInstance.putstr("It's working :)")
#             sleep(2)
#             lcdInstance.clear()
#             lcdInstance.move_to(0,1)
#             lcdInstance.putstr(message1)
#             sleep(2)
#             lcdInstance.clear()
#             myLcd.scroll_message("This is a scrolling message with more than 16 characters",.3)


# except KeyboardInterrupt:
#     print("Keyboard interrupt")
#     lcdInstance.backlight_off()
#     lcdInstance.display_off()
#     sys.exit()

