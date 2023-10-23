# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:23:13 2023

@author: Radhakrishna
"""

# the implementation of the abstract method is up to the subclass itself. 
# Because of this, we can have different implementations of these methods which do different things – 
# as long as they have the correct names


# Implementing Different Methods for Classes
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def arrive_at_work(self):
        pass

class Manager(Employee):
    def arrive_at_work(self):
        print("Arriving at datagy.io headquarters!")

class Supervisor(Employee):
    def arrive_at_work(self):
        print("Reporting for duty at datagy.io!")

nik = Manager()
katie = Supervisor()

nik.arrive_at_work()
katie.arrive_at_work()