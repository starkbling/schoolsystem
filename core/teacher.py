#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from members import Member

class Teacher(Member):
    def __init__(self,name,age,sex,school):
        # Member.__init__(self, name, age,sex) #经典类的继承方式
        super(Teacher, self).__init__(name, age, sex)  #新式类的继承方式
        self.school = school.name
        self.__age = age

    def goto_class(self,classes):
        print("Teacher %s is going to teach %s"%(self.name,classes.name))
        self.course = classes.name

    def choice_class(self,classes):
        print("%s has assign to charge %s"%(self.name,classes.number))
        self.charge_class = classes.number
        classes.teacher.append(self.name)

    def check_student_in_class(self,class_):
        for student in class_[self.charge_class]["students"]:
            print(student.name)

    def modify_grade(self,class_):
        for student in class_[self.charge_class]["students"]:
            print(student.id," ",student.name," ",student.grade)
        student_name = input("Whose grade you want to change?")
        pass

    def show_age(self):
        print("%s is %s old"%(self.name,self.__age))
