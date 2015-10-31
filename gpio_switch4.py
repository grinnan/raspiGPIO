#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# GPIO PIN NUMBERS, INPUT: BUTTON, OUTPUT: LED
inpin = 14
outpin = 15
count = 0
countdown = 1

#INITIALIZE GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(inpin,GPIO.IN)
GPIO.setup(outpin,GPIO.OUT)

#LOOP


while True:
    input = GPIO.input(inpin)
    if input > 0:
            count = count + 1
            countdown = 30   
	   
	    
            print "ACTIVATED"
            print count
	    
    else:
            countdown = countdown - 1
            count = 0
            print "OFF"
            print countdown
            
    if count > 30:
            GPIO.output(outpin,GPIO.HIGH)
           # countdown = 30

    if countdown < 1:
            GPIO.output(outpin,GPIO.LOW)
            

    time.sleep(1.0)

