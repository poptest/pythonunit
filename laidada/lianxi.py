#-*- coding:utf-8 -*-
#
# def plus(num1,num2):
#     result = num1+num2
#     return result

def login(username,passwork):
    if username == "admin" and passwork == 123456:
        print("登入成功")
    else:
        print("登入失败")
    return None


ret = login("admin",123456)
print(ret)
