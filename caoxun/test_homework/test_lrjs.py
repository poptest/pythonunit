# -*- encoding:utf-8 -*-

import unittest

from caoxun.homework.lrjs import LiRunJiSuan

class MyTestCase(unittest.TestCase):

    def test_case_01(self):
        # 1. 准备测试数据
        zlr = 10
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 1
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)


    def test_case_02(self):
        # 1. 准备测试数据
        zlr = 20
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 1.75
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)


    def test_case_03(self):
        # 1. 准备测试数据
        zlr = 40
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 2.75
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    def test_case_04(self):
        # 1. 准备测试数据
        zlr = 60
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 3.35
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    def test_case_05(self):
        # 1. 准备测试数据
        zlr = 100
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 3.95
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    def test_case_06(self):
        # 1. 准备测试数据
        zlr = 101
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 3.96
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    def test_case_07(self):
        # 1. 准备测试数据
        zlr = 0
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 0
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    def test_case_08(self):
        # 1. 准备测试数据
        zlr = "a"
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = "null"
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)


    def test_case_09(self):
        # 1. 准备测试数据
        zlr = "是"
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = "null"
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    def test_case_10(self):
        # 1. 准备测试数据
        zlr = "*"
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = "null"
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)



if __name__ == '__main__':
    unittest.main()
