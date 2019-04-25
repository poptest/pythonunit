# -*- encoding: utf-8 -*-
import unittest
from junyi.homework.lrjs import LiRunJiSuan
from ddt import ddt, data, unpack
@ddt
class MyTestCase(unittest.TestCase):

    @data({"lr": 10, "jj": 9},
              {"lr": 20, "jj": 9},
              {"lr": 30, "jj": 10})
    @unpack
    def test_case01(self, lr, jj):

        #1. 准备测试数据
        zlr = lr
        #2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        #3. 定义期望结果
        exp_jj =jj
        #4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)



if __name__ == '__main__':
    unittest.main()
