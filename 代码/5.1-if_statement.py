"""练习5-3：外星人颜色
假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color的变量，
并将其赋值为'green'、'yellow'或'red'。
- 编写一条if语句，检查外星人是否是绿色的。如果是，就打印一条消息，
指出玩家获得了5分。
- 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中
未通过（未通过测试时没有输出）。"""
# alien_color = "red"
# if alien_color == "green":
#     print("You got 5 points!")

"""练习5-4：外星人颜色2
像练习5-3那样设置外星人的颜色，并编写一个if-else结构。
- 如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5分。
- 如果外星人不是绿色的，就打印一条消息，指出该玩家获得了10分。
编写这个程序的两个版本，在一个版本中执行if代码块，在另一个代码中
执行else代码块。"""
# alien_color = "green"
# if alien_color == "green":
#     print("You got 5 points!")
# else:
#     print("You got 10 points!")

"""练习5-5：外星人颜色3
将练习5-4中的if-else结构改为if-elif-else结构。
- 如果外星人是绿色的，就打印一条消息，指出玩家获得了5分。
- 如果外星人是黄色的，就打印一条消息，指出玩家获得了10分。
- 如果外星人是红色的，就打印一条消息，指出玩家获得了15分。
- 编写这个程序的三个版本，分别在外星人为绿色、黄色和红色时打印一条消息。"""
alien_color = "red"
if alien_color == "green":
    print("You got 5 points!")
elif alien_color == "yellow":
    print("You got 10 points!")
else:
    print("You got 15 points!")








