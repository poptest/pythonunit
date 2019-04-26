# -*- encoding:utf-8 -*-

dic = {
    "name": "xiaoyan",
    "xingbie": "nan",
    "nianling":"18",
    "dengji":"doudi"
    }


dic["tel"]= "1301918819"
msg ="电话；%s,姓名;%s,性别；%s,等级；%s,年龄；%s" % (dic["tel"],dic["name"],dic["xingbie"],dic["dengji"],dic["nianling"])
print msg