# -*- coding: utf-8 -*-
import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t1=time.time()
        res=fn(*args, **kw)
        t2=time.time()
        print('%s executed in %s s' % (fn.__name__, t2-t1))
        return res
    return wrapper
    
# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
