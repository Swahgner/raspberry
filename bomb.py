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
orange = (255,140,0)


def setColor(color):
  for x in range(8):
    for y in range(8):
      sense.set_pixel(x,y,color)



timer = 45
boolGameOn = False
glbGameType = 0
gameIsOver = False

# Game Types
# 0 = standard timer



for y in range(8):
  for x in range(8):
    sense.set_pixel(x,y,yellow)
    time.sleep(0.025)

time.sleep(1)

for y in range(8):
  for x in range(8):
    sense.set_pixel(x,y,green)
    
time.sleep(0.5)

sense.clear()




def startGame():
  setColor(green)
  sense.show_message("10 SECONDS", back_colour=green, text_colour=[0, 0, 0], scroll_speed=0.05)
  print("10 Seconds until start")
  time.sleep(5)
  setColor(orange)
  sense.show_message("5 SECONDS", back_colour=orange, text_colour=[0, 0, 0], scroll_speed=0.05)
  print("5 Seconds until start")
  time.sleep(2)
  setColor(yellow)
  sense.show_message("3", back_colour=yellow, text_colour=[0, 0, 0], scroll_speed=0.05)
  print("3 Seconds until start")
  time.sleep(1)
  setColor(red)
  sense.show_message("2", back_colour=red, text_colour=[255, 255, 255], scroll_speed=0.05)
  print("2 Seconds until start")
  time.sleep(1)
  sense.show_message("1", back_colour=red, text_colour=[255, 255, 255], scroll_speed=0.05)
  print("1 Seconds until start")
  time.sleep(1)
  





while True:
  
  if (boolGameOn == False):
    # Main Menu Start
    
    if (gameIsOver == True):
      for event in sense.stick.get_events():
        if (event.action == "pressed"):
          boolGameOn = False
          setColor(nothing)
          break
    
    for event in sense.stick.get_events():
      if (event.action == "pressed"):
        
        if (event.direction == "right"):
          boolGameOn = True
          glbGameType = 0 #
          print("Starting game of: Standard Timer")
          print("Timer: ", timer)
          startGame()
          print("Game started!")
    
    # Main Menu End
  else:
    if (glbGameType == 0):
      # Standard timer game
      
      if (timer > (timer / 10)):
        setColor(yellow)
        timer = timer - 1
        time.sleep(0.02)
        setColor(nothing)
        time.sleep(0.98)
        print(timer, " seconds")
      elif (timer > 0 and timer <= (timer / 10)):
        setColor(red)
        timer = timer - 1
        time.sleep(0.02)
        setColor(nothing)
        time.sleep(0.48)
        setColor(red)
        time.sleep(0.02)
        setColor(nothing)
        time.sleep(0.48)
        print(timer, " seconds")
      else:
        print("DEAD!")
        setColor(red)
        gameIsOver = True
      
      # -------------------
      
      
      
      
      
      
      
      
      
      
      
      
