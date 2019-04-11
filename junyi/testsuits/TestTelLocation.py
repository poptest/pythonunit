import unittest
from junyi.utils.tellocation import TelLocationUtil
from ddt import ddt, file_data

@ddt
class MyTestCase(unittest.TestCase):

    @file_data("TestTelLocation.json")
    def test_tel_location(self, tel, exp_status_code, exp_provice, exp_city, exp_areacode, exp_zip, exp_company, exp_card):

        resp = TelLocationUtil.get_location(tel)

        act_statu_code = resp[TelLocationUtil.STATUS_CODE]
        act_provice = resp[TelLocationUtil.PROVINCE]
        act_city = resp[TelLocationUtil.CITY]
        act_areacode = resp[TelLocationUtil.AREACODE]
        act_zip = resp[TelLocationUtil.ZIP]
        act_company = resp[TelLocationUtil.COMPANY]
        act_card = resp[TelLocationUtil.CARD]

        self.assertEqual(exp_status_code, act_statu_code)
        self.assertEqual(exp_provice, act_provice)
        self.assertEqual(exp_city, act_city)
        self.assertEqual(exp_areacode, act_areacode)
        self.assertEqual(exp_zip, act_zip)
        self.assertEqual(exp_company, act_company)
        self.assertEqual(exp_card, act_card)


if __name__ == '__main__':
    unittest.main()
