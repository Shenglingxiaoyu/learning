for i in range(10):       #嵌套循环
    for j in range(i+1):
        print(f'{i+1}','*',f'{j+1}','=',f'{(i+1)*(j+1)}',end='\t')       #很牛逼
    print()
