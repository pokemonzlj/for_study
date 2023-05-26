# -*- coding: utf-8 -*-
import os
import sys

def test_format():
    print("输出{}和{}".format(1,"good"))
    print("输出{1}和{2}".format(2, "excellent", "batman"))  #带数字的索引
    print("输出{man}和{zhuangtai}".format(age=2, zhuangtai="excellent", man="batman"))  # 关键字取值
    a=[2, "excellent", "batman"]
    b={"age":3, "zhuangtai":"excellent！","man":"spiderman"}
    print("输出{1}和{2}".format(*a))  #元祖传参
    print("输出{man}和{zhuangtai}".format(**b))   #字典传参
    print("输出{1},{2}和{zhuangtai}".format(*a, **b))

#闭包：用比较容易懂的人话说，就是当某个函数被当成对象返回时，夹带了外部变量，就形成了一个闭包。看例子。

def make_printer(msg):
    def printer():
        print(msg)# 夹带私货（外部变量）
    return printer  # 返回的是函数，带私货的函数

#在下面这个例子，我们想要一个给content加tag的功能，但是具体的tag_name是什么样子的要根据实际需求来定，对外部调用的接口已经确定，就是add_tag(content)。如果按照面向接口方式实现，我们会先把add_tag写成接口，指定其参数和返回类型，然后分别去实现a和b的add_tag。
#但是在闭包的概念中，add_tag就是一个函数，它需要tag_name和content两个参数，只不过tag_name这个参数是打包带走的。所以一开始时就可以告诉我怎么打包，然后带走就行。
def tag(tag_name):
    def add_tag(content):
        return "<{0}>{1}</{0}>".format(tag_name, content)
    return add_tag


# 何时使用闭包：假如你需要写一个带参数的装饰器，那么一般都会生成闭包。
# 为什么？因为装饰器是一个固定的函数接口形式。它要求你的装饰器函数（或装饰器类）必须接受一个函数并返回一个函数：
def wrapper(func1):  # 接受一个callable对象
    # return func2  # 返回一个对象，一般为函数
    pass

def target_func(*args):  # 目标函数
    pass

# 调用方式一，直接包裹
# result = wrapper(target_func)(*args)

# 调用方式二，使用@语法，等同于方式一
@wrapper
def target_func(*args):
    pass
# result = target_func()

def debug(func):
    def wrapper(*args, **kwargs):  # 可变参数，可以用于任意目标函数
        print("[DEBUG]: enter {}()".format(func.__name__))
        print('Prepare and say...')
        return func(*args, **kwargs)
    return wrapper  # 返回

@debug
def say(something):
    print("hello {}!".format(something))

# 如果装饰器带参数，那么就需要在原来的装饰器上再包一层，用于接收这些参数。
# 这些参数（私货）传递到内层的装饰器里后，闭包就形成了。
# 所以说当装饰器需要自定义参数时，一般都会形成闭包。（类装饰器例外）
def html_tags(tag_name):
    print('begin outer function.')
    def wrapper_(func):
        print("begin of inner wrapper function.")
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            print("<{tag}>{content}</{tag}>".format(tag=tag_name, content=content))
        print('end of inner wrapper function.')
        return wrapper
    print('end of outer function')
    return wrapper_

# @html_tags('bob')
def hello(name='Toby'):
    return 'Hello {}!'.format(name)

# 不用@的写法如下
hello = html_tags('bob')(hello)
# 执行hello("kobe")
# html_tags('bob') #是一个闭包，它接受一个函数，并返回一个函数

#例子2：
#装饰器需要完成的功能不仅仅是能在进入某个函数后打出log信息，而且还需指定log的级别，那么装饰器就会是这样的。
def logging(level):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print("[{level}]: enter function {func}()".format(
                level=level,
                func=func.__name__))
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@logging(level='INFO')
def say(something):
    print("say {}!".format(something))

# 如果没有使用@语法，等同于
# say = logging(level='INFO')(say)

@logging(level='DEBUG')
def do(something):
    print("do {}...".format(something))


if __name__ == '__main__':
    hello("kobe")
    print(hello.__name__)  #wrapper



