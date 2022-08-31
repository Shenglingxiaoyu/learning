def cale(a,b):            #a,b为形参，形式参数，用来自定义想要的函数
    c=a+b
    return c              #return后面的形参就是这个函数最后所得到的结果

result = cale(10,20)     #这个地方的10，20为实参，实际参数，意为所调用的参数
print(result)

res = cale(b=10,a=20)    #也可以自定义实参的所赋予的形参
print(res)

def fun(age1,age2):
    print('age1',age1)
    print('age2',age2)
    age1=100
    age2.append(200)
    print('age1',age1)
    print('age2',age2)
    #return               这个地方因为没有结果返回，所以不屑return

n1 = 10
n2 = [10,20,30]             #在函数的调用过程中，不可变的数据，在函数调用后不会改变原有赋予其变量的值
fun(n1,n2)
print('n1',n1)
print('n2',n2)

'''函数的返回值'''
def fun1(variable1):
    list1 = []
    list2 = []
    for it in variable1:
        if it%2:
            list1.append(it)
        else:
            list2.append(it)
    return list1,list2
list = [1,2,3,4,5,6,7,8,9,10]
res1 = fun1(list)
print(res1)

'''个数可变的位置形参'''
def fun2(*age1):    #没有加星号的情况下，形参只有一个，实参也只能有一个
    print(age1)
#fun2(10,20)        这用会报错
fun2(10,20)      #会生成元组

def fun3(**age1):      #可变的关键字形参
    print(age1)
fun3(a=10,b=20)         #会形成一个字典