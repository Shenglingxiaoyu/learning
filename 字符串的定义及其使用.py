'''字符串中的查询方法'''
a = 'hello,hello'
print(a.index('lo'))        #从开头寻找想要的数据，并返还所在的位置(如果没有找到就会报错)
print(a.rindex('lo'))       #从末尾寻找想要的数据，并返还所在的位置(如果没有找到就会报错)

print(a.find('lo'))         #从开头寻找所要的数据，并返还所在的位置(没有找到会返回-1)
print(a.rfind('lo'))        #从末尾寻找想要的数据，并返还所在的位置(没有找到会返回-1)

'''字符串的大小写转换'''
b = 'hello,world'
b1 = b.upper()        #将字符串中的所有字母变成大写
print(b1)

c = 'HELLO,WORLD'
c1 = c.lower()       #将字符串中的所有字母变成小写
print(c1)

d = 'HelLo,WoRld'
d1 = d.swapcase()    #将字符串中的所有大些变成小写，将小写全部变成大写
print(d1)

e = 'heLLO,WORld'
e1 = e.capitalize()  #将字符串中的打一个字母变成大写，其他全部小写
print(e1)

f = 'hELLO,wORLD'
f1 = f.title()       #将字符串中的每个单词的第一个字母变成大些，其他变成小写
print(f1)

'''字符串的内容对齐'''
#居中对齐
s = 'hello world'
s1 = s.center(20,'*')   #逗号前面的数字为填充的数量(从中间开始数，实际填充的格子为数字减去字符串的长度，若填充的数字小于字符串则返回原字符)，后面为填充的符合
print(s1)
s1s = s.center(20)            #后面不写就是默认对齐
print(s1s)

#左对齐
s2 = s.ljust(20,'*')
print(s2)

#后对齐
s3 = s.rjust(20,'*')
print(s3)

#用0填充右对齐
s4 = s.zfill(20)
print(s4)

'''字符串的劈分'''
variable = 'hello world python'
variable2 = 'hello|world|python'
result = variable.split()         #将字符串从中间某个位置分开，默认为空格，结果为列表
print(result)

result1 = variable2.split(sep='|',maxsplit=1)  #maxsplit意为分几段,split意为从左边劈分
print(result1)

result2 = variable2.rsplit(sep='|',maxsplit=1)    #rsplit意为从右边劈分
print(result2)


'''字符串的替换与合并'''
#字符串的替换
name = 'hello,world,python,java'
name1 = name.replace('hello','java')   #replace括号左边为被替换的字符，后边为替换的字符
print(name)

#将列表或元组的字符串合并成一个字符串
list = ['10','20','30']            #注意列表或元组里面必须是字符才可以
list_result = '|'.join(list)
print(list_result)
t = ('10','20','30')
t_result = '|'.join(t)
print(t_result)
list_branch_result = ''.join(list)
print(list_branch_result)

'''字符串的比较'''
#<,>,<=,>=,==,!=
print('apple'>'banana')    #先对比字符的第一位，在对比第二位，依次往后比较(比较的是ascll码)unicode的前128位就是ascll码

'''字符串的切片'''
w = 'hello,world,python'      #列表，字典都可以切片
w1 = w[:5]
print(w1)
w2 = w[12:]
print(w2)
w3 = w[6:11]
print(w3)

'''格式化字符串'''
name1 = '小宇'
age = 18
print('我叫%s,今年%i' % (name1,age))    #%s代表字符串(str),%i代表整数(int),%f代表小数(float)

print('我叫{0},今年{1}'.format(name1,age))

print(f'我叫{name1},今年{age}')         #python3.0以上的版本才可以这样操作

'''字符串的编码与解码'''
str1 = '我叫小宇'
str_1 = str1.encode(encoding='gbk')    #将字符串转化成二进制数字，不过gbk会显示16进制的数字
print(str_1)
str_2 = str_1.decode('gbk')
print(str_2)