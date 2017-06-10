# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 21:45:18 2017

@author: Administrator
"""

astr = 'Hello, world'
bstr = astr[:6] + ' python!'
print bstr
count = 0
for char in bstr[:]:
    if char in ',.!?' :
        count += 1
print "the number of punctuation mark is %d" %count
     