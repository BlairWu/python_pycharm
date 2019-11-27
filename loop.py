#!/usr/bin/env python3

print("************ 条件控制 *************")
print("""Python 中的循环语句有 for 和 while, 在 Python 中没有 do..while 循环""")

print("************ while 循环  *************")
"""
while 判断条件(condition)：
    执行语句(statements)……
"""

# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print("1 到 %d 的之和为: %d " % (n,sum))

# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + (counter**2)
#     counter += 2
# print("1 到 %d 之间的奇数的幂之和为: %d " % (n,sum))




print("************ 无限循环 *************")
"""
我们可以通过设置条件表达式永远不为 false 来实现无限循环
"""
# var = 1
# while var == 1:   # 表达式永远为 true
#     num = int(input("输入一个数字："))
#     print("你输入的数字是：", num)
# print("Goog Bye !")
#  CTRL+C 来退出当前的无限循环

print("************ while 循环使用 else 语句 *************")
# 在 while … else 在条件语句为 false 时执行 else 的语句块
# count = 0
# while count < 5:
#     print(count, "小于5")
#     count = count + 1
# else:
#     print(count, "大于或等于 5")

print("************ 简单语句组 *************")
# 类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中
# flag = 1
# while(flag) :print('欢迎访问菜鸟教程！')
# print("Good Bye !")

print("************ for 语句 *************")
"""
for <variable> in <sequence>:
    <statements>
else:
    <statements>
"""

# languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#     print(x)

print("""以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体""")
# sites = [ 'Google', 'Baidu', 'Runoob', 'Taobao']
# # sites = [ 'Runoob', 'Google', 'Baidu', 'Taobao']
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程！")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据！")
# print("完成循环！")


print("************ range()函数 *************")
# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
# for i in range(5):
#     print(i)

# 指定区间的值
# for n in range(5,9):
#     print(n)

# 负数：
# for i in range(-10, -100, -30):
#     print(i)

# 您可以结合range()和len()函数以遍历一个序列的索引
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len((a))):
#     print("a[",i,"]:" , a[i])

# 还可以使用range()函数来创建一个列表
# a = list(range(5))
# print(a)

print("************ break 和 continue 语句及循环中的 else 子句  *************")
"""
while <expr>
↑   <statement>
|   <statement>
|     break ------
|   <statement>  |
|   <statement>  |
----- continue   |
    <statement>  |
    <statement>  |
<statement>   ←---
"""

# break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
# continue 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break     # 结束循环，不需要运行print（2）
#     print(n)
# print('循环结束。')
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue     # 继续循环，不需要运行print（2）
#     print(n)
# print('循环结束。')

print("第一个实例：for 循环，break")
# for letter in 'Runoob':
#     if letter == 'b':
#         break
#     print('当前字母为：', letter)
# print('for循环结束')
# print()
print("第二个实例：while 循环，break")
# var = 10
# while var > 0:
#     print('当前变量值为：', var)
#     var = var - 1
#     if var == 5:
#         break
# print("while循环结束")

# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。
print("100以内的质数")
# for n in range(2,100):         # 第一层循环
#     for x in range(2,n):                    ## 第二层循环
#         if n % x == 0:                      ## 是否存在整除的数，存在就不是质数
#             print(n,'等于',x,'*',n//x)      ## 整除，不需要小数点
#             break
#     else:
#         #循环语句中没有找到元素
#         print(n,'是质数')                  ## 第二层循环
# print('哈 ！ 哈 ！ 哈 ！')   # 第一层循环

# print("1000以内的质数")
# for n in range(2,1000):
#     for x in range(2,n):
#         if n % x == 0:
#             print(n,'equal to',x,'*',n//x)
#             break
#     else:
#         print(n,'is a prime number')
# print('The end')

print("************ pass 语句  *************")
# pass是空语句，是为了保持程序结构的完整性。
# pass 不做任何事情，一般用做占位语句
# while True:
#     pass # 等待键盘中断（Ctrl + C）

# 以下实例在字母为 o 时 执行 pass 语句块
# for letter in 'Runoob':
#     if letter == 'o':
#         pass
#         print('执行pass块')
#     print('当前字母：',letter)
# print("The end !")


