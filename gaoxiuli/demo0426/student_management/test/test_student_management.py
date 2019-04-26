# -*- encoding:utf-8 -*-
import unittest

from gaoxiuli.demo0426.student_management.db.student_db import student_list
from gaoxiuli.demo0426.student_management.model.student_management import StudentMgr


class MyTestCase(unittest.TestCase):
    def test_something(self):
        #调用注册学员的方法
        StudentMgr.student_reg("xiaoke","m",14,2349,1)
        for student in student_list:
            print student

        print ("*---------*")

        #调用查询所有的学员的方法
        StudentMgr.student_search_all()
        print (student_list)
        print ("*---------*")
        # 调用查询学员的方法
        StudentMgr.student_search_byname("xiaoke")
        StudentMgr.student_search_byname("xiaoming")
        StudentMgr.student_search_byname("xiaoying")
        StudentMgr.student_search_byname("zhishi")
        StudentMgr.student_search_byname("elio")

        print ("*---name------*")
        StudentMgr.student_search_bynum(2345)
        StudentMgr.student_search_bynum(2346)
        StudentMgr.student_search_bynum(2347)
        StudentMgr.student_search_bynum(2348)
        StudentMgr.student_search_bynum(2349)
        print ("*-----num----*")
        StudentMgr.student_search_bysex("w")
        StudentMgr.student_search_bysex("m")
        print ("*-----sex----*")
        StudentMgr.student_search_byage(12)
        StudentMgr.student_search_byage(13)
        StudentMgr.student_search_byage(14)
        print ("*----age-----*")
        StudentMgr.student_search_byclass(1)
        StudentMgr.student_search_byclass(2)
        StudentMgr.student_search_byclass(3)
        print ("*----class-----*")

        StudentMgr.student_tonghi_byclass(1)
        StudentMgr.student_tonghi_byclass(2)
        print ("*---tongji-class-----*")
        StudentMgr.student_delete_bynum(2345)
        for student in student_list:
            print student
        print ("*---delete-num-----*")




if __name__ == '__main__':
    unittest.main()
