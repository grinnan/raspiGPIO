#!/usr/bin/python

import logging
import RPi.GPIO as GPIO
import time
import datetime

# GPIO PIN NUMBERS, INPUT: BUTTON, OUTPUT: LED
inpin = 14
outpin = 15
count = 0
sixty = 0
countdown = 1

#INITIALIZE GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(inpin,GPIO.IN)
GPIO.setup(outpin,GPIO.OUT)

def logout(message):
  f=open('/var/log/gpio.log','a')
  now = datetime.datetime.now()
  timestamp = now.strftime("%Y/%m/%d %H:%M:%S")
  outstring = str(timestamp)+"\t"+message+"\n"
  f.write(outstring)
  f.close()

#LOOP
logging.info('BEGIN LOOP')

while True:
    input = GPIO.input(inpin)
    sixty += 1
    if (sixty == 10):
            sixty=0
	    logout('SIXTY: COUNT='+str(count)+', COUNTDOWN='+str(countdown))

    if input > 0:
            count = count + 1
	    logout('ACTIVATED: COUNT='+str(count)+', COUNTDOWN='+str(countdown))

            countdown = 30   
	    
            print "ACTIVATED"
            print count
	    
    else:
            countdown = countdown - 1
            count = 0
            print "OFF"
	    logout('OFF: COUNT='+str(count)+', COUNTDOWN='+str(countdown))
            print countdown
            
    if count > 30:
            GPIO.output(outpin,GPIO.HIGH)
           # countdown = 30

    if countdown < 1:
            GPIO.output(outpin,GPIO.LOW)
            

    time.sleep(1.0)

