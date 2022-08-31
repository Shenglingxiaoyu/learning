for variable1 in 'Python':     #for in 循环（冒号注意) 意为将in后面的数据提出来
    print(variable1)   #意为将变量依此从python中取出
for variable2 in range(10):          #range范围的使用
    print(variable2)
for _ in range(5):                  #for后面加_且in后用range函数意为将结果输出多少次
    print('你好')

sum=0
for variable3 in range(1,101):
    if variable3%2==0:
        sum+=variable3
print(sum)



#else的用法
for _ in range(3):
    password = int(input('please import your password'))
    if password == 8888:
        print('password correct')

        break
    else:
        print('password wrong')
else:
    print('password wrong all')        #for in 循环与else的用法，循环结束后再执行else后的内容