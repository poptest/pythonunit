import unittest
from ddt import ddt, file_data

from junyi.Calcultor import Calcultor


@ddt
class CalculatorTester(unittest.TestCase):

    @file_data("TestCalcultorAdd.json")
    def test_jia(self, num1, num2, exp_val):
        act_val = Calcultor.jia(num1, num2)
        self.assertEqual(exp_val, act_val)


if __name__ == '__main__':
    unittest.main()
