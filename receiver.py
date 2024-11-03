import paho.mqtt.client as mqtt
import logging
import atexit

# Setup logging
logging.basicConfig(filename='receiver.log', level=logging.INFO, format='%(message)s')

# Define the callback function for when a message is received
def on_message(client, userdata, msg):
    message = msg.payload.decode()
    logging.info(message)
    print(f"Received: {message}")
    global message_count
    message_count += 1

# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("mqtt/messages")

# Create a client instance
client = mqtt.Client()

# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
broker = "127.0.0.1"
port = 1883
client.connect(broker, port, 60)

# Initialize message count
message_count = 0

# Register a function to print the total count of messages received when exiting
def print_message_count():
    print(f"Total messages received: {message_count}")

atexit.register(print_message_count)

# Start the loop to process callbacks
client.loop_forever()