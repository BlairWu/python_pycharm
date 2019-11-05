#! /usr/bin/python3

print("************访问列表list中的值*************")
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符

# list1 = ['Google','Runoob',1997,2000]
# list2 = [1,2,3,4,5,6,7]
# print("使用下标索引来访问列表中的值 list1[0]:",list1[0])
# print("使用方括号的形式截取字符 list2[1:5]:",list2[2:5])

print("************更新列表list*************")
# 你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项

# list = ['Google','Runoob',1997,2000]
# print("第三个元素为：",list[2])
# list[2] = 2001
# print("更新后第三个元素为：",list[2])

print("************删除列表list元素*************")
# 使用 del 语句来删除列表的的元素

# list = ['Google','Runoob',1997,2000]
# print("原始列表：",list)
# del list[2]
# print("删除第三个元素为：",list)

print("************列表list脚本操作符*************")
# 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
# Python                               表达式	结果 	                    描述
# len([1, 2, 3])	                             3	                       长度
# [1, 2, 3] + [4, 5, 6]	           [1, 2, 3, 4, 5, 6]	               组合
# ['Hi!'] * 4	                      ['Hi!', 'Hi!', 'Hi!', 'Hi!']      	重复
# 3 in [1, 2, 3]                           	True                元素是否存在于列表中
# for x in [1, 2, 3]: print(x, end=" ")      	1 2 3                   	迭代

# list = ['Google','Runoob',1997,2000]
# print("list长度：",len(list))
# sublist = [1995,'xwwu']
# print("list组合：",list+sublist)
# print("list重复：",list*3)
# print("'95'是否存在于list中：",95 in list)
# print("'95'是否存在于sublist中：",95 in sublist)
# print("迭代输出list：")
# for x in list:
#     print(x,end=" * ")

print("************列表list截取与拼接*************")
# L=['Google', 'Runoob', 'Taobao']
# Python表达式	    结果                	描述
# L[2]	           'Taobao'	                读取第三个元素
# L[-2]	           'Runoob'	                 从右侧开始读取倒数第二个元素: count from the right
# L[1:]	            ['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素

L=['Google', 'Runoob', 'Taobao']
print("打印列表L",L)
print("读取第三个元素",L[2])
print("从右侧开始读取倒数第二个元素",L[-2])
print("输出从第二个元素开始后的所有元素",L[1:])

squares = [1, 4, 9, 16, 25]
print("原始列表：",squares)
squares += [36, 49, 64, 81, 100]
print("拼接后列表：",squares)
















