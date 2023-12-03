"""练习7-4：披萨配料
编写一个循环，提示用户输入一系列披萨配料，并在用户输入'quit'时结束循环。
每当用户输入一种配料后，都打印一条消息，指出我们会在披萨中添加这种配料。"""
user_input = input("请输入您想要添加的配料：")
while user_input != "quit":
    print("好的，皮萨里会为您添加" + user_input)
    user_input = input("请输入您想要添加的配料：")