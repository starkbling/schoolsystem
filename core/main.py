#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
from school import  School
from teacher import Teacher
from student import  Student
from login import login
from pickle_data import pickle_load,pickle_dump

funcs_dic = {
    "role_list":["admin","student","teacher"],
    "admin":["set_course","set_class","hire"],
    "student":["eroll","pay_tuition","choice_class"],
    "teacher": ["goto_class","choice_class","check_student_in_class","modify_grade"]
}
users = {"admin":["123456",0,"01"],"s10001":["123",2,"01"],"t10001":["123",1,"01"]}
# 对应的参数分别是用户名、密码、角色代码（0：管理员，1：教师，2：学生）、学校代码
teachers = []
students = []
schools = []
total_data = [funcs_dic, users, students, schools]

def auth_cmd(users,funcs_dic ):
    role_list = funcs_dic["role_list"]
    login_data = login(users)
    txt = "Please choice create a class or a course."
    if login_data[0]:
        print(txt)
        user_role = role_list[int(login_data[1])]
        i = 1
        if user_role == "admin":
            username = "school01"
            for func in funcs_dic[user_role]:
                print("%s. %s"%(i,func))
                i = i + 1
        while True:   #确保输入的是数字
            choice = input("What do you want to do :")
            if choice.isdigit():
                if int(choice) <=len(funcs_dic[user_role]):
                    cmd = funcs_dic[user_role][int(choice)-1]
                    return username, cmd
                    break
                else:
                    print("Invalid command!")
            else:
                print("Invalid Choice!")

if __name__=="__main__":
    school02 = School("GoodMM","ShangHai",12)
    school01 = School("Dream", "Beijing", 11)
    cmd  = auth_cmd(users,funcs_dic)
    func = getattr(eval(cmd[0]),cmd[1])   #eval()函数将传入的字符串转换为内存变量，这样就能够调用方法
    func("HH")
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