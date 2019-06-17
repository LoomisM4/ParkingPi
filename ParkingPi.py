from sensors.ultrasonic.UltrasonicSensor import UltrasonicSensor
import time
import pydevd_pycharm
pydevd_pycharm.settrace('192.168.178.20', port=9000, stdoutToServer=True, stderrToServer=True)

print("Welcome to ParkingPi.")
print("This Software runs in the background and communicates with a MQTT-Broker. So never mind missing outputs.")

time.sleep(20)

sensor = UltrasonicSensor(18, 24)

for i in range(5):
    distance = sensor.measure_distance()
    print(distance)
    time.sleep(5)
