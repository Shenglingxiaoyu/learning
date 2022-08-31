for _ in range(3):
    variable1 = int(input('请输入密码'))
    if variable1 == 8888:
        print('密码正确')
        break                     #break函数，截断，停止循环
    else:
        print('密码错误')