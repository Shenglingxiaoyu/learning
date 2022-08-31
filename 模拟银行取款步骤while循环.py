a=0
while a<=3:

    password = int(input('输入密码'))
    if password == 258369:
       print('密码正确')

       variable1 = 100000
       variable2 = input('存款/取款')

       if variable2 == '存款':
           variable3 = int(input('请输入存款金额'))
           print('存款成功，余额为：', variable1 + variable3)

       elif variable2 == '取款':
           variable = range(100, 1001, 300)
           print('请选择以下取款金额', list(variable))

           variable4 = int(input('请选择取款金额'))

           if variable4 in variable:
               print('取款成功,余额为：', variable1 - variable4)

           else:
               print('不好意思，你输入的取款金额有误(\'.\')')

           break


    elif password!=258369:
        if a == 0:
            print('密码错误,请再次输入密码')
        if a == 1:
            print('密码错误，剩余输入密码次数：1')
        if a == 2:
            print('密码错误,错误超过三次,账户已被封锁')

            break

    a+=1