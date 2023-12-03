"""练习4-4：一百万
创建一个包含数 1 ~ 1 000 000的列表，再使用一个for循环将这些数打印出来。
（如果输出时间太长，按ctrl + c停止输出或关闭输出窗口。）"""
numbers_list = []
for num in range(1,1000001):
    numbers_list.append(num)
# for num in numbers_list:
#     print(num)

"""练习4-5：一百万求和
创建一个包含数 1 ~ 1 000 000的列表，再使用min()和max()
核实该列表确实是从1开始、到1 000 000结束的。
另外，对这个列表调用函数sum()，看看python将一百万个数相加要多长时间。"""
print(min(numbers_list))
print(max(numbers_list))
print(sum(numbers_list))