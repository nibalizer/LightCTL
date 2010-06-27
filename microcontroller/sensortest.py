#!/usr/bin/python2.6

#Spencer Krum
#Sensor Test FTW


import serial, time, sys


x = serial.Serial('/dev/ttyACM1')

x.write('\x07\x00\n')
t = x.read(2)
p = x.read(2)
t = x.read()
print p


