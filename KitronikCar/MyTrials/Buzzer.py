'''
Buzzer pin16
Pushbutton =0
right forward =6
right backward =7
left backward =19
left forward =20
LEDs  akk fiour on GPIO Pin 18
'''
from machine import Pin
import time
buzzPin=20
# buzzPin=16
Buzzer=Pin(buzzPin,Pin.OUT)
butPin=0
Button=Pin(butPin,Pin.IN,Pin.PULL_DOWN)
while True:
    ButVal=Button.value()
    print(ButVal)
    
    if ButVal ==1:
        for i in range(40):
            Buzzer.value(1)
            time.sleep(.01)
            print('Buzzer')
            Buzzer.value(0)
            time.sleep(.01)