# Python 数字数据类型用于存储数值。
# 数据类型是不允许改变的,这就意味着如果改变数字数据类型的值，将重新分配内存空间。
# 以下实例在变量赋值时 Number 对象将被创建：
# 您也可以使用del语句删除一些数字对象的引用。
# del var1[,var2[,var3[....,varN]]]

# Python 支持三种不同的数值类型：
#     整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
#     浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
#     复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
# Python支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
# number = 0XA0F
# print('十六进制：',number)
# number = 0o37
# print('八进制：',number)

print('Python 数字类型转换')
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
#     int(x) 将x转换为一个整数。
#     float(x) 将x转换到一个浮点数。
#     complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
#     complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

# a = 1.0
# a = int(a)
# print('浮点型转换为整型',a)


print('Python 数字运算')
# 表达式的语法很直白： +, -, * 和 /, 和其它语言（如Pascal或C）里一样
# 注意：在不同的机器上浮点运算的结果可能会不一样。
# 在整数除法中，除法 / 总是返回一个浮点数，如果只想得到整数的结果，丢弃可能的分数部分，可以使用运算符 // ：
# print('除法: 17 / 3 =',17/3)
# print('整除: 17 // 3 =',17//3)
# print('取余: 17 % 3 =',17%3)
# 注意：// 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
# print('整除: 17.0 // 3 =',17.0//3)
# print('整除: 17 // 3.0 =',17//3.0)

# 变量在使用前必须先"定义"（即赋予变量一个值），否则会出现错误：NameError: name 'n' is not defined
# 不同类型的数混合运算时会将整数转换为浮点数
# print('3 * 3.75 / 1.5 =',3 * 3.75 / 1.5)
# print('7.0 / 2 =',7.0 / 2)

# 在交互模式中，最后被输出的表达式结果被赋值给变量 _
# 此处， _ 变量应被用户视为只读变量。
# >>> tax = 12.5 / 100
# >>> price = 100.50
# >>> price * tax
# 12.5625
# >>> price + _
# 113.0625
# >>> round(_, 2)

# 113.06
# import math
print('Python 数学函数:import math')
# a = 111.235
# a = abs(a)
# print('绝对值函数：abs(111.235) =',a)
# a = math.ceil(4.1)
# print('上入整数函数：math.ceil(4.1) =',a)
# a = math.floor(4.9)
# print('下舍整数函数：math.ceil(4.9) =',a)
# a = math.e
# print('自然指数e：math.e =',a)
# a = math.exp(2)
# print('e的x幂函数：math.exp(2) =',a)
# a = math.fabs(-10.0)
# print('绝对值：math.fabs(-10.0) =',a)
# a = math.log(math.e)
# print('ln-log以2为底x的对数：math.log(math.e) =',a)
# a = math.log10(100)
# print('log以10为底x的对数：math.log10(100) =',a)
# a = max('a','b','c')
# print('返回最大值：max(a,b,c) =',a)
# a = min('吴','秀','文')
# print("返回最小值：min('吴','秀','文') =",a)
# a = math.modf(11554.124)
# print("返回小数部分和整数部分：math.modf(11554.124) =",a)
# a = math.pow(5,4)
# print("幂运算：math.pow(5,4) =",a)
# a = math.sqrt(8)
# print("平方根：math.sqrt(8) =",a)
# a = round(5.4)
# print("浮点数四舍五入：round(5.4) =",a)

print('Python 伪随机函数:import random')
# 随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。
# 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
# # random() 方法返回随机生成的一个实数，它在[0,1)范围内

import random
# a = random.random()
# print("从[0,1)生成一个随机数：random() =",a)
# a = random.choice(range(10))
# print("从0到9中随机挑选一个整数：random.choice(range(10)) =",a)
# # 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
# a = random.randrange(0,55,2)
# print('从0到55中随机挑选一个偶数：a = random.randrange(0,55,2) =', a)

# # seed() 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。。
# # x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
# a = random.seed()
# a = random.random()
# print ("使用默认种子生成随机数：random.seed() =",a)
# a = random.seed(10)
# a = random.random()
# print ("使用整数种子生成随机数：random.seed(10) =",a)
# a = random.seed("hello",2)
# a = random.random()
# print ("使用字符串种子生成随机数：random.seed('hello',2) =",a)
# # 将序列的所有元素随机排序
# list = [20,202,2020];
# random.shuffle(list)
# print ("将序列的所有元素随机排序：random.shuffle(list) =",list)
# # 随机生成下一个实数，它在[x,y]范围内。
# a = random.uniform(5,10)
# print("uniform(5, 10) 的随机浮点数 : ",a)
# a = random.uniform(7,14)
# print("uniform(7, 14) 的随机浮点数 : ",a)

print('Python 三角函数:略 https://www.runoob.com/python3/python3-number.html')

print('Python 数学常量')
import math
print("数学常量 pi（圆周率，一般以π来表示）:",math.pi)
print('数学常量 e，e即自然常数（自然常数）:',math.e)













