import paho.mqtt.client as client

from mqtt.Settings import Settings


class MQTT:
    def publish(self, message):
        settings = Settings()
        mqtt = client.Client()
        mqtt.username_pw_set(settings.USERNAME, settings.PASSWORD)
        mqtt.connect(settings.SERVER, settings.PORT)
        mqtt.publish(settings.TOPIC, message, 1)
        mqtt.disconnect()
