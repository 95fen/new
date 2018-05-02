#工厂方法模式
# class Store(object):
#     def select_car(self):
#         pass
#     def order(self,car_type):
#         return self.select_car(car_type)
#
# class BMWCarStore(Store):
#     def select_car(self,car_type):
#         return  BMWFactory().select_car_by_type(car_type)
#
#
# bmw_store =BMWCarStore()
# bmw=bmw_store.order("720li")
# class Dog(object):
#     def __init__(self):
#         print("init")
#     def __new__(cls): #cls此时是DOG指向的那个类对象
#         print("new方法")
#         return  object.__new__(cls) #调用父类方法调用对象
#     def __del__(self):
#         print("del")
#     def __str__(self):
#         print("str")
#
# xtq=Dog()

# class Dog(object):
#     __instance=None#判断调用次数
#     __init_flag=False
#
#     def __new__(cls,name ):
#         if cls.__instance==None:
#             cls.__instance=object.__new__(cls)
#             return  cls.__instance
#
#         else:
#             return   cls.__instance    #("上次创建的对象")
#     def __init__(self,name):
#         if Dog.__init_flag==False:
#             self.name=name
#             Dog.__init_flag=True
#
# a= Dog("旺财")
# print(id(a))
# print(a.name)
# b=Dog("哮天犬")
# print(id(b))
# print(b.name)
#异常
# try:
#     print(aa)
#     print("---------")
# except nameErro:
#        print("如果出现异常处理............")
# class AA():
#     def love(self,a,b):
#         print(a+b)
#
# t=AA()
# print(t.love(100,500))

#---==与is
# a=[11,22,33]
# b=[11,22,33]
# a=100
# b=100
# print(a==b)
# print(a is b)
#-----------深浅拷贝
# a=[11,22,33]
# # b=a
# import copy
# a=[11,22,330]
# c=copy.deepcopy(a)
# print(id(a))#1166603179720
# print(id(c))#1166603179592
# print(5<<5)
# #
# class Test(object):
#     def __init__(self):
#         self.__num=100 #私有化加双下划线。表示privter
#     def setNum(self,newNum):
#         self.__num=newNum
#     def getNum(self):
#         return self.__num
#     num=property(getNum,setNum) #用于方便调用值的方法。
#
#
#
# t=Test()
# # t.num=200
# print(t.getNum())#获取私有变量num的值
# t.num=200#相当于t.setNum(200)
# print(t.num)

#
# class Test(object):
#     def __init__(self):
#         self.__num=100 #私有化加双下划线。表示privter
#     @property
#     def num(self):
#             return self.__num
#     print("--------get")
#     @num.setter
#     def num(self,newNum):
#         self.__num=newNum
#         print("-------set")
#
#
#
#
#
# t=Test()
# t.num=200  #相当于调用了t.setNum(200)
# print(t.num)#相当于调用了t.getnum()
#
# from collections import Iterable
# from collections import Iterator
#
# s=isinstance("abc",Iterable)
# d=isinstance((x for x in range(10)),Iterator)
# print(s,d)
# #迭代器
# a=[11,22,33,44,88,55]
# b=iter(a)
# print(b)
# print(next(b))
# for i in  range(10):
#    c= next(b)
#    print(c)

# a=[x*2 for x in range(100000000)]
# print(a)
#创建生成器的方式
# a=(x*2 for x in range(100)) #把列表的[]改为（）
# for i in range(10):
#   print(next(a))
# def creatNum():
#     print("---start--")
#     a,b=0,1
#     for i in range(5):
#         yield b  #生成器，停在此处，并返回b的值，在次执行，从此处开始继续
#         a,b=b,a+b
#         print(a)
#         print(b)
#         print("---stop-")
#
# a=creatNum()
# # for i in a:
# #    print(i)


#一行代码打个心
#print#('\n'.join([''.join([('Love'[(x-y) % len('love')] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))
#-------------send()
# def test():
#     i =0
#     while i<5:
#         temp=yield i
#         print(temp)
#         i+=1
#
# t=test()
# t.__next__()
# t.send("hah") #可以给生成器传值
#------------------生成器应用
# def test1():
#     while True:
#         print("---1---")
#         yield  None
# def test2():
#     while True:
#         print("------2-----")
#         yield None
#
# t1=test1()
# t2=test2()
# while True:
#     t1.__next__()
#     t2.__next__()

# def test():
#     print("-----1----")
#
# print(test())
#-------闭包------------
# def test(number):
#     print("--1--")
#     def test_in(number2):
#         print("--2--")
#         print(number+100)
#     print("--3--")
#     return test_in  #核心
# ret=test(100)#值传给test的number
# ret(100)#此处把100传给test_in中的number2
#------闭包例子-------、
# def test(a,b):
#     def test_in(x):
#         print(a*x+b)
#     return test_in
# line1=test(1,1)
# line1(0)
# line2=test(10,4)
# line2(0)
#
# line1(0)
#-----装饰器
# def w1(func):
#     def inner():
#         print("正在验证")
#         func()
#     return inner
# def f1():
#     print("---f1----")
# def f2():
#     print("---f2----")
#
# innerFunc =w1(f1)
# f1()

#----两个装饰器
# def w1(func):
#     def inner():
#         print("正在验证")
#         func()
#     return inner
# #@w1等价于f1=w1(f1)
# @w1
# def f1():
#     print("---f1----")
# @w1
# def f2():
#     print("---f2----")
#
# f1()
# f2()

#---------多个装饰器
#定义函数：完成包裹数据
# def makeBold(fn):
#     def wrapped():
#         print("--1--")
#         return "<b>"+fn()+"</b>"
#     return wrapped
# #定义函数2：完成包裹数据
# def makeItalic(fn):
#     def wrapped():
#         print("--2--")
#         return "<i>"+fn()+"</i>"
#     return wrapped
# #使用装饰器
# @makeBold
# @makeItalic
# def test3():
#     print("--3--")
#     return "hello world-3"
#
# ret=test3()
# print(ret)
#------------无参装饰器
# def func(functionName):
#     def func_in():
#         print("--funcin-1--")
#         functionName()
#         print("--func-2--")
#     print("--func-3--")
#     return func_in
# @func #this=test=func(test)
# def test():
#     print("--test--")
#
# #test=func(test)
# test()
#------有参数装饰器
#-------有返回值装饰器
# def func(functionName):
#     def func_in():
#         print("--funcin-1--")
#         xxx=functionName()
#         print("--func-2--")
#         return xxx
#     print("--func-3--")
#     return func_in
# @func
# def test():
#     print("--test--")
#     return "haha"
# #test=func(test)
# ret= test()
# print("test return value is %s"%(ret))
#----------通用装饰器-----
# def func(functionName):
#     def func_in(*args,**kwargs):
#         print("--记录日志-")
#         print("--funcin-1--")
#         xxx=functionName(*args,**kwargs)
#         return xxx
#     return func_in
# @func
# def test():
#     print("--test--")
#     return "haha"
# @func
# def test2():
#     print("--test2--")
# @func
# def test3(a):
#     print("test3--a=%d"%a)
#
# ret= test()
# print("test return value is %s"%(ret))
#
# a=test2()
# if a==None:
#     print("此处不返回，")
# print(a)
#
# test3(11)

#-----有参数的装饰器
# def func_arg(arg):
#     def func(functionName):
#         def func_in():
#             print("--日志-arg=%s-"%arg)
#             if arg=="heihei":
#                 print("要做区分")
#                 functionName()
#                 functionName()
#             else:
#                 functionName()
#         return func_in
#     return func
#     #1.先执行func_arg("heiehi")函数，这个函数return 的结果是func 这个函数的引用
#     #2，@func
#     #3, 使用@func对test进行装饰
# #带有参数的装饰器，能够起到在运行时，有不同的功能
# @func_arg("heihei")
# def test():
#     print("--test--")
#
# test()

# #------LEGB规则
# num=100
# def test():
#     num=200
#     print(num)
#
# test()

# #动态添加属性
# class Person(object):
#     def __init__(self,newName,newAge):
#         self.name=newName
#         self.age=newAge
#
# laowang=Person("老王",100)
# print(laowang.name)
# print(laowang.age)
# laowang.addr="北京"#此处动态添加,跟对象绑定在一起
# print(laowang.addr)
# #给类添加属性
# Person.num=100
#动态添加方法
# import types #引入添加方法的工具types
# class Person(object):
#     def __init__(self,newName,newAge):
#         self.name=newName
#         self.age=newAge
#     def eat(self):
#         print("---%s---正在吃"%self.name)
#
# def run(self):
#     print("-----%s正在跑"%self.name)
#
# p1 = Person("p1",10)
# p1.eat()
#
# p1.run=types.MethodType(run,p1)  #将run方法绑定到p1对象
# p1.run()


