# !/usr/bin/python3

# 保留字
import keyword
print(keyword.kwlist)


print('*******************注释*******************')
# 单行注释
# 第二个注释

'''
多行注释
第四注释
'''

"""多行注释
第六注释"""

# *******************行与缩进******************* #
print('*******************行与缩进*******************')
# if True:
#     print("Answer")
#     print ("True")
# else:
#     print("Answer")
#  print("False") # 缩进不一致，会导致运行错误

# *******************多行语句******************* #
print('*******************多行语句*******************')
# total = item_one + \
#         item_two + \
#         item_three
# print(total)
#
# total2 = [
#     'item_one',
#     'item_two',
#     'item_three',
#     'item_four',
#     'item_five'
# ]
# print(total2)

# *******************数字类型 int/bool/float/complex ******************* #
print('*******************数字类型 int/bool/float/complex*******************')

# int 整数 长整型
# bool 布尔 True
# float 浮点数 1.23
# complex 复数 1 + 2j

# *******************字符串 String******************* #
print('*******************字符串 String*******************')
# word = '字符串'
# print("word :",word)
#
# sentence = "这是一个句子。"
# print("sentence :",sentence)
#
# paragraph = """
# 这是一个段落，
# 可以由多行组成
# """

# print("paragraph :",paragraph)
#
# str = 'Wuxiuwen'
# print(str)
# print(str[0])              # 输出字符串第一个字符
# print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
# print(str[0:5]) # 输出从第1个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始的后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + 'is girl')  # 连接字符串
# print(str + 'is girl')  # 连接字符串
#
# print('------------------------------')
#
# print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# *******************空行******************* #
print('*******************空行*******************')

# *******************等待用户输入******************* #
print('*****************等待用户输入******************')
# input("\n\n按下 enter 键后退出。")

# *******************同一行显示多条语句******************* #
print('*****************同一行显示多条语句******************')
# import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# *******************多个语句构成代码组******************* #
print('*****************多个语句构成代码组******************')
# if expression :
#    suite
# elif expression :
#    suite
# else :
#    suite

# *******************Print 输出******************* #
print('*****************Print 输出******************')
# x = 'a'
# y = 'b'
# # 换行输出
# print(x)
# print(y)
# print('---------')
# print(x,end="\n")
# print(y,end="\n")
# print('---------')
# # 不换行输出
# print(x, end=" ")
# print(y, end=" ")
# print()

# *******************import 与 from...import******************* #
print('================ python : import  ==================')
#导入sys模块
import sys
# print('命令行参数列表为：')
# for i in sys.argv:
#     print(i)
# print('\n python 路径为',sys.path)
# print('参数个数为：',len(sys.argv),'个参数。')
# print('参数列表',str(sys.argv))

print('============== python : from...import ===================')
# # 导入特定成员
# from sys import argv, path
# # 因为已经导入path成员，所以此处引用时不需要加sys.path
# print('path:',path)
# print('argv:',argv)

# 命令行输入参数：python argv.py hello world !
# from sys import argv
# pyname, a, b, c = argv
# print('python file name is :',pyname)
# '''
# print('The first word is :',a)
# print('The second word is :',b)
# print('The third word is :',c)
# '''
# print("==argv==",argv)

print('============== getopt 模块===================')
# Python 中也可以所用 sys 的 sys.argv 来获取命令行参数：
#     sys.argv 是命令行参数列表。
#     len(sys.argv) 是命令行参数个数。
# 注：sys.argv[0] 表示脚本名。

# 该模块提供了两个方法【 getopt.getopt、getopt.gnu_getopt】及一个异常处理【getopt.GetoptError】来解析命令行参数。

# getopt.getopt 方法用于解析命令行参数列表：getopt.getopt(args, options[, long_options])
# args:要解析的命令行参数列表
# options：以字符串格式定义，带“：”表示选项必须附加参数
# long_options：以列表格式定义，带“=”表示选项必须附加参数
# 该方法返回值由两个元素组成
# 第一个是（option，value）元组的列表
# 第二个是参数列表，包含那些没有“-”、“--”的参数

# getopt.GetoptError
# 在没有找到参数列表，或选项的需要的参数为空时会触发该异常
# 异常的参数是一个字符串，表示错误的原因。属性msg、opt为相关选项的错误信息

# import sys,getopt
# def main(argv):
#     inputfile = ''
#     outputfile = ''
#     try:
#         opts,args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
#     except getopt.GetoptError:
#         print('test.py -i <inputfile> -o <outputfile>')
#         sys.exit(2)
#     for opt,arg in opts:
#         if opt == '-h':
#             print('test.py -i <inputfile> -o <outputfile>')
#             sys.exit()
#         elif opt in ("-i","--ifile"):
#             inputfile = arg
#         elif opt in ("-o","--ofile"):
#             outputfile = arg
#     print('输入的文件名为：',inputfile)
#     print('输出的文件名为：',outputfile)
#
# if __name__ == "__main__":
#     main(sys.argv[1:])

# 一段程序作为主线运行程序时其内置名称就是 __main__
# 自己的 __name__ 在自己用时就是 main，当自己作为模块被调用时就是自己的名字(脚本名)
# import hello
# print("自己的name：",__name__)
# print("引用的文件名：",hello.__name__)