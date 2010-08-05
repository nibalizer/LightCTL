#!/usr/bin/python2.6
#Spencer Krum
#LED Teensy Experiments
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


wait = float(sys.argv[1])
prescalar = 2

x.write('\x04\x01\x00\n')
x.read(4)
x.write('\x04\x02\x00\n')
x.read(4)
x.write('\x04\x03\x00\n')
x.read(4)
x.write('\x04\x04\x00\n')
x.read(4)
x.write('\x04\x05\x00\n')
x.read(4)
x.write('\x04\x06\x00\n')
x.read(4)
x.write('\x04\x07\x00\n')
x.read(4)
x.write('\x04\x00\x00\n')
x.read(4)


while True:
    t = x.inWaiting()
    x.read(t)
    x.write('\x07\x01\n')
    x.read(2)
    for i in range(9):
        l = x.read(3)
        print "l is %s" % l
        x.read()
        t += int(l, 16)
        t = float(t)
        t /=2
    x.read(2)
    t /= 498
    print "t is %f" % t
    for i in range(8):
        x.write('\x04' + chr(i) + '\xFF\n')
        x.read(4)
    time.sleep(wait*t*prescalar)
    for i in range(8):
        x.write('\x04' + chr(i) + '\x00\n')
        x.read(4)
