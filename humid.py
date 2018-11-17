from sense_hat import SenseHat
from random import randint
import time
import os

sense = SenseHat()

green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
orange = (255,140,0)

sense.clear()

# get CPU temperature
def get_cpu_temperature():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return t

def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x,x,x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x
    xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
    return xs

def set(col):
  for x in range(8):
    for y in range(8):
      sense.set_pixel(x,y,col)
      time.sleep(0.02)
      
  temp1 = sense.get_temperature_from_humidity()
  temp2 = sense.get_temperature_from_pressure()
  temp_cpu = get_cpu_temperature()

  humidity = sense.get_humidity()
  pressure = sense.get_pressure()

  temp = int((temp1+temp2)/2)
  temp_corr = temp - ((temp_cpu-temp)/1.5)
  temp_corr = get_smooth(temp_corr)
  
  msg = str(round(temp_corr,2))
  
  msg += " C"
  
  sense.show_message(msg, text_colour=(0,0,0), back_colour=col, scroll_speed=0.08)

while True:
  
  temp1 = sense.get_temperature_from_humidity()
  temp2 = sense.get_temperature_from_pressure()
  temp_cpu = get_cpu_temperature()

  humidity = sense.get_humidity()
  pressure = sense.get_pressure()

  temp = (temp1+temp2)/2
  temp_corr = temp - ((temp_cpu-temp)/1.5)
  temp_corr = get_smooth(temp_corr)

  print("")
  print("Humidity: ", sense.get_humidity())
  print("Temperature: ", temp_corr)
  print("")
  print("------")
  
  
  if (temp_corr > 30 and temp < 36):
    set(orange)
  elif (temp_corr > 22 and temp <= 30):
    set(green)
  elif (temp_corr <= 22):
    set(blue)
  else:
    set(red)
  
  time.sleep(0.5)
