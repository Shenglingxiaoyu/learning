#元组的创建
'''元组的第一种创建方式'''
t = ('yes','no','emmm',80)
print(t,type(t))

'''元组的第二种创建方式'''
t1 = tuple(('sdjhbrt','sjkebr','sjdkg',456))        #使用tuple函数创建元组
print(t1,type(t1))

'''元组的创建方式3'''
t2 = ('hsidrh',)           #若使用小括号创建元组，内只有一个元素的时候，需要加逗号，不然会认为是赋值
print(t2,type(t2))

'''空元组'''
t = ()

'''元组为不可变序列，不可以增加，减少，删改
不过，元组内的列表或字典是可以，增加，减少的'''
t3 = ('gseg',[20,30],'sdrgfs')
t3[1].append(50)
print(t3)

'''元组的索引，以及遍历'''
t4 = ('sdr','gsreg','sdtrd',6452)
print(t4[0])

for it in t4:
    print(it)