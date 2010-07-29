import time, sys, serial

x = serial.Serial('/dev/ttyACM0')


def read():
	x.write('\x07\x00\n')
	time.sleep(.25)
	t = x.inWaiting()
	x.read(t)

def pull():
	x.write('\x07\x00\n'); time.sleep(.25); t=x.inWaiting(); x.read(t)
