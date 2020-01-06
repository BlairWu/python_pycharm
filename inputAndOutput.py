#!/usr/bin/python3

print("== == == 输出格式美化 == == ==")
"""
    str()： 函数返回一个用户易读的表达形式。
    repr()： 产生一个解释器易读的表达形式。
"""

"""
#  repr() 函数可以转义字符串中的特殊字符
hello = 'Hello, runoob\n'
hellos = repr(hello)
print(hellos)

x = 10 * 3.25
y = 200 * 200
s = 'x 的值为：' + repr(x) + ', y的值为：' + repr(y) + "..."
print(s)
# repr() 的参数可以是 Python 的任何对象
repr((x, y, ('Google', 'Runoob')))  # 元组(x, y, ('Google', 'Runoob'))
"""

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print()





