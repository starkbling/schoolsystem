#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""

class Member(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.__age = age
        self.sex = sex
        self.member = []

    def show_age(self):
        print("%s is %s old" % (self.name, self.__age))
