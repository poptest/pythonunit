# -*- encoding:utf-8 -*-
# 学生
#   姓名：name
#   性别：sex
#   学号：no
#   班级：class
#   年龄：age

# 任务：
# 定义学员资料的数据集合
# 并通过循环，输出每一个学员的名字
student_list = [
    {"name": "Xiaoming", "sex": "nan", "no": "9527", "class": 1, "age": 16},
    {"name": "Xiaohong", "sex": "nv", "no": "9528", "class": 1, "age": 15},
    {"name": "Xiaobai", "sex": "nan", "no": "9529", "class": 1, "age": 16},
    {"name": "Xiaohui", "sex": "nv", "no": "9530", "class": 1, "age": 16}
]

#定义一个方法(函数、指令)
#def 方法名(参数传入的内容):
#   执行的逻辑

# 需求，传入学生名单，和指定的性别，返回指定性别的人数

def tongji(students, sex):
    count = 0
    for student in students:
        if student['sex'] == sex:
            count = count + 1
    return count

shuliang = tongji(student_list, 'nv')
print("女神的数量%s个" % shuliang)

shuliang = tongji(student_list, 'nan')
print("男神的数量%s个" % shuliang)

# student_count = len(student_list)
# i = 0
# for student in student_list:
#     sex = student['sex']
#     if sex == "nv":
#         i += 1      #i = i + 1
#
# print("女神的数量%s个" % i)
# print("女神的数量" + str(i) + "个")

# student_count = len(student_list)
# print("一共有%s个学生" % student_count)
# student_1 = student_list[0]['name']
# print("学生%s: %s" % ("1", student_1))
# student_2 = student_list[1]['name']
# print("学生%s: %s" % ("2", student_2))
# student_3 = student_list[2]['name']
# print("学生%s: %s" % ("3", student_3))
# student_4 = student_list[3]['name']
# print("学生%s: %s" % ("4", student_4))
