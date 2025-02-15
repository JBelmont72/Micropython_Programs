'''
module thingspeak.py 

'''
import urequests
# import ThingSpeakConfig
# from BME_Class import BME_Temperature

class ThingSpeakApi:
    def __init__(self, field1):
        self.server =server = "http://api.thingspeak.com/"
        self.apikey = 'YZRDGNJ7C9JZI3MP'
        # self.server = ThingSpeakConfig.server
        # self.apikey = ThingSpeakConfig.apikey
        self.HTTP_HEADERS = {'Content-Type': 'application/json'}        
        self.field = field1
        self.fieldvalue=30
  
        
    def WriteData(self, fieldvalue): 
        url = f"{self.server}/update?api_key={self.apikey} json = self.fieldvalue, headers =self.HTTP_HEADERS"
        url = f"{self.server}/update?api_key={self.apikey}&field{self.field}={fieldvalue}"       
        # request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = self.HTTP_HEADERS ) 
        request = urequests.post(url)
        request.close()