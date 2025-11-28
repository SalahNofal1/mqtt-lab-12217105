import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "people_pub_12217105")
client.connect("localhost", 1883, 60)

while True:
    people = random.randint(0, 10)
    msg = f"StudentID: 12217105 | People Count: {people}"
    client.publish("salah/people", msg)
    print("Published:", msg)
    time.sleep(2)
