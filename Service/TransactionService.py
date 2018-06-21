'''
Created on Jun 21, 2018

@author: M1030081
'''
from Entities.Customer import Customer
from Entities.Payee import Payee
from DAO.TransactionDAO import TransactionDAO

class TransactionService(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    def deposit_amount(self, amount,customer: Customer):
        daoObj=TransactionDAO()
        if customer!=None and amount>0:
            flagDeposited=daoObj.deposit_amount(amount,customer)
            
        if flagDeposited:
            customer.set_account_balance(customer.get_account_balance()+amount)
        
        return customer
    
    def transfer_amount(self, amount,customer: Customer, payee_account_number):
        daoObj=TransactionDAO()
        if customer==None and amount<=0 and payee_account_number==None:
            print("Unable to transfer amount, either Customer, payee or amount to transfer is none")
            return customer
        
        flag_tranfered=daoObj.transfer_amount(amount,customer,payee_account_number)
            
        if flag_tranfered:
            customer.set_account_balance(customer.get_account_balance()-amount)
        
        return customer