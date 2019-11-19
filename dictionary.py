#! /usr/bin/python3
# 字典是另一种可变容器模型，且可存储任意类型对象。
# 字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
# d = {key1 : value1, key2 : value2 }
# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# 也可如此创建字典
# dict1 = { 'abc': 456 }
# dict2 = { 'abc': 123, 98.6: 37 }

print("=========Dictionary（字典）:访问字典里的值==========")
# 把相应的键放入到方括号中
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ", dict['Age'])
# print("dict['Class']:",dict['Class'])
# 如果用字典里没有的键访问数据，会报错
# print("dict[Class]:",dict[Class])

print("=========Dictionary（字典）:修改字典==========")
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8   # 更新Age
# dict['School'] = "菜鸟教程"  # 添加信息
# print("dic['Age']:", dict['Age'])
# print("dict['School']:", dict['School'])
# print("dict[]:", dict)

print("=========Dictionary（字典）:删除字典元素==========")
# 能删单一的元素也能清空字典，清空只需一项操作。显示删除一个字典用del命令
# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
# del  dict['Name'] # 删除键'Name'
# print("del dict:", dict)
# dict.clear()   #清空字典
# print("dict.clear:", dict)
# del dict     #删除字典
# print("del dict:", dict)
# # print("dic['Age']:", dict['Age'])
# # print("dict['School']:", dict['School'])

print("=========Dictionary（字典）:字典键的特性==========")
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
# 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
# print("dict['Name']: ", dict['Name'])
# # dict = {['Name']: 'Runoob', 'Age': 7}
# print ("dict['Name']: ", dict['Name'])

print("=========Dictionary（字典）:字典内置函数==========")
# dict = {'Name': 'Runoob', 'Sex': 'male', 'Age': '7', 'Class': 'First'}
# print("len(dict)):", len(dict))   # 计算字典元素个数，即键的总数。
# print("dict:", dict)
# print("str(dict)):", str(dict))   # 输出字典，以可打印的字符串表示。
# print("type(dict):", type(dict))   # 返回输入的变量类型

print("=========Dictionary（字典）:字典内置方法==========")
# 1 .clear
# dict = {'Name': 'Runoob', 'Sex': 'male', 'Age': '7', 'Class': 'First'}
# print("字典长度 randiansdict.len：",len(dict))
# dict.clear()
# print("删除字典内所有元素 randiansdict.clear：",len(dict))

# 2 .copy
# dict = {'Name': 'Runoob', 'Sex': 'male', 'Age': '7', 'Class': 'First'}
# dict2 = dict.copy()
# print("新复制的字典 randiansdict.copy：",dict2)

# 3 .fromkeys
# 原文
# seq = ('name', 'age', 'sex')
# dict = dict.fromkeys(seq)   # seq -- 字典键值列表
# print ("新的字典为 : %s" %  str(dict))
# dict = dict.fromkeys(seq, 10)
# print ("新的字典为 : %s" %  str(dict))
# x = ('key1', 'key2', 'key3')
# thisdict = dict.fromkeys(x)
# print(thisdict)
# # 自定义
# dict1 = dict.fromkeys(seq)
# print("新的字典为：",str(dict1))
# dict1 = dict.fromkeys(seq,10)
# print("新的字典为：",str(dict1))

# 4 .get 返回指定键的值，如果值不在字典中返回default值
# dict = {'Name': 'Runoob', 'Age': 27}
# print("字典为： %s" % dict)
# print("Age 值为 ： %s" % dict.get('Age'))
# print("Age 值为 ： %s" % dict.get('Sex'))
# print("Age 值为 ： %s" % dict.get('Sex', 'NA'))
# print("新字典为： %s" % dict)

# 8 .setdefault 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
# dict = {'Name': 'Runoob', 'Age': 7}
# print("字典为： %s" % dict)
# print("Age 键的值为： %s" % dict.setdefault('Age', None))
# print("Sex 键的值为： %s" % dict.setdefault('Sex', None))
# print("新字典为： %s" % dict)

# 5 key in dict
# dict = {'Name': 'Runoob', 'Age': 7}
# if 'Age' in dict:
#     print("键 Age 存在")
# else:
#     print("键 Age 不存在")
# if 'Sex' not in dict:
#     print("键 Sex 不存在")
# else:
#     print("键 Sex 存在")

# 6 .items() 遍历的(键, 值) 元组数组
# dict = {'Name': 'Runoob', 'Age': 7}
# print("Dict Value : %s"%dict.items())
# result = []
# for i,j in dict.items():
#     result.append(i)
#     result.append(j)
# print("List value: %s"%result)
# for i,j in dict.items():
#     print(i, ":\t", j)

# 7 .keys
# dict1 = {'Name': 'Runoob', 'Age': 7}
# print("dict1.keys(): ", dict1.keys())    # 调用keys方法
# print("list(dict1.keys()): ", list(dict1.keys()))   # 转换为列表

# 9 .update() 在字典末尾追加到字典，更新字典
# dict1 = {'Name': 'Runoob', 'Age': 7}
# print("初始dict1: %s" % dict1)
# dict2 = {'Sex': 'female' }
# print("初始dict2: %s" % dict2)
# dict1.update(dict2)
# print("更新dict1: %s" % dict1)

# 10 .values() 获取字典键值
# dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
# print ("字典所有值(dict)为 : ",  dict.values())
# print ("字典所有值(list)为 : ",  list(dict.values()))

# 11 .pop 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# print("原site：",site)
# pop_obj1 = site.pop('name','Default')
# print("pop_obj1，删除键'name'，键值为：",pop_obj1)
# print("site：",site)
# print()
# pop_obj2 = site.pop('website','NA')
# print("pop_obj2，删除键'website'，不存在返回'NA'：",pop_obj2)
# print("site：",site)
# print()
# pop_obj3 = site.pop('alexa','Default')
# print("pop_obj3，删除键'alexa'，键值为：",pop_obj3)
# print("site：",site)
# print()

# 12 .popitem 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。按照 LIFO（Last In First Out 后进先出法） 顺序规则
#             如果字典已经为空，却调用了此方法，就报出KeyError异常。
# site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
# print("原site：", site)
# pop_obj0 = site.popitem()
# print("采用.popitem()删除的末尾的键值对：", pop_obj0)
# print("采用.popitem()删除的末尾的键值对后的site：", site)
# print()
# pop_obj1 = site.popitem()
# print("采用.popitem()删除的末尾的键值对：", pop_obj1)
# print("采用.popitem()删除的末尾的键值对后的site：", site)
# print()
# pop_obj2 = site.popitem()
# print("采用.popitem()删除的末尾的键值对：", pop_obj2)
# print("采用.popitem()删除的末尾的键值对后的site：", site)