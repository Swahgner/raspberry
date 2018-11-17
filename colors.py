from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()


while True:
  x = randint(0,8)
  y = randint(0,8)
  
  color = (randint(50,255), randint(50,255), randint(50,255))
  
  sense.set_pixel(x,y,color)
