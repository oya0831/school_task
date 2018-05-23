import RPi.GPIO as GPIO
import time

#SW1はGPIOに接続されている
SW1=7

#GPIO番号で指定
GPIO.setmode(GPIO.BCM)

#GPIO7を入力モードに設定する
GPIO.setup(SW1,GPIO.IN)

#無限ループで1秒ごとにGPIO7の状態を調べ、その情報を出力する
while 1:
        #SW1と表示して改行しない(,end='')
        print("SW1=",end='')

        #GPIOポートの状態を調べる
        print(GPIO.input(SW1))

        #1秒スリープする
        time.sleep(1)
