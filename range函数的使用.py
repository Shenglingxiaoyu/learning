r=range(10)   #range函数的使用
print(r)              #单一数为‘stop’（从0开始）
print(list(r))        #数列里面有0，1，2，3，4，5，6，7，8，9但不包括10，右边为开区间。
a=range(1,10)         #（start,stop)指定开始
print(a)              #（1，10）
print(list(a))        #1.2.3.4.5.6.7.8.9
b=range(1,10,2)       #(start,stop,step)step为位差
print(b)              #(1,10,2)
print(list(b))        #1.3.5.7.9