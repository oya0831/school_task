#coding:utf-8
import RPi.GPIO as GPIO
import time

PIN=[21,22,16,12]
number=1
led=0

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

#GPIOのセットアップ
for num in range(len(PIN)):
  GPIO.setup(PIN[num],GPIO.OUT)

while 1:
    while number<=15:
        GPIO.output(PIN[led],GPIO.HIGH)
        print('n=',number)
        time.sleep(2)
        number+=1
        for num in range(led):
           GPIO.output(PIN[num],GPIO.HIGH)
           print('n=',number)
           time.sleep(2)
           number+=1
           GPIO.output(PIN[num],GPIO.LOW)
        GPIO.output(PIN[led],GPIO.LOW)
        led+=1
    number=1
    led=1
