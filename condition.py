
print("************ 条件控制 *************")


print("************ if 语句 *************")


""" if 语句
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3  """

# Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。
# 注意：
#     1、每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块。
#     2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
#     3、在Python中没有switch – case语句。

# var1 = 100
# if var1:
#     print("1 - if 表达式条件为 true")
#     print("var1 = %s" % var1)
# var2 = 0
# if var2:
#     print("2 - if 表达式条件为 true")
#     print("var2 = %s" % var2)
# print("Good bye!")

# print("计算狗狗年龄对应人类年龄")
# age = float(input("请输入你家狗狗的年龄(单位/岁)："))
# print()
# if age <= 0:
#     print("请输入年龄！")
# elif age <= 1:
#     human = age * 14
#     print("对应人类年龄： %s 岁" % human)
# elif age <= 2:
#     human = 14 + (age - 1) * 8
#     print("对应人类年龄： %s 岁" %  human)
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄：  %s 岁" %  human)
# input("点击 enter 键退出")

# print("请问 5==6 ? ", 5 == 6)
# x = 5
# y = 8
# print("请问 x==y ? ", x == y)

# print("数字猜谜游戏!")
# number = 7
# guess = -1
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字太小了...")
#     elif guess > number:
#         print("猜的数字太大了...")

print("************ if 嵌套 *************")
# 在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
"""if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句"""

# num = int(input("输入一个数字："))
# if num % 2 == 0:
#     if num % 3 == 0:
#         print("您输入的数字可以整除 2 和 3")
#     else:
#         print("您输入的数字可以整除 2，但不能整除 3")
# else:
#     if num % 3 == 0
#         print("您输入的数字可以整除 3，但不能整除 2")
#     else:
#         print("您输入的数字不能整除 2 和 3")




