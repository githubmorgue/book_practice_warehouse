"""练习6-5：河流
创建一个字典，在其中存储三条重要河流及其流经的国家。
例如，一个键值对可能为'nile':'egypt'。
- 使用循环为每条河流打印一条消息，下面是一个例子。
The Nile runs through Egypt.
- 使用循环将该字典中每条河流的名字打印出来。
- 使用循环将该字典包含的每个国家的名字打印出来。"""
rivers = {"nile":"egypy","Yangtze River":"China",
          "Amazon River":"Brazil"}
for river,country in rivers.items():
    print("The "+river+" runs through "+country+".")
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)