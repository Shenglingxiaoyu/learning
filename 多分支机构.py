variable1=int(input('输入一个成绩'))            #多分支结构
if variable1>=90 and variable1<=100:
    print('你的等级为A')
elif variable1>=80 and variable1<90:
    print('你的等级为B')
elif variable1>=70 and variable1<80:
    print('你的等级为C')
elif variable1>=60 and variable1<70:
    print('你的等级为D')
elif variable1>=0 and variable1<60:
    print('你的等级为E,不及格')
else:
    print('对不起，你的成绩有误''\'.\'')