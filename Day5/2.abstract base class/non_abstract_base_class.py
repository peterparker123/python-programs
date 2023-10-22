# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 15:12:20 2023

@author: Radhakrishna
"""


# All of these classes have methods that, functionally, do the same thing – have the employee get to work. 
# However, if we want to actually have the employee object show up at work, we need to use three different 
# implementations for the same thing.

# Implementing Classes Without Abstract Base Classes
class Manager:
    def arrive_at_work(self):
        print("Arrived at work")

class Supervisor:
    def get_to_work(self):
        print("Got to work")

class Staff:
    def show_up(self):
        print("Showed up")