money=10000#双分支结构
money=float(money)
variable1=float(input('输入取款金额'))
if money>=variable1:       #注意if写完条件后需要加：
    money-=variable1
    print('余额',money)
else:                       #双分支结构,条件要么够,要么不够,ture and false:布尔类型bool
    print('余额不足')