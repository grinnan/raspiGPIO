#!/bin/bash

/home/pi/raspiGPIO/gpio_switch4.py | tee -a /var/log/gpioswitch.log 2>&1
