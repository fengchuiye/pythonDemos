# -*- coding: utf-8 -*-
from functools import reduce
def prod(L):
    return reduce(lambda x,y: x*y ,L)
    
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
    
    
    
    
    
    

# -*- coding: utf-8 -*-
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def pos(s):
    a=s.find('.')
    print('pos',a)
    return len(s)-a-1

def str2num(s):
    return DIGITS[s]

def deldot(s):
    a=s.find('.')
    new_s=s[:a]+s[a+1:]
    return new_s

def str2float(s):
    position=pos(s)
    new_s=deldot(s)
    num=reduce(lambda x,y: 10*x+y, map(str2num,new_s))
    print(num)
    print(position)
    f=pow(0.1,position)*num
    return f


