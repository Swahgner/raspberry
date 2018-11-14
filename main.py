from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()
sense.low_light = True


# HAKAN


i = 0
def fire():
  sense.clear()
  while(True):
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    white = (255,255,255)
    nothing = (0,0,0)
    pink = (255,105, 180)
    black = (20, 20, 20)
    random = randint(50,255)
    randomColor = (random, random, random)

    firework = SenseHat()
    if(i<1):
      firework.set_pixel(3, 7, white)
      time.sleep(0.2)
      firework.set_pixel(3, 6, white)
      time.sleep(0.2)
      firework.set_pixel(3, 5, white)
      time.sleep(0.2)
      firework.set_pixel(3, 4, white)
      time.sleep(0.2)
      firework.set_pixel(2, 3, white)
      firework.set_pixel(4, 3, randomColor)
      firework.set_pixel(3, 3, randomColor)
      firework.set_pixel(2, 4, randomColor)
      firework.set_pixel(4, 4, randomColor)
      time.sleep(0.2)
      firework.set_pixel(3, 2, randomColor)
      firework.set_pixel(5, 2, randomColor)
      firework.set_pixel(1, 2, randomColor)
      firework.set_pixel(1, 5, randomColor)
      firework.set_pixel(5, 5, randomColor)
      time.sleep(0.2)
      firework.set_pixel(3, 1, randomColor)
      firework.set_pixel(6, 1, randomColor)
      firework.set_pixel(0, 1, randomColor)
      firework.set_pixel(0, 6, randomColor)
      firework.set_pixel(6, 6, randomColor)
      time.sleep(0.2)
      firework.set_pixel(3, 0, randomColor)
      firework.set_pixel(7, 0, randomColor)
      firework.set_pixel(6, 6, randomColor)
      time.sleep(0.2)
      firework.clear()

# -----


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

p_col = yellow

bombList = []
clearSpots = []


def init():
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
    
def win():
  for y in range(8):
    for x in range(8):
      sense.set_pixel(x,y, blue)
  
  for bomb in bombList:
    sense.set_pixel(bomb[0], bomb[1], white)
    
  fire()
  
  print("YOU WON!!!")




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
    return [0,255,0] # Green
  elif (adjBomb == 2):
    return [0,0,255] # Blue
  elif (adjBomb == 3):
    return [255,0,0] # Red
  elif (adjBomb == 4):
    return [255,105,180] # Pink
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
                spot[2] = 1
                  
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
        
        sense.set_pixel(px, py, yellow)
        
        totalSpots = len(clearSpots)
        
        for spot in clearSpots:
          if (spot[3] == 1): # If it's a bomb
            totalSpots = totalSpots - 1
          elif (spot[2] == 1): #If it's cleared
            totalSpots = totalSpots - 1
          
        if (totalSpots == 0):
          win()
        




run(p_x, p_y)
