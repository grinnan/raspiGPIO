#!/usr/bin/python

import logging
import RPi.GPIO as GPIO
import time
import datetime
from poolcon import logdat
from poolmailer import mailer

#mailer('username','password','recipeint address','subject','body')
mailer('Pool Startup','Sensors are starting')

# GPIO PIN NUMBERS, INPUT: BUTTON, OUTPUT: LED
inpin = 14
outpin = 15
count = 0
sixty = 0
countdown = 1
gpioout=1

#INITIALIZE GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(inpin,GPIO.IN)
GPIO.setup(outpin,GPIO.OUT)

#LOOP
logging.info('BEGIN LOOP')

while True:
    input = GPIO.input(inpin)
    sixty += 1
    if (sixty == 10):
        sixty=0
        logdat('SIXTY',gpioout,count,countdown)

    if input > 0:
        count = count + 1
        logdat('ACTIVATED',gpioout,count,countdown)
        countdown = 30   
    else:
        countdown = countdown - 1
        count = 0
        logdat('OFF',gpioout,count,countdown)
            
    if count > 30:
        GPIO.output(outpin,GPIO.HIGH)
        if (gpioout != 1):  # If it is not equal to what its gonna be
            logdat('CHANGE(LOW TO HIGH)',gpioout,count,countdown)
            gpioout = 1
            # countdown = 30
            mailer('Pumps Activated','Water level sensor is High. Pumps ok to start')

    if countdown < 1:
        GPIO.output(outpin,GPIO.LOW)
        if (gpioout != -1):  # If it is not equal to what its gonna be
            logdat('CHANGE(HIGH TO LOW)',gpioout,count,countdown)
            gpioout = -1
            mailer('Low Level Alert','Sensor detects low water level. Pumps Shutdown')
    time.sleep(1.0)

