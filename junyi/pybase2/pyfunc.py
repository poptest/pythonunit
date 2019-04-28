# -*- encoding: utf-8 -*-

def plus(num1, num2):
    result = num1 + num2
    return result

def login(username, password):
    if username == "admin" and password == 123456:
        print("登陆成功")
    else:
        print("登陆失败")
    return None

print(login)
ret = login("junyi", 123456)
print(ret)