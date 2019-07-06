from paho.mqtt.publish import single


def publish(message):
    single(topic="/smp/spots", payload=message, qos=2, hostname="iot.eclipse.org")