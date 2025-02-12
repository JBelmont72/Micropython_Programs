'''internal sensor of pico W'''
from machine import ADC
import time
class Temperature:
    
    def __init__(self):
        adcpin = 4
        self.sensor = ADC(adcpin)
        
    def ReadTemperature(self):
        adc_value = self.sensor.read_u16()
        volt = (3.3/65535)*adc_value
        temperature = 27 - (volt - 0.706)/0.001721
        # tempF=32 +(9/5)*temperature
        
        return round(temperature, 1)

def main():
    myTemp=Temperature()
    while True:
        
        temperature = myTemp.ReadTemperature()
        print(temperature)
        time.sleep(5)
if __name__=='__main__':
    main()