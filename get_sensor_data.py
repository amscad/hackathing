from sense_hat import SenseHat
sense = SenseHat()
while True:
    temperature = sense.get_temperature()
    pressure = sense.get_pressure()
    humidity = sense.get_humidity()
    sense.show_message("The temperature is %d, the pressure is %d, and the humidity is %d." % (temperature, pressure, humidity))