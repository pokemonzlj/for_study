# -*- coding: utf-8 -*-
import os
import sys

class Demo(object):
    def __init__(self):
        self.table = 128
        self.desk = "expensive"

    def run(self, name, age):
        print("run the function named run")
        return f"My name is {name}, age is {age}!"

# 如果demo对象中有属性table,desk则打印self.table的值，否则打印'non-existent'
# 需要实例化Demo才能找到下面的属性
print(getattr(Demo, 'table', 'non-existent-table'))
print(getattr(Demo(), 'table', 'non-existent-table'))
print(getattr(Demo, 'desk', 'non-existent-desk'))
print(getattr(Demo(), 'desk', 'non-existent-desk'))
# 如果有方法run，打印其地址
print(getattr(Demo, 'run'))
print(getattr(Demo(), 'run'))
# 如果有方法run，运行函数并打印返回值
print(getattr(Demo, 'run')(1, "grace", "26"))
print(getattr(Demo(), 'run')("ding", "15"))


# getattr()函数用于返回一个对象属性值。
# 语法结构：getattr(object, name[, default])
# object -- 对象
# name -- 字符串，对象属性
# default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     test_format()

