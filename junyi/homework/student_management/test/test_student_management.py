import unittest

from junyi.homework.student_management.model.student_management import StudentMgr
from junyi.homework.student_management.db.student_db import student_list

class MyTestCase(unittest.TestCase):

    def test_reg(self):
        name = "XiaoYa"
        sex = "nv"
        no = "9533"
        clas = "2"
        age = "18"
        StudentMgr.student_reg(name, sex, no, clas, age)
        print(student_list)

    def test_serach_all(self):
        students = StudentMgr.student_search_all()
        print(students)

    def test_search_by_name(self):
        student = StudentMgr.student_search_by_name("Xiaoming")
        print(student)

    def test_search_by_no(self):
        student = StudentMgr.student_search_by_no("9528")
        print(student)



if __name__ == '__main__':
    unittest.main()
