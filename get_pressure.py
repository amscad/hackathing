from sense_hat import SenseHat

sense = SenseHat()
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

# alternatives
print(sense.pressure)

sense.rotation = 180
p = str(pressure)
sense.show_message(p, text_colour=[255, 0, 0])
