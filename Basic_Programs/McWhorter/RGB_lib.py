'''rgb_lib library'''

from machine import Pin,PWM
from time import sleep

myColor ={'red':[255,0,0]}

myColor.update({'blue':[0,0,255],'green':[0,255,0],'cyan':[0,255,255],'magenta':[255,0,255],'yellow':[255,63,0],
                'orange':[255,32,0],'white':[255,255,255],'off':[0,0,0],'purple':[127,0,255]})

    
 