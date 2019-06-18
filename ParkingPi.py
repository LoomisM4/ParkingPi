from ParkingSpot import ParkingSpot
from sensors.ultrasonic.UltrasonicSensor import UltrasonicSensor
from mqtt.MQTT import MQTT
import time
#import pydevd_pycharm
#pydevd_pycharm.settrace('192.168.178.20', port=9000, stdoutToServer=True, stderrToServer=True)

TRIGGER_HEIGHT = 60
TIMEOUT = 30

print("Welcome to ParkingPi.")
print("This Software runs in the background and communicates with a MQTT-Broker. So never mind missing outputs.")

# set up the sensors
sensor = UltrasonicSensor(trigger_pin=18, echo_pin=24)

# set up the parking spots
spot1 = ParkingSpot(1, sensor, None)

# add the spots to an array
spots = [spot1]

while True:
    mqtt = MQTT()

    for spot in spots:
        distance = spot.ULTRASONIC_SENSOR.measure_distance()

        if distance <= TRIGGER_HEIGHT and spot.FREE:
            # spot is now in use
            spot.FREE = False
            # TODO RFID
            mqtt.publish("In Benutzung: " + str(spot.ID))
        elif distance > TRIGGER_HEIGHT and not spot.FREE:
            # spot is free now
            spot.FREE = True
            mqtt.publish("Wieder frei: " + str(spot.ID))
        else:
            # spot is either still in use or still not in use
            pass

        time.sleep(TIMEOUT)
