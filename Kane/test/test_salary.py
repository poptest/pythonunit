# -*- encoding: utf-8 -*-
import unittest


from junyi.homework.lrjs import LiRunJiSuan


class MyTestCase(unittest.TestCase):

    # 月利润为-1万
    def test_case01(self):

        # 1. 测试准备测试数据
        zlr = -1
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj =None
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为0万
    def test_case02(self):

        # 1. 测试准备测试数据
        zlr = 0
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 0
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为10万
    def test_case03(self):
        # 1. 测试准备测试数据
        zlr = 10
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 1
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为20万
    def test_case04(self):
        # 1. 测试准备测试数据
        zlr = 20
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 1.75
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为40万
    def test_case05(self):
        # 1. 测试准备测试数据
        zlr = 40
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 2.75
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为60万
    def test_case06(self):
        # 1. 测试准备测试数据
        zlr = 60
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 3.35
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为100万
    def test_case07(self):
        # 1. 测试准备测试数据
        zlr = 100
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 3.95
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为101万
    def test_case08(self):
        # 1. 测试准备测试数据
        zlr = 101
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 3.96
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为一万
    def test_case09(self):
        # 1. 测试准备测试数据
        zlr = "一万"
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = None
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为+10万
    def test_case10(self):
        # 1. 测试准备测试数据
        zlr = +10
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = None
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

    # 月利润为月利润为10.000001万
    def test_case11(self):
        # 1. 测试准备测试数据
        zlr = 10.000001
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = 1.00000075
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)

if __name__ == '__main__':
    unittest.main()
