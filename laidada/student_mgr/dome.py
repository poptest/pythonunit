# -*- coding:utf-8  -*-

from laidada.db.students_db import student_list
class studentmgr():

    @classmethod
    def student_zengjia(cls,name,sex,no,clas,age):
        student = {"name":name,"sex":sex,"no":no,"class":clas,"age":age}
        student_list.append(student)

    @classmethod
    def student_chaxun_all(cls):
        return student_list

    @classmethod
    def student_chaxun_name(cls,name):
        for student in student_list:
            if student["name"] == name:
                return student

    @classmethod
    def student_tongji(cls,sex):
        count = 0
        for student in student_list:
            if student["sex"] == sex:
                count += 1
        return count

    @classmethod
    def student_shanchu(cls,no):
        index = 0
        for student in student_list:
            if student["no"] == no:
                student_list.pop(index)
            else:
                index += 1

    @classmethod
    def student_xiugai(cls,no,name,sex,clas,age):
        index = 0
        for student in student_list:
            if student["no"] == no:
                break
            else:
                index += 1

        target_student = student_list[index]
        target_student["name"] = name
        target_student["sex"] = sex
        target_student["clas"] = clas
        target_student["age"] = age




