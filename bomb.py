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


def setColor(color):
  for x in range(8):
    for y in range(8):
      sense.set_pixel(x,y,color)



timer = 45





def runTime():
  global timer
  print(timer)
  
  if (timer > 10):
    setColor(yellow)
    timer = timer - 1
    time.sleep(0.01)
    setColor(nothing)
    time.sleep(0.99)
    runTime()
  elif (timer > 0 and timer <= 10):
    setColor(red)
    timer = timer - 1
    time.sleep(0.01)
    setColor(nothing)
    time.sleep(0.49)
    setColor(red)
    time.sleep(0.01)
    setColor(nothing)
    time.sleep(0.49)
    runTime()
  else:
    print("DEAD!")
    setColor(red)


for y in range(8):
  for x in range(8):
    sense.set_pixel(x,y,yellow)
    time.sleep(0.025)

time.sleep(1)

for y in range(8):
  for x in range(8):
    sense.set_pixel(x,y,red)
    
time.sleep(0.5)

sense.clear()

runTime()
