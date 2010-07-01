#!/usr/bin/python2.6
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
    x.read(16)


def one():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\xFF\n')
    x.read(16)


def two():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\x00\n')
    x.read(16)


def three():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\xFF\n')
    x.read(16)



def four():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\x00\n')
    x.read(16)



def five():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\xFF\n')
    x.read(16)



def six():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\x00\n')
    x.read(16)



def seven():
    x.write('\x04\x01\xFF\n')
    x.write('\x04\x02\x00\n')
    x.write('\x04\x04\xFF\n')
    x.write('\x04\x05\xFF\n')
    x.read(16)



def eight():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\xFF\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\x00\n')
    x.read(16)


def nine():
    x.write('\x04\x01\x00\n')
    x.write('\x04\x02\xFF\n')
    x.write('\x04\x04\x00\n')
    x.write('\x04\x05\xFF\n')
    x.read(16)

def count():
        while True:
            one()
            time.sleep(.5)
            two()
            time.sleep(.5)
            three()
            time.sleep(.5)
            four()
            time.sleep(.5)
            five()
            time.sleep(.5)
            six()
            time.sleep(.5)
            seven()
            time.sleep(.5)
            eight()
            time.sleep(.5)
            nine()
            time.sleep(.5)
            zero()
            time.sleep(.5)


def sensor_readout():
    while True:
        t = x.inWaiting()
        x.read(t)
        x.write('\x07\x00\n')
        x.read(2)
        for i in range(9):
            l = x.read(3)
            print "l is %s" % l
            x.read()
            t += int(l, 16)
            t = float(t)
            t /=2
        x.read(2)
        print "t is %f" % t
        if (t < 102):
            zero()
        elif (t < 204):
            one()
        elif (t < 306):
            two()
        elif (t < 408):
            three()
        elif (t < 510):
            four()
        elif (t < 612):
            five()
        elif (t < 714):
            six()
        elif (t < 816):
            seven()
        elif (t < 918):
            eight()
        elif (t < 1023):
            nine()


sensor_readout()


