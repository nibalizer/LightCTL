#!/usr/bin/python2.6
#Spencer Krum
#(should) run The solar panel testing apparatus in Dr. Wamsers lab.
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



def mainmenu():
	print "Welcome to the Solar Panel testing program"
	print "This program will allow you to vary the voltage across the halogen lamp"
	print "From Wikipedia: \"Light output is proportional to voltage cubed, I = v^3 \""
	print "The halogen lamp is designed for %d volts" % halogen_base_voltage
	print "Over-voltaging the halogen lamp is not advised as it will decrease the lifetime of the bulb"
	print "You may choose voltages between %sV and %sV" % (hwlow,hwhigh)
	print "Type 'help' to get help"
	
def help():
	print "If it is tragicially broken email krum.spencer@gmail.com and kwp@pdx.edu"
	print "You should be able to enter the following commands at any time: q, help, any number."
	print "q will quit the program"
	print "help will display this help"
	print "A number between %s and %s will set the voltage across the lamp." % (hwlow,hwhigh)
	print "Voltages below %sV and %sV are beyond the range of the hardware at this time" % (hwlow, hwhigh)
	

##	Normal Functions	##
def prompt(prompt):
    while True:
	response = raw_input(prompt)
	try:
		if response == 'q':
			print "Thank you for using this python chemistry program"
			exit()
		elif response == 'help':
			print "Displaying Help"
			help()
		elif float(response) < float(hwlow):
				print "Voltages below %s volts are beyond the range of the hardware at this time." % hwlow
	   	elif float(response) > float(hwhigh):
				print "Volates above %s volts are beyond the range of the hardware at this time." % hwhigh
		else: 
			number = float(response)
	   		return number
	except ValueError:
	    print "You did not enter a number.\n"


mainmenu()
while True:
	voltage = prompt("Please enter the Voltage you would like across the lamp. (%sV - %sV): " % (hwlow,hwhigh))
	voltage_ = voltage - float(hwlow)
	voltage_ = voltage_ / (float(hwhigh) - float(hwlow))
	voltage_ = voltage_ * 255
	x.write('\x04\x07' + chr(int(voltage_)) + '\n')
	print "Attempting to set voltage to %f" % voltage
	reinput = x.read(4)
	#print "Microcontroller reports: %s" % (reinput)
	
