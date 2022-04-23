import json

class RootUser:
    def __init__(self,gt,myTables):
        self.gt = gt
        self.myTables = myTables

        with open('myLib/basics/print_errors.json') as f:
            self.errors = json.load(f)
        with open('myLib/basics/print_statements.json') as fs:
            self.statements = json.load(fs)

    def print_query_menu(self,tname,req_op):
        all_ops = ["Create a new entry", "Read some entries", "Update some entries", "Delete some entries", "Read all entries", "Delete all entries"]
        print("Following operations are available for " + tname +" table : ")
        cnt = 1 
        for i in range(len(all_ops)):
            if req_op[i]==1:
                print(str(cnt) + ". " + all_ops[i])
                cnt+=1

    def execute_query(self,myt,mytname,req_ops,inp):
        cnt = 1
        ind = -1 
        for i in range(len(req_ops)):
            if req_ops[i]==1:
                if int(cnt)==int(inp):
                    ind = i
                    break
                cnt+=1

        if ind == 0:
            print("[Create a new entry]")
            self.gt.create(myt,mytname)
        elif ind == 1:
            print("[Read some entries]")
            self.gt.read(myt,mytname)
        elif ind == 2:
            print("[Update some entries]")
            self.gt.update(myt,mytname)
        elif ind == 3:
            print("[Delete some entries]")
            self.gt.delete(myt,mytname)
        elif ind == 4:
            print("[Read all entries]")
            self.gt.readAll(mytname)
        elif ind == 5:
            print("[Delete all entries]")
            self.gt.truncateAll(mytname)
        else:
            print(self.errors["input_mismatch_in_query"])

    def branch_op(self):
        mytname = self.myTables[0][0] 
        myt = self.myTables[0][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)
        # print(myt)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def bank_account_op(self):
        mytname = self.myTables[1][0] 
        myt = self.myTables[1][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)
        # print(myt)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def department_op(self):
        mytname = self.myTables[2][0] 
        myt = self.myTables[2][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)
        # print(myt)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)      

    def employee_op(self):
        mytname = self.myTables[3][0] 
        myt = self.myTables[3][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)
        # print(myt)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def branch_managed_by_op(self):
        mytname = self.myTables[4][0] 
        myt = self.myTables[4][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def customer_op(self):
        mytname = self.myTables[5][0] 
        myt = self.myTables[5][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def customer_phone_number_op(self):
        mytname = self.myTables[6][0] 
        myt = self.myTables[6][1] 
        req_ops = [1,1,0,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def collateral_op(self):
        mytname = self.myTables[7][0] 
        myt = self.myTables[7][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def documents_link_op(self):
        mytname = self.myTables[8][0] 
        myt = self.myTables[8][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def personal_customer_op(self):
        mytname = self.myTables[9][0] 
        myt = self.myTables[9][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def business_customer_op(self):
        mytname = self.myTables[10][0] 
        myt = self.myTables[10][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def savings_account_op(self):
        mytname = self.myTables[11][0] 
        myt = self.myTables[11][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def current_account_op(self):
        mytname = self.myTables[12][0] 
        myt = self.myTables[12][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def minor_account_op(self):
        mytname = self.myTables[13][0] 
        myt = self.myTables[13][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def zero_balance_account_op(self):
        mytname = self.myTables[14][0] 
        myt = self.myTables[14][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def card_op(self):
        mytname = self.myTables[15][0] 
        myt = self.myTables[15][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def debit_card_op(self):
        mytname = self.myTables[16][0] 
        myt = self.myTables[16][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def prepaid_card_op(self):
        mytname = self.myTables[17][0] 
        myt = self.myTables[17][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def atm_card_op(self):
        mytname = self.myTables[18][0] 
        myt = self.myTables[18][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def credit_card_op(self):
        mytname = self.myTables[19][0] 
        myt = self.myTables[19][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def account_linked_creditcard_op(self):
        mytname = self.myTables[20][0] 
        myt = self.myTables[20][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def loan_op(self):
        mytname = self.myTables[21][0] 
        myt = self.myTables[21][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def collateral_loan_op(self):
        mytname = self.myTables[22][0] 
        myt = self.myTables[22][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def non_collateral_loan_op(self):
        mytname = self.myTables[23][0] 
        myt = self.myTables[23][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def documents_pdf_op(self):
        mytname = self.myTables[24][0] 
        myt = self.myTables[24][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def loan_account_op(self):
        mytname = self.myTables[25][0] 
        myt = self.myTables[25][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def insurance_op(self):
        mytname = self.myTables[26][0] 
        myt = self.myTables[26][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def asset_insurance_op(self):
        mytname = self.myTables[27][0] 
        myt = self.myTables[27][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def loan_protection_insurance_op(self):
        mytname = self.myTables[28][0] 
        myt = self.myTables[28][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def term_life_insurance_op(self):
        mytname = self.myTables[29][0] 
        myt = self.myTables[29][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def medical_insurance_op(self):
        mytname = self.myTables[30][0] 
        myt = self.myTables[30][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def transaction_details_op(self):
        mytname = self.myTables[31][0] 
        myt = self.myTables[31][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def passbook_op(self):
        mytname = self.myTables[32][0] 
        myt = self.myTables[32][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def upi_op(self):
        mytname = self.myTables[33][0] 
        myt = self.myTables[33][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def upi_transactions_op(self):
        mytname = self.myTables[34][0] 
        myt = self.myTables[34][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def bill_payment_op(self):
        mytname = self.myTables[35][0] 
        myt = self.myTables[35][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def card_transactions_op(self):
        mytname = self.myTables[36][0] 
        myt = self.myTables[36][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def auto_payment_op(self):
        mytname = self.myTables[37][0] 
        myt = self.myTables[37][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def auto_payment_loan_op(self):
        mytname = self.myTables[38][0] 
        myt = self.myTables[38][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def auto_bill_payment_op(self):
        mytname = self.myTables[39][0] 
        myt = self.myTables[39][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def transaction_log_op(self):
        mytname = self.myTables[40][0] 
        myt = self.myTables[40][1] 
        req_ops = [1,1,0,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def ad_channel_op(self):
        mytname = self.myTables[41][0] 
        myt = self.myTables[41][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def advertisement_op(self):
        mytname = self.myTables[42][0] 
        myt = self.myTables[42][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def user_credential_op(self):
        mytname = self.myTables[43][0] 
        myt = self.myTables[43][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def employee_credential_op(self):
        mytname = self.myTables[44][0] 
        myt = self.myTables[44][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def closed_account_op(self):
        mytname = self.myTables[45][0] 
        myt = self.myTables[45][1] 
        req_ops = [1,1,0,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def blocked_card_op(self):
        mytname = self.myTables[46][0] 
        myt = self.myTables[46][1] 
        req_ops = [1,1,0,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def fixed_deposit_op(self):
        mytname = self.myTables[47][0] 
        myt = self.myTables[47][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def recurring_deposit_op(self):
        mytname = self.myTables[48][0] 
        myt = self.myTables[48][1] 
        req_ops = [1,1,1,1,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def chequebook_op(self):
        mytname = self.myTables[49][0] 
        myt = self.myTables[49][1] 
        req_ops = [1,1,0,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def bank_statement_op(self):
        mytname = self.myTables[50][0] 
        myt = self.myTables[50][1] 
        req_ops = [1,1,0,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def otps_op(self):
        mytname = self.myTables[51][0] 
        myt = self.myTables[51][1] 
        req_ops = [1,1,0,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def installment_op(self):
        mytname = self.myTables[52][0] 
        myt = self.myTables[52][1] 
        req_ops = [1,1,1,0,1,1]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
