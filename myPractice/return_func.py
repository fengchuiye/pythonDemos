# -*- coding: utf-8 -*-

def createCounter():
    def count():
        i=0
        while True:
            i=i+1
            yield i
    num=count()
    def counter():
        return next(num)
    return counter
    
##################################
def createCounter():
    fs=[0]
    def counter():
        fs[0]=fs[0]+1
        return fs[0]
    return counter