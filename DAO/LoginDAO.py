'''
Created on Jun 19, 2018

@author: M1030081
'''
from Util.DBUtil import MySQLDB
from Entities.Customer import Customer
from Entities.Payee import Payee


class LoginDAO(object):
    
    def validate_login(self, Customer):
        found=False
        account_number=Customer.get_account_number()
        account_password=Customer.get_account_password()
        dbObj=MySQLDB()
        con=dbObj.get_connection()
        sql = "SELECT * FROM customer"
        con.query(sql)
        all_recs = con.store_result()
        no_of_recs = all_recs.num_rows()
        rec = all_recs.fetch_row()
        while (rec):
            for account_no, account_name, account_balance, account_password in rec:
                account_no = account_no
                print (account_no, '->', account_password)
                if Customer.get_account_number()==int(account_no) and Customer.get_account_password()==account_password:
                    payeeList=self.get_payees(Customer.get_account_number())
                    Customer.set_account_name(account_name)
                    Customer.set_account_balance( account_balance)
                    Customer.set_payees(payeeList)
                    print(len(payeeList))
                    found=True
                    
                rec = all_recs.fetch_row()
            

        dbObj.close_connection()
        if found:
            return Customer
        else:
            return None
        
    def set_forgot_password(self, Customer):
        found=False
        account_number=Customer.get_account_number()
        account_password=Customer.get_account_password()
        dbObj=MySQLDB()
        con=dbObj.get_connection()
        updateStatement = "UPDATE customer set account_password = '"+str(account_password)+"' where account_no="+str(account_number)
        cursor= con.cursor()
        cursor.execute(updateStatement)
        con.commit()
        rows_affected=cursor.rowcount         
       

        dbObj.close_connection()
        if rows_affected==0:
            return None
        else:
            return True
        
    def get_payees(self,customer_account):
        payeelist=[]
        dbObj=MySQLDB()
        con=dbObj.get_connection()
        sql = "SELECT account_number,account_name,bank FROM testpythondb.payees p where customer_account="+str(customer_account)
        con.query(sql)
        all_recs = con.store_result()
        no_of_recs = all_recs.num_rows()
        rec = all_recs.fetch_row()
        while (rec):
            for account_number, account_name, bank in rec:
                account_number = int(account_number)
                print (account_number, '->', bank)
                payee=Payee(account_number,account_name,bank)
                
                payeelist.append(payee)                    
                rec = all_recs.fetch_row()
                
        return payeelist
    def __init__(self):
        '''
        Constructor
        '''
        