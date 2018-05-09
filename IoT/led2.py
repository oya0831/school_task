#coding:utf-8

import RPi.GPIO as GPIO
import time

PIN=[21,20]

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

for num in range(2):
  GPIO.setup(PIN[num],GPIO.OUT)

while 1:
  for num in range(2):
    GPIO.output(PIN[num],GPIO.HIGH)
    time.sleep(1)
    GPIO.output(PIN[num],GPIO.LOW)
