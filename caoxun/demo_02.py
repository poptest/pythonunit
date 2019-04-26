'''
def sayhellow():
    print("hello world")
    print("hello world")
sayhellow()

total = 10 + \
           20 + \
    30
print(total)

dict = {"name":"caoxun","tel":123456}
print(dict["name"])


name = "caoxun"
num = 1
num2 = 2.0

print(name)
print(type(name))
print(num2)
print(type(num))
a = float(num)
print(type(a))
'''

list = ["a","b",2,3,4,5]
list_1 = [1,2,3,4,5,6,7,8,9]
print(list[0:3])
print(list_1[2:7:2])


list.append("world")
print(list)
list.append([6,7,8,9])
print(list)
print(list[-1][-2])
print(list_1[2])

dict = {"name":"xiao ming","tel ":[12344444,2233333],"email":"adress123"}
print(dict["name"])
print(dict["tel "][0])
print(dict["tel "][-1])
print(dict)
dict["adress"] = "wuhan"
print(dict)
dict["name"] = "xiao zi"
print(dict["name"])

print(dict.keys())
print(dict.has_key("tel"))