'''

'''
from RGB_lib import *
from machine import PWM,Pin
from time import sleep
# from machine import Pin,PWM
# from time import sleep

# myColor ={'red':[255,0,0]}
# # print(myColor)
# # print(myColor['red'])
# # mc = 'red'
# # print(myColor[mc])
# myColor.update({'blue':[0,0,255],'green':[0,255,0],'cyan':[0,255,255],'magenta':[255,0,255],'yellow':[255,63,0],
#                 'orange':[255,32,0],'white':[255,255,255],'off':[0,0,0],'purple':[127,0,255]})
# # print(myColor)
# ## set up pwm for three pins for RGB led
def LightLED(mc):
    print('selected color is ',mc)

rPin=14
gPin=17
bPin=16
rLed=PWM(Pin(rPin))
rLed.freq(1000)
rLed.duty_u16(0)
gLed=PWM(Pin(gPin))
gLed.freq(1000)
gLed.duty_u16(0)
bLed=PWM(Pin(bPin))
bLed.freq(1000)
bLed.duty_u16(0)
def RGB(mc):
    rgb = myColor[mc]
    print('rgb',rgb)
    print(rgb[0])
    print(rgb[1])
    print(rgb[2])
    rLed.duty_u16(int(rgb[0]*65535/255))
    print(rgb[0])
    print(int(rgb[0]*65535/255))
    gLed.duty_u16(int(rgb[1]*65535/255))
    bLed.duty_u16(int(rgb[2]*65535/255))
    
try:    
    while True:

        mc = input('Enter your desired color.')
        if mc in myColor:
            mc =mc.lower()
            print(mc)
        if mc not in myColor:
            print('not a valid selection. try again.')
            continue
        RGB(mc)
        ## effefctive ways to obtain the value of a specific key in dictionary    
        # x =myColor[mc]
        # print('x',x)
        # y =myColor.get(mc)
        # print('y: ',y)
except KeyboardInterrupt:
    print('done')
    rLed.duty_u16(0)
    gLed.duty_u16(0)
    bLed.duty_u16(0)
       
# Dict={1:'A',2:'B',3:'Bob',4:'Jane'}
# print(Dict.items())
# print(Dict.keys())
# Dict[5]='Sam'
# print(Dict)
# Dict['Hi']='good-bye'
# print(Dict)
# Dict['friends']=['Tom','Bill','Mike','Joe']
# print(Dict)
# print(Dict['friends'])
# print(Dict['friends'][0])
# Dict['dog']='Fuzzer'
# print(Dict.values())
# print(Dict.keys())
# if 'A' not  in Dict: ## must use the key value
#     print("'A' is not in Dict")
# if 1 in Dict:
#     print('1 is in Dict')
# if 'dog'  in Dict:
#     print('"dog" is in Dict')
#     print("'dog' is the key. the Value is ",Dict['dog']) ## this gives the value of the key 'dog'
# for i in Dict:
#     print(i, ' ',Dict[i],'  ')