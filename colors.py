from sense_hat import SenseHat
import time
from random import randint

s = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)



while True:
  for y in range(8):
    for x in range(8):
      color = (randint(100,255),randint(100,255),randint(100,255))
      s.set_pixel(x,y,color)
