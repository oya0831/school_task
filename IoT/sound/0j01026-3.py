# coding:utf-8;
import RPi.GPIO as GPIO
import pygame.mixer
import time

SW=7
PIN=[21,20]
sounds=["Guide.mp3","red.wav"]

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW,GPIO.IN)

for num in range(len(PIN)):
  GPIO.setup(PIN[num],GPIO.OUT)

def delete():
  for num in range(len(PIN)):
    GPIO.output(PIN[num],GPIO.LOW)

delete()
GPIO.output(PIN[0],GPIO.HIGH)
pygame.mixer.init()
pygame.mixer.music.load(sounds[0])

while 1:
  if GPIO.input(SW)==True:
      print('通りました')
      time.sleep(2)
      GPIO.output(PIN[0],GPIO.LOW)
      GPIO.output(PIN[1],GPIO.HIGH)
      pygame.mixer.music.play(1)
      time.sleep(2)
      pygame.mixer.music.load(sounds[1])
      pygame.mixer.music.play(1)
      time.sleep(3)
      for num in range(5):
         GPIO.output(PIN[1],GPIO.LOW)
         time.sleep(0.2)
         GPIO.output(PIN[1],GPIO.HIGH)
         time.sleep(0.2)
      pygame.mixer.music.stop();
      GPIO.output(PIN[1],GPIO.LOW)
      GPIO.output(PIN[0],GPIO.HIGH)
