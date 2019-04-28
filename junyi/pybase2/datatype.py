# -*- encoding: utf-8 -*-

week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")

for today in week:
    if today == "星期日":
        print("今天是%s ，今天不上课" % today)
    else:
        print("今天是%s ，今天上课" % today)


