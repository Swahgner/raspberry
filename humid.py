from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
orange = (200,50,50)

sense.clear()

def set(col):
  for x in range(8):
    for y in range(8):
      sense.set_pixel(x,y,col)

while True:
  
  print("")
  print("Humidity: ", sense.get_humidity())
  print("Temperature: ", sense.get_temperature())
  print("")
  print("------")
  
  temp = sense.get_temperature()
  
  if (temp > 30 and temp < 36):
    set(orange)
  elif (temp > 22 and temp <= 30):
    set(green)
  elif (temp <= 22):
    set(blue)
  
  time.sleep(2)
