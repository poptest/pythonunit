#-*- encoding:utf-8 -*-
name = "zhaoyongqi"
name2 = "meidusha"

#列表
x = [1, 2, 3, 4, 5]
x1 = ['Q','W','E','R']

print (x[0:3])
print (x1[0:4])

#字典
dic = {"name":"xiaoyan","age":"18","thewife":["meidusha","xuner"]}
print(dic["name"])
print (dic["thewife"][0])
print (dic["thewife"][0:2])

dic["name"] = "zhaoyongqi"
print (dic["name"])
print (dic.has_key("name"))
print (dic.keys())
#增加
dic["tall"] = 180
print (dic["tall"])

#if
print 1+1==2
print 1+1!=2
print 1+1==3
print 1+1==0
print 1+1!=1
