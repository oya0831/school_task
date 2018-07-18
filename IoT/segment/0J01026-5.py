# coding: utf-8
#
# すべてのセグメントを1秒ごとに点灯、消灯する

import RPi.GPIO as GPIO
import time,datetime,math

# 7セグメントLEDとGPIOポートの対応付け
LED_A=25
LED_B=24
LED_C=16
LED_D=21
LED_E=20
LED_F=8
LED_G=7
LED_DP=12

# ON/OFFの定義
ON=GPIO.LOW
OFF=GPIO.HIGH

# warning抑止
GPIO.setwarnings(False)

# モード設定
GPIO.setmode(GPIO.BCM)

# PINというリスト(配列)を用意してGPIOピン番号を入れる
PIN=[LED_A,LED_B,LED_C,LED_D,LED_E,LED_F,LED_G,LED_DP]

# セグメント構成情報をDATAにセットする
DATA=[0xfc,0x60,0xda,0xf2,0x66,0xb6,0xbe,0xe0,0xfe,0xe6,0xee,0x3e,0x9c,0x7a,0x9e,0x8e,0x01]

# PINのそれぞれの要素を出力に設定
for i in PIN:
    GPIO.setup(i,GPIO.OUT)

#あらかじめ全部のLEDを消しておく
for i in PIN:
    GPIO.output(i,OFF)
      
#while True:
date=datetime.datetime.now()
clock=[]
clock.append(date.second)
clock.append(date.minute)
clock.append(date.hour)
formatClock=[]
num=clock

for i in range(len(clock)):
  while clock[i]!=0:
    formatClock[i].append(clock[i]%10)
    clock[i]=int(clock[i]/10)
    #formatClock.reverse()
print(formatClock)
  
#  for j in PIN:
#        if i & 0x80==0x80:
#              GPIO.output(j,ON)
#        else:
#              GPIO.output(j,OFF)
#      time.sleep(1)
