#!/usr/bin/python2.6


#Spencer Krum
#(should) run The solar panel testing apparatus in Dr. Wamsers lab.



##	Syntax Reference	## 
#\x00 is B7
#\x01 is D0
#\x02 is B5
#\x03 is B6
#\x04 is B4
#\x05 is D1
#\x06 is C6
#\x07 is C5


import serial, sys, time

x = serial.Serial('/dev/ttyACM0')


#wait = float(sys.argv[1])

x.write('\x04\x01\x00\n')
x.write('\x04\x02\x00\n')
x.write('\x04\x03\x00\n')
x.write('\x04\x04\x00\n')
x.write('\x04\x05\x00\n')
x.write('\x04\x06\x00\n')
x.write('\x04\x07\x00\n')
x.write('\x04\x00\x00\n')

halogen_base_voltage = 12
hwlow = "6.04"
hwhigh = "11.97"


