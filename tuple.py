#! /usr/bin/python3

print("=========标准数据类型：Tuple（元组）==========")
# Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# tup1 = ('Google','Runoob',1997,2000)
# tup2 = (1, 2, 3, 4, 5)
# tup3 = "a", "b", "c", "d"    #不需要括号也可以  !!!!!!!!!
# print("打印type：",type(tup3))

print("=========Tuple（元组）:仅包含一个元素==========")
# 元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用
# tup1 = (50)
# print("打印type：",type(tup1))
# tup1 = (50,)
# print("打印type：",type(tup1))

print("=========Tuple（元组）：访问元组==========")
# 元组可以使用下标索引来访问元组中的值
# tup1 = ('Google','Runoob',1997,2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7)
# print("tup1[0]:",tup1[0])
# print("tup2[1:5]:",tup2[1:5])

print("=========Tuple（元组）：修改元组==========")
# 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
# tup1 = (12, 34.56)
# tup2 = ('abc', 'xyz')
# # 以下修改元组元素操作是非法的。  tup1[0] = 100  创建一个新的元组
# tup3 = tup1 + tup2
# print (tup3)

print("=========Tuple（元组）：删除元组==========")
# 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组
# tup = ('Google', 'Runoob', 1997, 2000)
# print(tup)
# del tup
# print("删除后的元组 tup : ", tup)

print("=========Tuple（元组）：元组运算符==========")
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
# tup1 = ('Google', 'Runoob', 1997, 2000)
# print("tup1:",tup1)
# print("len(tup1):",len(tup1))
# tup2 = (1, 2, 3, 4, 5, 6, 7)
# print("tup2:",tup2)
# print("tup1 + tup2:",tup1 + tup2)
# print("tup1 * 4:", tup1 * 4)

# if 3 in tup2:
#     print("3是否在tup2中：",True)
# else:
#     print("3是否在tup2中：",False)
# print(3 in tup2)

# for x in tup2:
#     print("迭代元组tup2：",x,)

print("=========Tuple（元组）：元组索引，截取==========")
# L = ('Google', 'Taobao', 'Runoob')
# print("读取第三个元素:",L[2])
# print("反向读取；读取倒数第二个元素:",L[-2])
# print("截取元素，从第二个开始后的所有元素。:",L[1:])

print("=========Tuple（元组）：元组内置函数==========")
# tuple1 = ('Google', 'Taobao', 'Runoob')
# list1 = ['Google', 'Taobao', 'Runoob']

# len(tuple)  计算元组元素个数。
# print(len(tuple1))

# max(tuple)  返回元组中元素最大值。
# print(max(tuple1))

# min(tuple)  返回元组中元素最小值。
# print(min(tuple1))

# tuple(seq) 将列表转换为元组。
# tup = tuple(list1)
# print(tup)




