# temperature calibration from:
#    yaab-arduino.blogspot.com/2016/08/accurate-temperature-reading-sensehat.html

from sense_hat import SenseHat
import os
import time

sense = SenseHat()

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

while True:
    temp1 = sense.get_temperature_from_humidity()
    temp2 = sense.get_temperature_from_pressure()
    temp_cpu = get_cpu_temperature()
    
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    temp = (temp1+temp2)/2
    temp_corr = temp - ((temp_cpu-temp)/1.5)
    temp_corr = get_smooth(temp_corr)
    
    text = "T=" + str(round(temp_corr,2)) + "C h=" + str(round(humidity,2)) + "%"
    print text
    print "Temperature raw = " + str(round(sense.get_temperature(),2))
    sense.show_message(text)
