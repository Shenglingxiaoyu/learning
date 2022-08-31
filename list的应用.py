#列表的应用(将多个元素存储到一个对象中）空列表也需使用内存id
lst = [] #此为空列表，可在此中填入多个元素          []为列表
lst1 = ['yes','mge','85']
lst2 = list(['no','sdf','466'])
print(lst1.index('yes'))                  #index函数为索引，可以寻找列表中元素所在在位置
print(lst1.index('mge',0,3))              #可以在特定范围内寻找其元素所在的位置(同样为左闭右开)
print(lst1[2])                      #可以指定索引位置，显示其值[]里写索引位置
print(lst1[1:3:1])              #将原列表进行一个拷贝在输出，(同样左闭右开)（start.stop,step)
print('yes' in lst1)
print('yes' not in lst2)
for it in lst1:
    print(it)

#列表的添加
lst.append(10)           #在数列的末尾添加"一"个元素(此元素可以是另一个列表)则输出结果会包含整个列表   比如lst.append(lst1)
lst.extend(lst1)       #在数量的末尾添加至少一个元素，可以是多个(如果是添加列表则会添加另一个列表里面的元素) 比如lst.extend(lst1)
print(lst)
lst.insert(1,'no')            #在指定位置添加元素
lst4 = ['sd','sdg','sdgt',456,123,4563,87895,125]
lst[1:] = lst4        #切片，将指定位置的元素直接替换

#列表的删除
list1 = [2345,1354,53,123,475,1455,45358]
list1.remove(2345)           #删除一个想要删除的元素
list1.pop(1)            #删除指定索引的元素
list1.pop()            #删除列表最后的一个元素
print(list1)
new_list = list1[1:3]                   #填索引的时候中间必须是冒号，不能是逗号
list1[1:3] = []             #不新建新的列表对象，删除东西
list1.clear()               #删除列表里面的所有东西
del list1                   #直接将删除列表

#列表的修改
list2 = [543,895,231564,27,465,1,56431,54612,246123,345,5443]
list2[2]=2000           #在指定位置修改内容
print(list2)
list2[1:3] = [225,134,15050]
print(list2)         #同样可以用切片进行替换

#列表的排序
list3 = [10,1345,1234,3120,243,10,54,5545]
list3.sort()             #将原列表从小到大排序好，不产生新的序列
print(list3)
list3.sort(reverse=True)
print(list3)             #将列表从大到小排序好，不产生新的列表
new_list1 = sorted(list3)   #从小到大排序好，产生新的列表对象
print(new_list1)
new_list2 = sorted(list3,reverse=True)
print(new_list2)           #从大到小排序好，产生新的列表对象

#列表生成式
list4 = [i for i in range(1,10,1)]   #产生一个1-9的序列   for前面的i为元素表达式，为真正的输出列表的数据
print(list4)
list5 = [i*2 for i in range(1,10,1)]  #将列表*2
print(list5)
