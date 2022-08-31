#集合的定义
'''集合就是一个没有value的字典，只有键，同样使用{}去定义'''

#集合的创建方式
'''创建方式1(使用大括号)'''
s = {10,20,30,10,20,30}  #有重复元素的时候，只会显示一次
print(s,type(s))

'''创建方式2(使用set函数)'''
#可以将一个数列范围变成集合
s1 = set(range(6))
print(s1,type(s1))

#可以将一个列表变成集合
s2 = set([1,2,3,4,5,6])
print(s2,type(s2))

#可以将元组变成集合
s3 = set((1,2,3,4,5,6))
print(s3,type(s3))

#可以将字典变成集合
s4 = set({'dfg':12,'dfd':20})      #只会显示key，不现实value
print(s4,type(s4))

#将字符串变成集合
s5 = set('python')
print(s5,type(s5))

#空集合的创建方式
#不能直接使用variable = {}去创建，直接这样使用是空字典
s6 = set()

'''集合为可变序列，有增删操作'''
#集合的增加
s7 = {10,20,30,40}
s7.add(500)           #add函数一次只能增加一个元素
print(s7)
s7.update([12,65,25,34,62])     #update函数一次至少增加一个函数，可增加多个，增加一个列表，字典，元组，集合等等
print(s7)

#集合的删改
s7.remove(65)            #一次移除一个元素，若元素不在集合内，则会报错
print(s7)
s7.discard(34)
s7.discard(500)
print(s7)               #一次移除一个元素，若元素不在集合内，也不会报错
s7.pop()               #随机移除一个元素，()内不可加元素
print(s7)              #虽然定义上是随机删除一个元素，但在ide环境里面总是删除最左边的元素
s7.clear()             #清空集合内的所有元素
print(s7)

'''集合的判定'''
print(10 in s7)
print(10 not in s7)

'''集合间的关系'''
s8 = {10,20,30,40,50}
s9 = {10,20,30}
s10 = {10,20,90}

print(s8==s9)
print(s8!=s9)

print(s9.issubset(s8))              #s9是s8的子集
print(s8.issuperset(s9))           #s8是s9的超集
print(s8.isdisjoint(s9))           #用于求两个集合是否有交集，isdisjoint为不相交的，若有交集则显示false
#此三种函数的结果都是布尔数值

print(s8.intersection(s9))         #intersection函数为求出集合的交集
print(s8 & s9)                    #与intersection一样的用法，都是求交集，简便方法

print(s8.union(s9))              #求两个集合的并集
print(s8 | s9)                   #简易写法是|都是求并集

print(s8.difference(s9))         #求差集
print(s8 - s9)

print(s10.symmetric_difference(s8))   #求对称差值，就是并集减去其交集
print(s10 ^ s8)
#此四种皆为输出值


'''集合生成式'''
set1 = {i*i for i in range(10)}
print(set1)                      #它是无序的