# -*- encoding:utf-8 -*-

#调用db包里的student_list

from gaoxiuli.demo0426.student_management.db.student_db import student_list

class StudentMgr():
    @classmethod
    #学员注册
    def student_reg(cls,name,sex,age,num,clas):
        student = {
            "name" : name,
            "sex" : sex,
            "age" : age,
            "num" : num,
            "class" : clas
        }
        student_list.append(student)



    @classmethod
    def student_search_all(cls):
        return student_list

    @classmethod
    def student_search_byname(cls,name):
        for student in student_list:
            if student["name"]==name:
                print student


    @classmethod
    def student_search_bynum(cls,num):
        for student in student_list:
            if student["num"]==num:
                print student


    @classmethod
    def student_search_bysex(cls,sex):
        for student in student_list:
            if student["sex"]==sex:
                print student


    @classmethod
    def student_search_byage(cls,age):
        for student in student_list:
            if student["age"]==age:
                print student


    @classmethod
    def student_search_byclass(cls,clas):
        for student in student_list:

            if student["class"]==clas:
                print student

    @classmethod
    def student_tonghi_byclass(cls,clas):
        count=0
        for student in student_list:
            if student["class"] == clas:
                count += 1
        print count

    @classmethod
    def student_delete_bynum(cls,num):
        index = 0
        for student in student_list:
            if student["num"] == num:
                student_list.pop(index)
            else:
                index +=1

    @classmethod
    def student_modify_by_no(cls, name, age, num, clas, sex):
        index = 0
        for student in student_list:
            if student['num'] == num:
                break
            else:
                index += 1
