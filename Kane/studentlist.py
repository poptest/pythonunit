# -*- encoding:utf-8 -*-

#建立一个包含字典的列表
sudent_list=[
    {"name":"Kane", "age":"12", "sex":"nan"},
    {"name":"Alley", "age":"12", "sex":"nv"},
    {"name":"Lily", "age":"12", "sex":"nv"},
    {"name":"Alex", "age":"12", "sex":"nan"},
]
count=0
#通过for循环遍历list中的字典，并通过相应的key等到相应的val
for student in sudent_list:
    studnet_name=student["name"]
    print ("name:%s"%studnet_name)
    #判断性别是否为女
    if(student["sex"]=="nv"):
        count+=1

print ("一共有%s个女生"%count)