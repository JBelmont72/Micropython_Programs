'''
https://randomnerdtutorials.com/micropython-hc-sr04-ultrasonic-esp32-esp8266/ this is for pico/ esp32
https://tutorials-raspberrypi.com/raspberry-pi-ultrasonic-sensor-hc-sr04/    this is for the raspberry pi
make sure echo pin only feeds 3.3 volts inot the pico or will damage, use 100,200 ohm voltage splitter

distance to an object = ((speed of sound in the air)*time)/2

'''
# import RPi.GPIO as GPIO   ## for raspberry pi
import machine
import time
 
#GPIO Mode (BOARD / BCM)
# GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 15
 
#set GPIO direction (IN / OUT)
# GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
# GPIO.setup(GPIO_ECHO, GPIO.IN)
Echo=machine.Pin(machine.Pin(15), machine.Pin.IN, machine.Pin.PULL_DOWN) 
Trigger=machine.Pin(16),machine.Pin.OUT
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
