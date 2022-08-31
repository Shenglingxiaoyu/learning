for _ in range(3):                    #相当于循环次数
    password=int(input('请输入密码'))
    if password==8888:
        print('密码正确')
        break                       #截至不再往后循环
    else:
        print('密码错误')