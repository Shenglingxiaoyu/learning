'''类与对象的定义'''
class Student:       #class后面为类的名称
    native_place = '小宇'      #此为类的属性(就相当于一个变量赋予了值，不过在所有所创建的对象都有这个变量)

    #初始化方法
    def __init__(self,name,age):           #self的目的是定义哪一个对象，因为一个类可以创建多个对象
        self.name = name
        self.age = age

    #实例方法
    def eat(self):
        print('学生在吃饭')

    #静态方法
    @staticmethod
    def method():
        print('我是用了staticmethod')

    #类方法
    @classmethod
    def cm(cls):
        print('使用了classmethod进行修饰，所以为类方法')

    __brand = '韩小宇'                   #Python中如果该属性不希望在类对象的外部被访问，则在使用前加两个__

    def new(self):
        print(self.__brand)




'''对象的创建'''
stu1 = Student('小宇','18')
#实例方法的调用
stu1.eat()
Student.eat(stu1)          #都是调用类里面的eat方法
print(stu1.name)
print(stu1.age)

print('----------------------------------')

'''类属性的使用方式'''
print(Student.native_place)
#对象继承了类的所有属性(类所有的属性，对象也一定会有)
print(stu1.native_place)
#类的属性可以在类之外修改
Student.native_place = 'xiaoyu'
print(stu1.native_place)

'''类方法的使用方式'''
Student.cm()
stu1.cm()

'''静态方法的使用方式'''
Student.method()
stu1.method()

'''python中动态绑定对象的属性与方法'''
stu2 = Student('小毅',16)

#属性的绑定(python中对象除了会继承类的所有属性，还可以给某一个对象额外添加属性，此为动态绑定，而此绑定为这一个对象多特有的属性个，别的对象没有)
stu1.gender = '男'
stu2.gender = '男'
print(stu1.gender,stu2.gender)
#左边为对象新绑定的属性名称，右边有绑定属性的内容

#对象绑定方法
def show():
    print('定义类之外的称为函数')
stu1.show = show             #左边写对象新加方法后的名字，右边为所新加方法的函数名
stu1.show()

'''类也是对象的一个封装'''
print(stu1.native_place)
#Python中如果该属性不希望在类对象的外部被访问，则在使用前加两个__

stu1.new()

print('--------------------------------')

'''类的继承(类与类之间可以有上下关系，称为父类与子类，所有类的最终的父类都是object，创建类的时候默认也是object)'''
class Person(object):          #此为父类

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name,self.age)

class Teacher(Person):        #此为子类包含person的所有属性，方法

    def __init__(self,name,age,Teacheryears):     #所写的变量中，如果与父类重名，则会默认为父类的变量。
        super().__init__(name,age)      #super()为调用父类的方法,super()还可以调用父类的属性
        self.Teacheryears = Teacheryears

    def info(self):                #方法的重写
        super().info()
        print(self.Teacheryears)

        #print(self.name,self.age,self.Teacheryears)，这是其中的一种写法


class Studend1(Person):

    def __init__(self,name,age,stu_num):
        super().__init__(name,age)
        self.stu_num = stu_num

    def info(self):                #子类可以修改父类中的方法，使其成为自己子类的方法，不过也可以在子类中独自创建一个方法，按需求而定
        super().info()
        print(self.stu_num)



studend1 = Studend1('小宇',18,23)
teacher1 = Teacher('小毅',16,2)

studend1.info()
teacher1.info()


'''object类'''
class example:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'我叫{self.name},今年{self.age}'

ex1 = example('小宇',18)
print(dir(ex1))             #dir函数可以查看对象与类所含有的属性与方法(生成的是列表)
#print(dir(example))
print(ex1)

'''面向对象三大特征之一的多态'''
#多态的解释 不同的子类可以继承同一个父类，而子类中又可以改写父类中的方法，但每个子类所改的方法都可以不一样，这使得每个子类中同一个方法的名字
#可以有很多种不同的执行方式，在调用函数的时候，只需要写一个函数，只需修改调用时的子类或对象，便可得到不同的结果，因为每个子类，或对象的方法都是
#一样的。



class Animal(object):

    def eat(self):
        print('动物要吃东西')

class Dog(Animal):

    def eat(self):
        print('狗吃肉')

class Cat(Animal):

    def eat(self):
        print('猫吃鱼')

class person(object):

    def eat(self):
        print('人吃五谷杂粮')

def fun(variable):          #此函数为调用类中的方法
    variable.eat()

fun(Animal())          #类也是一个对象，也是可以用函数进行使用
fun(Dog())
fun(Cat())
fun((person()))

'''类的赋值操作(类也是一个对象，所以也可以赋值给一个变量)'''
#但最终变量都还是指向一个对象
class CPU:
    pass

class disk:
    pass

class computer(CPU,disk):

    def __init__(self,cpu,disk):
        self.cpu = cpu
        self.disk = disk

cpu1 = CPU()       #创建对象
cpu2 = cpu1        #对象的赋值

print(cpu1)
print(cpu2)

'''类的浅拷贝与深拷贝'''
#拷贝的意义便是拷贝出来的内容与原来的一样，但会生成一个新的文件
#浅拷贝
import copy
disk = disk()

computer1 = computer(cpu1,disk)
print(computer1,id(computer1),id(computer1.cpu),id(computer1.disk))

computer2 = copy.copy(computer1)
print(computer2,id(computer2),id(computer2.cpu),id(computer2.disk))

#复制后的新对象会有新的内存地址，但内部的属性还是指向原来的地址，只copy里浅层的东西，就相当于就复制粘贴了一份新的模板，但内部的东西却没有复制粘贴

#深拷贝
computer3 = copy.deepcopy(computer1)

print(computer1,id(computer1),id(computer1.cpu),id(computer1.disk))

print(computer3,id(computer3),id(computer3.cpu),id(computer3.disk))

#深拷贝会拷贝子对象，也就是完全拷贝，将对象里面的所有属性，方法全部拷贝一份






'''创建对象的时候就已经进行了一次赋值操作，等号的左边就是想要赋的值，等号的右边是类对象
(创建对象的时候等号左边的，值同时是一个变量，也是一个对象)'''

#创建实例对象的是一个内置函数，__new__

class new(object):

    def __new__(cls, *args, **kwargs):
       obj = super().__new__(cls)        #这个过程为创建实例对象，但创建完后的对象只是一个空壳
       return obj

    def __init__(self,name,age):        #这个过程是为新创建的对象赋值，上面的obj会调入到self内，再到下面的赋值
        self.name = name
        self.age = age

new1 = new('小宇',18)    #这一个快速创建对象的书写方法




'''在不适用@在def前进行修饰的都为实例方法'''

'''在类之外定义的def称为函数，在类之内定义的def称为方法'''

'''类就相当于一个模板，而对象就是类的实体化，对象是由类创建出来的，一个类可以创建多个对象'''

'''类的使用对比自定义函数来说，它的选择性会更强，使用类创建的对象可以自定义选择想要执行的任务，自定义对象的特征，不同点等等，而是用函数来运行
任务的话，会默认运行所有的程序，这样选择性就不强了'''