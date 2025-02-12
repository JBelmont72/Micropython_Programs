'''
module thingspeak.py 

'''
import urequests
import thingspeakconfig

class ThingSpeakApi:
    def __init__(self, field):
        self.server = thingspeakconfig.server
        self.apikey = thingspeakconfig.apikey
        self.field = field
        
    def WriteData(self, fieldvalue):
        url = f"{self.server}/update?api_key={self.apikey}&field{self.field}={fieldvalue}"
        request = urequests.post(url)
        request.close()