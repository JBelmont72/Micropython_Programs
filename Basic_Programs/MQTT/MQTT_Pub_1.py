'''7 March 2025
Broker: The server that handles messages (hivemq in this case)
Topic: The channel where messages are sent (motor/control)
Message: What you want to send (e.g., "Turn Motor ON")
Connect, publish, disconnect: Basic steps to send data!

'''
import paho.mqtt.client as mqtt  

broker = "broker.hivemq.com"  
port = 1883  
topic = "motor/control"  

# Create an MQTT client  
client = mqtt.Client()  

# Connect to the broker  
client.connect(broker, port, 60)  

# Publish a message  
client.publish(topic, "Turn Motor ON")  
print(f"Message sent to topic '{topic}'")  

# Disconnect  
client.disconnect()
