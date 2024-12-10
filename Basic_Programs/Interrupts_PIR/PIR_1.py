'''
recreating the PIR interrupt with two flags motion and motion_printed

excellent tutorial and details adjusting my PIR model
https://www.makerguides.com/hc-sr501-arduino-tutorial/

shilleh has the best PIR funciton  very much like PW 84 pico but no IRQ method
https://shillehtek.com/blogs/news/how-to-connect-and-use-the-hcsr501-pir-sensor-with-a-raspberry-pi-pico-pico-w?utm_source=youtube&utm_medium=product_shelf
'''

# from machine import Pin,Timer
# import time

# rPin=16
# rLed =Pin(rPin,Pin.OUT)
# pirPin=0
# PIR =Pin(pirPin,Pin.IN)
# PIRtimer=Timer()
# global motion  
# global motion_printed
# motion=False
# motion_printed=False
# rLed.value(0)
# def led_on(pin):
#     global motion
#     motion =True
#     print('Hi')
#     PIRtimer.init(period = 5000,mode=Timer.ONE_SHOT,callback=led_off)
    
# def led_off(pin):
#     global motion, motion_printed
#     print('Motion Not Detected')
#     rLed.value(0)
#     motion =False
#     motion_printed= False
    
    
# PIR.irq(trigger= Pin.IRQ_RISING,handler=led_on)
# try:
#     while True:
        
#         if motion ==True and motion_printed==False:
#             print('Motion Detected')
#             rLed.value(1)
#             motion_printed = True
#         elif motion==False and motion_printed==False:
#             print('sleeping')
#             rLed.value(0)
#             time.sleep(.5)
            
        
# except:
#     rLed.value(0)
#     print('All Done')

# recreating the PIR interrupt with two flags motion and motion_printed

# excellent tutorial and details adjusting my PIR model
# https://www.makerguides.com/hc-sr501-arduino-tutorial/

# from machine import Pin,Timer
# import time

# rPin=16
# rLed =Pin(rPin,Pin.OUT)
# pirPin=0
# PIR =Pin(pirPin,Pin.IN)
# PIRtimer=Timer()

# gPin=17
# gLed=Pin(gPin,Pin.OUT)

# global motion  
# global motion_printed
# counter =0

# motion=False
# motion_printed=False
# rLed.value(0)
# def led_on(pin):
#     global motion, counter
#     motion =True
#     counter+=1
#     print('Hi, counter= ',counter)
#     gLed.value(1)
#     PIRtimer.init(period = 3000,mode=Timer.ONE_SHOT,callback=led_off)
    
# def led_off(pin):
#     global motion, motion_printed
#     print('Motion Not Detected')
#     rLed.value(0)
#     gLed.value(0)
#     motion =False
#     motion_printed= False
    
    
# PIR.irq(trigger= Pin.IRQ_RISING,handler=led_on)
# try:
#     while True:
#         time.sleep_ms(200)
#         if motion ==True and motion_printed==False:
    
#             print('Motion Detected')
#             rLed.value(1)
#             motion_printed = True
#         elif motion==False and motion_printed==False:
#             rLed.value(0)
#             time.sleep(.5)
#             print('sleeping')
#             # pass
        
# except:
#     rLed.value(0)
#     gLed.value(0)
#     print('All Done')

###~~~~~~~~~~~~~~~~~~~~
# from machine import Pin,Timer
# import time

# rPin=16
# rLed =Pin(rPin,Pin.OUT)
# pirPin=0
# PIR =Pin(pirPin,Pin.IN,Pin.PULL_DOWN)
# PIRtimer=Timer()

# gPin=17
# gLed=Pin(gPin,Pin.OUT)

# global motion  
# global motion_printed
# counter =0

# motion=False
# motion_printed=False
# rLed.value(0)
# def pir_handler(pin):
#     global motion
#     print('ALARM, intruder!')
#     for i in range(50):
#         rLed.toggle()
#         time.sleep_ms(100)
#     motion =True
#     PIRtimer=Timer()
#     PIRtimer.init(mode=Timer.ONE_SHOT,period=2000,callback=LedOff)
# def LedOff(pin):
#     global motion 
#     motion =False
#     rLed.value(0)
# PIR.irq(trigger=Pin.IRQ_RISING,handler=pir_handler)
# while True:
#     PirVal=PIR.value()
#     counter+=1
#     print(PirVal, counter)
#     time.sleep(.3)
#     if motion == True and motion_printed==False:
#         print('Motion = True ')
#     elif motion == False and motion_printed==False:
#         print('I am sleeping. Do not wake.')
#         time.sleep(.5)
###~~~~~~~~~~~~~~~~~
##https://shillehtek.com/blogs/news/how-to-connect-and-use-the-hcsr501-pir-sensor-with-a-raspberry-pi-pico-pico-w?utm_source=youtube&utm_medium=product_shelf
## I modified by adding the count so that it would not start by recardng a motion

from machine import Pin
import time

# Initialize PIR sensor on GPIO 0
pir = Pin(0, Pin.IN, Pin.PULL_DOWN)
led = Pin(16, Pin.OUT)  # Initialize LED on GPIO 2
pir_state = False  # Start assuming no motion detected
last_motion_time = 0  # Timestamp of the last motion detected
debounce_time = 5  # Debounce period in seconds

print("PIR Module Initialized")
time.sleep(1)  # Allow the sensor to stabilize
print("Ready")
count=0
while True:
    val = pir.value()  # Read input value from PIR sensor
    current_time = time.time()

    if val == 1:  # Motion detected
        count+=1
        if not pir_state and (current_time - last_motion_time >= debounce_time)and count>1:
            count+=1
            print(current_time - last_motion_time)
            print("Motion detected! and count= ", count)
            pir_state = True  
            led.on()  # Turn on LED
            last_motion_time = current_time  # Update the last motion timestamp

    elif val == 0: 
        if pir_state and (current_time - last_motion_time >= debounce_time):
            pir_state = False
            led.off()
            last_motion_time = current_time  # Update the last motion timestamp

    time.sleep(0.1)  # Small delay to prevent spamming