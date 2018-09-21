#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
def test(a,b,c,d):
    """这是一个用于测试的函数"""
    print(locals())   #在函数内部打印函数各个变量的值

# print(locals())
print(test.__name__)  #打印函数的名字
print(test.__doc__)  #打印函数的说明文档
print(test.__annotations__)