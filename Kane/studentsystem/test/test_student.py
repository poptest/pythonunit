# -*- encoding:utf-8 -*
import unittest

#连接相应的学生数据列表集和学生管理模型
from Kane.studentsystem.student_model.student_model import studentMar
from Kane.studentsystem.student_database.student_base import student_list


class MyTestCase(unittest.TestCase):

    #测试学生系统的添加功能
    def test_student_reg(self):
        name = "XiaoYa"
        sex = "nv"
        no = "9533"
        clas = "2"
        age = "18"
        studentMar.student_reg(name, sex, no, clas, age)
        print(student_list)

    #测试通过学号查询学生功能
    def test_student_search_byno(self):
        student=studentMar.student_search_byno("95000")
        print (student)

    #测试通过性别统计的方法


if __name__ == '__main__':
    unittest.main()
