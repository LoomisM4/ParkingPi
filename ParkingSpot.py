from sensors.ultrasonic.UltrasonicSensor import UltrasonicSensor


class ParkingSpot:
    ULTRASONIC_SENSOR: UltrasonicSensor = None
    RFID_SENSOR = None

    ID = None
    FREE = True

    def __init__(self, id, ultrasonic_sensor, rfid_sensor):
        self.ID = id
        self.__ULTRASONIC_SENSOR = ultrasonic_sensor
        self.__RFID_SENSOR = rfid_sensor


