'''
subscriber 7 March 2025
on_message: Handles incoming messages and prints them
subscribe: Listens for messages on the same topic as the publisher (motor/control)
loop_forever: Keeps the script running to listen for messages continuously
'''
import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "motor/control"

# Define what happens when a message is received
def on_message(client, userdata, message):
    print(f"Received message: '{message.payload.decode()}' on topic '{message.topic}'")

# Create an MQTT client
client = mqtt.Client()

# Set up the callback function
client.on_message = on_message

# Connect to the broker and subscribe
client.connect(broker, port, 60)
client.subscribe(topic)

print(f"Subscribed to topic '{topic}' — waiting for messages...")

# Keep the connection alive
client.loop_forever()
