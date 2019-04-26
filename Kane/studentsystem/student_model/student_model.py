# -*- encoding:utf-8 -*
'''
定义学员管理模型
实现：
1. 学员注册
2. 学员查询
3. 学员统计
4. 学员注销
5. 学员信息修改
'''
#连接本地的数据列表集
from Kane.studentsystem.student_database.student_base import student_list

class studentMar():

    #定义学生注册的方法
    @classmethod
    def student_reg(cls, name, sex, no, clas, age):
        student = {
            "name": name,
            "sex": sex,
            "no": no,
            "class": clas,
            "age": age
        }
        student_list.append(student)

    #定义学生查询的方法
    @classmethod
    def student_search_byno(cls ,no):
        for student in student_list:
            if student["no"]==no:
                return student
            # else:
            #     print ("查无此人")

    #定义学生的统计的方法
    @classmethod
    def student_tongji(cls):
        pass

    #定义学生的删除的方法
    @classmethod
    def student_delete(cls):
        pass

    #定义学生的修改的方法
    @classmethod
    def student_modify(cls):
        pass
