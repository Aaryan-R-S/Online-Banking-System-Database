import json
from myLib.basics import connect_to_db
from myLib.basics import basic_functionalities as bf
from myLib import generalized_tables as GT
from myLib.users import root_user as ru
from myLib.users import employee as emp
from myLib.users import personal_customer as pc
from myLib.users import business_customer as bc

print()

myConnection = connect_to_db.DBConnector()
myBf = bf.RunQuery(myConnection)

with open('myLib/basics/print_errors.json') as fe:
    errors = json.load(fe)
with open('myLib/basics/print_statements.json') as fs:
    statements = json.load(fs)
with open('myLib/allTables.json') as ft:
    allTables = json.load(ft)
            
myTable = GT.Gen_Table(myBf)
lis = list(allTables.items())

def input_credentials(which=0):
    login_id = input("Login ID: ")
    login_pwd = input("Login Pwd: ")
    if which==0 and login_id=="root@db" and login_pwd=="root@db7":
        return 1
    if which in [1,2]:
        ret_val = myBf.search_credentials(login_id, login_pwd, which)
        if ret_val != []:
            return ret_val[0][0]
    return -1

def menu_for_root(myRootUser):
    print()
    while True:
        try:
            print("Enter:")
            print(" 1 for Branch")
            print(" 2 for Bank Account")
            print(" 3 for Department")
            print(" 4 for Employee")
            print(" 5 for Branch Managed By")
            print(" 6 for Customer")
            print(" 7 for Customer Phone Number")
            print(" 8 for Collateral")
            print(" 9 for Documents Link")
            print("10 for Personal Customer")
            print("11 for Business Customer")
            print("12 for Savings Account")
            print("13 for Current Account")
            print("14 for Minor Account")
            print("15 for Zero Balance Account")
            print("16 for Card")
            print("17 for Debit Card")
            print("18 for Prepaid Card")
            print("19 for ATM Card")
            print("20 for Credit Card")
            print("21 for Account Linked Credit Card")
            print("22 for Loan")
            print("23 for Collateral Loan")
            print("24 for Non Collateral Loan")
            print("25 for Documents PDF")
            print("26 for Loan Account")
            print("27 for Insurance")
            print("28 for Asset Insurance")
            print("29 for Loan Protection Insurance")
            print("30 for Term Life Insurance")
            print("31 for Medical Insurance")
            print("32 for Transaction Details")
            print("33 for Passbook")
            print("34 for UPI")
            print("35 for UPI Transactions")
            print("36 for Bill Payment")
            print("37 for Card Transactions")
            print("38 for Auto Payment")
            print("39 for Auto Payment Loan")
            print("40 for Auto Bill Payment")
            print("41 for Transaction Log")
            print("42 for Advt Channel")
            print("43 for Advertisement")
            print("44 for User Credential")
            print("45 for Employee Credential")
            print("46 for Closed Account")
            print("47 for Blocked Card")
            print("48 for Fixed Deposit")
            print("49 for Recurring Deposit")
            print("50 for Chequebook")
            print("51 for Bank Statement")
            print("52 for OTPs")
            print("53 for Installment")
            print("54 for Order by Branch")
            print("55 for Total Bank Collateral")
            print("56 for All Account Balances")
            print("57 for All Debit Cards")
            print("58 for Cutomer in _pur city")
            print("59 for Transaction Between")
            print("60 for Group By Accounts")
            print("61 for Inner Join All Accounts")
            print("62 for Left Join All Accounts")
            print("63 for Inner Join Some Accounts")
            print("64 for Union All Names")
            print(" 0 for Logging Out")
            inp = int(input("\nEnter your choice: "))
            if inp==1:
                ret_val = myRootUser.branch_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==2:
                ret_val = myRootUser.bank_account_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==3:
                ret_val = myRootUser.department_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==4:
                ret_val = myRootUser.employee_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==5:
                ret_val = myRootUser.branch_managed_by_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==6:
                ret_val = myRootUser.customer_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==7:
                ret_val = myRootUser.customer_phone_number_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==8:
                ret_val = myRootUser.collateral_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==9:
                ret_val = myRootUser.documents_link_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==10:
                ret_val = myRootUser.personal_customer_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==11:
                ret_val = myRootUser.business_customer_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==12:
                ret_val = myRootUser.savings_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==13:
                ret_val = myRootUser.current_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==14:
                ret_val = myRootUser.minor_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==15:
                ret_val = myRootUser.zero_balance_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==16:
                ret_val = myRootUser.card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==17:
                ret_val = myRootUser.debit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==18:
                ret_val = myRootUser.prepaid_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==19:
                ret_val = myRootUser.atm_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==20:
                ret_val = myRootUser.credit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==21:
                ret_val = myRootUser.account_linked_creditcard_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==22:
                ret_val = myRootUser.loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==23:
                ret_val = myRootUser.collateral_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==24:
                ret_val = myRootUser.non_collateral_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==25:
                ret_val = myRootUser.documents_pdf_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==26:
                ret_val = myRootUser.loan_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==27:
                ret_val = myRootUser.insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==28:
                ret_val = myRootUser.asset_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==29:
                ret_val = myRootUser.loan_protection_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==30:
                ret_val = myRootUser.term_life_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==31:
                ret_val = myRootUser.medical_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==32:
                ret_val = myRootUser.transaction_details_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==33:
                ret_val = myRootUser.passbook_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==34:
                ret_val = myRootUser.upi_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==35:
                ret_val = myRootUser.upi_transactions_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==36:
                ret_val = myRootUser.bill_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==37:
                ret_val = myRootUser.card_transactions_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==38:
                ret_val = myRootUser.auto_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==39:
                ret_val = myRootUser.auto_payment_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==40:
                ret_val = myRootUser.auto_bill_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==41:
                ret_val = myRootUser.transaction_log_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==42:
                ret_val = myRootUser.ad_channel_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==43:
                ret_val = myRootUser.advertisement_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==44:
                ret_val = myRootUser.user_credential_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==45:
                ret_val = myRootUser.employee_credential_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==46:
                ret_val = myRootUser.closed_account_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==47:
                ret_val = myRootUser.blocked_card_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==48:
                ret_val = myRootUser.fixed_deposit_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==49:
                ret_val = myRootUser.recurring_deposit_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==50:
                ret_val = myRootUser.chequebook_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==51:
                ret_val = myRootUser.bank_statement_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==52:
                ret_val = myRootUser.otps_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==53:
                ret_val = myRootUser.installment_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==54:
                ret_val = myBf.order_branch_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==55:
                ret_val = myBf.bank_collateral_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==56:
                ret_val = myBf.account_balances_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==57:
                ret_val = myBf.all_debit_card_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==58:
                ret_val = myBf.pur_customer_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==59:
                ret_val = myBf.transaction_between_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==60:
                ret_val = myBf.group_by_accounts_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==61:
                ret_val = myBf.inner_join_all_accounts_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==62:
                ret_val = myBf.left_join_all_accounts_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==63:
                ret_val = myBf.inner_join_some_account_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==64:
                ret_val = myBf.union_names_query()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==0:
                print("Logging Out...")
                return
            else:
                print(errors["input_mismatch_in_query"])
        except Exception as e:
            print(errors["input_mismatch_in_query"])
            print(e)
        print()

def menu_for_emp(myRootUser):
    print()
    while True:
        try:
            print("Enter:")
            print(" 2 for Bank Account")
            print(" 4 for Employee")
            print(" 6 for Customer")
            print(" 7 for Customer Phone Number")
            print(" 8 for Collateral")
            print(" 9 for Documents Link")
            print("10 for Personal Customer")
            print("11 for Business Customer")
            print("12 for Savings Account")
            print("13 for Current Account")
            print("14 for Minor Account")
            print("15 for Zero Balance Account")
            print("16 for Card")
            print("17 for Debit Card")
            print("18 for Prepaid Card")
            print("19 for ATM Card")
            print("20 for Credit Card")
            print("21 for Account Linked Credit Card")
            print("22 for Loan")
            print("23 for Collateral Loan")
            print("24 for Non Collateral Loan")
            print("25 for Documents PDF")
            print("26 for Loan Account")
            print("27 for Insurance")
            print("28 for Asset Insurance")
            print("29 for Loan Protection Insurance")
            print("30 for Term Life Insurance")
            print("31 for Medical Insurance")
            print("32 for Transaction Details")
            print("33 for Passbook")
            print("37 for Card Transactions")
            print("41 for Transaction Log")
            print("42 for Advt Channel")
            print("43 for Advertisement")
            print("45 for Employee Credential")
            print("46 for Closed Account")
            print("47 for Blocked Card")
            print("48 for Fixed Deposit")
            print("49 for Recurring Deposit")
            print("50 for Chequebook")
            print("51 for Bank Statement")
            print("53 for Installment")
            print(" 0 for Logging Out")
            inp = int(input("\nEnter your choice: "))
            if inp==2:
                ret_val = myRootUser.bank_account_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==4:
                ret_val = myRootUser.employee_op()       
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==6:
                ret_val = myRootUser.customer_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==7:
                ret_val = myRootUser.customer_phone_number_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==8:
                ret_val = myRootUser.collateral_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==9:
                ret_val = myRootUser.documents_link_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==10:
                ret_val = myRootUser.personal_customer_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==11:
                ret_val = myRootUser.business_customer_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==12:
                ret_val = myRootUser.savings_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==13:
                ret_val = myRootUser.current_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==14:
                ret_val = myRootUser.minor_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==15:
                ret_val = myRootUser.zero_balance_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==16:
                ret_val = myRootUser.card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==17:
                ret_val = myRootUser.debit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==18:
                ret_val = myRootUser.prepaid_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==19:
                ret_val = myRootUser.atm_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==20:
                ret_val = myRootUser.credit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==21:
                ret_val = myRootUser.account_linked_creditcard_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==22:
                ret_val = myRootUser.loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==23:
                ret_val = myRootUser.collateral_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==24:
                ret_val = myRootUser.non_collateral_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==25:
                ret_val = myRootUser.documents_pdf_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==26:
                ret_val = myRootUser.loan_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==27:
                ret_val = myRootUser.insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==28:
                ret_val = myRootUser.asset_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==29:
                ret_val = myRootUser.loan_protection_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==30:
                ret_val = myRootUser.term_life_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==31:
                ret_val = myRootUser.medical_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==32:
                ret_val = myRootUser.transaction_details_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==33:
                ret_val = myRootUser.passbook_op()      
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==37:
                ret_val = myRootUser.card_transactions_op()      
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==41:
                ret_val = myRootUser.transaction_log_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==42:
                ret_val = myRootUser.ad_channel_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==43:
                ret_val = myRootUser.advertisement_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==45:
                ret_val = myRootUser.employee_credential_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==46:
                ret_val = myRootUser.closed_account_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==47:
                ret_val = myRootUser.blocked_card_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==48:
                ret_val = myRootUser.fixed_deposit_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==49:
                ret_val = myRootUser.recurring_deposit_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==50:
                ret_val = myRootUser.chequebook_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==51:
                ret_val = myRootUser.bank_statement_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==53:
                ret_val = myRootUser.installment_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==0:
                print("Logging Out...")
                return
            else:
                print(errors["input_mismatch_in_query"])
        except Exception as e:
            print(errors["input_mismatch_in_query"])
            print(e)
        print()

def menu_for_pc(myRootUser):
    print()
    while True:
        try:
            print("Enter:")
            print(" 7 for Customer Phone Number")
            print("12 for Savings Account")
            print("14 for Minor Account")
            print("15 for Zero Balance Account")
            print("17 for Debit Card")
            print("18 for Prepaid Card")
            print("19 for ATM Card")
            print("20 for Credit Card")
            print("21 for Account Linked Credit Card")
            print("22 for Loan")
            print("23 for Collateral Loan")
            print("24 for Non Collateral Loan")
            print("26 for Loan Account")
            print("27 for Insurance")
            print("28 for Asset Insurance")
            print("29 for Loan Protection Insurance")
            print("30 for Term Life Insurance")
            print("31 for Medical Insurance")
            print("32 for Transaction Details")
            print("33 for Passbook")
            print("34 for UPI")
            print("35 for UPI Transactions")
            print("36 for Bill Payment")
            print("37 for Card Transactions")
            print("38 for Auto Payment")
            print("39 for Auto Payment Loan")
            print("40 for Auto Bill Payment")
            print("44 for User Credential")
            print("46 for Closed Account")
            print("47 for Blocked Card")
            print("48 for Fixed Deposit")
            print("49 for Recurring Deposit")
            print("50 for Chequebook")
            print("51 for Bank Statement")
            print("52 for OTPs")
            print("53 for Installment")
            print(" 0 for Logging Out")
            inp = int(input("\nEnter your choice: "))
            if inp==7:
                ret_val = myRootUser.customer_phone_number_op()      
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==12:
                ret_val = myRootUser.savings_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==14:
                ret_val = myRootUser.minor_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==15:
                ret_val = myRootUser.zero_balance_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==17:
                ret_val = myRootUser.debit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==18:
                ret_val = myRootUser.prepaid_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==19:
                ret_val = myRootUser.atm_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==20:
                ret_val = myRootUser.credit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==21:
                ret_val = myRootUser.account_linked_creditcard_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==22:
                ret_val = myRootUser.loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==23:
                ret_val = myRootUser.collateral_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==24:
                ret_val = myRootUser.non_collateral_loan_op()   
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==26:
                ret_val = myRootUser.loan_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==27:
                ret_val = myRootUser.insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==28:
                ret_val = myRootUser.asset_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==29:
                ret_val = myRootUser.loan_protection_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==30:
                ret_val = myRootUser.term_life_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==31:
                ret_val = myRootUser.medical_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==32:
                ret_val = myRootUser.transaction_details_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==33:
                ret_val = myRootUser.passbook_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==34:
                ret_val = myRootUser.upi_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==35:
                ret_val = myRootUser.upi_transactions_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==36:
                ret_val = myRootUser.bill_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==37:
                ret_val = myRootUser.card_transactions_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==38:
                ret_val = myRootUser.auto_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==39:
                ret_val = myRootUser.auto_payment_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==40:
                ret_val = myRootUser.auto_bill_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==44:
                ret_val = myRootUser.user_credential_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==46:
                ret_val = myRootUser.closed_account_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==47:
                ret_val = myRootUser.blocked_card_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==48:
                ret_val = myRootUser.fixed_deposit_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==49:
                ret_val = myRootUser.recurring_deposit_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==50:
                ret_val = myRootUser.chequebook_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==51:
                ret_val = myRootUser.bank_statement_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==52:
                ret_val = myRootUser.otps_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==53:
                ret_val = myRootUser.installment_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==0:
                print("Logging Out...")
                return
            else:
                print(errors["input_mismatch_in_query"])
        except Exception as e:
            print(errors["input_mismatch_in_query"])
            print(e)
        print()

def menu_for_bc(myRootUser):
    print()
    while True:
        try:
            print("Enter:")
            print(" 7 for Customer Phone Number")
            print("13 for Current Account")
            print("17 for Debit Card")
            print("19 for ATM Card")
            print("20 for Credit Card")
            print("21 for Account Linked Credit Card")
            print("22 for Loan")
            print("23 for Collateral Loan")
            print("24 for Non Collateral Loan")
            print("26 for Loan Account")
            print("27 for Insurance")
            print("28 for Asset Insurance")
            print("29 for Loan Protection Insurance")
            print("32 for Transaction Details")
            print("33 for Passbook")
            print("34 for UPI")
            print("35 for UPI Transactions")
            print("36 for Bill Payment")
            print("37 for Card Transactions")
            print("38 for Auto Payment")
            print("39 for Auto Payment Loan")
            print("40 for Auto Bill Payment")
            print("44 for User Credential")
            print("46 for Closed Account")
            print("47 for Blocked Card")
            print("50 for Chequebook")
            print("51 for Bank Statement")
            print("52 for OTPs")
            print("53 for Installment")
            print(" 0 for Logging Out")
            inp = int(input("\nEnter your choice: "))
            if inp==7:
                ret_val = myRootUser.customer_phone_number_op()        
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==13:
                ret_val = myRootUser.current_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==17:
                ret_val = myRootUser.debit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==19:
                ret_val = myRootUser.atm_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==20:
                ret_val = myRootUser.credit_card_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==21:
                ret_val = myRootUser.account_linked_creditcard_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==22:
                ret_val = myRootUser.loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==23:
                ret_val = myRootUser.collateral_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==24:
                ret_val = myRootUser.non_collateral_loan_op()   
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==26:
                ret_val = myRootUser.loan_account_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==27:
                ret_val = myRootUser.insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==28:
                ret_val = myRootUser.asset_insurance_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==29:
                ret_val = myRootUser.loan_protection_insurance_op()  
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==32:
                ret_val = myRootUser.transaction_details_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==33:
                ret_val = myRootUser.passbook_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==34:
                ret_val = myRootUser.upi_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==35:
                ret_val = myRootUser.upi_transactions_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==36:
                ret_val = myRootUser.bill_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==37:
                ret_val = myRootUser.card_transactions_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==38:
                ret_val = myRootUser.auto_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==39:
                ret_val = myRootUser.auto_payment_loan_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==40:
                ret_val = myRootUser.auto_bill_payment_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==44:
                ret_val = myRootUser.user_credential_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==46:
                ret_val = myRootUser.closed_account_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==47:
                ret_val = myRootUser.blocked_card_op()  
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==50:
                ret_val = myRootUser.chequebook_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==51:
                ret_val = myRootUser.bank_statement_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==52:
                ret_val = myRootUser.otps_op()    
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==53:
                ret_val = myRootUser.installment_op()
                if ret_val != [] and ret_val != None:
                    print(ret_val)
            elif inp==0:
                print("Logging Out...")
                return
            else:
                print(errors["input_mismatch_in_query"])
        except Exception as e:
            print(errors["input_mismatch_in_query"])
            print(e)
        print()

print("****************** Welcome to Online Banking System - Database ******************")
while True:
    try:
        print("To login enter:")
        print("1 for Root User")
        print("2 for Branch Employee")
        print("3 for Personal Customer")
        print("4 for Business Customer")
        print("5 for Exit")
        inp = int(input("\nEnter your choice: "))
        if inp==1:
            ret_val = input_credentials()
            if ret_val==-1:
                print(errors["incorrect_login"])
            else:
                myRootUser = ru.RootUser(myTable,lis)
                print(statements["login_success"])
                menu_for_root(myRootUser)
        elif inp==2:
            emp_id = input_credentials(1)
            if emp_id==-1:
                print(errors["incorrect_login"])
            else:
                myEmployee = emp.Employee(myTable,lis,emp_id)
                print(statements["login_success"])
                # print(emp_id)
                menu_for_emp(myEmployee)
        elif inp==3:
            pc_id = input_credentials(2)
            if pc_id==-1:
                print(errors["incorrect_login"])
            else:
                myPersonalCustomer = pc.PersonalCustomer(myTable,lis,pc_id)
                print(statements["login_success"])
                # print(pc_id)
                menu_for_pc(myPersonalCustomer)
        elif inp==4:
            bc_id = input_credentials(2)
            if bc_id==-1:
                print(errors["incorrect_login"])
            else:
                myBusinessCutomer = bc.BusinessCustomer(myTable,lis,bc_id)
                print(statements["login_success"])
                # print(bc_id)
                menu_for_bc(myBusinessCutomer)
        elif inp==5:
            print("Thanks for using Online Banking System - Database!")
            print()
            exit()
        else:
            print(errors["input_mismatch_in_query"])
    except Exception as e:
        print(errors["input_mismatch_in_query"])
        print(e)
    print()
