"""练习10-5：访客簿
编写一个 while 循环，提示用户输入名字。收集用户输入的所有名字，
将其写入 guest_book.txt，并确保这个文件中每条记录都独占一行。"""
from pathlib import Path

names = ""
user_input = input("请输入访客的名字（完成所有名字输入后，请输入q退出程序）：")
while user_input != "q":
    names += user_input + "\n"
    user_input = input("请输入访客的名字（完成所有名字输入后，请输入q退出程序）：")

path = Path("guest_book.txt")
path.write_text(names)
