# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:54:59 2023

@author: Radhakrishna
"""

from abc import ABC, abstractmethod

# in this abstract class, the method sound will be declared, but will not be implemented
# When we will create different classes, which will inherit from the Animal class
# then the implementation detail for sound method would be provided in those classes

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    
# Wrong way to use an abstract class
class Dog(Animal):
    def bark(self):
        print("Bow bow")
        
dog = Dog()