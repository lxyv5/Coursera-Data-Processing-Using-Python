# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 18:41:05 2017

@author: Administrator
"""

def proc(n ):
    if (n<0):
        print '-', 
        n = -n
    if (n / 10):
        proc(n / 10 )
    print n % 10,

proc(-345 )