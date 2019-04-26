import unittest

from caoxun.homework.student_managerment.model.student_managerment import StudentMgr
from caoxun.homework.student_managerment.database.student_db import student_list

class MyTestCase(unittest.TestCase):
    def test_reg(self):
        name = "caoxun"
        sex = "nan"
        no = "1060026"
        clas = "1"
        age = "22"
        StudentMgr.student_reg(name,sex,no,clas,age)
        print(student_list)


    def test_search_all(self):
        students = StudentMgr.student_search_all()
        print(students)


    def test_search_name(self):
        student = StudentMgr.student_search_name("Xiaohui")
        print(student)


    def test_search_no(self):
        student = StudentMgr.student_search_no("9529")
        print(student)



if __name__ == '__main__':
    unittest.main()
