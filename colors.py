from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()


while True:
  x = randint(0,7)
  y = randint(0,7)
  
  color = (randint(10,255), randint(10,255), randint(10,255))
  
  sense.set_pixel(x,y,color)
  time.sleep(0.05)
