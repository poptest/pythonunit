import unittest
from TianYang.FangFa import FangFa
from ddt import ddt,file_data


@ddt
class Tase_Chu(unittest.TestCase):

    @file_data("Chu.json")
    def ChuFa(self,sz1,sz2,exp_value):
        act_value= FangFa.chu(sz1, sz2)

        self.assertEqual(exp_value,act_value)





if __name__ == '__main__':
    unittest.main()
