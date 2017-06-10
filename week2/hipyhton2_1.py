# -*- coding: utf-8 -*-
"""
Created on Fri Jun 09 20:51:38 2017

@author: Administrator
"""

f = open(r'D:\Pythonexercise\blowing in the wind.txt','w')
s = '''How many roads must a man walk down

Before they call him a man

How many seas must a white dove sail

Before she sleeps in the sand

How many times must the cannon balls fly

Before they're forever banned

The answer my friend is blowing in the wind

The answer is blowing in the wind'''
f.writelines(s)
f.close()

f = open(r'D:\Pythonexercise\blowing in the wind.txt','a+')
contents = f.readlines()     
songname = '''blowin' in the wind'''

contents.insert(0,songname)

singer = 'bob dylan'

contents.insert(len(songname)+1,singer)

company = '1962 by Warner Bros. Inc.'

contents.insert(len(contents)+1,company)

print contents

f.close()
