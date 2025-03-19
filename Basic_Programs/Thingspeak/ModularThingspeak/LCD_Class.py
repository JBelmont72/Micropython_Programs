'''
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
    print(I2C_ADDR)
    lcd.blink_cursor_on()
    lcd.putstr("I2C Address:"+str(I2C_ADDR)+"\n")
    sleep(1)
    lcd.clear()


'''
# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/
## this attempt at class LCD had an attribute issue. WIll need to icorporate changes.
from machine import Pin, SoftI2C,ADC
from pico_i2c_lcd import I2cLcd
from time import sleep
import sys




class LCD:
    def __init__(self,Sda,Scl):
        self.I2C_ADDR = 0x27
        self.I2C_NUM_ROWS = 2
        self.I2C_NUM_COLS = 16
        self.Sda=Sda
        self.Scl=Scl
        self.i2c = SoftI2C(sda=Pin(Sda), scl=Pin(Scl), freq=400000)
    def LCD_Method(self):
            self.lcd = I2cLcd(self.i2c, self.I2C_ADDR, self.I2C_NUM_ROWS, self.I2C_NUM_COLS)
            return self.lcd
        ## Updated scroll message:
    def scroll_message(self, lcd, message, delay=0.3):
        message = " " * self.I2C_NUM_COLS + message + " "
        for i in range(len(message) - self.I2C_NUM_COLS + 1):
            lcd.move_to(0, 0)
            lcd.putstr(message[i:i + self.I2C_NUM_COLS])
            sleep(delay)
        ##the above corrects the below
    # def scroll_message(self,message, delay=0.3):
    #     self.message=message
    #     self.delay=delay
    # # Add spaces to the beginning of the message to make it appear from the right
    #     self.message = " " * self.I2C_NUM_COLS + self.message + " "
    #     # Scroll through the message
    #     for i in range(len(self.message) - self.I2C_NUM_COLS + 1):
    #         self.lcd.move_to(0, 0)
    #         self.lcd.putstr(message[i:i + self.I2C_NUM_COLS])
    #         sleep(delay)
def main():
    try:
        message_scrolling = "This is a scrolling message with more than 16 characters   "
        message1="My LCD Class"
        myLcd=LCD(2,3)
        while True:        
###The I2cLcd class from pico_i2c_lcd does not have an attribute I2C_ADDR. This attribute is defined in your LCD class, but when you call:
            lcdInstance = myLcd.LCD_Method()    ##  You get an instance of I2cLcd, not your LCD class.
###     To fix this, you should access I2C_ADDR from the myLcd instance instead of lcdInstance:
            # print(lcdInstance.I2C_ADDR)   ## wrong
            print(myLcd.I2C_ADDR)       ##note the difference 

            lcdInstance.blink_cursor_on()
            addr=myLcd.I2C_ADDR
            lcdInstance.putstr("I2C Address:" + str(myLcd.I2C_ADDR) + "\n")## the updated putstr()

            # ###lcdInstance.putstr("I2C Address:"+str(addr)+"\n")##
            sleep(1)
            lcdInstance.clear()
            
            
            
            lcdInstance.putstr("It's working :)")
            sleep(2)
            lcdInstance.clear()
            lcdInstance.move_to(0,1)
            lcdInstance.putstr(message1)
            sleep(2)
            lcdInstance.clear()
            # myLcd.scroll_message("This is a scrolling message with more than 16 characters",.3)
            myLcd.scroll_message(lcdInstance, "This is a scrolling message with more than 16 characters", .3)


    except KeyboardInterrupt:
        print("Keyboard interrupt")
        lcdInstance.backlight_off()
        lcdInstance.display_off()
        sys.exit()

if __name__== '__main__':
    main()
else:
    print('''   ''')
'''  
THe above program had these errors:
The error message AttributeError: 'I2cLcd' object has no attribute 'I2C_ADDR' is caused by this line in your main() function:

print(lcdInstance.I2C_ADDR)
Issue:
The I2cLcd class from pico_i2c_lcd does not have an attribute I2C_ADDR. This attribute is defined in your LCD class, but when you call:

lcdInstance = myLcd.LCD_Method()
You get an instance of I2cLcd, not your LCD class.

Solution:
To fix this, you should access I2C_ADDR from the myLcd instance instead of lcdInstance:


print(myLcd.I2C_ADDR)
Also, update the putstr line accordingly:


lcdInstance.putstr("I2C Address:" + str(myLcd.I2C_ADDR) + "\n")
Another Issue: scroll_message Not Using lcd
Your scroll_message method references self.lcd but never initializes self.lcd. Instead, you should pass lcdInstance to scroll_message, like this:

Updated scroll_message method:


def scroll_message(self, lcd, message, delay=0.3):
    message = " " * self.I2C_NUM_COLS + message + " "
    for i in range(len(message) - self.I2C_NUM_COLS + 1):
        lcd.move_to(0, 0)
        lcd.putstr(message[i:i + self.I2C_NUM_COLS])
        sleep(delay)
Call scroll_message Correctly in main():

myLcd.scroll_message(lcdInstance, "This is a scrolling message with more than 16 characters", .3)
Final Fixes:
Replace print(lcdInstance.I2C_ADDR) → print(myLcd.I2C_ADDR)
Replace lcdInstance.putstr("I2C Address:"+str(addr)+"\n") → lcdInstance.putstr("I2C Address:"+str(myLcd.I2C_ADDR)+"\n")
Update scroll_message to accept lcdInstance as a parameter and pass it correctly in main()
After these changes, your program should run without the AttributeError.






 
          https://randomnerdtutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/
          https://maxpromer.github.io/LCD-Character-Creator
          from machine import Pin, SoftI2C,ADC
from pico_i2c_lcd import I2cLcd
from time import sleep
import sys
class LCD(sda pin,scl pin0
LCD_METHOD()
Scroll_message(message,delay=0.3)

'''
    ### https://randomnerdtutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/

# # Create custom characters here: https://maxpromer.github.io/LCD-Character-Creator/
# thermometer = bytearray([0x04, 0x0A, 0x0A, 0x0A, 0x0A, 0x1B, 0x1F, 0x0E])
# lcd.custom_char(0, thermometer)

# umbrella = bytearray([0x00, 0x04, 0x0E, 0x1F, 0x04, 0x04, 0x014, 0x0C])
# lcd.custom_char(1, umbrella)

# heart = bytearray([0x00, 0x0A, 0x1F, 0x1F, 0x0E, 0x04, 0x00, 0x00])
# lcd.custom_char(2, heart)

# try:
#     lcd.putstr("Characters")
#     lcd.move_to(0, 1)
#     # Display thermometer
#     lcd.putchar(chr(0))
#     # Display umbrella
#     lcd.move_to(2, 1)
#     lcd.putchar(chr(1))
#     # Display heart
#     lcd.move_to(4, 1)
#     lcd.putchar(chr(2))







# # Define the LCD I2C address and dimensions
# I2C_ADDR = 0x27
# I2C_NUM_ROWS = 2
# I2C_NUM_COLS = 16

# # Initialize I2C and LCD objects
# i2c = SoftI2C(sda=Pin(0), scl=Pin(1), freq=400000)
# lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# lcd.putstr("It's working :)")
# sleep(4)

# #led_onboard = machine.Pin(25, machine.Pin.OUT)
# adc = machine.ADC(26)

# conversion_factor = 100 / (65535)
# '''
# while True:
#     moisture = 130 - (adc.read_u16() * conversion_factor)
#     print("Moisture: ", round(moisture, 1), "% - ")
#     lcd.lcd_display_string("Moisture: {:.1f}%  ".format(moisture,), 1)
    
#     if moisture >= 70 :
#         led_onboard.value(0)
#         sleep(30)
#     elif moisture < 70 :
#         led_onboard.toggle()
#         utime.sleep_ms(500)

# '''

# try:
#     while True:
#         # Clear the LCD
#         lcd.clear()
#         # Display two different messages on different lines
#         # By default, it will start at (0,0) if the display is empty
#         lcd.putstr("Hello World!")
#         sleep(1)
#         lcd.clear()
#         moisture=adc.read_u16()
#         #moisture = (adc.read_u16() * conversion_factor)
#         print("Moisture: ", round(moisture, 2), "% - ")
#         lcd.putstr(f'Moisture: {moisture}')
#         if moisture >= 70 :
#             #led_onboard.value(0)
#             print('over 70')
#             sleep(3)
#         elif moisture < 70 :
#             #led_onboard.toggle()
#             sleep(2)
#         lcd.clear()
#         # Starting at the second line (0, 1)
#         lcd.move_to(4, 1)
#         lcd.putstr("Hello World!")
#         sleep(1)

# except KeyboardInterrupt:
#     # Turn off the display
#     print("Keyboard interrupt")
#     lcd.backlight_off()
#     lcd.display_off()
    
    
# from machine import I2C, Pin
# from lcd1602 import LCD
# import utime

# # Initialize I2C communication (I2C0)
# i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# # Create an LCD object
# lcd = LCD(i2c)

# message = "Scrolling Text Demo "
# lcd.clear()
# while True:
#    for i in range(len(message)):
#       lcd.write(0, 0, message[i:i+16])  # Display 16 characters at a time
#       utime.sleep(0.3)