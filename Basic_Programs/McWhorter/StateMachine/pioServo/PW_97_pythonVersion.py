'''
python version of sgnal timeing for servo 
PW lesson 97
HS-422 hitec servo
 Pulse Width: 900~2100μs(Center:1500μs
'''
import time
from machine import Pin
while True:
    servoPin=Pin(16,Pin.OUT)
    angle=180
    pw=int(angle*2000/180+500)
    servoPin.on()
    time.sleep_us(pw)
    servoPin.off()
    time.sleep_us(20000-pw)
    print(pw)



