class MyError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):         #如果不修改__str__将会返回一个对象的形式
        return repr(self.value)

try:
    num = input('请输入一个正数')
    if not num.isdigit():
        raise MyError(num)
except MyError as e:
    print('请输入数字，你输入的是',e.value)