import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1, "hum_pub_12217105")
client.connect("localhost", 1883, 60)

while True:
    hum = random.randint(30, 90)
    msg = f"StudentID: 12217105 | Humidity: {hum}%"
    client.publish("salah/humidity", msg)
    print("Published:", msg)
    time.sleep(2)
