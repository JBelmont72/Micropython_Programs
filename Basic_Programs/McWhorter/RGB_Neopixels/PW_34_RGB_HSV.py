'''PW 34
 convert an angle on the HSV color wheel into an RGB value that can be applied to an RGB LED. 
 In effect, we can find a color we like on the HSV color wheel, and turn the LED in our project that color. 
 The video above shows the framework we are using, and then derives the equations, and then develops the code. For 
 convenience, the code for the conversion is shown below. To make this a library, we save it as h2RGB. py on our Raspberry Pi Pico W. You can save it either in the same folder your main programs are in, or in the lib folder. To use the library, then simply import the file (h2RGB) and call the method h2RGB.getRGB(degrees), where degrees is the point on the HSV color wheel you want to convert. 
 All of this is explained in detail in the above video.


'''
def getRGB(deg):
    m=1/60
    if deg>=0 and deg<60:
        R=1
        G=0
        B=m*deg
    if deg>=60 and deg<120:
        R=1-m*(deg-60)
        G=0
        B=1
    if deg>=120 and deg<180:
        R=0
        G=m*(deg-120)
        B=1
    if deg>=180 and deg<240:
        R=0
        G=1
        B=1-m*(deg-180)
    if deg>=240 and deg<300:
        R=m*(deg-240)
        G=1
        B=0
    if deg>=300 and deg<360:
        R=1
        G=1-m*(deg-300)
        B=0
    myColor=(R,G,B)
    return myColor