#! /usr/bin/env python3

# Python语言支持以下类型的运算符:
#     算术运算符
#     比较（关系）运算符
#     赋值运算符
#     逻辑运算符
#     位运算符
#     成员运算符
#     身份运算符
#     运算符优先级

print('Python 算数运算符')
# a = 10
# b = 21
# print('a + b =',a+b)
# print('a - b =',a-b)
# print('a * b =',a*b)
# print('a / b =',a/b)
# print('a % b =',a%b)
# print('a ** b =',a**b)
# print('a // b =',a//b)

# a = 21
# b = 10
# c = 0
#
# c = a + b
# print('21 + 10 的值为：',c)
#
# c = a - b
# print('21 - 10 的值为：',c)
#
# c = a * b
# print('21 * 10 的值为：',c)
#
# c = a / b
# print('21 / 10 的值为：',c)
#
# c = a % b
# print('21 % 10 的值为：',c)
#
# # 修改变量a、b、c
# a = 2
# b = 3
# c = a**b
# print('2 ** 3 的值为:',c)
#
# a = 10
# b = 5
# c = a // b
# print('10 // 5 的值为：',c)

print('Python 比较运算符')
# print('========================= ')
# print('变量 a=21、b=10、c=0')
# a = 21
# b = 10
# c = 0
# if (a == b):
#     print('a 等于 b')
# else:
#     print('a 不等于 b')
# if (a != b):
#     print('a 不等于 b')
# else:
#     print('a 等于 b')
# if (a < b):
#     print('a 小于 b')
# else:
#     print('a 小于等于 b')
# if (a > b):
#     print('a 大于 b')
# else:
#     print('a 小于等于 b')
#
# print('========================= ')
#
# print('变量 a=5 和 b=20 ')
# a = 5;
# b = 20;
# if (a <= b):
#     print('a 小于等于 b')
# else:
#     print('a 大于 b')
# if (b >= a):
#     print("b 大于等于 a")
# else:
#     print('b 小于 a')

print('Python 赋值运算符')
# print('变量 a=21、b=10、c=0')
# a = 21
# b = 10
# c = 0
# c = a+b
# print('简单的赋值运算= :c = a+b =',c)
# c += a
# print('加法赋值运算符+= :c += a =',c)
# c -= a
# print('减法赋值运算符-= :c -= a =',c)
# c *= a
# print('乘法赋值运算符*= :c *= a =',c)
# c /= a
# print('除法赋值运算符/= :c /= a =',c)
# c %= a
# print('取模赋值运算符%= :c %= a =',c)
# c **= a
# print('幂赋值运算符**= :c **= a =',c)
# c //= a
# print('取整除赋值运算符//= :c //= a =',c)

print('Python 位运算符')
# 按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：
# a = 60        #60 = 00111100
# b = 13        #13 = 00001101
# c = 0
# c = a & b;   # 12 = 0000 1100
# print('按位与运算：a&b =',c)
# c = a | b;   # 61 = 0011 1101
# print('按位或运算：a|b =',c)
# c = a ^ b;   # 49 = 0011 0001
# print('按位异或运算：a^b =',c)
# c = ~a;     # -61 = 1100 0011
# print('按位取反运算：~a =',c)
# c = a << 2; # 240 = 1111 0000
# print("做移动运算：a << 2 =", c)
# c = a >> 2;  # 15 = 0000 1111
# print("右移动运算：a >> 2 =", c)

print('Python 逻辑运算符')
# a = 10
# b = 20
# print('a = 10')
# print('b = 20')
# if (a and b):
#     print('布尔与运算：a and b = true')
# else:
#     print('布尔与运算：a and b = false')
# if (a or b):
#     print('布尔或运算：a or b = true')
# else:
#     print('布尔或运算：a or b = flase')

# a = 0
# print('a = 0')
# if (a and b):
#     print('布尔与运算：a and b = true')
# else:
#     print('布尔与运算：a and b = false')
# if (a or b):
#     print('布尔或运算：a or b = true')
# else:
#     print('布尔或运算：a or b = false')
# if not(a and b):
#     print('布尔非运算：not(a and b) = true')
# else:
#     print('布尔非运算：not(a and b) = false')


print('Python 成员运算符')
# 测试实例中包含了一系列的成员，包括字符串，列表或元组。
# a = 10
# b = 20
# list = [1,2,3,4,5]
# print('a =',a)
# print('b =',b)
# print('lsit =',list)
# if (a in list):
#     print('变量a在给定的列表list中')
# else:
#     print('变量a不在给定的列表list中')
# if (b not in list):
#     print('变量b不在给定的列表list中')
# else:
#     print('变量b在给定的列表list中')
#
# a = 2
# print('a =',a)
# if (a in list):
#     print('变量a在给定的列表list中')
# else:
#     print('变量a不在给定的列表list中')


print('Python 身份运算符')
# 身份运算符用于比较两个对象的存储单元
# 注： id() 函数用于获取对象内存地址。
# a = 20;
# b = 20;
# print('a=20, b=20')
# if (a is b):
#     print('a 和 b 有同样的标识')
# else:
#     print('a 和 b 没有同样的标识')
# if (id(a) == id(b)):
#     print('id(a) 和 id(b) 有同样的标识')
# else:
#     print('id(a) 和 id(b) 没有同样的标识')
# # 修改变量b的值
# b = 30;
# print('a=20, b =30')
# if (a is b):
#     print('a 和 b 有同样的标识')
# else:
#     print('a 和 b 没有同样的标识')
# if (a is not b):
#     print('a 和 b 没有同样的标识')
# else:
#     print('a 和 b 有同样的标识')
# if (id(a) == id(b)):
#     print('id(a) 和 id(b) 有同样的标识')
# else:
#     print('id(a) 和 id(b) 没有同样的标识')

# is 与 == 区别：
# is 用于判断两个变量引用对象是否为同一个，
# == 用于判断引用变量的值是否相等。

print('Python 运算符优先级')
a = 20
b = 10
c = 15
d = 5
e = 0
print('a=20, b=10, c=15, d=5, e=0')
e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)
e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)
e = (a + b) * (c / d);  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)
e = a + (b * c) / d;  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)
