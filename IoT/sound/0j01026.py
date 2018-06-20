# coding:utf-8;
import RPi.GPIO as GPIO
import pygame.mixer
import time

SW=7
PIN=[21,20]
#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

#GPIOのセットアップ
for num insrange(len(PIN)):
  GPIO.setup(PIN[num],GPIO.OUT)

#mixerモジュールの初期化
pygame.mixer.init()


while 1:
  
#音楽ファイルの読み込み
pygame.mixer.music.load("se_maoudamashii_chime10.mp3")

#音楽再生、および再生回数の設定(-1はループ再生)
pygame.mixer.music.play(-1)

time.sleep(60)
#再生の終了
pygame.mixer.music.stop()
