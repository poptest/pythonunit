import unittest

from junyi.pyunit.caltultor import Calcultor


class TestCalcultor(unittest.TestCase):

    def test_plus(self):
        a = 1
        b = 1
        act_ret = Calcultor.plus(a, b)
        exp_ret = 2
        self.assertEqual(exp_ret, act_ret)


if __name__ == '__main__':
    unittest.main()
