from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

sense.clear()

while True:
  
  print("")
  print("Humidity: ", sense.get_humidity())
  print("Temperature: ", sense.get_temperature_from_humidity())
  print("")
  print("------")
  
  time.sleep(2)
