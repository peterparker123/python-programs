# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:58:52 2023

@author: Radhakrishna
"""

# Inheritance is the mechanism which is used to 
# create another class, by deriving some attributes from the base class

# for e.g.

# Base class

class Person():
    def __init__(self, name,age):
        self.name = name
        self.age = age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def Print(self):
        return self.name, self.age
    
# This is the method to perform inheritance in python
# Here, the Student is child of Person
# or Person is base class of Student

class Student(Person):
    # in the inheritded class, we can add more methods
    def setSubject(self,subjectname):
        self.subjectname = subjectname
        
    def getSubject(self):
        return self.subjectname
    
    # overriding the base class method
    # For e.g overriding the print method
    def Print(self):
        return self.name, self.age, self.subjectname
        


# instantiate the student class

student1 = Student('lambu',40)
print(student1.getName())
print(student1.getAge())  

student1.setSubject('physics')

print(student1.getSubject())  

print(student1.Print())
    
