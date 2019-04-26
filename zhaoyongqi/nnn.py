#-*- encoding:utf-8 -*-
import random
shuzi=(random.randint(1, 100))
print shuzi

while True:
    oo = int(raw_input("输入一个数字"))

    if oo > shuzi:
        print ("大了")
    elif oo < shuzi:
        print ("小了")
    elif oo == shuzi:
        print ("666")
        break