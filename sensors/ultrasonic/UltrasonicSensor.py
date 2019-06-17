import RPi.GPIO as GPIO
import time


class UltrasonicSensor:
    TRIGGER_PIN = None
    ECHO_PIN = None

    start = None
    end = None

    __speed_of_sound = 343.2

    def __init__(self, trigger_pin, echo_pin):
        self.TRIGGER_PIN = trigger_pin
        self.ECHO_PIN = echo_pin

    def __setup_pi(self):
        GPIO.setwarnings(False)
        # Setup BCM mode
        GPIO.setmode(GPIO.BCM)
        # Setup the Trigger-Pin and output low
        GPIO.setup(self.TRIGGER_PIN, GPIO.OUT)
        GPIO.output(self.TRIGGER_PIN, GPIO.LOW)
        # Setup the Echo-Pin
        GPIO.setup(self.ECHO_PIN, GPIO.IN, GPIO.PUD_DOWN)

    def __calculate_distance(self):
        t = self.end - self.start
        return t * self.__speed_of_sound / 2

    def measure_distance(self):
        try:
            self.__setup_pi()

            self.start = time.time()
            GPIO.output(self.TRIGGER_PIN, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(self.TRIGGER_PIN, GPIO.LOW)

            counter = 1
            while GPIO.input(self.ECHO_PIN) == 0:
                # no signal received yet
                if counter < 1000:
                    self.start = time.time()
                    counter += 1
                else:
                    print("end")
                    break
            while GPIO.input(self.ECHO_PIN) == 1:
                # signal received
                self.end = time.time()

            # calculate the distance in meters
            distance = self.__calculate_distance()
            # return the distance in centimeters
            return distance * 100
        finally:
            GPIO.cleanup
