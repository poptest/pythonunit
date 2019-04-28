import unittest

from laidada.db.students_db import student_list
from laidada.student_mgr.dome import studentmgr
class MyTestCase(unittest.TestCase):

    def test_case01(self):
        name = "xiaoya"
        sex = "nv"
        no = "2"
        clas = "3"
        age = "15"
        studentmgr.student_zengjia(name,sex,no,clas,age)
        print(student_list)

    def test_case02(self):
        student = studentmgr.student_chaxun_all()
        print(student)


    def test_case03(self):
        student = studentmgr.student_chaxun_name("Xiaoming")
        print(student)

    def test_case04(self):
        student = studentmgr.student_tongji("nan")
        print(student)

    def test_case05(self):
        student = studentmgr.student_shanchu("9527")
        print(student)



if __name__ == '__main__':
    unittest.main()
