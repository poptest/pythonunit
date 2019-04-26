#-*- encoding:utf-8 -*-

from zhaoyongqi.stundent_xyglxt.sj.zyq1 import student_list

class studentMgr():
    @classmethod
    def student_reg(cls,name,sex,tall,age,cla):
        student={"name":name,
                 "sex" : sex,
                 "tall":tall,
                 "age":age,
                 "cla":cla}
        student_list.append(student)

    @classmethod
    def student_serch_all(cls):
          return student_list

    @classmethod
    def studengt_serch_by_name(cls,name):
        for student in student_list:
            if student["name"] == name:
             return student

    @classmethod
    def student_serch_by_tall(cls,tall):
        for student in student_list:
            if student["tall"] == tall:
                return student


    @classmethod
    def student_serch_by_sex(cls,sex):
        count=0
        for student in student_list:
            if student["sex"] == sex:
                count +=1
        return count

    @classmethod
    def student_serch_by_cla(cls,cla):
        count=0
        for student in student_list:
            if student["cla"] ==cla:
                count+=1
        return count

    @classmethod
    def student_delete_by_tall(cls, tall):
        index = 0
        for student in student_list:
            if student["tall"] == tall:
              student_list.pop(index)
            else:
                index += 1







