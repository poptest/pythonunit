import unittest
from zhaoyongqi.stundent_xyglxt.sj.zyq1 import student_list
from zhaoyongqi.stundent_xyglxt.modei666.zyq2 import studentMgr


class MyTestCase(unittest.TestCase):

    def test_something(self):
        name = "yafei",
        sex = "nv",
        tall = "173"
        age = "19"
        cla = "2"
        studentMgr.student_reg(name,sex,tall,age,cla)
        print (student_list)

    def test_student_all(self):
        student = studentMgr.student_serch_all()
        print (student)

    def test_student_by_name(self):
        student=studentMgr.studengt_serch_by_name("")
        print (student)

    def test_student_search_by_tall(self):
        student=studentMgr.student_serch_by_tall("176")
        print (student)

    def test_student_search_by_sex(self):
        student=studentMgr.student_serch_by_sex("nv")
        print (student)

    def test_student_search_by_cla(self):
         student=studentMgr.student_serch_by_cla("2")
         print (student)

    def test_student_delete_by_tall(self):
         student=studentMgr.student_delete_by_tall("176")
         print (student)















if __name__ == '__main__':
    unittest.main()
