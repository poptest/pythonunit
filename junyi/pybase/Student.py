#encoding:utf-8
#名字name
#年龄age
#性别sex
#班级clas
#学号no
student_list=[
    {"name":"xiaoming","age":"12","xingbie":"nan","clas":"1","no":"110"},
    {"name":"xiaohong","age":"11","xingbie":"nv","clas":"2","no":"111"},
    {"name":"xiaofang","age":"14","xingbie":"nv","clas":"3","no":"112"},
    {"name":"xiaozhu","age":"16","xingbie":"nan","clas":"4","no":"113"},
    {"name":"xiaoniu","age":"13","xingbie":"nan","clas":"5","no":"114"},
]
def nvsheng(student_list ,sex):
    count = 0
    for student in student_list:

        if student["xingbie"]=="sex":
            count+=1
    return count

shuliang=nvsheng(student_list ,"nv")
print (shuliang)

