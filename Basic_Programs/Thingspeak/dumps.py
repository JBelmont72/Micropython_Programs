'''
'''
import ujson

# It's mandatory to close response objects as soon as you finished
# working with them. On Pycopy platforms without full-fledged
# OS, not doing so may lead to resource leaks and malfunction.

THINGSPEAK_API_KEY='aaaaaaa'
t=float(3.555)
h= int(10)
data = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": t,
        "field2": h,
    }

print(data)
data1 =ujson.dumps(data)
print(data1)


