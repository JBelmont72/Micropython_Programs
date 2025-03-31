'''  Avoidance  sensor  number 31  HW-488
.ino code:int Led = 13 ;// define LED Interface
int buttonpin = 3; // define the obstacle avoidance sensor interface
int val ;// define numeric variables val
void setup ()
{
  pinMode (Led, OUTPUT) ;// define LED as output interface
  pinMode (buttonpin, INPUT) ;// define the obstacle avoidance sensor output interface
}
void loop ()
{
  val = digitalRead (buttonpin) ;// digital interface will be assigned a value of 3 to read val
  if (val == HIGH) // When the obstacle avoidance sensor detects a signal, LED flashes
  {
    digitalWrite (Led, HIGH);
  }
  else
  {
    digitalWrite (Led, LOW);
  }
}
left grnd, + 3.3 V, out is sensor
'''
import sys
from machine import Pin
from time import sleep
pin=17
trigPin=Pin(pin,Pin.IN)
try:
    while True:
        Trigger =trigPin.value()
        if Trigger==1:
            print('High')
        else:
            print('Low')
        print(Trigger)
        sleep(.1)
except KeyboardInterrupt:
    sys.exit()