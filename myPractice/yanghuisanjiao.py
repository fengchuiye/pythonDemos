# -*- coding: utf-8 -*-

def triangles():
    L0=[1]
    while True:
        yield L0
#        L0.insert(0,0)
#        L0.append(0)
        L1=list(range(0,len(L0)+1))
        for i in list(range(0,len(L0)+1)):
            if i==0:
                L1[i]=L0[i]
            elif i==len(L0):
                L1[i]=L0[i-1]
            else:
                L1[i]=L0[i-1]+L0[i]
        L0=L1
        
        
        
def triangles():
    L0=[1]
    while True:
        yield L0[:]
        L0.insert(0,0)
        L0.append(0)
        L1=[]
        #L1=list(range(0,len(L0)-1))
        for i in list(range(0,len(L0)-1)):
                L1.append(L0[i]+L0[i+1])
        L0=L1
        
        
        