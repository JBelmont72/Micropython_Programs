'''
https://microcontrollerslab.com/micropython-dc-motor-l298n-driver-esp32-esp8266/
'''
from machine import Pin, ADC, PWM  #importing PIN,ADC and PWM
import time #importing time   
import utime 

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
# Defining motor pins

#OUT1  and OUT2
In1=Pin(3,Pin.OUT)  #IN1`
In2=Pin(4,Pin.OUT)  #IN2
EN_A=PWM(Pin(5))




#OUT3  and OUT4
In3=Pin(2,Pin.OUT)  #IN3
In4=Pin(1,Pin.OUT)  #IN4
EN_B=PWM(Pin(0))

  
# Defining frequency for enable pins
EN_A.freq(1500)
EN_B.freq(1500)


# Forward
def move_forward():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    
# Backward
def move_backward():
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
try:
    while True:
        time.sleep(0.1)
        # xValue=36000
        # yValue=36000
        yValue = yAxis.read_u16()
        xValue = xAxis.read_u16()
        print(yValue)
        print(xValue)
        
   ##     if yValue >= 32000 and yValue <= 34000 or xValue >= 32000 and xValue <= 34000:
        if yValue >= 50000 and yValue <= 54000 :
        # if yValue >= 50000 and yValue <= 54000 or xValue >= 48000 and xValue <= 52000:

            stop()
            

        
        
        if yValue >= 54000:
            duty_cycle = (((yValue-65535/2)/65535)*100)*2
            print("Move backward: Speed " + str(abs(duty_cycle)) + " %")
            duty_cycle = ((yValue/65535)*100)*650.2
            print('Y highrer dutyCycled',duty_cycle)
            # EN_A.duty_u16(int(duty_cycle))
            # EN_B.duty_u16(int(duty_cycle))
            
            # move_backward()

            

        
        elif yValue <= 50000:
            duty_cycle = ((yValue-65535/2)/65535*100)*2
            print("Move Forward: Speed " + str(abs(duty_cycle)) + " %")
            duty_cycle = abs(duty_cycle)*650.2
            print('y lower duty cycle:c',duty_cycle)
            EN_A.duty_u16(int(duty_cycle))
            EN_B.duty_u16(int(duty_cycle))
            
            move_forward()
        
        
        # elif xValue < 48000:
        #     duty_cycle = (((xValue-65535)/65535)*100)
        #     print("Move Left: Speed " + str(abs(duty_cycle)) + " %")
        #     duty_cycle = abs((duty_cycle)*650.25)

        #     EN_B.duty_u16(0)
        #     EN_A.duty_u16(int(duty_cycle))
            
        #     move_forward()


        # elif xValue > 54000:
        #     duty_cycle = ((xValue-65535/2)/65535*100)*2
        #     print("Move Right: Speed " + str(abs(duty_cycle)) + " %")
        #     duty_cycle = abs(duty_cycle)*650.2

        #     EN_B.duty_u16(int(duty_cycle))
        #     EN_A.duty_u16(0)
            
        #     move_forward()
except KeyboardInterrupt:
    EN_B.duty_u16(0)
    EN_A.duty_u16(0)
    print('DOne')
        
    

# from machine import PWM,ADC
# import time
# xPin=27
# xADC=ADC(xPin)
# yPin=26
# yADC =ADC(yPin) 
# while True:
#     yVal =yADC.read_u16()
#     xVal =xADC.read_u16()  
#     print('xVal:  ',xVal,'  yVal:  ',yVal)
#     time.sleep(.5)
    
    