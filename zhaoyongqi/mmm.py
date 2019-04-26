#-*- encoding:utf-8 -*-

student_list = [
    {"name": "xiaoyan","sex": "nan","tall":"180","age":"19"},
    {"name": "yuner","sex":"nv", "tall":"175","age":"18"},
    {"name": "meidusha","sex":"nv", "tall":"176","age":"19"},
    {"name": "zhaoyongqi","sex":"nv", "tall":"171","age":"19"},
]
sex = raw_input("请输入学员性别")
def renshu(students, sex):
    count = 0
    for student in students:
        if student["sex"] == sex:
             count = count+1
    return count

sl= renshu(student_list,"nv")
print ("女生数量为%s"%  sl)

sl= renshu(student_list,"nan")
print ("男生数量为%s"% sl)


