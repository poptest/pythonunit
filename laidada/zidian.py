# -*- encoding:utf-8 -*-

result = [{"province": "浙江","city": "杭州","areacode": "0571","zip": "310000","company": "移动","card": ""},
          {"province": "湖北","city": "武汉","areacode": "0572", "zip": "310001","company": "联通","card": ""},
        {"province": "广西","city": "钦州","areacode": "0570", "zip": "31008","company": "联通","card": ""},
          {"province": "广东","city": "深圳","areacode": "0572", "zip": "310090","company": "联通","card": ""} ]

def tongji(results):

    for k in results:
        count = 0
        if k["company"] == "联通":
            conut = count + 1
    print(count)

shuliang = tongji(result)
print("联通营业厅的数量%s个"%shuliang)


# city_count = len("result")
# print(city_count)
# for k in result:
#     print(k["city"])

# dic["phone"]="13977726454"
# phone = "13977726454"
# province = "浙江"
# city = "杭州"
# areacode = "0571"
# zip = "310000"
# company = "移动"
#
# str ="电话:%s,省份:%s,城市:%s,编号:%s,邮编:%s,运营商:%s" % (dic["phone"],dic["result"]["province"],dic["result"]["city"],\
#      dic["result"]["areacode"],dic["result"]["zip"],dic["result"]["company"])
# print(str)