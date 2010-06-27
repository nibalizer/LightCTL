#!/usr/bin/python2.6

#Spencer Krum
#Sensor Test FTW


import serial, time, sys

wait = float(sys.argv[1])

x = serial.Serial('/dev/ttyACM1')

while True:
    x.write('\x07\x00\n')
    x.read(2)
    p = x.read(2)
    x.read()
    print p
    time.sleep(wait)
