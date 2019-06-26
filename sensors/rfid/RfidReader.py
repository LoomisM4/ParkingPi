import time
import RPi.GPIO as GPIO
import MFRC522

class RfidReader:
    __continue_reading = True
    MAX_TIMES_READING = 5

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    def read_card(self):
        i = 1
        # This loop keeps checking for chips. If one is near it will get the UID and authenticate
        while self.__continue_reading:
            if i == self.MAX_TIMES_READING:
                self.__stop_reading()
                return "null"

            # Scan for cards
            (status, TagType) = self.MIFAREReader.MFRC522_Request(self.MIFAREReader.PICC_REQIDL)

            # Get the UID of the card
            (status, uid) = self.MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, continue
            if status == self.MIFAREReader.MI_OK:
                self.__stop_reading()
                return uid

            i = + 1
            time.sleep(3)

    def __stop_reading(self):
        self.__continue_reading = False
        GPIO.cleanup()
