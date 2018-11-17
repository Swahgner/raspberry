from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

sense.clear()


print("Temp: ", get_temperature_from_humidity())
