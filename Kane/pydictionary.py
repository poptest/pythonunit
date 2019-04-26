# -*- encoding:utf-8 -*-

#声明一个字典
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

# str = "%s %s %s"
# 电话号码:13429667914, 省份：浙江， 城市：杭州， 区域编码：0571， 邮编：310000， 运营商：移动
#往字典里面添加相应的数据
dic["result"]["tel"] = 13429667914
dic["result"]["name"] = "Kane","Alley"

#根据要求取出相应的数据
name = dic["result"]["name"][0]
province = dic["result"]["province"]
city = dic["result"]["city"]
areacode = dic["result"]["areacode"]
zip = dic["result"]["zip"]
company = dic["result"]["company"]
tel = dic["result"]["tel"]

#拼接字符串，并打印输出
str="电话号码：%s\r\n姓名：%s\r\n省份：%s\r\n城市：%s\r\n区域编码：%s\r\n邮编：%s\r\n运营商：%s"%(tel, name, province, city, areacode, zip, company)
print (str)
