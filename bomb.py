from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()
sense.clear()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
yellow = (255,255,0)



for x in range(8):
  for y in range(8):
    sense.set_pixel(x,y,yellow)
    time.sleep(0.005)

time.sleep(1)

sense.clear()
