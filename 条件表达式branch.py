age=(input('请输入你的年龄'))
if age:                            #age:可以单为条件，age加冒号表示条件ture，else:表示false.
    print(age)
else:
    print('你的年龄为'+age)
print(age if age else '你的年龄为'+age)