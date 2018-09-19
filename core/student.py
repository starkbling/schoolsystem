#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from members import  Member

class Student(Member):
    def __init__(self,name,age,sex):
        super(Student,self).__init__(name,age,sex)
        self.tuition = False

    def eroll(self,school):
        print("%s has enter %s"%(self.name,school.name))
        self.school = school.name
        school.eroll(self)

    def pay_tuition(self):
        print("%s payed tuition"%self.name)
        self.tuition = True

    def choice_class(self):
        pass


