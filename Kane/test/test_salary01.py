# -*- encoding: utf-8 -*-
import unittest

from junyi.homework.lrjs import LiRunJiSuan

from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):

    @data({"lr":-1, "jj":None},
          {"lr":0, "jj":0},
          {"lr": 10, "jj": 1},
          {"lr": 20, "jj": 1.75},
          {"lr": 40, "jj": 2.75},
          {"lr": 60, "jj": 3.35},
          {"lr": 100, "jj": 3.95},
          {"lr": 101, "jj": 3.96},
          {"lr": "一万", "jj": None},
          {"lr": +10, "jj": None},
          {"lr":10.000001, "jj":1.00000075})

    @unpack
    def case(self, lr, jj):
        # 1. 测试准备测试数据
        zlr = lr
        # 2. 运行测试步骤，并获取实际结果
        act_jj = LiRunJiSuan.jisuan(zlr)
        # 3. 定义期望结果
        exp_jj = jj
        # 4. 判断期望奖金与实际奖金是否相等
        self.assertEqual(exp_jj, act_jj)


if __name__ == '__main__':
    unittest.main()
