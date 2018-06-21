'''
Created on Jun 19, 2018

@author: M1030081
'''
from DAO.LoginDAO import LoginDAO
from Entities.Customer import Customer


class LoginService(object):
    daoObj=None
    def validate_login(self,customer_account_number,customer_password):
        daoObj=LoginDAO()
        customer=Customer()
        customer.set_account_number(customer_account_number)
        customer.set_account_password(customer_password)
        return daoObj.validate_login(customer)
    
    def set_forgot_password(self,customer_account_number,customer_new_password):
        daoObj=LoginDAO()
        customer=Customer()
        customer.set_account_number(customer_account_number)
        customer.set_account_password(customer_new_password)
        return daoObj.set_forgot_password(customer)


    def __init__(self):
        pass
        