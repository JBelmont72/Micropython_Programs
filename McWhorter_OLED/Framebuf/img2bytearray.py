'''



https://www.tomshardware.com/how-to/oled-display-raspberry-pi-pico
To convert the image to a bytearray we shall use Don Hui’s (Novaspirit) img2bytearray python script.

1. Download and extract the ZIP archive to your machine. This creates a folder, img2bytearray which stores the Hui’s Python file.

2. Copy your image to the img2bytearray folder.

3. Open a Command Prompt / Terminal window and navigate to the img2bytearray folder.

4. To convert the image we call the command img2bytearray. We need to provide three extra parameters. First is the name of the image file, the next two are the dimensions of the image, in this case 64 by 64 pixels.

python3 img2bytearray.py YOUR-IMAGE.jpg 64 64
5. The command outputs a stream of bytes. Copy the text from b’ … ‘ and paste it inside the parenthesis of our TH object.

TH = bytearray(b’...’)
The final code should look like this 

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

i2c=I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)
TH = bytearray(b’...’)

fb = framebuf.FrameBuffer(TH,64,64, framebuf.MONO_HLSB)
oled.fill(0)
oled.blit(fb,32,0)
oled.show()


'''


from io import BytesIO
from PIL import Image
import sys

if len(sys.argv) > 1:
    path_to_image = str(sys.argv[1])
    x = int(sys.argv[2])
    y = int(sys.argv[3])

    im = Image.open(path_to_image).convert('1')
    im_resize = im.resize((x,y))
    buf = BytesIO()
    im_resize.save(buf, 'ppm')
    byte_im = buf.getvalue()
    temp = len(str(x) + ' ' + str(y)) + 4
    print(byte_im[temp::])
else:
    print("please specify the location of image i.e img2bytearray.py /path/to/image width heigh")
