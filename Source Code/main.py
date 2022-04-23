import json
from myLib.basics import connect_to_db
from myLib.basics import basic_functionalities as bf
from myLib import generalized_tables as GT
from myLib.users import root_user as ru
from myLib.users import employee as emp
from myLib.users import personal_customer as pc
from myLib.users import business_customer as bc

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

# for i in range(len(lis)):
#     print(str(i+1)+lis[i][0])

# for i in range(len(lis)):
#     print("myrootuser."+lis[i][0]+"_op()")

myRootUser = ru.RootUser(myTable,lis)
myEmployee = emp.Employee(myTable,lis)
myPersonalCustomer = pc.PersonalCustomer(myTable,lis)
myBusinessCutomer = bc.BusinessCustomer(myTable,lis)

# myrootuser.branch_op()
# for i in range(5):
# myrootuser.bank_account_op()
# myrootuser.department_op()
# myrootuser.employee_op()
# myrootuser.branch_managed_by_op()
# myrootuser.customer_op()
# myrootuser.customer_phone_number_op()
# myrootuser.collateral_op()
# myrootuser.documents_link_op()
# myrootuser.personal_customer_op()
# myrootuser.business_customer_op()
# myrootuser.savings_account_op()
# myrootuser.current_account_op()
# myrootuser.minor_account_op()
# myrootuser.zero_balance_account_op()
# myrootuser.card_op()
# myrootuser.debit_card_op()
# myrootuser.prepaid_card_op()
# myrootuser.atm_card_op()
# myrootuser.credit_card_op()
# myrootuser.account_linked_creditcard_op()
# myrootuser.loan_op()
# myrootuser.collateral_loan_op()
# myrootuser.non_collateral_loan_op()
# myrootuser.documents_pdf_op()
# myrootuser.loan_account_op()
# myrootuser.insurance_op()
# myrootuser.asset_insurance_op()
# myrootuser.loan_protection_insurance_op()
# myrootuser.term_life_insurance_op()
# myrootuser.medical_insurance_op()
# myrootuser.transaction_details_op()
# myrootuser.passbook_op()
# myrootuser.upi_op()
# myrootuser.upi_transactions_op()
# myrootuser.bill_payment_op()
# myrootuser.card_transactions_op()
# myrootuser.auto_payment_op()
# myrootuser.auto_payment_loan_op()
# myrootuser.auto_bill_payment_op()
    # myrootuser.transaction_log_op()
# myrootuser.ad_channel_op()
# myrootuser.advertisement_op()
# myrootuser.user_credential_op()
# myrootuser.employee_credential_op()
# myrootuser.closed_account_op()
# myrootuser.blocked_card_op()
# myrootuser.fixed_deposit_op()
# myrootuser.recurring_deposit_op()
# myrootuser.chequebook_op()
# myrootuser.bank_statement_op()
# myrootuser.otps_op()
# myrootuser.installment_op()


# currTableName = lis[0][0]
# currTable = lis[0][1]

# myTable.create(currTable, currTableName)
# myTable.read(currTable, currTableName)
# myTable.update(currTable, currTableName)
# myTable.delete(currTable, currTableName)
# myTable.readAll(currTableName)
# myTable.truncateAll(currTableName)


# CREATING ALL TABLES JSON FROM CODE
# myConnection.cur = myConnection.con.cursor()
# final_d={}
# myConnection.cur.execute('''SHOW TABLES FROM online_banking_system''')
# all_table_name=myConnection.cur.fetchall()
# for tables in all_table_name:
#     name=tables[0]
#     print(name)
#     d={}
#     myConnection.cur.execute('''SHOW COLUMNS FROM {}'''.format(name))
#     columns=myConnection.cur.fetchall()
#     for col in columns:
#         d[col[0]]="GET "+col[0]
#     final_d[name]=d
# print(len(all_table_name))


# with open("data.json", "w") as write_file:
#     json.dump(final_d, write_file)