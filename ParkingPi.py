from objects.ParkingSpot import ParkingSpot
from sensors.rfid.RfidReader import RfidReader
from sensors.ultrasonic.UltrasonicSensor import UltrasonicSensor
from mqtt.MQTT import MQTT
import time

TRIGGER_HEIGHT = 60
TIMEOUT = 30

json = "spot_id: {}, user_id: {}, free: {}, since: {}"

print("Welcome to ParkingPi.")
print("This Software runs in the background and communicates with a MQTT-Broker. So never mind missing outputs.")

# set up the sensors
sensor = UltrasonicSensor(trigger_pin=12, echo_pin=18)
rfid = RfidReader()

# set up the parking spots
spot1 = ParkingSpot(1, sensor, rfid)

# add the spots to an array
spots = [spot1]

mqtt = MQTT()


def publish_json(spot_id, user_id, free, timestamp):
    temp = json.format(spot_id, user_id, free, timestamp)
    mqtt.publish("{" + temp + "}")


def get_current_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


while True:
    for spot in spots:
        distance = spot.ULTRASONIC_SENSOR.measure_distance()

        if distance <= TRIGGER_HEIGHT and spot.free:
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
