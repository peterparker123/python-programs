# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:02:35 2023

@author: Radhakrishna
"""

# static method are those methods, which don't need any instance of the class
# to be initialized
# In order to make a method static, use the @staticmethod
# staticmethod are those methods, which are bound to the class

class BankAccount(object):
    def __init__(self,balance=0):   
        name = None
        account_no = None
        
    # In a bank transaction, the name,and account_no is usually going to be static
    
    @staticmethod
    def setDetail(name,account_no):
        name = name
        account_no = account_no
        return name, account_no
    
    
myBankaccount = BankAccount()

print(BankAccount.setDetail('francis','555-4444-3333'))
# print(BankAccount.getDetail())
