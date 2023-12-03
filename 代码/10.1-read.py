"""练习10-1：Python学习笔记
在文本编辑器中新建一个文件，写几句话总结一下你至此学到的Python知识，
其中每一行都以"In Python you can"打头。
将这个文件命名为 learning_python.txt，并存储到为完成本章练习而编写的
程序所在目录中。
编写一个程序，它读取这个文件，并将你所写的内容打印三次；
第一次打印时读取整个文件；第二次打印时先将所有行都存储在一个列表中，
再遍历列表中的各行。"""
from pathlib import Path

path = Path("learning_python.txt")

# 读取整个文件
content = path.read_text()  # 在path类里面调用 read_txt() 函数
print(content)
print(type(content))

# 将所有行存储到一个列表中
# splitlines()函数将结果存储到列表中
lines = content.splitlines()  # 在文本内容中进行操作
print("\n")
print(type(lines))  # 打印lines的变量形式
for line in lines:
    print(line, end=" second print \n")
