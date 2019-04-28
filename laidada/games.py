#-*- coding:utf-8 -*-

import random
ran = random.randint(0,100)
while True:
    num = int(raw_input("请输入一个数："))
    if num == ran:
        print("66666666")
        break
    if num>ran:
        print("提示大了")
    else:
        print("提示小了")

