import RPi.GPIO as GPIO
import time

SW1=7
PIN=21
cnt=0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1,GPIO.IN)
GPIO.setup(PIN,GPIO.OUT)
GPIO.output(PIN,GPIO.LOW)

while 1:
  time.sleep(0.3)
  print("SW1=",GPIO.input(SW1))
  if GPIO.input(SW1)==True:
     cnt+=1
     print("cnt=",cnt)
     if cnt%2==1:
        GPIO.output(PIN,GPIO.HIGH)
     else:
        GPIO.output(PIN,GPIO.LOW)

