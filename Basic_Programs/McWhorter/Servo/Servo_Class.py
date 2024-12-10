'''Servo library, 
enterDutyCycle(self,dutyCycle)  for entering duty cycle
enterDegree(self,deg) for entering degree(0-180) and returning a PWM between 1638 and 8191 which is the range of a 180 degree servo
  to call the class is" myServ=ServoClass(18)" with servo pin as 18,  myServ is the object in this case but can be many
create a servo class and then a servo library
1638 is .5/20 * 65535 = 1638   2.5/20 * 65535 is 8191
pwm = deg/180 *65535     m=    (8191-1638)/180 =36.40556
y = mx+b  8191=36.4(180)+b   b=1639
'''

class ServoClass:
    def __init__(self,sPin):
        from machine import Pin,PWM
        self.sPin = sPin
        self.myServo1=PWM(self.sPin)
        self.myServo1.freq(50)
    def enterDutyCycle(self,dutyCycle):
        self.dutyCycle=dutyCycle
        self.myServo1.duty_u16(dutyCycle)
        print(self.dutyCycle)
        return self.dutyCycle
        
    def enterDegree(self,deg):
        self.deg=deg       
        dutyCycle =int((36.4* deg)+1639)
        self.myServo1.duty_u16(dutyCycle)
        print(dutyCycle)
        return self.dutyCycle
        
import time        
        
        
while True:
    dutyCycle =int(input('Enter duty Cycle'))
    deg =int(input('Enter degrees'))
    myServ=ServoClass(18)
    a=myServ.enterDutyCycle(dutyCycle)
    time.sleep(1)
    b=myServ.enterDegree(deg)
    # a=myServ.servoFx
    print('a:',a,' b: ',b)
    # b=myServ.degree
    # print('duty; ',a,'Deg: ',b)
    
    

        

