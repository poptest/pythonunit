# -*- encoding:utf-8 -*-

jiangjin = float(raw_input("请输入利润（万元）："))
sum = 0.0
if jiangjin >= 0 and jiangjin < 10:
    sum = jiangjin * 0.1
    print sum
elif jiangjin > 10 and jiangjin < 20:
    sum = 10 * 0.1 + (jiangjin - 10) * 0.075
    print sum
elif jiangjin >= 20 and jiangjin < 40:
    sum = 10 * 0.1 + 10 * 0.075 + (jiangjin - 20) * 0.05
    print sum
elif jiangjin >= 40 and jiangjin < 60:
    sum = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + (jiangjin - 40) * 0.03
    print sum
elif jiangjin > 60 and jiangjin < 100:
    sum = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + (jiangjin - 60) * 0.015
    print sum
elif jiangjin >= 100:
    sum = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03 + 40 * 0.015 + (jiangjin - 100) * 0.01
    print sum
else:
    print ("请输入正确的利润！")