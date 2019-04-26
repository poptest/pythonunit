# -*- encoding: utf-8 -*-
import unittest

from junyi.homework.demo0425.lrjs import LiRunJiSuan


class MyTestCase(unittest.TestCase):

    def test_something(self):
        #1. 准备测试数据
        zlr = 40
        #2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        #3. 定义期望结果
        exp_jj =
        #4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)


if __name__ == '__main__':
    unittest.main()
