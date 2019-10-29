#!/usr/bin/python3

# Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
# 在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
# 等号（=）用来给变量赋值。
# 等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

print("=========单个变量赋值==========")
# counter = 100 #整型变量
# miles = 1000.0 #浮点型变量
# name = "runoob" #字符型
#
# print("整型值：",counter)
# print("浮点型值：",miles)
# print("字符串值：",name)

print("=========多个变量赋值==========")
# a = b = c = 1
# print("a = ",a,"; b = ",b,"; c = ",c)
#
# a, b, c = 1, 20.2, "runoob"
# print("a = ",a,"; b = ",b,"; c = ",c)


print("=========标准数据类型==========")
# Python3 中有六个标准的数据类型：
#     Number（数字）
#     String（字符串）
#     List（列表）
#     Tuple（元组）
#     Set（集合）
#     Dictionary（字典）

# Python3 的六个标准数据类型中：
#     不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
#     可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

print("=========标准数据类型：Number（数字）==========")
# Python3 支持 int、float、bool、complex（复数）。
# 在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
# 像大多数语言一样，数值类型的赋值和计算都是很直观的。
# 内置的 type() 函数可以用来查询变量所指的对象类型。

# a, b, c, d, e = 1, 20.2, "runoob", True, 4+3j
# print("type a is",type(a))
# print("type b is",type(b))
# print("type c is",type(c))
# print("type d is",type(d))
# print("type e is",type(e))
#
# isinstance(a,int)
# isinstance(a.float)
# isinstance(a,str)
# isinstance(a,bool)
# isinstance(a,complex)

# isinstance和type的区别在于：   ????没懂????
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

# 注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到 Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。

# 通过使用del语句删除单个或多个对象
# del vars
# del var_a,var_b

# 数值运算
# print('加法：5 + 4 =',5+4)
# print('减法：4.3 - 2 =',4.3-2)
# print('乘法：3 * 7 =',3*7)
# print('除法：2 / 4 =',2/4)
# print('整除：2 // 4 =',2//4)
# print('取余：17 % 3 =',17%3)
# print('乘方：2 ** 5 =',2**5)

# Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
# print('复数：',3.14j)

print("=========标准数据类型：String（字符串）==========")
# Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符
# 变量[头下标:尾下标]

# str = 'Runoob'
# print('输出字符串',str)
# print('输出第一个到倒数第二个字符',str[0:-1]) # -1从末尾开始
# print('输出字符串第一个字符',str[0])
# print('输出字符串从第三个开始到第五个的字符',str[2:5])
# print('输出字符串从第三个开始的所有字符',str[2:])
# print('输出字符串两次',str*2)
# print('连接字符串',str + 'Test')

# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
# print('Ru\noob')
# print(r'Ru\noob')

# 与 C 字符串不同的是，Python 字符串不能被改变。向一个索引位置赋值，比如word[0] = 'm'会导致错误
# TypeError: 'str' object does not support item assignment

# 注意：
# 1、反斜杠可以用来转义，使用r可以让反斜杠不发生转义。
# 2、字符串可以用 + 运算符连接在一起，用 * 运算符重复。
# 3、Python中的字符串有两种索引方式，从左往右以0开始，从右往左以 - 1 开始。
# 4、Python中的字符串不能改变。

print("=========标准数据类型：List（列表）==========")
# List（列表） 是 Python 中使用最频繁的数据类型。
# 列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
# 列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
# 和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。
# 变量[头下标:尾下标]
# 索引值以 0 为开始值，-1 为从末尾的开始位置。
# 加号 + 是列表连接运算符，星号 * 是重复操作

# classmate=["Michael","Bob","Tracy"]
# print(classmate[0])
# print(classmate[1])
# print(classmate[2])

# list = ['abcd',1234,'runoob','1234',3.14]
# tinylist = [789,'runoob']
# print('输出完整列表：',list)
# print('输出列表第一个元素：',list[0])
# print('输出列表第二个到第三个元素：',list[1:3])
# print('输出列表第二个之后的全部元素：',list[1:])
# print('输出列表两次：',list*2)
# print('连接列表：',list+tinylist)

#! 与Python字符串不一样的是，列表中的元素是可以改变的：
# list = [1,2,3,4,5]
# list[0] = 'a'
# list[1] = 'b'
# print(list)
# list[2:5] = 'cde'
# print(list)
# list[0:] = []
# print(list)

# List 内置了有很多方法，例如 append()、pop() 等等，这在后面会讲到。
# 注意：
#     1、List写在方括号之间，元素用逗号隔开。
#     2、和字符串一样，list可以被索引和切片。
#     3、List可以使用+操作符进行拼接。
#     4、List中的元素是可以改变的。

# Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
# 如果第三个参数为负数表示逆向读取
# letter = ['c','h','e','c','k','i','o']
# print('letter[1:4:2] =',letter[1:4:2])

# def reverseWord(input):
#     # 通过空格将字符串分隔，把各个单词分隔为列表
#     inputWords = input.split(" ")
#
#     # 翻转字符串
#     # 假设列表 list = [1,2,3,4],
#     # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
#     # inputWords[-1::-1] 有三个参数
#     # 第一个参数 -1 表示最后一个元素
#     # 第二个参数为空，表示移动到列表末尾
#     # 第三个参数为步长，-1 表示逆向
#     inputWords=inputWords[-1::-1]
#
#     # 重新组合字符串
#     output = ' '.join(inputWords)
#
#     return  output
#
# if __name__ == "__main__":
#     input = 'I like runoob'
#     rw = reverseWord(input)
#     print(rw)

print("=========标准数据类型：Tuple（元组）==========")
# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
# 元组中的元素类型也可以不相同：

# tuple = ('abcd',789,2.23,'runoob',70.2)
# tinytuple = (123,'runoob')
# print('输出完整元组',tuple)
# print('输出元组的第一个元素',tuple[0])
# print('输出从第二个元素开始到第三个元素',tuple[1:3])
# print('输出从第三个元素开始的所有元素',tuple[2:])
# print('输出元组两次',tuple*2)
# print('连接元组',tuple+tinytuple)

# 元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
# 其实，可以把字符串看作一种特殊的元组。
# tup = (1,2,3,4,5,6)
# print('tup[0] =',tup[0])
# print('tup[1:5] =',tup[1:5])
# TypeError: 'tuple' object does not support item assignment
# tup[0] = 11

#! 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# tup = (['a','b'],2,'abc')
# print('tup[0] =',tup[0])

# 构造包含 0 个或 1 个元素的元组比较特殊，所以有一些额外的语法规则：
# tup1 = ()
# tup2 = (20,)

# string、list 和 tuple 都属于 sequence（序列）。
# 注意：
#     1、与字符串一样，元组的元素不能修改。
#     2、元组也可以被索引和切片，方法一样。
#     3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
#     4、元组也可以使用+操作符进行拼接。

print("=========标准数据类型：Set（集合）==========")
# 集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
# 基本功能是进行成员关系测试和删除重复元素。
# 可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

# student = {'Tom','Jim','Marry','Tom','Jack','Rose'}
# # 输出集合，重复元素被自动去掉
# print('输出student集合',student)
#
# # 测试成员
# if 'Rose' in student:
#     print('Rose 在集合中')
# else:
#     print('Rose 不在集合中')

# 个人Demo
# personnel = {'xwwu','changli','ddwu','jialchen','kkbao','hryu'}
# if 'wuxiuwen' or 'xwwu' in personnel:
#     print('吴秀文在小组中')
# else:
#     print('吴秀文不在小组中')

# # set可以进行集合运算
# a = set('abcdafafadfaf')
# b = set('acdcadca')
# print('集合a',a)
# print('a和b的差集',a-b)
# print('a和b的并集',a|b)
# print('a和b的交集',a&b)
# print('a和b中不通时存在的元素',a^b)

print("=========标""准数据类型：Dictionary（字典）==========")
# 字典（dictionary）是Python中另一个非常有用的内置数据类型。
# 列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
# 字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
# 键(key)必须使用不可变类型。
# 在同一个字典中，键(key)必须是唯一的。

# dict = {}
# dict['one'] = "1 - 菜鸟教程"
# dict[2] = "2 - 菜鸟工具"
# print('输出键值为‘one’的值',dict['one'])
# print('输出键2的值',dict[2])
#
# tinydict = {'name':'runoob','code':1,'site':'www.runoob.com'}
# print('输出完整的字典',tinydict)
# print('输出所有键',tinydict.keys())
# print('输出所有值',tinydict.values())

# 构造函数 dict() 可以直接从键值对序列中构建字典如下
# print(dict([('Runoob',1),('Google',2),('Taobao',3)]).keys())
# print(dict([('Runoob',1),('Google',2),('Taobao',3)]).values())
# print(dict([('Runoob',1),('Google',2),('Taobao',3)]).clear())

# print('{x : x**2 for x in (2,4,6)} = ',{x : x**2 for x in (2,4,6)})

# print('dict(Runoob=1,Google=2,Taobao=3).clear() =',dict(Runoob=1,Google=2,Taobao=3).clear())
# print('dict(Runoob=1,Google=2,Taobao=3).keys() =',dict(Runoob=1,Google=2,Taobao=3).keys())
# print('dict(Runoob=1,Google=2,Taobao=3).values() =',dict(Runoob=1,Google=2,Taobao=3).values())
# print('dict(Runoob=1,Google=2,Taobao=3).copy() =',dict(Runoob=1,Google=2,Taobao=3).copy())

# 另外，字典类型也有一些内置的函数，例如clear()、keys()、values()等。
# 注意：
#     1、字典是一种映射类型，它的元素是键值对。
#     2、字典的关键字必须为不可变类型，且不能重复。
#     3、创建空字典使用 { }。

print("=========Python 数据类型转换 ==========")
# 有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。
# 以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。
# a = 123456
# print(type(a))
# a = str(a)
# print(type(a))
