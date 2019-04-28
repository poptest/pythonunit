# encoding:utf-8
from junyi.pybase.Student import student_list


# 学生管理模块
class students():
    # 定义一个学生注册的方法
    @classmethod
    def reg(cls,name, age, xingbie, clas, no):
        student = {
            "name": name,
            "age": age,
            "xingbie": xingbie,
            "clas": clas,
            "no": no
        }
        student_list.append(student)

    @classmethod
    def search(cls):
        return student_list

    @classmethod
    def tongji_name(self, name):
        for student in student_list:
            if student["name"]==name:
                return student

    @classmethod
    def tongji_no(self,no):
        for student in student_list:
            if student["no"]==no:
                return student

    @classmethod
    def tongji_clas(self,clas):
        for student in student_list:
            if student["clas"]==clas:
                return student

    @classmethod
    def dell(self,no):
        index=0
        for student in student_list:
            if student["no"]==no:
                student_list.pop(index)
            else:
                index+=1



    @classmethod
    def modify(self,name,age,xingbie,clas,no):
        index=0
        for student in student_list:
            if student["no"]==no:
                break
            else:
                index+=1
        modify_student=student_list[index]
        modify_student["name"]=name
        modify_student["age"] = age
        modify_student["xingbie"] = xingbie
        modify_student["clas"] = clas




