'''
Created on Jun 20, 2018

@author: M1030081
'''
from Util.DBUtil import MySQLDB
from Entities.Customer import Customer
from Entities.Payee import Payee


class PayeeDAO(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    def add_payee(self, customer:Customer,payee:Payee):
        
        if customer==None or payee==None:
            return False
        
        customer.add_payee(payee)
        
        dbObj=MySQLDB()
        con=dbObj.get_connection()
        insertStatement= "insert into payees values ("+ str(payee.get_account_number()) +", '"+ str(payee.get_account_name()) +"', '"+str(payee.get_bank())+"'," +str(customer.get_account_number())+")"
        cursor= con.cursor()
        cursor.execute(insertStatement)
        con.commit()
        rows_affected=cursor.rowcount
        dbObj.close_connection()
        
        if rows_affected==0:
            return False
        else:
            return True
        
    def delete_payee(self,payee_account):
        
        if payee_account==None:
            return False
        
        dbObj=MySQLDB()
        con=dbObj.get_connection()
        deleteStatement= "delete from payees where account_number="+str( payee_account)
        cursor= con.cursor()
        cursor.execute(deleteStatement)
        con.commit()
        rows_affected=cursor.rowcount
        dbObj.close_connection()
        
        if rows_affected==0:
            return False
        else:
            return True