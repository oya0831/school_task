#coding:utf-8
import RPi.GPIO as GPIO
import time

PIN=[21,20,16,12]

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

#GPIOのセットアップ
for num in range(len(PIN)):
  GPIO.setup(PIN[num],GPIO.OUT)

#LEDのライトを全部消す処理
def delete():
   for num in range(len(PIN)):
     GPIO.output(PIN[num],GPIO.LOW)

#初期化
delete()

while 1:
  for number in range(1,16):
    #10進数を2進数に変換
    str=bin(number)
    #'0b'をカット
    cut_str=str[2:6]
    #4桁になるようにフォーマット
    cut_str="{0:04d}".format(int(cut_str))
    #ループで使うためリストに入れる
    list_str=[int(li) for li in cut_str]
    #逆順にリストに格納
    list_str.reverse()
    for num in range(len(list_str)):
      #1ならば光らせる
      if list_str[num]==1: 
        GPIO.output(PIN[num],GPIO.HIGH)
    #10進数をcui上に表示
    print('n=',number)
    #2秒間停止
    time.sleep(2)
    #全部消す
    delete()
    number+=1
number=1
