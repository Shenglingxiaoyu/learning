for _ in range(3):
    password = int(input('输入密码'))

    if password == 258369:
        print('密码正确')

        variable1 = 100000
        variable2 = input('存款/取款')

        if variable2 == '存款':
            variable3=int(input('请输入存款金额'))
            print('存款成功，余额为',variable1+variable3)

        elif variable2 == '取款':
            variable4 = range(100,1001,300)
            print(f'请选择以下取款金额{list(variable4)}')

            variable5 = int(input('请输入取款金额'))

            if variable5 in variable4:
                print('取款成功，余额为',variable1-variable5)
            else:
                print('不好意思，你输入的取款金额有误(\'.\')')

        break

    else:
        if _ == 0:
            print('密码错误，请再次输入密码')

        if _ == 1:
            print('密码错误，剩余密码输入次数为1')

        if _ == 2:
            print('密码错误，密码输入次数超过三次，账号已被封锁')





