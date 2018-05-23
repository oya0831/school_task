#coding:utf-8
import RPi.GPIO as GPIO
import time

PIN=[21,20,16,12]
number=1

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

#GPIOのセットアップ
for num in range(len(PIN)):
  GPIO.setup(PIN[num],GPIO.OUT)

while 1:
  if 15>=number:
    #10進数を2進数に変換
    str=bin(number)
    #'0b'をカット
    cut_str=str[2:6]
    #ループで使うためリストに入れる
    list_str=[int(lstr) for lstr int list(str(cut_str))]
    for num in range(len(list_str)):
      #1ならば光らせる
      if list_str[num]==1: 
        GPIO.output(PIN[num],GPIO.HIGH)
    #10進数をcui上に表示
    print('n=',number)
    #2秒間停止
    time.sleep(2)
    #全部消す
    for num in range(len(PIN)):
      GPIO.output(PIN[num],GPIO.LOW)
    number+=1
  number=1
