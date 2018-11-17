from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
orange = (255,140,0)

sense.clear()

def set(col):
  for x in range(8):
    for y in range(8):
      sense.set_pixel(x,y,col)
      time.sleep(0.02)
      
  time.sleep(0.2)
      
  for x in range(8):
    for y in range(8):
      sense.set_pixel(x,y,(0,0,0))
      time.sleep(0.01)
  
  temp = int(sense.get_temperature())
  
  msg = str(temp)
  
  msg += " C"
  
  sense.show_message(msg, text_colour=(255,255,255), back_colour=(0,0,0), scroll_speed=0.08)

while True:
  
  print("")
  print("Humidity: ", sense.get_humidity())
  print("Temperature: ", sense.get_temperature())
  print("")
  print("------")
  
  temp = sense.get_temperature()
  
  if (temp > 30 and temp < 36):
    set(orange)
  elif (temp > 22 and temp <= 30):
    set(green)
  elif (temp <= 22):
    set(blue)
  else:
    set(red)
  
  time.sleep(0.5)
