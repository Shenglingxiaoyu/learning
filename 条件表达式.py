number1=int(input('请输入第一个整数'))   #条件表达式
number2=int(input('请输入第二个整数'))
print('true' if number1>=number2 else 'flase')   #else后不用加：
print(str(number1)+'大于等于'+str(number2) if number1>=number2 else str(number1)+'小于'+str(number2)) #条件表达式，条件的后面不用加:
#条件表达式    if else的简写（输出结果ture and false）