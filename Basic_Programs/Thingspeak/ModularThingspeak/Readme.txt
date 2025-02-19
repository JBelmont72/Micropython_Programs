
https://www.halvorsen.blog/documents/technology/iot/pico/pico_thingspeak.php

https://microdigisoft.com/weather-monitoring-with-raspberry-pi-pico-w-bme280-and-thingspeak/#google_vignette


for my modular format of thinspeak I have the BME280.py library in lib folder.
NOte that I changed or int16   to b binary
the main.py calls the BNE_Class.py for the values.
The WiFiNetwork.py  activates the link and has a watchdog.
THe Thingspeak.py uses the field (number of fields and the field_data from the BME_Class.py to 
build the url and then do the get requests(()Of COurse the functio is called ain the main.py)