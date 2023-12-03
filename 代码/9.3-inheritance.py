"""练习9-6：冰淇淋小店
冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，
让它继承为完成练习9-1或9-4而编写的 Restaurant 类。
让两个版本的 Restaurant 类都可以，挑选你更喜欢的那个即可。
添加一个名为 flavors 的属性，用于储存一个各种口味的冰淇淋组成的列表。
编写一个显示这些冰淇淋的方法。创建一个 IceScreamStand 实例，并调用这个方法。"""


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


class IceCreamStand(Restaurant):
    # def __init__(self, restaurant_name, cuisine_type, flavor):
    #     super().__init__(restaurant_name, cuisine_type)

    # 冰淇凌的菜系一定是甜品，这样写可节省一个参数
    def __init__(self, restaurant_name, flavor):
        super().__init__(restaurant_name, "甜品")
        self.flavors = flavor

    def show_flavors(self):
        print(self.flavors)


so_sweet = IceCreamStand("so_sweet",
                         ["香蕉", "草莓", "哈密瓜", "开心果"])
so_sweet.describe_restaurant()
so_sweet.show_flavors()
