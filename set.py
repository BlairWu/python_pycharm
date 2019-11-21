#! /usr/bin/python3
# 集合（set）是一个无序的不重复元素序列。
# 可以使用大括号 { } 或者 set() 函数创建集合，
# 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
# 创建格式：
# parame = {value01,value02,...}
# 或者
# set(value)

print("=========Set（集合）:创建集合==========")
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print("basket：", basket)
# if 'orange' in basket:
#     print("'orange' in basket")
# else:
#     print("'orange' not in basket")
#
# if 'crabgrass' in basket:
#     print("'crabgrass' in basket")
# else:
#     print("'crabgrass' not in basket")
#
# for x in basket:
#     print("打印集合basket值 %s " % x)

# a = set('abracadabra')
# print('a %s' % a)   # 无序的不重复元素序列
# b = set('alacazam')
# print('b %s' % b)   # 无序的不重复元素序列
# print('集合a包含、集合b不包含的元素：a - b =', a-b)
# print('集合a或集合b中包含的所有元素：a | b =', a|b)
# print('集合a和集合b中都包含了的元素：a & b =', a&b)
# print('不同时包含于集合a、集合b的元素：a ^ b =', a^b)

print("=========Set（集合）:添加元素 s.add( x )、s.update( x ) ==========")
# thisset = set (("Google","Runoob","Taobao"))
# # thisset.add("Facebook")
# # print(thisset)
# thisset.update({"a",3})
# print(thisset)
# thisset.update([1,4],[5,6])  # 参数可以是列表，元组，字典等
# print(thisset)

# 已存在的元素，则不执行添加操作
# fruits = {"apple", "banana", "cherry"}
# fruits.add("apple")
# print(fruits)

print("=========Set（集合）:移除元素 s.remove( x )、s.discard( x )、s.pop() ==========")
# thisset = set (("Google","Runoob","Taobao"))

# thisset.remove("Taobao")
# print(thisset)

# thisset.remove("Facebook")   # 不存在会发生错误
# print(thisset)

# thisset.discard("Facebook")   # 不存在不会发生错误
# print(thisset)

# thisset.add("Facebook")
# thisset.pop()   # 随机删除
# print(thisset)

print("=========Set（集合）:计算集合元素个数 len(s)==========")
# thisset = set (("Google","Runoob","Taobao"))
# x = len(thisset)
# print(x)

print("=========Set（集合）:清空集合 s.clear()==========")
# thisset = set (("Google","Runoob","Taobao"))
# thisset.clear()
# print(thisset)

print("=========Set（集合）:判断元素是否在集合中存在==========")
# thisset = set (("Google","Runoob","Taobao"))
# if "Google" in thisset:
#     print(True)
# else:
#     print(False)

print("=========Set（集合）:集合内置方法完整列表==========")
# .copy() 拷贝集合
# thisset = set (("Google","Runoob","Taobao"))
# x = thisset.copy()
# print(x)



# difference_update() 方法与 difference() 方法的区别在于
# difference() 方法返回一个移除相同元素的新集合，
# difference_update() 方法是直接在原来的集合中移除元素，没有返回值。
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# .difference() 差集，返回多个集合的差集
# z = x.difference(y)
# print(z)
# .difference_update() 差集，移除集合中的元素，该元素在指定的集合也存在。
# x.difference_update(y)
# print(x)

# .intersection(set1, set2 ... etc) 方法用于返回两个或更多集合中都包含的元素，即交集。
# z = x.intersection(y)
# print(z)
# x.intersection_update(y)
# print(x)

# .sdisjoint() 方法用于判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "facebook"}
# z = x.isdisjoint(y)
# print(z)

# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# # .issubset() 方法用于判断集合的所有元素是否都包含在指定集合中，如果是则返回 True，否则返回 False。
# # 判断指定集合是否为该方法参数集合的子集。
# z = x.issubset(y)
# print(z)
# # .issuperset() 方法用于判断指定集合的所有元素是否都包含在原始的集合中，如果是则返回 True，否则返回 False。
# # 判断该方法的参数集合是否为指定集合的子集
# z = x.issuperset(y)
# print(z)

# x = {"apple", "banana", "cherry"}
# y = {"google", "runoob", "apple"}
# .symmetric_difference() 方法返回两个集合中不重复的元素集合，即会移除两个集合中都存在的元素。
# .symmetric_difference_update()移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
# z = x.symmetric_difference(y)
# print(z)
# x.symmetric_difference_update(y)
# print(x)
# .union() 方法返回两个集合的并集，即包含了所有集合的元素，重复的元素只会出现一次。 并集
# z = x.union(y)
# print(z)

# 合并多个集合
x = {"a", "b", "c"}
y = {"f", "d", "a"}
z = {"c", "d", "e"}
result = x.union(y, z)
print(result)