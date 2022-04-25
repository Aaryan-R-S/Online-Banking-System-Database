import json

class RunQuery:
    # query_obj = {
    #     "relation" : "r_name",
    #     "op_type" : "c",    # OR "r", "u", "d"
    #     "data": {"f_name_1":"val_1", "f_name_2":"val_2"}, 
    #     # "c" (all fields in sorted order) 
    #     # "r" (primary field)
    #     # "u" (primarty field 'where' and remaining fields 'set')
    #     # "d" (primary field)
    # } 
    
    def __init__(self, myConnection):
        self.connection = myConnection
        with open('myLib/basics/print_errors.json') as f:
            self.errors = json.load(f)
        with open('myLib/basics/print_statements.json') as fs:
            self.statements = json.load(fs)
    
    def run_query(self, query_obj):
        if("relation" not in query_obj.keys()):
            print(self.errors["missing_relation"])
        if("data" not in query_obj.keys()):
            print(self.errors["missing_data"])
        if("op_type" not in query_obj.keys()):
            print(self.errors["missing_op_type"])
        elif(query_obj["op_type"]=="c"):
            self.create_query(query_obj)   
        elif(query_obj["op_type"]=="r"):
            return self.fetch_query(query_obj)
        elif(query_obj["op_type"]=="u"):
            self.update_query(query_obj)
        elif(query_obj["op_type"]=="d"):
            self.delete_query(query_obj)
        else:
            print(self.errors["invalid_op_type"])
    
    def create_query(self, query_obj):
        val = ""
        for k,v in query_obj["data"].items():
            val += f" '{v}',"
        val = val[:-1]
        # print(val)
        queryInsert = '''INSERT INTO {} VALUES({})'''.format(query_obj["relation"], val)
        # print(queryInsert)
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryInsert)
            self.connection.con.commit()
            print(self.statements["query_success"], end=" ")
            print(self.connection.cur.rowcount, "record inserted.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
    
    def fetch_query(self, query_obj):
        lis = list(query_obj["data"].items())
        # print(lis)
        queryFetch = '''SELECT * FROM {} WHERE {} = {}'''.format(query_obj["relation"], lis[0][0], f"'{str(lis[0][1])}'")
        # print(queryFetch)
        self.connection.cur = self.connection.con.cursor()
        myList = []
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
    
    def update_query(self, query_obj):
        lis = list(query_obj["data"].items())
        fields = ""
        for i in range(1, len(lis)):
            fields += " " + f"{str(lis[i][0])}" + " = " + f"'{str(lis[i][1])}'" + ","
        fields = fields[:-1]
        # print(lis)
        queryUpdate = '''UPDATE {} SET{} WHERE {} = {}'''.format(query_obj["relation"], fields, lis[0][0], f"'{str(lis[0][1])}'")
        # print(queryUpdate)
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryUpdate)
            self.connection.con.commit()
            print(self.statements["query_success"], end=" ")
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records updated.")
            else:
                print(self.connection.cur.rowcount, "record updated.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
    
    def delete_query(self, query_obj):
        lis = list(query_obj["data"].items())
        # print(lis)
        queryUpdate = '''DELETE FROM {} WHERE {} = {}'''.format(query_obj["relation"], lis[0][0], f"'{str(lis[0][1])}'")
        # print(queryUpdate)
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryUpdate)
            self.connection.con.commit()
            print(self.statements["query_success"], end=" ")
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records deleted.")
            else:
                print(self.connection.cur.rowcount, "record deleted.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)

    def search_credentials(self, login_id, login_pwd, which):
        if which==1:
            queryFetchEmployee = '''SELECT employee_id FROM employee_credential WHERE employee_login_id = "{}" AND employee_login_password = "{}" '''.format(login_id, login_pwd)
        else:
            queryFetchUser = '''SELECT user_id FROM user_credential WHERE user_login_id = "{}" AND user_login_password = "{}" '''.format(login_id, login_pwd)
        self.connection.cur = self.connection.con.cursor()
        myList = []
        try:
            if which==1:
                self.connection.cur.execute(queryFetchEmployee)
            else:
                self.connection.cur.execute(queryFetchUser)
            myList += self.connection.cur.fetchall()
            print(self.statements["query_success"], end=" ")
            # print(myList)
            if len(myList)>1:
                print(len(myList), "records fetched.")
            else:
                print(len(myList), "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
    
    def order_branch_query(self):
        queryFetch = '''SELECT IFSC_Code, Branch_Name, District, State FROM Branch ORDER BY State ASC, Branch_Name DESC;'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
        
    def bank_collateral_query(self):
        queryFetch = '''SELECT COALESCE(SUM(Collateral_Value), 0) AS Total_Collateral_Value FROM Collateral;'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
        
    def account_balances_query(self):
        queryFetch = '''SELECT Account_Number, CASE WHEN Account_Balance > 500000 THEN 'The balance is greater than 5 lakhs' WHEN Account_Balance > 100000 THEN 'The balance is between 1 to 5 lakhs' ELSE 'The balance is under 1 lakh' END AS Balance FROM Bank_Account;'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
        
    def all_debit_card_query(self):
        queryFetch = '''SELECT Card_Number, Linked_Mobile_Number FROM Card WHERE EXISTS (SELECT * FROM Debit_Card WHERE Debit_Card.Card_Number = Card.Card_Number);'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
              
    def pur_customer_query(self):
        queryFetch = '''SELECT * FROM Customer WHERE City_Village_Town LIKE '%_pur';'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
        
    def transaction_between_query(self):
        print("Enter 1 for 'failed' transactions")
        print("Enter 2 for 'successful' transactions")
        inp = input("Enter your choice: ")
        if inp=="1":
            queryFetch = '''SELECT * FROM Transaction_Details WHERE Transaction_Status = 'failed' AND Transaction_Date_Time BETWEEN '2022-01-01 00:00:00' AND '2022-02-01 00:00:00';'''
        else:
            queryFetch = '''SELECT * FROM Transaction_Details WHERE Transaction_Status = 'success' AND Transaction_Date_Time BETWEEN '2022-01-01 00:00:00' AND '2022-02-01 00:00:00';'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
        
    def group_by_accounts_query(self):
        queryFetch = '''SELECT COUNT(Account_Number) , Min_Balance_Required FROM Bank_Account GROUP BY Min_Balance_Required Having COUNT(Account_Number)>100;'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
    
    def inner_join_all_accounts_query(self):
        queryFetch = '''SELECT Account_Number, Card_Number, Cash_Withdrawl_Limit FROM Bank_Account INNER JOIN ATM_Card ON Account_Number = Linked_Account;'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
    
    def left_join_all_accounts_query(self):
        queryFetch = '''SELECT Account_Number, Card_Number, Cash_Withdrawl_Limit FROM Bank_Account LEFT JOIN ATM_Card ON Account_Number = Linked_Account;'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
    
    def inner_join_some_account_query(self):
        queryFetch = '''SELECT Account_Number, Card_Number, Cash_Withdrawl_Limit FROM Bank_Account INNER JOIN ATM_Card ON Account_Number = Linked_Account WHERE Account_Number = '11000000120';'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList
    
    def union_names_query(self):
        queryFetch = '''SELECT first_name FROM Customer UNION SELECT first_name FROM Employee ORDER BY first_name;'''
        self.connection.cur = self.connection.con.cursor()
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"], end=" ")
            myList = self.connection.cur.fetchall()
            # print(myList)
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
        return myList

    