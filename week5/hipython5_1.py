# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:16:12 2017

@author: Xinyu Li
"""
class Animal(object):
    def __init__(self, name):
       self.name = name
    def getInfo(self): 
       print "This animal's name: %s" % self.name
    def sound(self): 
       print "The sound of this animal goes?"
       
class Dog(Animal):
    def __init__(self, name, size):
        self.name = name
        self.__size = size

    def getInfo(self):
        print "This dog's name: %s" % self.name 
        print "This dog’s size: %s" % self.__size
        
class Cat(Animal):
   def sound(self):
     print "The sound of cat goes meow ~" 