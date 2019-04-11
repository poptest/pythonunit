import unittest
from ddt import ddt, file_data
from zhangtest02.calcultor01 import Calcultor

@ddt
class MyTestCase(unittest.TestCase):
    @file_data("Testdata.json")
    def test_cheng(self,num1,num2,exp_val):
        actual_val = Calcultor.cheng(num1,num2)
        self.assertEqual(exp_val, actual_val)


if __name__ == '__main__':
    unittest.main()
