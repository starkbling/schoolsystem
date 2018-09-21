# -*- coding:utf-8 -*-


def sign_in():
    worning = "Wrong choice!"
    user = input("please enter your name:").strip()
    pswd = input("please enter your password:").strip()
    age = input("please enter your age:").strip()
    if not age.isdigit():
        print(worning)
        age = input("please enter your age again:").strip()
    gender = input("Your gender,M\F:").strip()
    while gender!="M" and gender != "F":
        print(worning)
        gender = input("Enter your gender again ,M\F:").strip()
    megbox = ("""
    Please enter number to choice which character you are:
    1. Teacher
    2. Student
    """)
    print(megbox)
    character = input("Your choice:").strip()
    if character not in ["1","2","3"]:
        print(worning)
        print(megbox)
        character = input("Enter your choice again:").strip()
    if character == "1":
        teacher = Teacher(user,int(age),gender)
        teachers.append(teacher)
        users[teacher.name]=[pswd,"1"]
    if character == "2":
        student = Student(user,int(age),gender)
        students.append(student)
        users[student.name]=[pswd,"2"]

def login(users):
    login_times = 0
    while login_times <3:
        username = input("please input your username:").strip()
        password = input("please input your password:").strip()
        if username in users:
            type = users[username][1]
            if users[username][0] == password:
                print("Welcome to BlingSchool!")
                authorize = True
                break
            else:
                print("Invalid username or password")
                authorize = False
                login_times += 1
                continue
        else:
            print("Invalid usernam or password")
            sign_ask = input(r"Do you want to sign in Y\N?:").upper()
            if sign_ask == "Y":  #判断用户是否需要注册
                sign_in()
                break
            authorize = False
            login_times += 1
            continue
    return authorize,type

def auth(type):
    login_status = login()
    if login_status and type == login_status[1]:
        print("You are authorized")
    else:
        return
    def out_wrapper(func):
        def wraper(*args,**kwargs):
            func(*args,**kwargs)
            return func
        return wraper
    return out_wrapper
