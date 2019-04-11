# -*- encoding:utf-8 -*-
import requests
import json
from junyi.config import TEL_LOCTION_URL, TEL_USER_KEY

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
