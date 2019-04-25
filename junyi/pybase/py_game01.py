# -*- encoding:utf-8 -*-
'''
开发一个猜数字的游戏
程序随机生成一个数字
用户通过输入的方式进行交互：
    输入一个数字后，程序提示大了，还是小了
    如果输入的数字，与程序生成的随机数一直，提示“666”
    直到用户才对，程序结束
'''
import random

ran = random.randint(0, 100)

while True:

    inp = int(raw_input("请输入一个数字:"))

    if inp == ran:
        print("666")
        break
    elif inp > ran:
        print("大了")
    else:
        print("小了")

