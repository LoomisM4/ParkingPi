class ParkingSpot:
    ULTRASONIC_SENSOR = None
    RFID_SENSOR = None

    ID = None
    free = True

    def __init__(self, id, ultrasonic_sensor, rfid_sensor):
        self.ID = id
        self.ULTRASONIC_SENSOR = ultrasonic_sensor
        self.RFID_SENSOR = rfid_sensor


