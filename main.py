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
nothing = (0,0,0)
pink = (255,105, 180)

emptlist = [0, 0, 0]
bluelist = [0, 0, 248]
redlist = [248, 0 , 0]
greenlist = [0, 252, 0]

sense.clear()

p_x = 4
p_y = 4

p_col = red

bombList = []
clearSpots = []


def init():
  bombs = 8
  bombsPlaced = 0
  count = 0
  
  for y in range(8):
    for x in range(8):
      #sense.set_pixel(x, y, white)
      
      if (randint(0,64) < 8):
        curbomb = [x,y]
        bombList.append(curbomb)
        clearSpots.append([x,y,0,1])
      else:
        clearSpots.append([x,y,0,0])
        
        
  for y in range(8):
    for x in range(8):
      sense.set_pixel(x,y,white)
      time.sleep(0.02)
  
  for x in range(8):
    for y in range(8):
      sense.set_pixel(x,y,nothing)
      time.sleep(0.01)
  
      
  sense.set_pixel(p_x, p_y, p_col)



def dead():
  for y in range(8):
    for x in range(8):
      sense.set_pixel(x, y, red)
  
  for bomb in bombList:
    sense.set_pixel(bomb[0], bomb[1], blue)




init()

def checkAdj(x, y):
  # Check if all adjacent spots are bombs or not
  # If has adjacant bomb, do not go to next
  
  adjBomb = 0
  
  for bomb in bombList:
    
    if (bomb[0] == (x - 1) and bomb[1] == (y - 1)):
      adjBomb = adjBomb + 1
    
    if (bomb[0] == (x) and bomb[1] == (y - 1)):
      adjBomb = adjBomb + 1
    
    if (bomb[0] == (x + 1) and bomb[1] == (y - 1)):
      adjBomb = adjBomb + 1
    
    if (bomb[0] == (x - 1) and bomb[1] == (y)):
      adjBomb = adjBomb + 1
    
    if (bomb[0] == (x + 1) and bomb[1] == (y)):
      adjBomb = adjBomb + 1
    
    if (bomb[0] == (x - 1) and bomb[1] == (y + 1)):
      adjBomb = adjBomb + 1
    
    if (bomb[0] == (x) and bomb[1] == (y + 1)):
      adjBomb = adjBomb + 1
    
    if (bomb[0] == (x + 1) and bomb[1] == (y + 1)):
      adjBomb = adjBomb + 1
    
    
  if (adjBomb == 1):
    return [0,255,255]
  elif (adjBomb == 2):
    return [255,255,0]
  elif (adjBomb == 3):
    return [255,0,255]
  else:
    return [255,255,255]
    
    
  # Bombs next to:
  # 0 = 255,255,255
  # 1 = 0,255,255
  # 2 = 255,255,0
  # 3 = 255,0,255
  


def run(px, py):
  
  oldColor = [0,0,0]
  
  while (True):
    old_x = px
    old_y = py
    
    for event in sense.stick.get_events():
      if (event.action == "pressed"):
        
        if (event.direction == "right"):
          px = px + 1
          py = py
        elif (event.direction == "left"):
          px = px - 1
          py = py
        elif (event.direction == "up"):
          px = px
          py = py - 1
        elif (event.direction == "down"):
          px = px
          py = py + 1
        elif (event.direction == "middle"):
          bombSpot = False
          for bomb in bombList:
            if (bomb[0] == px and bomb[1] == py):
              dead()
              bombSpot = True
              break
              
              
              
              print("BOOOOM!")
          
          if (bombSpot == False):
            for spot in clearSpots:
              if (spot[0] == px and spot[1] == py):
                spot = [px,py,1,0]
                  
                oldColor = checkAdj(px,py)
                
                
                print("CLEAR!")
              
          
          
        if (px < 0):
          px = 0
        
        if (px > 7):
          px = 7
          
        if (py < 0):
          py = 0
          
        if (py > 7):
          py = 7
          
          
        sense.set_pixel(old_x, old_y, oldColor)
          
        oldColor = sense.get_pixel(px,py)
        
        sense.set_pixel(px, py, red)
        
        
        




run(p_x, p_y)

