# -*- encoding:utf-8 -*-

dic = {
    "resultcode": "200",
    "reason": "Return Successd!",
    "result": {
        "province": "浙江",
        "city": "杭州",
        "areacode": "0571",
        "zip": "310000",
        "company": "移动",
        "card": ""
    },
    "error_code": 0
}



dic["tel"] = 13429667914
msg = "电话号码:%s,省份:%s,城市:%s,区域编码:%s,邮编:%s,运营商:%s" % \
      (dic["tel"],dic["result"]["province"],dic["result"]["city"],\
       dic["result"]["areacode"],dic["result"]["zip"],\
       dic["result"]["company"])


print(msg)
