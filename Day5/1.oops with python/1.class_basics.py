# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 10:39:11 2023

@author: Radhakrishna
"""

# Basics of class in python
# In python, classes are objects
# Immutable data sturcture
# The purpose of class is to create data attribbutes and define the methods on those data attributes

# key word class creates a class
#  class is a blueprint of the object, but not a real thing
# In order to use the class, we need to instantiate the class

# classes in Python are child of object

class Person(object):
    
    # constructor method to initialize the variable
    # which would be passed inside the class
    # self is not a mandatory keyword, and it's by choice
    
    def __init__(self,name=None, age=None):
        # associate the parameters with the class instance
        self.name = name
        self.age = age
        
    def getname(self):
        print("The name of the person is: ",self.name)
        
    def getage(self):
        print("The age of the person is: ",self.age)
        
    
# create an instance of the class
# instance with a default constructor
person = Person()

# classes are immutable
print(type(Person()))

print(hash(Person))


# create an instance of the class

person = Person('francis',age='35')

# call the attributes and get the data using those attributes
print(person.name)
print(person.age)


# call the methods and get the data using those methods
person.getname()
person.getage()
