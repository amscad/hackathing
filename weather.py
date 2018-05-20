#!/usr/bin/env python
from sense_hat import SenseHat
from time import sleep
import sys

sh = SenseHat()
sh.clear()
# sh.show_message("Starting Weather detection")

try:
  while True:
    temperature = sh.get_temperature()
    pressure = sh.get_pressure()
    humidity = sh.get_humidity()

    t = round(temperature, 2)
    p = round(pressure, 2)
    h = round(humidity, 2)
    #sh.show_message("The temperature is %d, the pressure is %d, and the humidity is %d." % (temperature, pressure, humidity))
    sh.show_message("Temp: %s, Pressure: %s, Humidity: %s." % (t, p, h))
    
    sleep(1)

except KeyboardInterrupt:
  print("Exiting...")

sh.clear()