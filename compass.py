#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sense_hat import SenseHat
from time import sleep

sh = SenseHat()

try:
    while True:
        north = sh.get_compass()
        north = round( north, 1 )
        

        print( "North = %s°" %(north) )
        sleep(2)

        bearing = sh.get_compass()
        print('Bearing: {:.0f} to North'.format(bearing))
    
except KeyboardInterrupt:
    print( "Exiting..." );
   
