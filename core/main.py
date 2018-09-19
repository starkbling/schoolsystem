#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from members import  Member
from school import  School
from teacher import Teacher
from student import  Student
from login import login
from pickle_data import pickle_load,pickle_dump

users = {1:2}
teachers = [1,2]
students = [11,212]
school01 = School("Dream","BeiJing",11)

pickle_dump(school01,"school01")
pickle_dump(users,"users")
pickle_dump(teachers,"users")
pickle_dump(students,"users")

users = pickle_load("users")
teachers = pickle_load("teachers")
students = pickle_load("students")
school03 = pickle_load("school01")
print(school03.name)   #pickle能够将类保存在文本文件中
print(teachers,students,users)


if __name__=="__main__":
    school02 = School("GoodMM","ShangHai",12)
    school01.set_class("101")
    school02.set_course("python",5000,45)
    s1 = Student("Bling",18,"F")
    s1.eroll(school01)
    s2 = Student("Can",17,"W")
    s2.eroll(school02)
    print(s1.id,s2.id)
    print(school01.student_lists)
    for student in school01.student_lists:
        print(student.school)
    for student in school02.student_lists:
        print(student.school)