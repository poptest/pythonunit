# -*- encoding:utf-8 -*-
import unittest

from junyi.homework.demo0425.lrjs import LiRunJiSuan
from ddt import ddt, data, unpack
#pip install ddt

@ddt
class MyTestCase(unittest.TestCase):

    @data({"lr":10, "jj":9},
          {"lr":20, "jj":9},
          {"lr":30, "jj":10})
    @unpack
    def test_case01(self, lr, jj):
        #1. 准备测试数据
        lr = lr
        #2. 执行测试步骤：调用利润计算去计算
        act_jj = LiRunJiSuan.jisuan(lr)
        #3. 定义期望值
        exp_jj = jj
        self.assertEqual(exp_jj, act_jj)

if __name__ == '__main__':
    unittest.main()
