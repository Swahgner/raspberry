from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

sense.clear()

while True:
  
  print("Humidity: ", sense.get_humidity())
  print("Temperature: ", sense.get_temperature_from_humidity())
  
  time.sleep(2)
