'''
Created on Jun 19, 2018

@author: M1030081
'''


class Payee(object):
   
    __accountNumber=None
    __accountName=None
    __bank=None
    
    def __init__(self, accountNumber, accountName, bank):
        self.__accountNumber = accountNumber
        self.__accountName = accountName
        self.__bank = bank

    def get_account_number(self):
        return self.__accountNumber


    def get_account_name(self):
        return self.__accountName


    def get_bank(self):
        return self.__bank


    def set_account_number(self, value):
        self.__accountNumber = value


    def set_account_name(self, value):
        self.__accountName = value


    def set_bank(self, value):
        self.__bank = value


    def del_account_number(self):
        del self.__accountNumber


    def del_account_name(self):
        del self.__accountName


    def del_bank(self):
        del self.__bank

    def __str__(self):
        return ("a/c no. - {0}; a/c name - {1}; payee account bank - {2}".format(self.accountNumber,self.accountName,self.bank))
    
    accountNumber = property(get_account_number, set_account_number, del_account_number, "accountNumber's docstring")
    accountName = property(get_account_name, set_account_name, del_account_name, "accountName's docstring")
    bank = property(get_bank, set_bank, del_bank, "bank's docstring")
    
    


        