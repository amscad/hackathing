#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()


sh.set_imu_config(True, True, True)

try:
    while True:
        pitch, roll, yaw = sh.get_orientation().values()

        pitch = round( pitch, 1 )
        roll = round( roll, 1 )
        yaw = round( yaw, 1 )
        sleep(0.1)

        print( "Pitch = %s°    Roll = %s°    Yaw = %s°" %(pitch, roll, yaw) )


##    o = sense.get_orientation()
##    print("p: {:.0f}, r: {:.0f}, y: {:.0f}".format(o['pitch'], o['roll'], o['yaw']))

except KeyboardInterrupt:
    print( "Exiting..." );

