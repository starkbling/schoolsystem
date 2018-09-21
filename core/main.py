#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from school import  School
from teacher import Teacher
from student import  Student
from login import login
from pickle_data import pickle_load,pickle_dump

tools_dic = {
    "admin":["set_course","set_class","hire"],
    "student":["eroll","pay_tuition","choice_class"],
    "teacher": ["goto_class","choice_class",]
}
users = {"admin":["123456",0]}
teachers = []
students = []
schools = []
total_data = [tools_dic, users, students, schools]

def auth_cmd(users):
    login_status = login(users)
    print(login_status[1])
    if login_status[1]=="0":
        choice = input("""
        Please choice create a class or a course.
        1. create class
        2. create course
        >>:""").strip()
    return cmd

print(users["admin"][0])
if __name__=="__main__":
    school02 = School("GoodMM","ShangHai",12)
    school01 = School("Dream", "Beijing", 11)

    school01.set_class("101")
    school02.set_course("python",5000,45)
    school02.set_course("linux", 3000, 40)
    school01.set_course("PHP", 3000, 30)
    s1 = Student("Bling",18,"F")
    t1 = Teacher("Alex",33,"F",school01)
    print(t1.show_age())
    print(t1.school)
    s1.eroll(school01)
    s2 = Student("Can",17,"W")
    s2.eroll(school02)
    print(s1.id,s2.id)
    print(school01.student_lists)
    for student in school01.student_lists:
        print(student.school)
    for student in school02.student_lists:
        print(student.school)