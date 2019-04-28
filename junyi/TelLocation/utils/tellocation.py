# -*- encoding:utf-8 -*-



class TelLocationUtil():

    STATUS_CODE = 'status_code'
    STATUS_CODE_IN_DIC = 'statu_code_in_dic'
    PROVINCE = 'province'
    CITY = 'city'
    AREACODE = 'areacode'
    ZIP = 'zip'
    COMPANY = 'company'
    CARD = 'card'

    @classmethod
    def get_location(cls, tel):
        #1. 定义返回值字典
        ret_dic = {}
        #2. 根据传入的电话号码调用对应的目标API
        params_dic = {"phone": tel,
                      "key": TEL_USER_KEY}
        resp = requests.get(TEL_LOCTION_URL, params_dic)

        #3. 获取并组合所需的返回值到字典中
        #3.1 将返回值转化成json_dic格式
        resp_dic = json.loads(resp.content)
        #3.1 向返回值字典中填在状态码
        ret_dic['status_code'] = resp.status_code
        ret_dic['statu_code_in_dic'] = resp_dic['resultcode']
        ret_dic['province'] = resp_dic['result']['province']
        ret_dic['city'] = resp_dic['result']['city']
        ret_dic['areacode'] = resp_dic['result']['areacode']
        ret_dic['zip'] = resp_dic['result']['zip']
        ret_dic['company'] = resp_dic['result']['company']
        ret_dic['card'] = resp_dic['result']['card']

        #4. 返回组装好的字典
        return ret_dic

    def tel_location_assert(self, resp, exp_status_code, exp_provice, exp_city, exp_areacode, exp_zip, exp_company,
                            exp_card):
        assert_result_pass = []
        assert_result_fail = []

        act_statu_code = resp[TelLocationUtil.STATUS_CODE]
        if act_statu_code == exp_status_code:
            assert_result_pass.append({"statu_code": [act_statu_code, exp_status_code]})
        else:
            assert_result_fail.append({"statu_code": [act_statu_code, exp_status_code]})

        act_provice = resp[TelLocationUtil.PROVINCE]
        if act_provice == exp_provice:
            assert_result_pass.append({"provice": [act_provice, exp_provice]})
        else:
            assert_result_fail.append({"provice": [act_provice, exp_provice]})

        act_city = resp[TelLocationUtil.CITY]
        if act_city == exp_city:
            assert_result_pass.append({"city": [act_city, exp_city]})
        else:
            assert_result_fail.append({"city": [act_city, exp_city]})

        act_areacode = resp[TelLocationUtil.AREACODE]
        if act_areacode == exp_city:
            assert_result_pass.append({"areacode": [act_areacode, exp_areacode]})
        else:
            assert_result_fail.append({"areacode": [act_areacode, exp_areacode]})

        act_zip = resp[TelLocationUtil.ZIP]
        if act_zip == exp_zip:
            assert_result_pass.append({"zip": [act_zip, exp_zip]})
        else:
            assert_result_fail.append({"zip": [act_zip, exp_zip]})

        act_company = resp[TelLocationUtil.COMPANY]
        if act_company == exp_company:
            assert_result_pass.append({"zip": [act_company, exp_company]})
        else:
            assert_result_fail.append({"zip": [act_company, exp_company]})

        act_card = resp[TelLocationUtil.CARD]
        if act_card == exp_card:
            assert_result_pass.append({"card": [act_card, exp_card]})
        else:
            assert_result_fail.append({"card": [act_card, exp_card]})

        return assert_result_pass, assert_result_fail
