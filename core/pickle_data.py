#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
import pickle
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

#将类实例化的方式

def pickle_dump(data,filename):
    data_path = path + r"\data\%s.pk"%filename
    with open(data_path,"wb") as fp:
        pickle.dump(data,fp)

def pickle_load(filename):
    data_path = path + r"\data\%s.pk" %filename
    with open(data_path, "rb") as fp:
        data = pickle.load(fp)
    return data

users = {1:2,"hello":"hi"}
teachers = [1,2]
students = [11,212]

pickle_dump(users,"users")
pickle_dump(teachers,"teachers")
pickle_dump(students,"students")

users = pickle_load("users")
teachers = pickle_load("teachers")
students = pickle_load("students")
print(teachers,students,users)