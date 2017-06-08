# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 19:13:27 2017

@author: Administrator
"""

import math
def is_prime(x):
    flag = 0
    i = int(math.sqrt(x))
    for j in range(1,i+1):
        if (x % i == 0):
            flag = 0
            break
        if (j >= i):
            flag = 1
    return flag
"""
Attention you must put n and x outside the loop,or I will not get the
desired result 
"""
n = 5
x = 1
print('P  M')
while n:
        
        y = 2 ** x - 1
        if is_prime(x) and is_prime(y):
            print ('%d  %d' %(x,y))
            n -= 1
        x += 1
        
        
    