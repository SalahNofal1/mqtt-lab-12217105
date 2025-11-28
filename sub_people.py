import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received:", message.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "people_sub_12217105")
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("salah/people")

client.loop_forever()
