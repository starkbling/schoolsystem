#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from course import Course
from classes import  Classes

class School(object):
    def __init__(self,name,address,id):
        self.name = name
        self.address = address
        self.course = []
        self.classes = []
        self.stuff_lists = []
        self.student_lists = []
        self.id = str(id)

    def hire(self,teacher,salary):
        """雇佣老师"""
        teacher.id = self.id + str(10000 + len(self.stuff_lists))
        teacher.salary = salary
        print("Hired %s, id %s "%(teacher.name,teacher.id))
        self.stuff_lists[teacher.id] = teacher

    def eroll(self,student):
        """学生报名"""
        student.id = self.id + str(10000 + len(self.student_lists))  #只有在报名之后才会有学号
        student.school = self.name
        print("%s has erolled"%student.name)
        self.student_lists.append(student)

    def set_course(self,course_name,fee,class_hour):
        """设立课程"""
        course = Course(course_name,fee,class_hour)
        self.course.append(course)
        print("Set course %s"%course_name)

    def set_class(self,class_name):
        """设立班级"""
        number = self.id + str(100+len(self.classes))
        class_ = Classes(class_name,number)
        self.classes.append(class_)
        print("Set class %s"%class_name)





