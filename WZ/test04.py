# -*- encoding:utf-8 -*-
import random

a=random.randint(0,100)
print "快来猜随机数值"
while True:
    b=int(raw_input("请输入一个整数数值："))
    if b<a:
        print "数值小了"
    elif b>a:
        print "数值大了"
    else:
        print "恭喜您答对了！"
        break

