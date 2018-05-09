#coding:utf-8
import RPi.GPIO as GPIO
import time

PIN=[21,20,16,12]
n=1

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

for num in range(4):
  GPIO.setup(PIN[num],GPIO.OUT)

while 1:
  if 15>=n:
    str=bin(n)
    cut_str=str[2:6]
    list_str=[int(cstr) for cstr int list(str(cut_str))]
    for decimal in range(4):

      for num in range(4):
        if num==1: 
          GPIO.output(PIN[num],GPIO.HIGH)

    print('n=',n)
    n+=1
    time.sleep(2)
    for num in range(4)
      GPIO.output(PIN[num],GPIO.LOW)
   n=1

