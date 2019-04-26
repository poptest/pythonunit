import unittest

from junyi.homework.student_management.model.student_management import StudentMgr
from junyi.homework.student_management.db.student_db import student_list

class MyTestCase(unittest.TestCase):

    def test_something(self):
        name = "XiaoYa"
        sex = "nv"
        no = "9533"
        clas = "2"
        age = "18"
        StudentMgr.student_reg(name, sex, no, clas, age)

        print(student_list)



if __name__ == '__main__':
    unittest.main()
