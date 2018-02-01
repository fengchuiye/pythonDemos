# -*- coding: utf-8 -*-
class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender=gender
        
        
#############################################
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        self.count = self.count+1