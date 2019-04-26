# -*- encoding:utf-8 -*-

import random

ran = random.randint(0,100)
#print(ran)

while True:
    code = int(raw_input("输入一个数字："))
    if code == ran:
        print("666")
        break
    elif code > ran:
        print("大了")
    else:
        print("小了")



