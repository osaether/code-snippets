from time import sleep
import ssl
import json
import os
from paho.mqtt.client import Client 

username = "your VRM email"
password = "your VRM pasword"
portal_id = "your VRM portal ID"

def on_message(client, userdata, message):
	val = json.loads(message.payload)
	print message.topic, " = ", val["value"]
	val = json.loads(message.payload)
	if val["value"] == 1:
		client.loop_stop()
		client.disconnect()
		os._exit(0)


def on_connect(client, userdata, rc, *args): 
	client.subscribe("N/%s/system/0/Relay/0/State" % portal_id)
	client.publish("W/%s/system/0/Relay/0/State" % portal_id, json.dumps({"value": 1}))

client = Client("P1")
client.tls_set(cert_reqs=ssl.CERT_NONE)
client.tls_insecure_set(True)
client.username_pw_set(username, password=password)
client.connect("mqtt.victronenergy.com", port=8883)
client.on_connect = on_connect
client.on_message = on_message

client.loop_start()

while True:
	sleep(1)
