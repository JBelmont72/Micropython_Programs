'''charlotte swift  lesson 3 of PW
'''
# from picozero import LED
# from time import sleep
# leds =[LED(16),LED(17),LED(18),LED(19)]
# num_leds =len(leds)
# overflow_num=2**len(leds)
# try: 
#     while True:
#         for i in range(overflow_num):
#             for j in range(num_leds):
#                 leds[j].brightness =int(bin(i+overflow_num)[j+3])
#             sleep(1)
# except KeyboardInterrupt:
#     for j in range(num_leds):
#         leds[j].off()
#     print('All Done')
    
## my modification for up down binary counter_ works    
from machine import Pin
from time import sleep
LED16=Pin(16,Pin.OUT)
LED17=Pin(17,Pin.OUT)
LED18=Pin(18,Pin.OUT)
LED19=Pin(19,Pin.OUT)
leds =[LED16,LED17,LED18,LED19]
num_leds =len(leds)
overflow_num=2**len(leds)
try: 
    while True:
        for i in range(overflow_num):
            for j in range(num_leds):
                a =int(bin(i+overflow_num)[j+3])
                leds[j].value(a)
                print(a)
            sleep(.3)
        for i in range(overflow_num):
            for j in range(num_leds-1,0,-1):
                print('j',j)
                a =int(bin(i+overflow_num)[j+3])
                k=abs(j-num_leds)
                leds[k].value(a)
                print(a)
            sleep(.5)
except KeyboardInterrupt:
    for j in range(num_leds):
        leds[j].off()
    print('All Done')
    