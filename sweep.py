from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
sense.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
black = (0,0,0)
pink = (255,105, 180)
orange = (255, 121, 0)
purple = (128,0,128)

def bomblist():
  list = []
  while(len(list)<10):
    curBomb = [randint(0,7),randint(0,7)]
    if list.count(curBomb) == 0:
      list.append(curBomb)
  return list
  
def pointlist(bombs):
  list = []
  colors = [black,blue,green,red,purple,pink]
  py = 0
  while(py<8):
    px = 0
    while(px<8):
      bombsInt = bombs.count([px-1,py]) + bombs.count([px-1,py-1]) + bombs.count([px,py-1]) + bombs.count([px+1,py-1]) + bombs.count([px+1,py]) + bombs.count([px+1,py+1]) + bombs.count([px,py+1]) + bombs.count([px-1,py+1])
      list.append([px,py,colors[bombsInt]])
      px += 1
    py += 1
    
  return list

def startScreen():
  bgy = 0
  times = 8
  start = 0
  minus = 1
  while (start != 5):
    while(bgy<times):
      bgx = start
      if bgy == start or bgy == times-minus:
        while(bgx<times):
          sense.set_pixel(bgx,bgy,white)
          bgx += 1
      else:
        sense.set_pixel(start,bgy,white)
        sense.set_pixel(times-minus,bgy,white)
      bgy += 1
    bgy = start;
    amount = times - 2
    start = start + 1
    minus = minus + 1
    time.sleep(0.15)
    
def checkBomb(x,y,bombs,points,oldcolor):
  pos = [x,y]
  if bombs.count(pos) == 0:
    for z in points:
      if z[0] == x and z[1] == y:
        
        return z[2]
    return oldcolor 
  else:
    return False
    
def deathScreen():
  bgy = 0
  times = 8
  start = 0
  minus = 1
  while (start != 5):
    while(bgy<times):
      bgx = start
      if bgy == start or bgy == times-minus:
        while(bgx<times):
          sense.set_pixel(bgx,bgy,black)
          bgx += 1
      else:
        sense.set_pixel(start,bgy,black)
        sense.set_pixel(times-minus,bgy,black)
      bgy += 1
    bgy = start;
    amount = times - 2
    start = start + 1
    minus = minus + 1
    time.sleep(0.15)
    

def init():
  startScreen()
  y = 0
  x = 0
  oldcolor = white
  bombs = bomblist()
  points = pointlist(bombs)
  sense.set_pixel(x,y,yellow)
  alive = True
  while (alive):
    oldy = y
    oldx = x
    for event in sense.stick.get_events():
      if event.action == 'pressed':
        if event.direction == 'up':
          y = y - 1
        elif event.direction == 'down':
          y = y + 1
        elif event.direction == 'left':
          x = x - 1
        elif event.direction == 'right':
          x = x + 1
        elif event.direction == "middle":
          oldcolor = checkBomb(x,y,bombs,points,oldcolor)
          if(oldcolor == False):
            alive = False
    if oldx != x or oldy != y:
      if 0 <= x <= 7 and 0 <= y <= 7:
        sense.set_pixel(oldx,oldy,oldcolor)
        oldcolor = sense.get_pixel(x,y)
        sense.set_pixel(x,y,yellow)
      else:
        x = oldx
        y = oldy
  
  deathScreen()
  loading = True
  while loading:
    for event in sense.stick.get_events():
      if event.action == 'pressed':
        if event.direction == "middle":
          loading = False
  init()
init()
