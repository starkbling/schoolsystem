#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from course import Course

class School(object):
    def __init__(self,name,address):
        self.name = name
        self.address = address
        self.course = []
        self.class_ = {}
        self.stuff = []
        self.students = []

    def hire(self,teacher,salary):
        """雇佣老师"""
        print("Hired %s"%teacher.name)
        self.stuff.append(teacher.name)
        teacher.salary = salary

    def eroll(self,student):
        """学生报名"""
        print("%s erolled"%student.name)
        self.students.append(student.name)

    def set_course(self,course_name,fee):
        """设立课程"""
        course = Course(course_name,fee)
        self.course.append(course)

    def set_class(self,class_name):
        """设立班级"""
        print("set class %s"%class_name)
        self.class_[class_name]["students"]=[]
        self.class_[class_name]["teachers"] = []




