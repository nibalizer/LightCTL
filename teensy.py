#!/usr/bin/python2.6
#Spencer Krum
#LED Testing
#\x00 is B7
#\x01 is D0
#\x02 is B5
#\x03 is B6
#\x04 is B4
#\x05 is D1
#\x06 is C6
#\x07 is C5
import serial, time, sys

x = serial.Serial('/dev/ttyACM0')

wait = float(sys.argv[1])



t = 0
up = True
while True:
	time.sleep(wait)
	if up:
		t += 1
		x.write('\x04\x07' + chr(t) + '\n')
		x.write('\x04\x06' + chr(abs(t-255)) + '\n')
		x.write('\x04\x05' + chr(abs(t-255)) + '\n')
		x.write('\x04\x04' + chr(t) + '\n')
		x.write('\x04\x03' + chr(abs(t-255)) + '\n')
		x.write('\x04\x02' + chr(t) + '\n')
		x.write('\x04\x01' + chr(abs(t-255)) + '\n')
		x.write('\x04\x00' + chr(abs(t-255)) + '\n')
	if t > 254:
			up = False
	else:
		t -=1
		x.write('\x04\x07' + chr(t) + '\n')
		x.write('\x04\x06' + chr(abs(t-255)) + '\n')
		x.write('\x04\x05' + chr(abs(t-255)) + '\n')
		x.write('\x04\x04' + chr(t) + '\n')
		x.write('\x04\x03' + chr(abs(t-255)) + '\n')
		x.write('\x04\x02' + chr(t) + '\n')
		x.write('\x04\x01' + chr(abs(t-255)) + '\n')
		x.write('\x04\x00' + chr(abs(t-255)) + '\n')
		if t < 2:
			up = True
