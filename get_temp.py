from sense_hat import SenseHat

sense = SenseHat()
temp = sense.get_temperature()
print("Temperature: %s C" % temp)

# alternatives
#print(sense.temp)
#print(sense.temperature)

t = str(temp)

sense.rotation = 180

sense.show_message(t, text_colour=[255, 0, 0])

