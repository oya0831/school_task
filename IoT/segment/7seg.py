# coding: utf-8
#
# すべてのセグメントを1秒ごとに点灯、消灯する

import RPi.GPIO as GPIO
import time

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

# PINのそれぞれの要素を出力に設定
for i in PIN:
    GPIO.setup(i,GPIO.OUT)

while True:
    #全てのセグメントを点灯する
    for i in PIN:
        GPIO.output(i,ON)

    time.sleep(1)

    # 全てのセグメントを消灯する
    for i in PIN:
        GPIO.output(i,OFF)

        time.sleep(1)
