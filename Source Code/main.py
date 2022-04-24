from cmath import log
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

def menu_for_root():
    pass

def menu_for_emp():
    pass

def menu_for_pc():
    pass

def menu_for_bc():
    pass

print("****************** Welcome to Online Banking System - Database ******************")
while True:
    try:
        print("To login enter:")
        print("1 for Root User")
        print("2 for Branch Employee")
        print("3 for Personal Customer")
        print("4 for Business Customer")
        print("5 for Exit")
        inp = int(input("Enter your choice: "))
        if inp==1:
            ret_val = input_credentials()
            if ret_val==-1:
                print(errors["incorrect_login"])
            else:
                myRootUser = ru.RootUser(myTable,lis)
                print(statements["login_success"])
                menu_for_root()
        elif inp==2:
            emp_id = input_credentials(1)
            if emp_id==-1:
                print(errors["incorrect_login"])
            else:
                myEmployee = emp.Employee(myTable,lis,emp_id)
                print(statements["login_success"])
                # print(emp_id)
                menu_for_emp()
        elif inp==3:
            pc_id = input_credentials(2)
            if pc_id==-1:
                print(errors["incorrect_login"])
            else:
                myPersonalCustomer = pc.PersonalCustomer(myTable,lis,pc_id)
                print(statements["login_success"])
                # print(pc_id)
                menu_for_pc()
        elif inp==4:
            bc_id = input_credentials(2)
            if bc_id==-1:
                print(errors["incorrect_login"])
            else:
                myBusinessCutomer = bc.BusinessCustomer(myTable,lis,bc_id)
                print(statements["login_success"])
                # print(bc_id)
                menu_for_bc()
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
