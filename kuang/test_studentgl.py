import unittest

from junyi.pybase.Student import student_list
from junyi.homework.student_management.test.studentgl import students


class MyTestCase(unittest.TestCase):

    def test_something(self):
        name = "xiaocheng",
        age = "12",
        xingbie = "nan"
        clas = "1"
        no = "115"
        students.reg(name, age, xingbie, clas, no)
        print (student_list)


    def test_search01(self):
        student = students.search()
        print (student)


    def test_tongji01(self):
        stedent = students.tongji_name("xiaoming")
        print (stedent)


    def test_tongji02(self):
        student = students.tongji_clas("1")
        print (student)


    def test_tongji03(self):
        student = students.tongji_no("110")
        print (student)


if __name__ == '__main__':
    unittest.main()
