"""练习6-1：人
使用一个字典来储存一个熟人的信息，包括 名、姓、年龄和居住的城市。
该字典应包含键first_name、last_name、age和city。
将储存在该字典中的每项信息都打印出来。"""
friend = {"first_name":"小美","last_name":"陈","age":25,"city":"南京"}
print("姓名是："+friend["last_name"]+friend["first_name"])
print("年龄是："+str(friend["age"])) #age的值是数字，要转换成字符串
print("城市是："+friend["city"])