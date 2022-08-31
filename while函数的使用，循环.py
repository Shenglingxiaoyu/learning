variable1=0             #初始化变量
variable2=0
while variable1<10:      #条件判断
    variable2+=variable1         #条件执行
    variable1+=1                 #改变变量（如果没有改变变量，此条件就会一直运行下去‘小心电脑炸掉’）
    print(variable2)             #输出结果



a = 0
while a<3:
    password = int(input('import your password'))
    if password == 8888:
        print('password correct')
        break
    else:
        print('password wrong')
    a+=1
else:
    print('password wrong all')