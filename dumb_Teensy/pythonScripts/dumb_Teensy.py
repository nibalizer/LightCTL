#dumb_teensy.py is (c) 2010 Spencer Krum and released under the GPLv3 or any later version
#see README, LICENSE for more information

import serial, sys, getopt, time

class LightController:
	def __init__(self, teensy):
		self.initTeensy(teensy)

	def _load(self, source):
		device = serial.Serial(source)
		return device

	def initTeensy(self, teensy):
		self.serial = self._load(teensy)
	def listen(self):
		bufsize = self.serial.inWaiting()
		buf = self.serial.read(bufsize)
		return buf
	def output(self, outgoing):
		print outgoing
	def write(self, message):
		self.serial.write(message)
	def relay(self, message):
		self.write(message)
		self.output(self.listen())
	def setPWM(self, port, value):
		self.serial.write('\x04' + chr(port) + chr(value) + '\n') 
		self.listenout()
	def setDIO(self, port, value):
		self.serial.write('\x09' + chr(port) + chr(value) + '\n')
		self.listenout()
	def listenout(self):
		self.output(self.listen())
def usage():
	print "There is not yet a usage, brah"
	
def main(argv):
	teensy = "/dev/ttyACM0"
	try:
		opts, args = getopt.getopt(argv, "hp:d1", ["help", "teensy-path="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt == '-d':
			global _debug
			_debug = 1
		elif opt in ("-p", "--teensy-path"):
			teensy = arg
		elif opt == '-1':
			teensy = "/dev/ttyACM1"
	if (args):
		usage()
		sys.exit(2)
    x = LightController(teensy)
    while (1):
        p = int(raw_input("Give me a number p for port: "))
        t = int(raw_input("Give me a number t for value: "))
        x.setDIO(p,t)
if __name__ == "__main__":
	main(sys.argv[1:])

