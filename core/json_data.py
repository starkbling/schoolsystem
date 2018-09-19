#-*- coding:utf-8 -*-
"""
__author__ = BlingBling
"""
import json
import os,sys
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

#将类实例化的方式

def json_store(class_,filename):
    data_path = path + r"\data\%s"%filename
    with open(data_path,"w") as fp:
        json.dump(class_.__dict__,fp)