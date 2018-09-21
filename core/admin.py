#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from members import  Member

class Admin(Member):
    def __init__(self,name,age,sex,school_id):
        super(Admin,self).__init__(name,age,sex)
        self.school_id = school_id

    def set_class(self):
        pass

    def set_course(self):
        pass

    def create_teaher(self):
        pass