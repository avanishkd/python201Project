'''
Created on Jun 20, 2018

@author: M1030081
'''
from DAO.PayeeDAO import PayeeDAO
from Entities.Customer import Customer
from Entities.Payee import Payee

class PayeeService(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
        
    def add_payee(self, customer:Customer,payee:Payee):
        daoObj=PayeeDAO()
        if customer==None or payee==None:
            print("Unable to add Payee, returned from service, either customer or payee is None")
            return customer
        flag_payee_added= daoObj.add_payee(customer, payee)
        if flag_payee_added:
            print("payee added successfully")
            customer.add_payee(payee)
            return customer
        else:
            print("payee was not added, due to some problem in DAO")
            return customer
        
    def delete_payee(self,customer:Customer,payee_account):
        daoObj=PayeeDAO()
        flagDeleted=daoObj.delete_payee(payee_account)
        if flagDeleted:
            for payees in customer.get_payees():
                if payees.get_account_number()==payee_account:
                    customer.remove_payee(payees)
                    return customer
        
        return customer
                