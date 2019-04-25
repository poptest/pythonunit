# -*- encoding:utf-8 -*-
# python 的数据类型

#1. 数字
num = 1
num1 = 1.0

#2. 字符串
name = "python"
name1 = 'xiaohong'

#3. 列表
#3.1 定义列表
l = [1, 2, 3, 4, 5]
l2 = ['a', 'b', 1, 2, "Hello"]
'''根据索引获取列表中的值'''
print(l2[0])
print(l2[0:3])
print(l2[1:2])
#3.2 列表赋值
l2[0] = 100
print(l2[0])
#3.2.
l2.append("World")
l2.append([1,2])
print(l2)
print(l2[-1][0])

#4. 元祖tuple
tp = ("xiaohong", "xiaoming", "laowang")
print(tp[0])
print(tp[-1])
# tp[0] = "xiaobai"

#5. 字典
dic = {"name":"XiaoMing", "age": 12, "email":"xiaoming@qq.com", "tel":[1399999999,1599999999]}
print(dic["name"])
print(dic["age"])
print(dic["tel"])
print(dic["tel"][0])
print(dic["tel"][1])
#变更字典内的元素值
dic["name"] = "Xiaohong"
print(dic["name"])
#获取字典中所有的key
print(dic.keys())
print(dic.has_key("address"))
print(dic.has_key("name"))
#在字典中新增一个新key
dic["address"] = "Hubei Wuhan"
#在字典中删除一个key
dic.pop("address")
print(dic.keys())