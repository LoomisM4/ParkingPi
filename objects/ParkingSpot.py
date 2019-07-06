class ParkingSpot:
    ULTRASONIC_SENSOR = None
    ULTRASONIC_SENSOR_BACKUP = None
    RFID_SENSOR = None

    ID = None
    free = True

    def __init__(self, id, ultrasonic_sensor, ultrasonic_sensor_backup, rfid_sensor):
        self.ID = id
        self.ULTRASONIC_SENSOR = ultrasonic_sensor
        self.ULTRASONIC_SENSOR_BACKUP = ultrasonic_sensor_backup
        self.RFID_SENSOR = rfid_sensor


