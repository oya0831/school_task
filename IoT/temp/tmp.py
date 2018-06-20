#!/usr/bin/python3
#coding:utf-8

import smbus
import time

bus=smbus.SMBus(1) #I2Cバス番号
address=0x48       #TMP102のI2Cアドレス

#I2C data read (block)
def blockread(reg,value):
    value=bus.read_i2c_block_data(address,reg,value)
    return value

while 1:
    temp_raw=blockread(0x00,2) #I2Cで温度データ(2byte)を取得
    #温度データを整形
    #バイト1は上位バイト、バイト2は下位バイトで
    #上位バイト T11 T10 T9 T8 T7 T6 T5 T4
    #下位バイト T3  T2  T1 T0 0  0  0  0 
    #上位バイト(temp_raw[0]を左に8ビットシフトし、下位バイトを右に4ビットシフトする)
    temp=((temp_raw[0] << 8) | temp_raw[1] >> 4)
    #分解能(0.0625℃ )倍する
    temp=temp*0.0625
    #表示出力
    print("temp="+str(temp)+"℃")

    time.sleep(1)  #1秒
