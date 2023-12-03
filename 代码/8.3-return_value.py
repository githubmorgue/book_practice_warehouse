"""练习8-6：城市名
编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
这个函数应返回一个格式，类似于下面的字符串：
”Santiago ,Chile“
至少使用三个城市国家对来调用这个函数，并打印它返回的值。"""


def city_country(city, country):
    return f"{city}, {country}"


city_country_1 = city_country("Santiago", "Chile")
city_country_2 = city_country("Shenzhen", "China")
city_country_3 = city_country("New York", "America")
print(city_country_1)
print(city_country_2)
print(city_country_3)
