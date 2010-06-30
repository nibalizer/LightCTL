#Spencer Krum
#LightCTL


#ATMega32u4

#\x00 is B7
#\x01 is D0
#\x02 is B5
#\x03 is B6
#\x04 is B4
#\x05 is D1
#\x06
#\x07


import sys, time, serial


x = serial.Serial('/dev/ttyACM0')


def zero():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\x00\n')


def one():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\xFF\n')


def two():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\x00\n')


def three():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\xFF\n')



def four():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\x00\n')



def five():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\xFF\n')



def six():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\x00\n')



def seven():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\xFF\n')



def eight():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\xFF\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\x00\n')


def nine():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\xFF\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\xFF\n')








