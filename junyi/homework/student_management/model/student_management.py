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

from junyi.homework.student_management.db.student_db import student_list

class StudentMgr():

    @classmethod
    def student_reg(cls, name, sex, no, clas, age):
        student = {
            "name": name,
            "sex": sex,
            "no": no,
            "class":clas,
            "age": age
        }
        student_list.append(student)

    @classmethod
    def student_search(cls):
        pass

    @classmethod
    def student_tongji(cls):
        pass

    @classmethod
    def student_delete(cls):
        pass

    @classmethod
    def student_modify(cls):
        pass