from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

sense.clear()


print("Humidity: ", sense.get_humidity())
print("Temp: ", sense.get_temperature_from_humidity())
