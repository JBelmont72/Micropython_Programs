''' 


'''
import neopixel
from machine import Pin
import time
 
pixPin = 0
pixSize = 8
pix = neopixel.NeoPixel(Pin(pixPin), pixSize)
 
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
    myColor=(int(R*255),int(G*255),int(B*255))
    return myColor
 
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8
import SERVO
IRdict ={69 : 'POWER', 70: 'MODE',71 : 'OFF',
         68: 'PLAY', 64 : 'BACK', 67 : 'FORWARD', 7: 'ENTER', 21: '-',
         9 : '+', 22 : 0,25 : 'LOOP', 13:'USD' ,
         12: 1, 24 : 2,94 : 3,
        8 :4, 28 : 5, 90 : 6,
        66 : 7, 82 : 8, 74 : 9}
 
newCommand=[]
beginRecord=False
cmdReady=False
angleString=''
newBit=""
irPin=16
cmd=0
myIR = Pin(irPin, Pin.IN)
def callback(IRbit, addr, ctrl):
    global newCommand
    global beginRecord
    global cmdReady
    global IRdict
    global cmd
    if IRbit==69:
        beginRecord=True
        newCommand=[]
        cmdReady=False
    if beginRecord==True and IRbit!=-1:
        newCommand.append(IRdict[IRbit])
    if IRbit==7:
        cmdReady=True
        cmd=newCommand[1]
        
IR = NEC_8(myIR, callback)  # Instantiate receiver
try:
    while True:
        if cmd==0:
            for i in range(0,8):
                pix[i]=[0,0,0]
            pix.write()
        if cmd==1:
            pix.fill([255,0,0])
            pix.write()
        if cmd==2:
            pix.fill([0,255,0])
            pix.write()
        if cmd==3:
            pix.fill([0,0,255])
            pix.write() 
        if cmd==4:
            for i in range(0,360,1):
                for j in range(0,8,1):
                    deg=i+(j)*45
                    if deg>=360:
                        deg=deg-360
                    color=getRGB(deg)
                    pix[j]=color
                    if cmd!=4:
                        break
                if cmd!=4:
                    break
                pix.write()
                time.sleep(.01)
        if cmd==5:
            for i in range(0,360,1):
                color=getRGB(i)
                pix.fill(color)
                pix.write()
                time.sleep(.01)
                if cmd!=5:
                    break
        if cmd==6:
            for i in range(1,8,1):
                pix.fill([255,0,0])
                pix[i]=[0,0,255]
                #pix[7-i]=green
                pix.write()
                time.sleep(.1)
                if cmd!=6:
                    break
            for i in range(6,-1,-1):
                pix.fill([255,0,0])
                pix[i]=[0,0,255]
                #pix[7-i]=green
                pix.write()
                time.sleep(.1)
                if cmd!=6:
                    break
 
except KeyboardInterrupt:
    IR.close()
    for i in range(0,8):
        pix[i]=[0,0,0]
        pix.write()
    print("Program Terminated")