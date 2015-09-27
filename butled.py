#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# GPIO PIN NUMBERS, INPUT: BUTTON, OUTPUT: LED
inpin = 17
outpin = 27

#INITIALIZE GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(inpin,GPIO.IN)
GPIO.setup(outpin,GPIO.OUT)

#STATE VARIABLE IS MULTIPLIED BY -1 EACH TIME BUTTON IS PRESSED
sint = -1

prev_input = 0

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

