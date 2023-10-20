# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:32:45 2023

@author: Radhakrishna
"""

# a python class to implement integer
# this will have all the methods, such as add, sub, mul and div



class Int(object):
    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y
        
    # Add method
    
    def add(self):
        return self.x + self.y
    
    def sub(self):
        return self.x - self.y
    
    def mul(self):
        return self.x * self.y
    
    def div(self):
        
        try:
            return self.x/self.y 
        except ZeroDivisionError:
            print("Division by zero error")
            
            
# If we are running this program as a python file
if __name__=='__main__':
    myInt = Int(4,0)
    print(myInt.add())
    print(myInt.sub())
    print(myInt.mul())
    print(myInt.div())    

    
        