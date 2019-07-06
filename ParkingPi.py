import json
import time

from mqtt.MQTT import publish
from objects.ParkingSpot import ParkingSpot
from sensors.rfid.RfidReader import RfidReader
from sensors.ultrasonic.UltrasonicSensor import UltrasonicSensor

TRIGGER_HEIGHT = 10
TIMEOUT = 10

print("Welcome to ParkingPi.")
print("This Software runs in the background and communicates with a MQTT-Broker. So never mind missing outputs.")

# set up the sensors
sensor = UltrasonicSensor(trigger_pin=12, echo_pin=18)
sensor2 = UltrasonicSensor(trigger_pin=3, echo_pin=5)
rfid = RfidReader()

# set up the parking spots
spot1 = ParkingSpot(1, sensor, sensor2, rfid)

# add the spots to an array
spots = [spot1]


def publish_json(spot_id, user_id, free, timestamp):
    obj = None
    if user_id is None:
        obj = {
            "parkingId": spot_id,
            "timestamp": timestamp,
            "isFree": free
        }
    else:
        obj = {
            "parkingId": spot_id,
            "timestamp": timestamp,
            "uid": str(user_id),
            "isFree": free
        }

    print json.dumps(obj)
    publish(json.dumps(obj))


def get_current_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


while True:
    for spot in spots:
        distance = spot.ULTRASONIC_SENSOR.measure_distance()

        if distance <= TRIGGER_HEIGHT and spot.free:
            # check if backup sensor agrees
            distance2 = spot.ULTRASONIC_SENSOR_BACKUP.measure_distance()
            if distance2 <= TRIGGER_HEIGHT:
                # spot is now in use
                tmstmp = get_current_timestamp()
                spot.free = False
                uid = spot.RFID_SENSOR.read_card()
                publish_json(spot.ID, uid, spot.free, tmstmp)
        elif distance > TRIGGER_HEIGHT and not spot.free:
            # spot is free now
            tmstmp = get_current_timestamp()
            spot.free = True
            publish_json(spot.ID, None, spot.free, tmstmp)
        else:
            # spot is either still in use or still not in use
            pass

        time.sleep(TIMEOUT)
