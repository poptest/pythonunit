# -*- encoding:utf-8 -*-

def plus(num1,num2):
    sum = num1 + num2
    return sum

def login(usernm,passwd):
    if usernm == "caoxun" and passwd == "123456":
        print("登陆成功")
    else:
        print("登陆失败")

login("caoxun","123456")