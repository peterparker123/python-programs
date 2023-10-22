# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:19:41 2023

@author: Radhakrishna
"""

# We can see that we now have a class Employee, which inherits from the ABC class itself. 
# The class has only a single method, which is decorated using the @abstractmethod decorator. 
# The method itself doesn’t do anything but accepts the self keyword as an argument. 
# This part is important: the method shouldn’t do anything except for exist.

# Now when we create subclasses of the Employee class, these classes will need to have a method named .arrive_at_work(). 
# Let’s see what happens when we create a subclass with a different method:
    
# Instantiating our Manager class raises a TypeError since we don’t have a .arrive_at_work() method
    
# Implementing an Abstract Base Class Without Correct Method
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def arrive_at_work(self):
        pass

class Manager(Employee):
    def show_up(self):
        print("I'm here!")

nik = Manager()

