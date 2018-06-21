'''
Created on Jun 19, 2018

@author: M1030081
'''
from Entities.Customer import Customer
from Entities.Payee import Payee
from Service.LoginService import LoginService
from builtins import int
import sys
from Service.PayeeService import PayeeService
from Service.TransactionService import TransactionService

def main():
    
    payeeService=PayeeService()
    transactionService=TransactionService()
    customer=user_login_first()
    choice=0
    if(customer==None):
        choice=int(input("Login attemt failed! Enter the choice to continue with login, press 1 to continue."))
        
    while(customer==None and choice==1):
        customer=user_login_first()
        if(customer==None):
            choice=int(input("Login attempt failed! Enter the choice to continue with login, press 1 to continue."))
    else:
        print("terminating the execution!")
        
    print("""Enter the choices with account operation:
            1.Add Payee
            2.Delete Payee
            3.Add Money
            4.Transfer Money
            5.Logout""")
    
    operation=int(input("Enter the choice"))
    
    if(operation==1):
        payee_account_number=int(input("Enter the account number of the payee"))
        payee_account_name=input("Enter the account name")
        payee_bank=input("Enter the bank name of payee")
        payee=Payee(payee_account_number,payee_account_name,payee_bank)
        customer=payeeService.add_payee(customer, payee)
        print(customer)
    elif operation==2:
        payee_account_number=int(input("Enter the account number of the payee to delete"))
        customer=payeeService.delete_payee(customer,payee_account_number)
        print(customer)
    elif operation==3:
        deposit_amount=int(input("Enter the amount to be deposited"))
        customer=transactionService.deposit_amount(deposit_amount, customer)
    elif operation==4:
        transfer_amount=int(input("Enter the amount to be transfered"))
        payee_account_number=int(input("Enter the payee account number to be transfered the amount"))
        customer=transactionService.transfer_amount(transfer_amount, customer,payee_account_number)
    elif operation==5:
        
        
        
        
        
            
        
        
    
def user_login_first():
    customer=login()
    forgot_pwd=1
    while(customer==None or forgot_pwd!=1):
        if customer==None:
            print("Account details does not match")
            forgot_pwd=int(input("please press 1 to enter new password"))
            if forgot_pwd==1:
                customer=forgotpassword()
                if(customer==None):
                    break
                else:
                    customer=login()
            else:
                sys.exit()
    
    return customer

def login():
    customer_account_number=int(input("Please enter account number to login"))
    customer_pwd=input("Please enter account password to login")
    
    loginService=LoginService()
    customer=loginService.validate_login(customer_account_number, customer_pwd)
    return customer

def forgotpassword():
     customer_account_number=int(input("Please enter account number to set the new password"))
     customer_new_password=input("Please enter new password to set the new password")
     loginService=LoginService()
     customer=loginService.set_forgot_password(customer_account_number, customer_new_password)
     return customer
     
    

if __name__ == '__main__':
    main()
    