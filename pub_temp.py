import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "temp_pub_12217105")
client.connect("localhost", 1883, 60)

while True:
    temp = random.randint(20, 35)
    msg = f"StudentID: 12217105 | Temperature: {temp}°C"
    client.publish("salah/temp", msg)
    print("Published:", msg)
    time.sleep(2)
