import unittest
from junyi.utils.tellocation import TelLocationUtil
from ddt import ddt, file_data


@ddt
class MyTestCase(unittest.TestCase):

    @file_data("TestTelLocation.json")
    def test_tel_location(self, tel, exp_status_code, exp_provice, exp_city, exp_areacode, exp_zip, exp_company,
                          exp_card):
        resp = TelLocationUtil.get_location(tel)

        pass_item, fail_item = TelLocationUtil.tel_location_assert(resp, exp_status_code, exp_provice, exp_city,
                                                                   exp_areacode, exp_zip, exp_company, exp_card)

        fail_count = len(fail_item)
        self.assertEqual(0, fail_count, str(fail_item))


if __name__ == '__main__':
    unittest.main()
