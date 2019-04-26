# -*- encoding:utf-8 -*-

shuiguo = ['apple','banana','tomayo']

for s in shuiguo:
    print (s),
print
print ("*---------*")

print (len(shuiguo)),
print
print ("*---------*")

for i in range(len(shuiguo)):
    print (shuiguo[i]),
print
print ("*---------*")

for i in range(-3,3):
    print (shuiguo[i]),
print
print ("*---------*")

dic = {
    "resultcode": "200",
    "reason": "Return Successd!",
    "result": {
        "province": "浙江",
        "city": "杭州",
        "areacode": "0571",
        "zip": "310000",
        "company": "移动",
        "card": ""
    },
    "error_code": 0
}

# str = "%s %s %s"
# 电话号码:13429667914, 省份：浙江， 城市：杭州， 区域编码：0571， 邮编：310000， 运营商：移动

tel = 13429667914
province = dic["result"]["province"]
city = dic["result"]["city"]
areacode = dic["result"]["areacode"]
zip = dic["result"]["zip"]
company = dic["result"]["company"]
print ("电话号码：%s , 省company份：%s ，城市：%s ，区域编码：%s , 邮编：%s ，运营商：%s "%(tel,province,city,areacode ,zip,company))
print ("*---------*")

s = {
    "name":"xiaoming",
    "sex":"男",
    "age":12,
    "xuehao":456,
    "class":1
}
s["name"]="小狼"
name = s["name"]
print name

s["girlfriend"]="小樱"

str = ("姓名：%s ，性别：%s ，年龄：%s ，学号：%s ，班级：%s,"%(s["name"],s["sex"],s["age"],s["xuehao"],s["class"]))
print str,
print("对象：%s"%s["girlfriend"])
print ("*---------*")

student_list = [
    {"name":"xiaolang","sex":"m","age":13,"num":2345,"class":1},
    {"name":"xiaoying","sex":"w","age":12,"num":2346,"class":1},
    {"name":"zhishi","sex":"w","age":12,"num":2347,"class":1},
    {"name":"elio","sex":"m","age":13,"num":2348,"class":1},
]
#
# student_count = len(student_list)
# print student_count
#
# #student_list是一个列表，将列表的元素赋给student，要打印的是student的name
# for student in student_list:
#     print (student["name"])
#     print(student)
# i = 0
# print ("这个班级的女生有:")
# for student in student_list:
#     if student["sex"] == "w":
#         i=i+1
#         print (student["name"]),
# print
# print ("这个班级有%s个女生"%i)

def nvsheng(students,s):
    count = 0

    for student in students:
        if student['sex']==s:
            count+=1
    # print ("这个班级的%s有%s个"%(s,count))
    return count


#调用这个nvsheng方法

s=nvsheng(student_list,'m')
print s

#python的类与调用其中的方法
class KongTiao():
    @classmethod
    def zhire(cls):
        print ("zhi re")

    @classmethod
    def zhileng(cls):
        print ("zhi leng")

    @classmethod
    def chushi(cls):
        print ("chu shi")

KongTiao.zhire()
KongTiao.zhileng()
KongTiao.chushi()
