#字典与列表的区别  字典的元素是一个键值对，key:value,前面的key是相当于一个索引
# value就是此索引的值，在字典中利用哈希函数计算key在字典中的位置，从而取到值。
'''字典为不可变序列，因为值与值之间需要用哈希函数取计算，每一个值都是唯一的，不可随意变动，键与键之间不是排序的'''
'''列表的索引[0,1,2,3,4,5...]
字典的索引可以自定义，name，age，high...'''


'''字典的创建第一种方法(利用花括号)'''
variable = {'key1':10,'key2':20,'key3':30}         #花括号简单快捷(注意索引需要加上引号与值之间采用冒号间隔)
print(variable)

'''字典的创建第二种方法(利用dict函数)'''
variable2 = dict(name="hanxiaoyu",age=18)          #dict函数(索引不加引号与值才开等号间隔)
print(variable2)


'''字典的元素查找'''
print(variable['key1'])          #第一种方法 中括号里输入键
'''如果字典中不存在其键，就会报错'''

print(variable.get('key1'))      #第二种方法 get函数，(都要注意，查找的是键，输出的是值)
'''如果字典中不存在其键，就会输入None'''

print(variable.get('key4',90))  #get函数的好处就是，不存在的键可以自定义内容

#key值得判断
print('key1' in variable)
print('key2' not in variable)

#key值的增加与删改              key使用[]括起来
del variable['key1']         #删掉key1的值
'''variable.clear()删掉字典里的所有元素'''
print(variable)
variable['key1']=100      #元素的增加
print(variable)

'''元素的修改'''
variable['key2']=200      #元素的增加与元素的修改一样
print(variable)


'''获取字典的视图'''
variable3 = {'name':10,'name1':20,'name3':30}
#获取字典中的所有key
keys = variable3.keys()
print(keys)
list_keys = list(keys)      #可将获取出来的键变成列表
print(list_keys)
#获取字典中所有的value
values = variable3.values()
print(values)
list_values = list(values)
print(list_values)
#获取字典中多有的key-value对
items = variable3.items()
print(items)
list_items = list(items)
print(list_items)


'''字典的遍历'''
variable4 = {'you':'yes','me':'no','he':'no'}     #key值不能重复，但value可以重复
for it in variable4:
    print(it)     #直接写it将输出key
    print(variable4[it])    #便可输出所有的key的值


'''字典生成式'''
#将两个列表组合成一个字典
list1 = ['lst1','lst2','lst3']
list2 = [10,20,30]
itt = { list_1.upper():list_2 for list_1,list_2 in zip(list1,list2)}     #upper可以把字母变大写
print(itt)
