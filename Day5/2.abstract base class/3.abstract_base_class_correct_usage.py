# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:58:54 2023

@author: Radhakrishna
"""

# In order to ensure that we work with Abstract base classes correctly
# the child class has to implement the method, declared inside the Abstract base class

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
    
class Dog(Animal):
    def sound(self):
        print("Dog's sound is bow bow")
        

class Cat(Animal):
    def sound(self):
        print("Cat's sound is meow-meow")
        
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()