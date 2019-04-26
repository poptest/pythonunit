# -*- encoding:utf-8 -*-
'''
定义学员管理模型
实现：
1. 学员注册
2. 学员查询
3. 学员统计
4. 学员注销
5. 学员信息修改
'''

from caoxun.homework.student_managerment.database.student_db import student_list

class StudentMgr():
    @classmethod
    def student_reg(cls,name,sex,no,clas,age):        #注册
        student = {
            "name" : name,
            "sex" : sex,
            "no" : no,
            "clas" : clas,
            "age" : age
        }
        student_list.append(student)
    @classmethod
    def student_search_all(cls):         #查询所有
        return student_list

    @classmethod
    def student_search_by_name(cls,name):
        for student in student_list:       #根据名字查询
            if student["name"] == name:
                return student

    @classmethod
    def student_search_by_no(cls, no):
        for student in student_list:       #根据学号查询
            if student["no"] == no:
                return student


    @classmethod
    def student_stat_by_sex(cls,sex):               #根据性别统计
        count = 0
        for student in student_list:
            if student["sex"] == sex:
                count += 1
        return count


    @classmethod
    def student_delete_by_no(cls,no):                        #删除
        index = 0
        for student in student_list:
            if student["no"] == no:
                student_list.pop(index)
            else:
                index += 1


    @classmethod
    def student_modify_by_no(cls,name,sex,no,clas,age):                                 #修改
        index = 0
        for student in student_list:
            if student["no"] == no:
                break
            else:
                 index += 1

