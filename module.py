#!/usr/bin/python3


"""
在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。这也是使用 python 标准库的方法。
"""

"""
# 文件名 ： using_sys.py
1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
2、sys.argv 是一个包含命令行参数的列表。
3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
"""

print("========import语句=========")
# import fibo
# a = fibo.fib(1000)
# print("1000以内的菲波拉契数有", a)
# b = fibo.fib2(100)
# print("返回100内的斐波拉契数列",b)

# # 以双下划线开头和结尾的是专用的标识
# print("fibo.__name__:", fibo.__name__)


# # 将模块 fibo 中的方法 fib 赋予一个本地名称 fib
# fib = fibo.fib
# print(fib(500))
"""
在一个模块（或者脚本，或者其他地方）的最前面使用 import 来导入一个模块，当然这只是一个惯例，而不是强制的。
被导入的模块的名称将被放入当前操作的模块的符号表中。
"""

print("========from...import语句=========")
# 导入模块 fibo 的 fib、fub2 函数
# form fibo import fib, fib2
# fib(1000)
"""
可以使用 import 直接把模块内（函数，变量的）名称导入到当前操作模块。
这种导入的方法不会把被导入的模块的名称放在当前的字符表中（所以在这个例子里面，fibo 这个名称是没有定义的）。 
"""

print("========from...import *语句=========")
# 导入模块 fibo 的所有内容（少用）
# form fibo import *
"""
可以一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表
这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。
大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。
"""

print("========__name__属性=========")
"""
一个模块被另一个程序第一次引入时，其主程序将运行。
如果我们想在模块被引入时，模块中的某一程序块不执行，
我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。 

说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。
说明：__name__ 与 __main__ 底下是双下划线， _ _ 是这样去掉中间的那个空格
"""
# if __name__ == '__main__':
#     print("程序自身在运行")
# else:
#     print('我来自另一模块')

print("========dir() 函数=========")
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回
# import fibo, sys
# a = dir(fibo)
# print("dir(fibo)", a)
# b = dir(sys)
# print("dir(sys)", b)

# 如果没有给定参数，dir() 函数会罗列出当前定义的所有名称:
# import fibo
# fib = fibo.fib
# print("dir()",dir())

print("========标准模块=========")
# Linux下
# import sys
# sys.ps1
# sys.ps2

print("== == == ==包== == == ===")
"""
在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，
主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
最简单的情况，放一个空的 :file:__init__.py就可以了。
当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的） __all__变量赋值。
用户可以每次只导入一个包里面的特定模块，比如:
import sound.effects.echo

这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

还有一种导入子模块的方法是:
from sound.effects import echo

这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:
echo.echofilter(input, output, delay=0.7, atten=4)

还有一种变化就是直接导入一个函数或者变量:
from sound.effects.echo import echofilter

同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:
echofilter(input, output, delay=0.7, atten=4)

注意当使用 from package import item 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），
或者包里面定义的其他名称，比如函数，类或者变量。

import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。
如果还没找到，抛出一个 :exc:ImportError 异常。

反之，如果使用形如 import item.subitem.subsubitem 这种导入形式，除了最后一项，都必须是包，
而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。 
"""







