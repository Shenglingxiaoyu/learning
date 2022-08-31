def fun(a,b):
    c=a+b
    return c
'''print(c)会报错因为c为局部变量，不能再函数的外面调用'''

name = '小宇'
def fun1():
    print(name)
fun1()    #name为全局变量，在函数里面也可以使用

def fun2():
    global age        #在函数里面对变量的前面加个global就可以变成全局变量
    age = 18
    print(age)
fun2()
print(age)

d = 10
def fun3():
    d = 20
    #print(d)
    def fun4():      #函数的函数里面使用global改变变量也会变成全局变量，所以想要在外一层改变变量使用nonlocal
        nonlocal d
        d = 30
    fun4()
    print(d)
fun3()




'''递归函数'''#在函数里面调用函数
def function(n):           #计算数字的阶乘
    if n == 1:
        return 1
    else:
        return n*function(n-1)
print(function(8))

