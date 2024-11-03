import time
import paho.mqtt.client as mqtt
import logging

# Setup logging
logging.basicConfig(filename='sender.log', level=logging.INFO, format='%(message)s')

# Define the callback function for when a message is published
def on_publish(client, userdata, mid, properties=None):
    print("Message Published")

# Create a client instance
client = mqtt.Client()

# Assign the callback function
client.on_publish = on_publish

# Connect to the broker
broker = "127.0.0.1"
port = 1883
client.connect(broker, port, 60)

# Publish messages
topic = "mqtt/messages"
message_count = 10000

for i in range(message_count):
    msg = f"Message {i+1}"
    info = client.publish(topic, payload=msg.encode('utf-8'), qos=0)
    info.wait_for_publish()
    logging.info(msg)
    print(f"Sent: {msg}")
    time.sleep(0.001)  # Adjust the sleep time as needed

print(f"Total messages sent: {message_count}")