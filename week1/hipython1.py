# -*- coding: utf-8 -*-
"""
Created on Thu Jun 08 17:27:37 2017

@author: Administrator
"""

'''
The goal of this program is to find the level of input score
'''
score = int(raw_input("Please input the score"))
if (90 < score <= 100):
    print "A"
elif (70 <= score <= 89):
    print "B"
elif (60 <= score  <= 69):
    print "C"    
elif (0 < score  <= 59):
    print "D"
else :
    print "others Invalid score"    