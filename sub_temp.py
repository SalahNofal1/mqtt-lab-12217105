import paho.mqtt.client as mqtt

def on_message(client, userdata, message):
    print("Received:", message.payload.decode())

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "temp_sub_12217105")
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("salah/temp")

client.loop_forever()
