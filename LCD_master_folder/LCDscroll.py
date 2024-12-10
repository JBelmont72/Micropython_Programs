'''
scrolling from random nerds
On that function, we start by adding a padding to our message that consists of as many blank spaces as the number of columns (I2C_NUM_COLS) and a final space at the end. We do this to create a space from where to start scrolling.
message = " " * I2C_NUM_COLS + message + " "
Then, we have a for loop that will iterate through the characters of our message. We set the cursor position to the top-left corner of the LCD (column 0, row 0) to ensure that each iteration starts from the beginning of the LCD.

lcd.move_to(0, 0)
Then, we display a portion of the message on the LCD, starting from the current iteration index i and covering the width of the LCD (I2C_NUM_COLS characters).

lcd.putstr(message[i:i + I2C_NUM_COLS])
The following expression message[i:i + I2C_NUM_COLS] gets just a portion of the message starting at the character with index i and ending at character i + IC2_NUM_COLS. As we increase the value of i, we select a new portion of the message, making the scrolling effect.

Finally, the delay at the end will determine the scrolling speed.

sleep(delay)
To scroll the text, call the scroll_message() function and pass as arguments the message you want to scroll and the delay time.

scroll_message(message_scroll, 0.4)
'''
# Rui Santos & Sara Santos - Random Nerd Tutorials
# Complete project details at https://RandomNerdTutorials.com/raspberry-pi-pico-i2c-lcd-display-micropython/

from machine import Pin, SoftI2C
from pico_i2c_lcd import I2cLcd
from time import sleep

# Define the LCD I2C address and dimensions
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD objects
i2c = SoftI2C(sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

def scroll_message(message, delay=0.3):
    # Add spaces to the beginning of the message to make it appear from the right
    message = " " * I2C_NUM_COLS + message + " "
    # Scroll through the message
    for i in range(len(message) - I2C_NUM_COLS + 1):
        lcd.move_to(0, 0)
        lcd.putstr(message[i:i + I2C_NUM_COLS])
        sleep(delay)

try:
    lcd.putstr("Testing scroll!")
    sleep(2)

    # Define the message to be scrolled
    message_scroll = "This is a scrolling message with more than 16 characters"

    while True:
        # Scroll the message on the LCD
        lcd.clear()
        scroll_message(message_scroll)

except KeyboardInterrupt:
    # Turn off the display when the code is interrupted by the user
    print("Keyboard interrupt")
    lcd.backlight_off()
    lcd.display_off()