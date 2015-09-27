#!/usr/bin/python

#GPIO           module     <module 'RPi.GPIO' from '<...>st-packages/RPi/GPIO.so'>
#input          int        1
#pasted_block   unicode    import time\n#initialise <...>ounce\n  time.sleep(0.05)
#pinNum         int        27
#prev_input     int        1
#sint           int        -1
#state          str        OFF
#time           module     <module 'time' (built-in)>

import RPi.GPIO as GPIO
import time

inpin = 17
outpin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(inpin,GPIO.IN)
GPIO.setup(outpin,GPIO.OUT)

prev_input = 0
sint = -1

while True:
    input = GPIO.input(inpin)
    if ((prev_input) and (not input)):
        sint*=-1
        if sint < 0:
            GPIO.output(outpin,GPIO.LOW)
            print "DEACTIVATED"
        else:
            GPIO.output(outpin,GPIO.HIGH)
            print "ACTIVATED"
    prev_input = input
    time.sleep(0.05)

