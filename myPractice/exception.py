class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n
    
    
###################################################
# -*- coding: utf-8 -*-
from functools import reduce

def str2num(s):
    if s.find('.') > 0:
        ss = s.split('.')
        return int(ss[0])+int(ss[1])*pow(0.1,len(ss[1]))
    else
        return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
