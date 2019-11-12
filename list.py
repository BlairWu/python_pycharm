#! /usr/bin/python3

print("************访问 列表list 中的值*************")
# 使用下标索引来访问列表中的值，同样你也可以使用方括号的形式截取字符

# list1 = ['Google','Runoob',1997,2000]
# list2 = [1,2,3,4,5,6,7]
# print("使用下标索引来访问列表中的值 list1[0]:",list1[0])
# print("使用方括号的形式截取字符 list2[1:5]:",list2[2:5])

print("************更新 列表list*************")
# 你可以对列表的数据项进行修改或更新，你也可以使用append()方法来添加列表项

# list = ['Google','Runoob',1997,2000]
# print("第三个元素为：",list[2])
# list[2] = 2001
# print("更新后第三个元素为：",list[2])

print("************删除 列表list 元素*************")
# 使用 del 语句来删除列表的的元素

# list = ['Google','Runoob',1997,2000]
# print("原始列表：",list)
# del list[2]
# print("删除第三个元素为：",list)

print("************列表list 脚本操作符*************")
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

print("************列表list 截取与拼接*************")
# L=['Google', 'Runoob', 'Taobao']
# Python表达式	    结果                	描述
# L[2]	           'Taobao'	                读取第三个元素
# L[-2]	           'Runoob'	                 从右侧开始读取倒数第二个元素: count from the right
# L[1:]	            ['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素

# L=['Google', 'Runoob', 'Taobao']
# print("打印列表L",L)
# print("读取第三个元素",L[2])
# print("从右侧开始读取倒数第二个元素",L[-2])
# print("输出从第二个元素开始后的所有元素",L[1:])
# squares = [1, 4, 9, 16, 25]
# print("原始列表：",squares)
# squares += [36, 49, 64, 81, 100]
# print("拼接后列表：",squares)

print("************嵌套 列表list*************")
# 使用嵌套列表即在列表里创建其它列表
# a = ['a','b','c']
# n = [1,2,3]
# x = [a,n]
# print(x)
# print(x[0])
# print(a[0])
# print(x[0][0])
# print(a[1])
# print(x[0][1])
# print(a[2])
# print(x[0][2])


print("************ 列表list 函数&方法 *************")
print("************ 列表list 函数:len、max、min、list *************")
# 当其中的元素全部为字符串类型(string)时，则比较的是每个字符串元素的第一个字符的 ASCII 的大小。如果列表或者元组中的元素为数字类型和字符串类型混杂时，则无法比较。
# name = ['吴','秀','文']
# print(len(name))
# print(max(name))
# print(min(name))
# print(list(name))

# list() 方法用于将元组或字符串转换为列表。注：元组与列表是非常类似的，区别在于元组的元素值不能修改，元组是放在括号中，列表是放于方括号中。
# aTuple = (123, 'Google', 'Runoob', 'Taobao')
# list1 = list(aTuple)
# print ("列表元素 : ", list1)
# tuple = ('wuxiuwen',"吴秀文")
# print(list(tuple))
# str="Hello World"
# list2=list(str)
# print ("列表元素 : ", list2)
# name1 = "吴秀文"
# print(list(name1))
# name2 = "wuxiuwen"
# print(list(name2))


print("************列表list 方法*************")
# 1.list.append(obj) 在列表末尾添加新的对象
# list1 = ['Google', 'Runoob', 'Taobao']
# list1.append('Baidu')
# print ("更新后的列表 : ", list1)

# 2.list.count(obj) 统计某个元素在列表中出现的次数
# list1 = [123,'Google', 'Runoob', 'Taobao',123]
# print("123 元素个数",list1.count(123))

# 3.list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） 该方法没有返回值，但会在已存在的列表中添加新的列表内容。
# list1 = ['Google', 'Runoob', 'Taobao']
# list2=list(range(5)) # 创建 0-4 的列表
# list1.extend(list2)  # 扩展列表
# print ("扩展后的列表：", list1)
# language = ['French', 'English', 'German']  # 语言列表
# print('                      初始列表: ', language)
# language_tuple = ('Spanish', 'Portuguese')  # 元组
# language_set = {'Chinese', 'Japanese'}   # 集合
# language.extend(language_tuple)
# print('添加元组元素到列表末尾 的新列表: ', language)
# language.extend(language_set)
# print('添加集合元素到列表末尾 的新列表: ', language)

# 4.list.index(obj) 从列表中找出某个值第一个匹配项的索引位置  该方法返回查找对象的索引位置，如果没有找到对象则抛出异常
# list1 = ['Google', 'Runoob', 'Taobao']
# print ('Google 第一个索引值为:', list1.index('Google'))
# print ('Runoob 第一个索引值为:', list1.index('Runoob'))
# print ('Taobao 第一个索引值为:', list1.index('Taobao'))
# list1 = ['Google', 'Runoob', 'Taobao', 'Google', 'Runoob', 'Taobao']
# list.index(x[, start[, end]])
# print('Google 索引值为:', list1.index('Google', 1, 5))

# 5.list.insert(index,obj) 将对象插入列表
# list1 = ['Google', 'Runoob', 'Taobao']
# print ('            原列表 : ', list1)
# list1.insert(1, 'Baidu')
# print ('列表[1]插入元素后为 : ', list1)
# list1.insert(0, 'wuxiuwen')
# print ('列表[0]插入元素后为 : ', list1)

# 6.list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值）
# list1 = ['Google', 'Runoob', 'Taobao']
# print("               原列表：", list1)
# list1.pop(1)
# print("     移除列表第2个元素：", list1)
# list1 = ['Google', 'Runoob', 'Taobao']
# list1.pop()
# print("移除列表末尾第一个元素：", list1)
# list1.pop(0)
# print("    移除列表第一个元素：", list1)

# 7.list.remove(obj) 移除列表中某个值的第一个匹配项
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# list1.remove('Taobao')
# print("移除列表中的元素'Tabobao'", list1)

# 8.list.reverse() 反向列表中元素
# list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
# print("    原列表：", list1)
# list1.reverse()
# print("反转原列表：", list1)

# 9.list.sort(key=None,reverse=False) 对元列表进行排序，首字母ASCII码
# key - - 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse - - 排序规则，reverse = True 降序， reverse = False 升序（默认）。
# aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
# print("    原列表：", aList)
# aList.sort()
# print("对列表排序：", aList)
# list1 = [3, 4, 1, 2, 5, 6, 0, 7, 9, 8]
# print("       原列表：", list1)
# list1.sort(reverse=False)
# print("对列表元素排序：", list1)
# list1.sort(reverse=True)
# print("对列表元素倒序：", list1)

# 获取列表的第二个元素
# def takeSecond(elem):
#     return  elem[1]
# # 列表
# random = [(2,2),(3,4),(4,1),(1,3)]
# # 指定第二个元素排序
# random.sort(key=takeSecond)     # error  random.sort(key=takeSecond())
# # 输出类别
# print('排序列表：',random)

# 10.list.clear() 清空列表
# aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
# aList.clear()
# print("清空列表后：",aList)

# 11.list.copy() 函数用于复制列表，类似于 a[:]
# aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
# bList = aList.copy()
# print("拷贝列表aList：",bList)

















