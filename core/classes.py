#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""

class Classes():

    def __init__(self,name,number):
        self.student_lists = []
        self.teachers_lists = []
        self.course_lists = []

    def add_student(self,student):
        self.student_lists.append(student)
        print("%s has enter this class"%student.name)

    def add_teacher(self,teacher):
        self.teachers_lists.append(teacher)
        print("%s has enter this class"%teacher.name)

    def add_course(self,course):
        print("This class add a new course %s"%course.name)
        self.course_lists.append(course)
        pass
