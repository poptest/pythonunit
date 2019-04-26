# -*- encoding: utf-8 -*-
import unittest

from junyi.homework.demo0425.lrjs import LiRunJiSuan
class MyTestCase(unittest.TestCase):

    def test_case01(self):
        lr = 10
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = "None"
        self.assertEqual(act_jj, exp_jj)

    def test_case02(self):
        lr = 20
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = 1.75
        self.assertEqual(act_jj, exp_jj)

    def test_case03(self):
        lr = 40
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = 2.75
        self.assertEqual(act_jj, exp_jj)

    def test_case04(self):
        lr = 60
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj ="None"
        self.assertEqual(act_jj, exp_jj)

    def test_case05(self):
        lr = 100
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = 3.95
        self.assertEqual(act_jj, exp_jj)

    def test_case06(self):
        lr = 0
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = 0.0
        self.assertEqual(act_jj, exp_jj)

    def test_case07(self):
        lr = "a"
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = "None"
        self.assertEqual(act_jj, exp_jj)

    def test_case08(self):
        lr = -10
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj ="请输入正数"
        self.assertEqual(act_jj, exp_jj)

    def test_case09(self):
        lr = 100.1
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = 3.95
        self.assertEqual(act_jj, exp_jj)

    def test_case10(self):
        lr = "@"
        act_jj = LiRunJiSuan.jisuan(lr)
        exp_jj = "None"
        self.assertEqual(act_jj, exp_jj)
if __name__ == '__main__':
    unittest.main()


