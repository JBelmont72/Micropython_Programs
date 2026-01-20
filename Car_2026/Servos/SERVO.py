'''Servo Library for Car 2026 
pos(angle) - set servo to angle 0-180
TiltPos(angle) - set tilt servo to angle 0-90

# get user input for PWMValue between 0 and 65535 and set the PWM duty cycle accordingly 2500 straight up 6800 down,5800 forward

'''


### SERVO library
from Car_2026.Servos.map_fx import map_value


class servo:
    def __init__(self,sPin):
        import machine
        self.servoPin=sPin
        self.obj=machine.PWM(machine.Pin(self.servoPin))
        self.obj.freq(50)
    
    def pos(self,angle):
        #writeVal=6553/180*angle+1638
        writeVal= -38.511 *angle +8600
        self.obj.duty_u16(int(writeVal))

    
    def AlternatePos(self,angle):   # using map function for mapping angle to PWM value
        if angle>180:
            angle=180
        if angle < 0:
            angle=0   
        for angle in range(0,181,10):
            pwm_value = map_value(angle, 0, 180, 2500, 6800)
            print(f'Angle: {angle}, PWM Value: {pwm_value}')
            self.obj.duty_u16(int(pwm_value))

    
        
    def TiltPos(self,angle):
        if angle>90:
            angle=90
        if angle < -7:
            angle=-7   
        #writeVal=6553/180*angle+1638
        writeVal= -(110 / 3) * angle +5800
        self.obj.duty_u16(int(writeVal))
    def AlternateTiltPos(self,angle):   # using map function for mapping angle to PWM value
        if angle>90:
            angle=90
        if angle < -7:
            angle=-7   
        for angle in range(0,91,10):
            pwm_value = map_value(angle, 0, 90, 5800, 6800)
            print(f'Angle: {angle}, PWM Value: {pwm_value}')
            self.obj.duty_u16(int(pwm_value))       