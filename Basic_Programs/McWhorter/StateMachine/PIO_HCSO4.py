'''
# https://www.youtube.com/watch?v=se1ypDUaHcA&t=15s

'''













# import time
# from machine import Pin

# # from PicoAutonomousRobotics import KitronikPicoRobotBuggy
# from time import sleep

# # buggy = KitronikPicoRobotBuggy()


# #Ultrasonic: from kiktronic
#     #there are 2 Ultrasonic headers. The front one is the default if not explicitly called wth 'r' for rear
#     # if we get a timeout (which would be a not fitted sensor, or a range over the sensors maximium the distance returned is -1           
# def getDistance(self, whichSensor = "f"):
#     trigger = Pin(14, Pin.OUT)
#     echo = Pin(15, Pin.IN)
#     if(whichSensor == "r"):
#         trigger = Pin(3, Pin.OUT) #rear
#         echo = Pin(2, Pin.IN)
#     trigger.low()
#     time.sleep_us(2)
#     trigger.high()
#     time.sleep_us(5)
#     trigger.low()
#     timePassed = time.sleep.time_pulse_us(echo, 1, self.maxDistanceTimeout)
#     if(timePassed ==-1): #timeout - range equivalent of 5 meters - past the sensors limit or not fitted
#         distance = -1
#     else:
#         distance = (timePassed * self.conversionFactor) / 2
#     return distance
    
# def setMeasurementsTo(self,units):
#     #0.0343 cm per microsecond or 0.0135 inches
#     if(units == "inch"):
#         self.conversionFactor = 0.0135 #if you ask nicely we can do imperial
#     else:
#         self.conversionFactor = 0.0343 #cm is default - we are in  metric world.
# while True:
#    frontDistance = getDistance("f")
#    print("Front Distance:", frontDistance)
#    sleep(1)