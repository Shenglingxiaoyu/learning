money=10000#单分支结构
money=float(money)
variable2=float(input('输入取款金额'))
if money>=variable2:
    money-=variable2
    print('余额：',money)