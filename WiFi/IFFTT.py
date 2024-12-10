'''need to set up the ifttt account
https://ifttt.com/maker_webhooks
'''
import network
import urequests
import json
import time
from machine import Pin
# from secrets import secrets
import machine

print("starting connection")
wlan = network.WLAN(network.STA_IF)

wlan.active(True)


print("connecting ...")
wlan.connect('NETGEAR48', 'waterypanda901')
# wlan.connect(secrets['ssid'], secrets['password'])

# Wait for connect or fail
wait = 10
while wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('wifi connection failed')
else:
    print('connected')
    
status = wlan.ifconfig()
print( 'ip = ' + status[0] )

def ifttt_webhook(event, key, values=None):
    url="https://maker.ifttt.com/trigger/"+event+"/with/key/"+key
    if values is not None:
        url = url + '?'
        for counter, value in enumerate(values, start=1):
            if counter < 4:
                if counter > 1:
                    url=url+'&'
                url=url+"value"+str(counter)+"="+values[counter-1]
    try:
        r = urequests.get(url)
        if r.status_code>199 and r.status_code<300:
            r.close()
            return 0
        else:
            r.close()
            return -1
    except:
        r.close()
        return -2

button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

current_state = 0
while True:
    new_state = button.value()
    if new_state != current_state:
        # if new_state == 1:
        #     ifttt_webhook(secrets['ifttt_eventname'], secrets['ifttt_key'], values=None)
        current_state = new_state
    time.sleep(0.5)
   