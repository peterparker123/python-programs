# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:22:12 2023

@author: Radhakrishna
"""

# Implementing an Abstract Base Class Correctly
from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def arrive_at_work(self):
        pass

class Manager(Employee):
    def arrive_at_work(self):
        print("Arriving at datagy.io headquarters!")

nik = Manager()

