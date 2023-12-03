"""练习9-1：餐馆
创建一个名为 Restaurant 的类，为其 __init__() 方法设置两个属性：
restaurant_name 和 cuisine_type。
创建一个名为 describe_restaurant() 的方法和一个名为
open_restaurant() 的方法，前者打印前述亮相信息，而后者打印一条消息，
指出餐馆正在营业。
根据这个类创建一个名为 restaurant 的实例，分别打印其两个属性，再调用前述两个方法。"""
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"餐厅名：{self.restaurant_name}")
#         print(f"菜系：{self.cuisine_type}")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name}餐馆正在营业...")
#
# taotaoju = Restaurant("陶陶居","粤菜")
# print(taotaoju.restaurant_name,taotaoju.cuisine_type)
# taotaoju.describe_restaurant()
# taotaoju.open_restaurant()

"""练习9-4：就餐人数
在为练习9-1编写的程序中，添加一个名为 number_served 的属性，
并将默认值设为0。根据这个类创建一个名为 restaurant 的实例。打印有
多少人在这家餐馆就餐过，然后修改这个值并在再次打印。
- 添加一个名为 set_number_served() 的方法，用来设置就餐人数。调用这个方法
并向它传递新的就餐人数，然后再打印这个和值。
- 添加一个名为 increment_number_served() 的方法，用来让就餐人数递增。调用这个方法
并向他传递一个这样的值： 你认为这家餐馆每天可能接待的就餐人数。 """


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.num_served = 0

    def describe_restaurant(self):
        print(f"餐厅名：{self.restaurant_name}")
        print(f"菜系：{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}餐馆正在营业...")

    def set_num_served(self, num_served):
        self.num_served = num_served

    def increment_number_served(self, increment_number):
        self.num_served += increment_number


taotaoju = Restaurant("陶陶居", "粤菜")
print(taotaoju.restaurant_name, taotaoju.cuisine_type)

# 打印最开始num_served的值
print(taotaoju.num_served)

taotaoju.describe_restaurant()
taotaoju.open_restaurant()

# 打印更新后的num_served的值
taotaoju.set_num_served(500)
taotaoju.increment_number_served(20)
print(taotaoju.num_served)
