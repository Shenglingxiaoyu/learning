# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
fp=3.1415926
print(fp,type(fp))
name='小宇'
age=18
print(type(name),type(age))
print('我叫'+name+',''今年'+str(age)+'岁.')#若内容为str则+为连接，int为相加
one=50
one+=50
print(one)#赋值运算符+=，-=，*=，/=
print(4&8)#二进制中对应数都为1就为1，否则为0
print(4|8)#二进制中对应数都为0就为0，否则为1
print(4<<1)#二进制中数位向左移一位，相当于值*2，<<的右边为左移的位数
print(4>>1)#二进制中数位向右移一位，相当于值/2，>>的右边为右移的位数
print(2>1)#比较运算符，结果为布尔数值，<,>,<=,>=,==(注意单=为赋值，==为比较），!=为不等于
#(==比较value,is ,is not比较id（在内存中的id))
a=1
b=2
print(a==1 and b==2)#布尔运算符and,or,not,in,not in/true
#字符串前加f的用法
name = '小宇'
print(f'我的名字是{name}')           #字符串前的f可让后面的字符串配合大括号输入并使用变量
print()                       #里面不加内容表示换行
print(eval('1+2'))      #eval的作用使将字符串变成python语句(就是将字符串的两个“”删掉)
print(repr(1+2))        #repr的作用就是将对象转化成字符串的形式

'''s="物品\t单价\t数量\n包子\t1\t2"
print(s)
print(repr(s))
运行结果：
物品    单价    数量
包子    1       2   
'物品\t单价\t数量\n包子\t1\t2'''

