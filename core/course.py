#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""

class Course(object):
    def __init__(self,course_name,fee):
        self.name = course_name
        self.fee = fee
        self.teachers = []
        self.students = []

    def add_teacher_to_course(self,teacher_name):
        """老师加入课程"""
        self.teachers.append(teacher_name)
        pass

    def student_attend_course(self, student_name):
        """学生报名参加课程"""
        self.students.append(student_name)
        pass

