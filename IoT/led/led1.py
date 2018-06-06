#coding:utf-8

import RPi.GPIO as GPIO
import time

PIN=20

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

GPIO.setup(PIN,GPIO.OUT)

while 1:
  GPIO.output(PIN,GPIO.HIGH)
  time.sleep(1)

  GPIO.output(PIN,GPIO.LOW)
  time.sleep(1)
  
