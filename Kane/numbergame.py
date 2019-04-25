# -*- encoding=utf-8 -*-
#获取用户输入的数字
a = int(raw_input("请输入一个数字"))

#引入随机的方法
import random

#获取一个随机数
b = random.randint(0, 101)

#进行死循环，直到正确才能退出循环
while True:
    if a == b:
        print ("恭喜通关")
        break
    elif a>b:
        print ("数字大了")
        a = int(raw_input("请输入一个数字"))

    else:
        print ("数字小了")
        a = int(raw_input("请输入一个数字"))

