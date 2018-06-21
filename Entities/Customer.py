'''
Created on Jun 19, 2018

@author: M1030081
'''
from Entities.Payee import Payee

class Customer(object):
    __accountNumber=None
    __accountName=None
    __accountBalance=None
    __accountPassword=None
    __payees=[]
        
    def __init__(self):
        pass
        
 
    def add_payee(self,payee:Payee):
        self.__payees.append(payee)
    
    def remove_payee(self,payee:Payee):
        self.__payees.remove(payee)
        
    def get_account_number(self):
        return self.__accountNumber


    def get_account_name(self):
        return self.__accountName


    def get_account_balance(self):
        return self.__accountBalance


    def get_account_password(self):
        return self.__accountPassword


    def get_payees(self):
        return self.__payees


    def set_account_number(self, value):
        self.__accountNumber = value


    def set_account_name(self, value):
        self.__accountName = value


    def set_account_balance(self, value):
        self.__accountBalance = value


    def set_account_password(self, value):
        self.__accountPassword = value


    def set_payees(self, value):
        self.__payees = value


    def del_account_number(self):
        del self.__accountNumber


    def del_account_name(self):
        del self.__accountName


    def del_account_balance(self):
        del self.__accountBalance


    def del_account_password(self):
        del self.__accountPassword


    def del_payees(self):
        del self.__payees
    
    def __str__(self):
        return ("a/c no. - {0}; password - {1}; balance - {2}; name - {3}; payees - {4}".format(self.accountNumber,self.accountPassword,self.accountBalance,self.accountName,self.payees))


    accountNumber = property(get_account_number, set_account_number, del_account_number, "accountNumber's docstring")
    accountName = property(get_account_name, set_account_name, del_account_name, "accountName's docstring")
    accountBalance = property(get_account_balance, set_account_balance, del_account_balance, "accountBalance's docstring")
    accountPassword = property(get_account_password, set_account_password, del_account_password, "accountPassword's docstring")
    payees = property(get_payees, set_payees, del_payees, "payees's docstring")