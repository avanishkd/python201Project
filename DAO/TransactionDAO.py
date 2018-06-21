'''
Created on Jun 21, 2018

@author: M1030081
'''
from Entities.Customer import Customer
from Util.DBUtil import MySQLDB
class TransactionDAO(object):
    '''
    classdocs
    '''


    def __init__(self):
        pass
    
    def deposit_amount(self,amount,customer:Customer):
        if amount==None or amount<=0:
            return False
        
        dbObj=MySQLDB()
        con=dbObj.get_connection()
        upadateStatement= "UPDATE customer set account_balance = account_balance+'"+str(amount)+"' where account_no="+str(customer.get_account_number())
        cursor= con.cursor()
        cursor.execute(upadateStatement)
        con.commit()
        rows_affected=cursor.rowcount
        dbObj.close_connection()
        
        if rows_affected==0:
            return False
        else:
            return True
        
    def transfer_amount(self,amount,customer:Customer, payee_account_number):
        flag_payee_found=False
        flag_sufficient_amount=False
        if amount==None or amount<=0:
            return False
        
        dbObj=MySQLDB()
        con=dbObj.get_connection()
        #payee saerch from here
        sql = "SELECT account_number FROM testpythondb.payees p where customer_account="+str(customer.get_account_number())
        con.query(sql)
        all_recs = con.store_result()
        no_of_recs = all_recs.num_rows()
        rec = all_recs.fetch_row()
        while (rec):
            for account_number in rec:
                
                print (account_number[0])
                if account_number[0]==payee_account_number:
                    print("Payee found in database")
                    flag_payee_found=True
                    break                    
                rec = all_recs.fetch_row()
            if flag_payee_found:
                break
        
        if flag_payee_found!=True:
            print ("Unable to find payee with provided account number so can't transfer the amount")
            return False
        #payee search upto here
        
        #check balance frmo here
        sql = "select account_balance from customer where account_no="+str(customer.get_account_number())
        con.query(sql)
        all_recs = con.store_result()
        no_of_recs = all_recs.num_rows()
        rec = all_recs.fetch_row()
        while (rec):
            for account_balance in rec:
                balance=account_balance[0]
                print (balance)
                if balance>=amount:
                    print("account balance is sufficient to tranfer")
                    flag_sufficient_amount=True
                    break                    
                rec = all_recs.fetch_row()
            break
        
        if flag_sufficient_amount!=True:
            print ("Unable to transfer amount due to insufficient account balance")
            return False
        # check balance upto here
        
        upadateStatement= "UPDATE customer set account_balance = account_balance-'"+str(amount)+"' where account_no="+str(customer.get_account_number())
        cursor= con.cursor()
        cursor.execute(upadateStatement)
        con.commit()
        rows_affected=cursor.rowcount
        dbObj.close_connection()
        
        if rows_affected==0:
            return False
        else:
            return True