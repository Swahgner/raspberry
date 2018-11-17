from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()


while True:
  x = randint(0,7)
  y = randint(0,7)
  
  r = randint(0,25)
  
  color = (r * 10, r * 10, r * 10)
  
  sense.set_pixel(x,y,color)
  time.sleep(0.0005)
