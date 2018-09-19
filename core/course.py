#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""

class Course(object):
    def __init__(self,course_name,fee,class_hour):
        self.name = course_name
        self.fee = fee
        self.class_hour = class_hour
        self.teacher_lists = []
        self.student_lists = []

    def add_teacher_to_course(self,teacher_name):
        """老师加入课程"""
        self.teacher_lists.append(teacher_name)

    def student_attend_course(self, student_name):
        """学生报名参加课程"""
        self.student_lists.append(student_name)


