'''importing the LCD class THat i have in the moisture_lcd.py program


'''

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
        moisture=90.44
        # moisture=self.adc.read_u16()
        conversion_factor = 100 / (65535)
        print("Moisture: ", round(moisture, 1), "% ")
        return str(moisture)
myLcd=LCD(0,1)        
myReading=Moisture(26)        
while True:
    moisture=myReading.Moisture_method()
    print(f'the moisture is{str(moisture)} ')
    moisture =str(moisture)
    i=myLcd.LCD_Method()
    # myLcd.LCD_Method.putstr(moisture)
    i.putstr(moisture)
    sleep(1)
    



adc = ADC(26)
conversion_factor = 100 / (65535)
myLCD=LCD(0,1)
while True:
    moisture=100.3
    # moisture = 130 - (adc.read_u16() * conversion_factor)
    print("Moisture: ", round(moisture, 1), "% ")
    lcd =myLCD.LCD_Method()
    # lcd=myLCD.LCD_Method("Moisture: {:.1f}%  ".format(moisture,), 1)
    lcd.putstr('its working')
    sleep(2)
    lcd.clear()
    lcd.putstr(str(moisture))
    sleep(2)
    lcd.clear()
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

