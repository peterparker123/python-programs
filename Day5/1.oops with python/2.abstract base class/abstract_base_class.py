# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:10:06 2023

@author: Radhakrishna
"""

# Abstract classes are classes that contain one or more abstract methods. 
# These methods are declared but not implemented.
# Use a subclass to provide the details for implementation via its abstract methods.

# Create abstract classes in Python, we can use the built-in abc module. 
# The module provides both the ABC class and the abstractmethod decorator. 
# Let’s dive into how to create an abstract base class:
    
    
# Implementing an Abstract Base Class
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def arrive_at_work(self):
        pass