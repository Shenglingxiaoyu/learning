'''python异常机制的处理'''     #此解决的是程序运行时会犯的错误
#try except的使用

try:                                   #程序的运行
    a = int(input('请输入第一个数字'))
    b = int(input('请输入第二个数字'))
    result = a/b
    #print(result)
except ZeroDivisionError:             #程序出错时所运行的代码，其中错误类型可以有多个，except也可以有多个
    print('对不起，你的输入有误')
else:
    print(result)                   #程序没出错时所运行的代码，使用else必须要有except，不然就不需要else直接运行try不是更方便
finally:
    print('谢谢你的使用')          #程序出没出错都会运行的代码