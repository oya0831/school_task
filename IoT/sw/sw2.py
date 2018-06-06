import RPi.GPIO as GPIO
import time
import datetime

#SW1はGPIOに接続されている
SW1=7

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

#GPIO7を入力モードに設定する
GPIO.setup(SW1,GPIO.IN)

#無限ループで1秒ごとにGPIO7の状態を調べ、その情報を出力する
while 1:
        if GPIO.input(SW1)==True:
            now=datetime.datetime.now()
            print(now,"SW1がONになりました")
        time.sleep(0.2)
