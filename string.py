# 字符串是 Python 中最常用的数据类型。我们可以使用引号( ' 或 " )来创建字符串
# 创建字符串很简单，只要为变量分配一个值即可。例如：
# var1 = 'Hello World!'
# var2 = "Runoob"

# Python 访问字符串中的值
# Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
# Python 访问子字符串，可以使用方括号来截取字符串，如下实例：
print('Python 访问字符串中的值')
# var1 = 'Hello World!'
# var2 = "Runoob"
# print('var1[0]:',var1[0])
# print('var2[1:5]:',var2[1:5])

print('Python 字符串更新')
# var1 = 'Hello World!'
# print('已更新字符串：',var1[:6] + 'Runoob!')

print('Python 转义字符')

print('Python 字符串运算符')
# # 下表实例变量a值为字符串 "Hello"，b变量值为 "Python"
# a = 'Hello'
# print('a： ',a)
# b = 'Python'
# print('b： ',b)
#
# c = a + b
# print('字符串连接：+ ',c)
# c = a * 2
# print('重复输入字符串：* ',c)
# c = a[1]
# print('通过索引获取字符串中字符：[] ',c)
# # 截取字符串中的一部分，遵循左闭右开原则，str[0,2] 是不包含第 3 个字符的。
# c = a[1:4]
# print('通过索引获取字符串中字符：[:] ',c)
#
# print('成员运算符：in && not in')
# if('H' in a):
#     print('H 在变量 a 中')
# else:
#     print('H 不在变量 a 中')
# if('M' not in a):
#     print('M 不在变量 a 中')
# else:
#     print('M 在变量 a 中')

# # 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
# print('原始字符串')
# print(r'\n')
# print(R'\n')

# Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
# 在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
print('Python 字符串格式化')
# print("我叫 %s 今年 %d 岁！" % ('小明',10))

# %c 格式化字符 及其 ASCII 码
# %s 格式化字符串
# %d 格式化整数
# %u 格式化无符号整型
# %o 格式化无符号八进制
# %x 格式化无符号十六进制数
# %X 格式化无符号十六进制数（大写）
# %f 格式化浮点数字，可指定小数点后的精度
# %e 用科学计数法格式化浮点数
# %E 作用同%e，用科学计数法格式化浮点数
# %g %f和%e的简写
# %G %f 和 %E 的简写
# %p 用十六进制数格式化变量的地址

# 格式化操作符辅助指令:
# *	定义宽度或者小数点精度
# -	用做左对齐
# +	在正数前面显示加号( + )
# <sp>	在正数前面显示空格
# #	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
# 0	显示的数字前面填充'0'而不是默认的空格
# %	'%%'输出一个单一的'%'
# (var)	映射变量(字典参数)
# m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

# Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。

# python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下
print('Python 三引号')
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
其它特殊字符 续行符:'\
"""
# print (para_str)

# 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
# 一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。

# errHTML = '''
# <HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT TYPE=button VALUE=Back
# ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>
# '''
# cursor.execute('''
# CREATE TABLE users (
# login VARCHAR(8),
# uid INTEGER,
# prid INTEGER)
# ''')
# print(errHTML)

print('Python Unicode字符串')
# Unicode字符串
# 在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。
# 在Python3中，所有的字符串都是Unicode字符串。

print('Python 字符串内建函数')
# #1.capitalize() 方法将字符串的第一个字符转换为大写
# str = "this is string example from runoob....wow!!!"
# c = str.capitalize()
# print('首字母大写函数：str.capitalize() -',c)

# # 2.center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。
# # width - - 字符串的总宽度。
# # fillchar - - 填充字符。
# str = "[www.runoob.com]"
# print ("str.center(40, '*') : ", str.center(40, '*'))
# print ("str.center(80, '#') : ", str.center(80, '#'))

# # 3.count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
# # str.count(sub, start= 0,end=len(string))
# # sub -- 搜索的子字符串
# # start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
# # end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置
# str = "www.runoob.com"
# sub = 'o'
# print("str.count('o'):",str.count('0'))

# str = "www.runoob.com.www.runoob.com.www.runoob.com.www.runoob.com.www.runoob.com"
# sub = 'o'
# print ("str.count('o') : ", str.count(sub))
# print ("str.count('o', 0, 10) : ", str.count(sub,0,10))

# 4.decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。
# bytes.decode(encoding="utf-8", errors="strict")
#
# 5.encoding - - 要使用的编码，如"UTF-8"。
# errors - - 设置不同错误的处理方案。默认为'strict', 意为编码错误引起一个UnicodeError。 其他可能得值有'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'以及通过codecs.register_error()注册的任何值。
# str = "菜鸟教程";
# str_utf8 = str.encode("UTF-8")
# str_gbk = str.encode("GBK")
# print("str：",str)
# print("UTF-8 编码：", str_utf8)
# print("GBK 编码：", str_gbk)
# print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
# print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

# 6.endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。
# str.endswith(suffix[, start[, end]])
# suffix -- 该参数可以是一个字符串或者是一个元素。
# start -- 字符串中的开始位置。
# end -- 字符中结束位置
# Str='Runoob example....wow run!!!'
# suffix='!!'
# print ("字符串'Runoob example....wow!!!'是否以后缀'!!'结尾",Str.endswith(suffix))
# print ("字符串'Runoob example....wow!!!'从第20个字符开始是否以后缀'!!'结尾",Str.endswith(suffix,20))
# suffix='run'
# print ("字符串'Runoob example....wow!!!'是否以后缀'run'结尾",Str.endswith(suffix))
# print ("字符串'Runoob example....wow!!!'从第0-25个字符是否以后缀'run'结尾",Str.endswith(suffix, 0, 25))

# 7.expandtabs() 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
# # tabsize -- 指定转换字符串中的 tab 符号('\t')转为空格的字符数。str.expandtabs(tabsize=8)
# str = "thie is\tstring example....wow!!!"
# print("原始字符串："+str)
# print("替换\\t符号："+str.expandtabs())
# print("替换\\t符号："+str.expandtabs(tabsize=8))
# print("使用16个空格替换\\t符号："+str.expandtabs((16)))

# 8.find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# 如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。
# str.find(str, beg=0, end=len(string))
# str - - 指定检索的字符串
# beg - - 开始索引，默认为0。
# end - - 结束索引，默认为字符串的长度。
# str1 = "Runoob example....wow!!!"
# str2 = "exam"
# print (str1.find(str2))
# print (str1.find(str2, 5, 8))
# print (str1.find(str2, 5, 11))
# print (str1.find(str2, 10))
# 27.rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。
# str.rfind(str, beg=0 end=len(string))
# str - - 查找的字符串
# beg - - 开始查找的位置，默认为0
# end - - 结束查找位置，默认为字符串的长度。
# str1 = "this is really a string example....wow!!!"
# str2 = "is"
# print("返回字符串‘is’最后一次在‘this is really a string example....wow!!!’出现的位置是",str1.rfind(str2))
# print("返回字符串‘is’在‘this is really a string example....wow!!!’0-10之间最后一次出现的位置是",str1.rfind(str2,0,10))
# print("返回字符串‘is’在‘this is really a string example....wow!!!’10-0之间最后一次出现的位置是",str1.rfind(str2,10,0))

# 9.index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，
# 该方法与 python find()方法一样，【！！！！！】只不过如果str不在 string中会报一个异常。
# str.index(str, beg=0, end=len(string))
# str - - 指定检索的字符串
# beg - - 开始索引，默认为0。
# end - - 结束索引，默认为字符串的长度。
# str1 = "Runoob example....wow!!!"
# str2 = "exam"
# print(str1.index(str2))
# print("************")
# print(str1.index(str2,5))
# print("************")
# print(str1.index(str2,10))
# 28.rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。
# str.rindex(str, beg=0 end=len(string))
# str - - 查找的字符串
# beg - - 开始查找的位置，默认为0
# end - - 结束查找位置，默认为字符串的长度。
# str1 = "this is really a string example....wow!!!"
# str2 = "is"
# print ("返回字符串‘is’最后一次在‘this is really a string example....wow!!!’出现的位置是",str1.rindex(str2))
# print ("返回字符串‘is’在‘this is really a string example....wow!!!’第10个字符开始最后一次出现的位置是",str1.rindex(str2,10))



# 10.isalnum() isalnum() 方法检测字符串是否由 字母 和 数字 组成。
# str.isalnum()
# str = "runoob2016"  # 字符串没有空格
# print("字符串'runoob2016'是否由字母和数字组成",str.isalnum())
# str = "www.runoob.com"
# print("字符串'www.runoob.com'是否由字母和数字组成",str.isalnum())

# 11.isalpha() Python isalpha() 方法检测字符串是否只由字母或文字组成。
# str.isalpha()
# 如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。
# str = "runoob"
# print ("字符串'runoob'是否只由字母 或 文字 组成",str.isalpha())
# # 字母和中文文字
# str = "runoob菜鸟教程"
# print ("字符串'runoob菜鸟教程'是否只由字母 或 文字 组成",str.isalpha())
# str = "Runoob example....wow!!!"
# print ("字符串'Runoob example....wow!!!'是否只由字母 或 文字 组成",str.isalpha())


# 12.isdigit()  Python isdigit() 方法检测字符串是否只由数字组成。
# str.isdigit()
# 如果字符串只包含数字则返回 True 否则返回 False。
# str = "123456";
# print ("字符串'123456'是否只包含数字",str.isdigit())
# str = "Runoob example....wow!!!"
# print ("字符串'Runoob example....wow!!!'是否只包含数字",str.isdigit())

# 13.islower()  方法检测字符串是否由小写字母组成。
# str.islower()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
# str = "RUNOOB example....wow!!!"
# print ("字符串'RUNOOB example....wow!!!'是否只包含小写字母",str.islower())
# str = "runoob example....wow!!!"
# print ("字符串'runoob example....wow!!!'是否只包含小写字母",str.islower())

# 14.isnumeric() 方法检测字符串是否只由数字组成，数字可以是： Unicode 数字，全角数字（双字节），罗马数字，汉字数字。指数类似 ² 与分数类似 ½ 也属于数字。
# s = '½'
# s = '\u00BD'
# str.isnumeric()
# 如果字符串中只包含数字字符，则返回 True，否则返回 False
# str = "runoob2016"
# print ("字符串'runoob2016'是否只由数字组成",str.isnumeric())
# str = "23443434"
# print ("字符串'23443434'是否只由数字组成",str.isnumeric())

# 15.isspace()    Python isspace() 方法检测字符串是否只由空白字符组成。
# str.isspace()
# 如果字符串中只包含空格，则返回 True，否则返回 False.
# str = "       "
# print("字符'       '是否只由空白字符组成",str.isspace())
# str = "Runoob example....wow!!!"
# print("字符'Runoob example....wow!!!'是否只由空白字符组成",str.isspace())

# 16.istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。
# str.istitle()
# 如果字符串中所有的单词拼写首字母是否为大写，且其他字母为小写则返回 True，否则返回 False.
# str = "This Is String Example...Wow!!!"
# print("字符串'This Is String Example...Wow!!!'是否仅首字母大写",str.istitle())
# str = "This is string example....wow!!!"
# print("字符串'This is string example....wow!!!'是否仅首字母大写",str.istitle())

# 17.isupper() 方法检测字符串中所有的字母是否都为大写。
# str.isupper()
# 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
# str = "THIS IS STRING EXAMPLE....WOW!!!"
# print("字符串'THIS IS STRING EXAMPLE....WOW!!!'是否全部为大写字符",str.isupper())
# str = "THIS is string example....wow!!!"
# print("字符串'THIS is string example....wow!!!'是否全部为大写字符",str.isupper())


# 18.join(seq) Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
# str.join(sequence)
# s1 = "-"
# s2 = ""
# seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
# print ("使用连接符字符串'-'",s1.join(seq))
# print ("使用连接字符串''",s2.join(seq))


# 19.len() Python len() 方法返回对象（字符、列表、元组等）长度或项目个数。
# len(s)


# 20.ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
# str.ljust(width[, fillchar])
# 29.rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。
# str.rjust(width[, fillchar])
# width - - 指定字符串长度。
# fillchar - - 填充字符，默认为空格。
# 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
str = "Runoob example....wow!!!"
print("以原字符串为左侧基准，填充'*'打印出50个字符",str.ljust(50,'*'))
print("以原字符串为右侧基准，填充'*'打印出50个字符",str.rjust(50,'*'))
# 39.zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。
# str = "this is string example from runoob....wow!!!"
# print ("str.zfill : ",str.zfill(40))
# print ("str.zfill : ",str.zfill(50))


# # 22.lstrip() 方法用于截掉字符串左边的空格或指定字符。
# # str.lstrip([chars])
# # chars --指定截取的字符。
# str = "     this is string example....wow!!!     ";
# print( str.lstrip() );
# str = "88888888this is string example....wow!!!8888888";
# print( str.lstrip('8') );
# # 30.rstrip() 删除字符串字符串末尾的空格.
# str = "     this is string example....wow!!!     ";
# print( str.rstrip() );
# str = "88888888this is string example....wow!!!8888888";
# print( str.rstrip('8') );
# # 34.strip([chars])
# # 在字符串上执行 lstrip()和 rstrip()
# str = "     this is string example....wow!!!     ";
# print( str.strip() );
# str = "88888888this is string example....wow!!!8888888";
# print( str.strip('8') );


# 23.maketrans()方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
# 第一个参数是字符串，表示需要转换的字符，
# 第二个参数也是字符串表示转换的目标。
# 两个字符串的长度必须相同，为一一对应的关系。
# 注：Python3.4 已经没有 string.maketrans() 了，取而代之的是内建函数: bytearray.maketrans()、bytes.maketrans()、str.maketrans()
# str.maketrans(intab, outtab)
# intab - - 字符串中要替代的字符组成的字符串。
# outtab - - 相应的映射字符的字符串。
# 37. translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符,要过滤掉的字符放到 deletechars 参数中。
# str.translate(table)
# bytes.translate(table[, delete])
# bytearray.translate(table[, delete])
# table - - 翻译表，翻译表是通过maketrans()方法转换而来。
# deletechars - - 字符串中要过滤的字符列表。
# 返回翻译后的字符串,若给出了 delete 参数，则将原来的bytes中的属于delete的字符删除，剩下的字符要按照table中给出的映射来进行映射 。
# intab = "aeiou"
# outtab = "12345"
# trantab = str.maketrans(intab, outtab)  # 制作翻译表
# str = "this is string example....wow!!!"
# print(str.translate(trantab))

intab = "ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ"
outtab = "1234567890"
trantab = str.maketrans(intab, outtab)
print('Ⅰ①Ⅱ②Ⅲ③Ⅳ④Ⅴ⑤Ⅵ⑥Ⅶ⑦Ⅷ⑧Ⅸ⑨Ⅹ⑩'.translate(trantab))

# 24.max() 方法返回字符串中最大的字母。
# max(str)
# 25.min() Python min() 方法返回字符串中最小的字母
# min(str)
# str = "runoob"
# print ("最大字符: " + max(str))
# print ("最小字符: " + min(str))


# 26.replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。
# str.replace(old, new[, max])
# old - - 将被替换的子字符串。
# new - - 新字符串，用于替换old子字符串。
# max - - 可选字符串, 替换不超过max次
# 返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。
# str = "www.w3cschool.cc"
# print("菜鸟教程旧地址：", str)
# print("菜鸟教程新地址：", str.replace("w3cschool.cc", "runoob.com"))
# str = "this is string example....wow!!!"
# print(str.replace("is", "was", 3))
# str = "A rafrashing breeze is blowing gently"
# print(str.replace("a","e",2))


# 31.split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。
# str.split(str="", num=string.count(str))
# str - - 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num - - 分割次数。默认为 - 1, 即分隔所有。
# str = "this is string example....wow!!!"
# print ("以空格为分隔符将原字符串分隔",str.split( ))
# print ("以第一个'i'为分隔符将原字符串分隔",str.split('i',1))
# print ("以前两个'i'为分隔符将原字符串分隔",str.split('i',2))
# print ("以前三个'i'为分隔符将原字符串分隔",str.split('i',3))
# print ("以'w'为分隔符将原字符串分隔",str.split('w'))
# txt = "Google#Runoob#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
# x = txt.split("#", 1)
# print(x)


# 32.splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# str.splitlines([keepends])
# print('ab c\n\nde fg\rkl\r\n'.splitlines())
# print('ab c\n\nde fg\rkl\r\n'.splitlines(True))


# 33.startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。
# str - - 检测的字符串。
# substr - - 指定的子字符串。
# strbeg - - 可选参数用于设置字符串检测的起始位置。
# strend - - 可选参数用于设置字符串检测的结束位置。
# str = "this is string example....wow!!!"
# print ("字符串是否以 this 开头：",str.startswith( 'this' ))
# print ("从第8个字符开始的字符串是否以 string 开头：",str.startswith( 'string', 8 ))
# print ("从第2个字符开始到第4个字符结束的字符串是否以 this 开头：",str.startswith( 'this', 2, 4 ))
# 21.lower()    Python lower() 方法转换字符串中所有大写字符为小写。
# str.lower()
# # 返回将字符串中所有大写字符转换为小写后生成的字符串。
# str = "Runoob EXAMPLE....WOW!!!"
# print("将所有字符'Runoob EXAMPLE....WOW!!!'转换为小写",str.lower())
# 35.swapcase() 方法用于对字符串的大、小写字母进行转换。
# str = "this is string example....wow!!!"
# print (str.swapcase())
# str = "This Is String Example....WOW!!!"
# print (str.swapcase())
# 36.title() 方法返回"标题化"的字符串,就是说所有单词的首个字母转化为大写，其余字母均为小写(见 istitle())。
# str = "this is string example from runoob....wow!!!"
# print (str.title())
# 38. upper()   转换字符串中的小写字母为大写
# str = "Runoob EXAMPLE....WOW!!!"
# print("字符串'Runoob EXAMPLE....WOW!!!'转换为大写",str.upper() )


# 40.isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
# 注意:定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。
# str = "runoob2016"
# print (str.isdecimal())
# str = "23443434"
# print (str.isdecimal())






