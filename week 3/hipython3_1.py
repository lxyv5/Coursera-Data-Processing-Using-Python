# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:03:26 2017

@author: Administrator
"""

data = {"test1":'1', "test2":'2', "test3":'3'}

def oldusers():
    a = raw_input("please type in user's name:")
    b = raw_input("please type in password:")
    if a in data and data[a] == b:
        print a + ", welcome back"
    elif a in data and data[a] != b:
        print ( "Incorrect password.")
    else:
        print "This users' name hasn't been registed."
        

def newusers():
    w = raw_input("please create your user's name:")
    if w in data:
        print "The user's name has existed."
    else:
        print "This user's can be used."
        y = raw_input("Please create your password:")
        data[w] = y
        print w + ", welcome join us."

def login(z):
    if z == 'N':
        newusers()
    elif z == 'O':
        oldusers()
    elif z == 'E':
        print 'Exit secceed.'
    else:
        print 'Unvalid commend, please try again.'
        login()