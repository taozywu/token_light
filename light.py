#!/usr/bin/python
# -*- coding: UTF-8 -*-
import rpc,json
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)
pin=12
GPIO.setup(pin,GPIO.OUT)

while(True):
    new_blance=(json.loads(rpc.get_balance()))["pending"]

    if new_blance==0:
        print ("off")
        GPIO.output(pin,GPIO.LOW)
        time.sleep(2)
    else:
        print ("on")
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(new_blance/100000)