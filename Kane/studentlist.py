# -*- encoding:utf-8 -*-

#建立一个包含字典的列表
sudent_list=[
    {"name":"Kane", "age":"12", "sex":"nan"},
    {"name":"Alley", "age":"12", "sex":"nv"},
    {"name":"Lily", "age":"12", "sex":"nv"},
    {"name":"Alex", "age":"12", "sex":"nan"},
]

#通过for循环遍历list中的字典，并通过相应的key等到相应的val
for student in sudent_list:
    studnet_name=student["name"]
    print ("name:%s"%studnet_name)