from time import sleep
import json
import os
from paho.mqtt.client import Client

broker = "mqtt.eclipse.org"
topic = "garage_light" # unique identifying topic for your device

def on_message(client, userdata, message):
    val = json.loads(message.payload)
    if val["POWER"] == "ON":
        client.loop_stop()
        client.disconnect()
        os._exit(0)

def on_connect(client, userdata, rc, *args): 
    client.subscribe("stat/%s/RESULT" % topic);
    client.publish("cmnd/%s/power" % topic, "ON")

client = Client("P1")
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883, 60)
client.loop_start()

while True:
    sleep(1)