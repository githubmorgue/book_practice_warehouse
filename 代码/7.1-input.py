"""练习7-3：10的整数倍
让用户输入一个数，并指出该数是否是10的整数倍。"""
number = int(input("请输入一个数字："))
if number % 10 == 0:
    print("您输入的数字是10的倍数")