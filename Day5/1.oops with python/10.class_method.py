# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:20:34 2023

@author: Radhakrishna
"""

# class method - > method which is associated with a class
# but, instead of taking an instance as argument, for e.g self
# it takes the class as the argument 


class Person:
    
    # declare class variables
    # class variables are available across the instance of the class
    #name = None
    #age = None
    def __init__(self):
        self.name=None
        self.age=None
        
    @classmethod
    def setDetails(cls,name,age):
        name = name
        age = age
        
    @classmethod
    def getDetails(cls):
        return name,age
    
    
person1 = Person()
person1.setDetails('francis', '30')
print(person1.getDetails()) 

person2 = Person()
print(person2.getDetails())       
        
        