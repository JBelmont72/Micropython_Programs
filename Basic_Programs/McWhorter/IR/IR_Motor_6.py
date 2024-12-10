'''

'''
from machine import Pin, PWM
from time import sleep

IN1 = Pin(3, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

speed = PWM(Pin(4))
speed.freq(1000)

while True:
        speed.duty_u16(10000)
        IN1.low()  #spin forward
        IN2.high()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
        
        speed.duty_u16(20000)
        IN1.high()  #spin backward
        IN2.low()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
    
        speed.duty_u16(30000)
        IN1.low()  #spin forward
        IN2.high()
        sleep(5)
        
        IN1.low()  #stop
        IN2.low()
        sleep(2)
        
        speed.duty_u16(40000)
        IN1.high()  #spin backward
        IN2.low()
        sleep(5)
        


class DCMotor:      
  def __init__(self, pin1, pin2, enable_pin, min_duty=750, max_duty=1023):
        self.pin1=pin1
        self.pin2=pin2
        self.enable_pin=enable_pin
        self.min_duty = min_duty
        self.max_duty = max_duty

  def forward(self,speed):
    self.speed = speed
    self.enable_pin.duty(self.duty_cycle(self.speed))
    self.pin1.value(0)
    self.pin2.value(1)
    
  def backwards(self, speed):
        self.speed = speed
        self.enable_pin.duty(self.duty_cycle(self.speed))
        self.pin1.value(1)
        self.pin2.value(0)

  def stop(self):
    self.enable_pin.duty(0)
    self.pin1.value(0)
    self.pin2.value(0)
    
  def duty_cycle(self, speed):
   if self.speed <= 0 or self.speed > 100:
        duty_cycle = 0
   else:
    duty_cycle = int(self.min_duty + (self.max_duty - self.min_duty)*((self.speed-1)/(100-1)))
    return duty_cycle