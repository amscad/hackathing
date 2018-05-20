from sense_hat import SenseHat
import time

sh = SenseHat()

while True:
    t = sh.get_temperature()
    h = sh.get_humidity()
    p = sh.get_pressure()
    print('Temp C:{:.2f} Hum:{:.0f} Pres:{:.0f}'.format(t, h, p))
    time.sleep(1)
