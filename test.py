import serial

x = serial.Serial('/dev/ttyACM0')

while True:

    x.write('\x07\x01\n')
    t = x.read(40)
    print t
