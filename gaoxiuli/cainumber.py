# -*- encoding:utf-8 -*-
import random

x = random.randint(0,100)

while 1:
    i = int(raw_input("请输入猜测的值:"))
    if i<x:
        print ("猜的数小了！")
    elif i>x:
        print ("猜的数大了！")
    else:
        print ("猜对了！666！！！")
        break