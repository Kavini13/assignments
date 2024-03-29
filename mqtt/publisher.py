import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
client.on_connect = on_connect

client.connect("localhost", 1883, 60)
client.loop_start()

while True:
    message = input("Enter message to publish: ")

    if message.lower() == 'exit':
        break
    client.publish("topic", message)

client.loop_stop()
client.disconnect()

