answer=input('请问你是否为会员，yes或no')              #嵌套分支结构
if answer=='yes':
    money = float(input('请输入购物金额'))

    if money>=200:
        print('你是会员，打八折，付款金额为：',money*0.8)
    elif money>=100 and money<200:
        print('你是会员，打九折，付款金额为：',money*0.9)
    elif money<=0:
        print('你的输入有误')
    else:
        print('你是会员，你的付款金额为：',money)

elif answer=='no':

    money = float(input('请输入购物金额'))

    if money>=300:
        print('你不是会员，但购物金额超过300，打9.5折，你的付款金额为：',money*0.95)
    elif money>0 and money<=300:
        print('你不是会员，你的付款金额为：',money)
    else:
        print('你的输入有误')

elif answer!='yes' or 'no':

    print('你的输入有误(\'.\')')