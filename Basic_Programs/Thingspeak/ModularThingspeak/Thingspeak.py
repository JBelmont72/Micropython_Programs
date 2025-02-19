'''XA19ARK93Z22UD33 the pico channel
module Thingspeak.py 
YZRDGNJ7C9JZI3MP 
'''
import urequests
import thingspeakconfig
import time
class ThingSpeakApi:
    
    def __init__(self, field):
        self.server = "http://api.thingspeak.com/"
        self.apikey = 'XA19ARK93Z22UD33'
        #self.server = thingspeakconfig.server
        #self.apikey = thingspeakconfig.apikey
        self.field=field
  
        
    #def WriteData(self, fieldvalue):
    #    url = f"{self.server}update?api_key={self.apikey}&field{self.field}={fieldvalue}"
     #   try:
     #
      #t(url)  # Use GET instead of POST for ThingSpeak (instead of post!!!)
        #request.close()
        #url = f"{self.server}/update?api_key={self.apikey} json = self.fieldvalue, headers =self.HTTP_HEADERS"
        #url = f"{self.server}/update?api_key={self.apikey}&field{self.field}={fieldvalue}"       
        # request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY, json = bme_readings, headers = self.HTTP_HEADERS ) 
        #request = urequests.post(url)
        #request.close()
    def WriteSingleField(self,fieldvalue):
        url = f"{self.server}/update?api_key={self.apikey}&field{self.field}={fieldvalue}"
        request = urequests.get(url)  # Use GET instead of POST for ThingSpeak (instead of post!!!)
        request.close()

    def WriteMultipleFields(self, field_data):
        url = f"{self.server}update?api_key={self.apikey}"
        try:           
            for i, field_value in enumerate(field_data, start=1):
                url += f"&field{i}={field_value}"  
            print(f"Sending to ThingSpeak: {url}")  # Debugging URL
            request = urequests.get(url)
            print(f"Response code: {request.status_code}")  # ✅ Print HTTP response code
            print(f"Response text: {request.text}")  # ✅ Print response content for debugging
            request.close()               
        except Exception as err:
            print(f"Error sending to ThingSpeak: {err}")


'''
    def WriteMultipleFields(self, field_data):
        url = f"{self.server}update?api_key={self.apikey}"
        try:
            for i, field_value in enumerate(field_data, start=1):
                url += f"&field{i}={field_value}"  
            print(f"Sending to ThingSpeak: {url}")  # Debugging URL
            request = urequests.get(url)
            print(f"Response code: {request.status_code}")  # ✅ Print HTTP response code
            print(f"Response text: {request.text}")  # ✅ Print response content for debugging
            request.close()

        except Exception as err:
            print(f"Error sending to ThingSpeak: {err}")
'''
'''   
    def WriteMultipleFields(self,field_data):
        i=1
        #url = f"{self.server}update?api_key={self.apikey}&field{self.field}={fieldvalue}"

        url = f"{self.server}/update?api_key={self.apikey}"
        try:
            for field_value in field_data:
                url= url + f"&field{i}={field_value}"
                print(f'{url}')
                i+=1
                if i==5:
                    request = urequests.get(url)  # Use GET instead of POST for ThingSpeak (instead of post!!!)
                    print(request)
                    i=1
            #print(f'{request}')
            time.sleep(15)
            request.close()
        except Exception as err:
            print(f'Error sending to Thingspeak: {err}')
'''