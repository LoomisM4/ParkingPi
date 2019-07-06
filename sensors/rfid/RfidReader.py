import time
import RPi.GPIO as GPIO
import MFRC522


class RfidReader:
    __continue_reading = True
    MAX_TIMES_READING = 5

    def read_card(self):
        # Create an object of the class MFRC522
        MIFAREReader = MFRC522.MFRC522()

        i = 0
        # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        for i in range(self.MAX_TIMES_READING):
            # Scan for cards
            (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # Get the UID of the card
            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == MIFAREReader.MI_OK:
                self.__stop_reading()
                return uid

            time.sleep(3)

        return None

    def __stop_reading(self):
        GPIO.cleanup()
