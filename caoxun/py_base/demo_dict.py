# -*- encoding:utf-8 -*-

student_list = [
    {"name":"xiaoming","sex":"nan","no":"0026","class":1,"age":19},
    {"name":"xiaolai","sex":"nv","no":"0012","class":1,"age":18},
    {"name":"xiaozi","sex":"nv","no":"0033","class":1,"age":7},
    {"name":"xiaohong","sex":"nv","no":"0015","class":1,"age":18}
]
student_count = len(student_list)
#print(student_count)
''''
count = 0
for student in student_list:
#    print(student["name"])
#    print("学生名字:%s,学生性别:%s"%(student["name"],student["sex"]))



    if student["sex"] == "nv" :
         count = count + 1
print("女生:%s:"%count)
'''






def tongji(stu,sex):
    count = 0
    for student in student_list:
        if student["sex"] == sex:
            count += 1
    return count

shuliang = tongji(student_list,"nv")
print("女生数量:%s"%shuliang)
shuliang = tongji(student_list,"nan")
print("男生数量:%s"%shuliang)
