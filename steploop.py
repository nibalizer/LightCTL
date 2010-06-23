#!/usr/bin/python2.6
#Spencer Krum
#LED Teensy Test


import serial, time, sys


x = serial.Serial('/dev/ttyACM0')


wait = float(sys.argv[1])

x.write('\x04\x01\x00\n')
x.write('\x04\x02\x00\n')
x.write('\x04\x03\x00\n')
x.write('\x04\x04\x00\n')
x.write('\x04\x05\x00\n')
x.write('\x04\x06\x00\n')
x.write('\x04\x07\x00\n')
x.write('\x04\x00\x00\n')

while True:
	x.write('\x04\x00\xFF\n')
	time.sleep(wait)
	x.write('\x04\x00\x00\n')
	x.write('\x04\x01\xFF\n')
	time.sleep(wait)
	x.write('\x04\x01\x00\n')
	x.write('\x04\x02\xFF\n')
	time.sleep(wait)
	x.write('\x04\x02\x00\n')
	x.write('\x04\x03\xFF\n')
	time.sleep(wait)
	x.write('\x04\x03\x00\n')
	x.write('\x04\x04\xFF\n')
	time.sleep(wait)
	x.write('\x04\x04\x00\n')
	x.write('\x04\x05\xFF\n')
	time.sleep(wait)
	x.write('\x04\x05\x00\n')
	x.write('\x04\x06\xFF\n')
	time.sleep(wait)
	x.write('\x04\x06\x00\n')
	x.write('\x04\x07\xFF\n')
	time.sleep(wait)
	x.write('\x04\x07\x00\n')
