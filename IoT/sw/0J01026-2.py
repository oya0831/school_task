import RPi.GPIO as GPIO
import time
import datetime

SW1=7
PIN=21
cnt=0
dt_now=datetime.datetime.now()
now1=0
now2=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN)
GPIO.setup(PIN,GPIO.OUT)

while 1:
  print(cnt)
  time.sleep(1)
  if GPIO.input(SW1)==True:
     now1=dt_now.microsecond
     print("SW=",GPIO.input(SW1))
     cnt+=1
     print("cnt=",cnt)
     if cnt%2==1:
        GPIO.output(PIN,GPIO.HIGH)
        print("通りました")
     else:
        GPIO.output(PIN,GPIO.LOW)

  now2=dt_now.microsecond
  t1=now1-now2
  print("time=",t1)
