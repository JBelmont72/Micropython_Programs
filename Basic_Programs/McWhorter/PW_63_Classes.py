''' PW _ 63 and then PW 64  classes
i put the method in init and placed the value in this variable
so i'm not calling the method, i am just retrieving the value
 return A,vol ## if return self. ... then i can use in other methods as well
'''

class rect:
    def __init__(self,wid,len=4,h=3):
        self.l=len
        self.w=wid
        self.area=self.Area()
        self.perimeter=self.Perimeter()
        self.vol = self.Volume(h)
        
        
    def Area(self):
        self.a=self.l * self.w
        return self.a
    def Perimeter(self):
        self.p=2* self.l + 2* self.w
        return self.p  
    def Volume(self,h):
        self.height=h 
        self.vol=self.height* self.l * self.w 
        return self.vol
## two ways to call the return value of def Area
myRect1=rect(2,3,4)
print(myRect1.area)
ar=myRect1.Area()
print(ar)
## all three below are same result
volume=myRect1.Volume(3)
print(volume)
vol=myRect1.vol
print(vol)
print(myRect1.vol)
#####~~~~~~~~~~ create led objects and a class to control
# class LED:
#     def __init__(self,ledPin):
#         from machine import Pin
#         self.pinNumber=ledPin
#         self.ledObject=Pin(self.pinNumber,Pin.OUT)
#     def blink(self,numBlink,delayTime):
#         import time
#         for i in range(0,numBlink,1):
#             self.ledObject.value(1)
#             time.sleep(delayTime)
#             self.ledObject.value(0)
#             time.sleep(delayTime)
# rPin=16
# gPin=17

# redBlink=5
# redDelay=.5

# greenBlink=10
# greenDelay=.25

# myLed1=LED(rPin)
# myLed1.blink(redBlink,redDelay)
# myLed2=LED(gPin)
# myLed2.blink(greenBlink,greenDelay)
