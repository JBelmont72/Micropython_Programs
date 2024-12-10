'''
https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico

convert a JPEG image into a string of bytes



'''

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
'''
Create an object, i2c, which stores the I2C channel in use, in this case zero,
the SDA and SCL pins that we are connected to, and finally the frequency at which we connect to the OLED screen. 
may need to run i2c scan and set the i2c to the right pin

Create an object, oled, which will be used to communicate with the OLED screen.
It has three arguments, the width and height of the screen (128 x 64 pixels) and the I2C connection details.
'''
i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
TH = bytearray()
#	TH which will store an array of bytes that make up our image.	
'''
Create an object, FB, which will load the image into the framebuffer.
We pass the name of the bytearray object, the dimensions of the image (64 x 64 pixels)
and then configure the image to be a 1-bit monochrome image.
'''
fb = framebuf.FrameBuffer(TH,64,64, framebuf.MONO_HLSB)

'''
Clear the screen, and then blit the image onto the screen. Then use show to update the screen.
Blitting draws the image to the screen, in this case it places the 64 x 64 image dead center of the screen.
Where 32 is the horizontal (x) position and 0 is the vertical (y) position.

'''
oled.fill(0)
oled.blit(fb,32,0)
oled.show()
'''
Our object, TH, currently has no image to display. To create a bytearray of an image we first need a suitable image.
The screen is 128 x 64 pixels in size,
but an image 64 x 64 pixels will fit nicely into the center of the screen. The image must be in a JPEG format.

To convert the image to a bytearray we shall use Don Hui’s (Novaspirit) img2bytearray python script.

1. Download and extract the ZIP archive to your machine. This creates a folder, img2bytearray which stores the Hui’s Python file.

2. Copy your image to the img2bytearray folder.

3. Open a Command Prompt / Terminal window and navigate to the img2bytearray folder.

4. To convert the image we call the command img2bytearray. We need to provide three extra parameters. First is the name of the image file,
the next two are the dimensions of the image, in this case 64 by 64 pixels.

'''




'''
Import the framebuf library. This library enables the code to create bitmap images and show them on the display.

Simple shapes and lines can be drawn to the display with just a single command. Each of these commands will need oled.show() in order to be seen. Note that most of these methods have a color parameter but, with a monochrome screen, you’ll always put a color of “1” (0 means pixel off).

oled.pixel(x,y,c): Draw a pixel at position x,y and uses c to set the color of the pixel, with 1 being lit, 0 being off. Example:
oled.pixel(10,10,1)
oled.hline(x,y,w,c): Draw a horizontal line from point x,y that has a set width (w) in pixels, and color ( c ). Example: 
oled.hline(2,3,4,1)
oled.vline(x,y,h,c): Draw a vertical line from point x,y that has a set height (h) in pixels, and color ( c ). Example:
oled.vline(0, 0, 64, 1)
oled.line(x1,y1,x2,y2,1): Draw a diagonal line from points x1, y1 to x2, y2 with the color ( c ). Example:
oled.line(0, 0, 128, 64, 1)
oled.rect(x,y,w,h,c): Draw a rectangle starting at point x.y and for a set width (w) and height(h). Use ( c ) to set the color of the pixels. For example:
oled.rect(0, 0, 64, 32, 1)
oled.fill_rect(x,y,w,h,c): Draw a filled rectangle starting at point x.y and for a set width (w) and height(h) use ( c ) to set the color of the pixels. For example:
oled.fill_rect(0, 0, 64, 32, 1)
oled.fill(False)
'''