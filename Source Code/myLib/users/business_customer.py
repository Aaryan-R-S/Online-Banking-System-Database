import json

class BusinessCustomer:
    def __init__(self,gt,myTables,bc_id):
        self.gt = gt
        self.myTables = myTables
        self.bc_id = bc_id
        self.bank_accounts = []
        self.loan_ids = []
        self.policy_ids = []
        self.upi_ids = []
        temp = self.gt.read_custom(self.myTables[12][1],self.myTables[12][0],"cin",self.bc_id)
        if temp!=[]:
            self.bank_accounts.append(temp[0][0])
        temp = self.gt.read_custom(self.myTables[21][1],self.myTables[21][0],"loan_given_to",self.bc_id)
        if temp!=[]:
            for i in range(len(temp)):
                self.loan_ids.append(temp[i][0])
        temp = self.gt.read_custom(self.myTables[26][1],self.myTables[26][0],"nominee_id",self.bc_id)
        if temp!=[]:
            for i in range(len(temp)):
                self.policy_ids.append(temp[i][0])
        temp = []
        for i in self.bank_accounts:
            temp2 = self.gt.read_custom(self.myTables[33][1],self.myTables[33][0],"account_number_linked",i)
            if temp2 != []:
                temp+=temp2
        if temp!=[]:
            for i in range(len(temp)):
                self.upi_ids.append(temp[i][0])
        # print(self.bank_accounts)
        # print(self.loan_ids)
        # print(self.policy_ids)
        # print(self.upi_ids)
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

    def execute_query(self,myt,mytname,req_ops,inp,key=None,bc_id=None):
        cnt = 1
        ind = -1 
        for i in range(len(req_ops)):
            if req_ops[i]==1:
                if int(cnt)==int(inp):
                    ind = i
                    break
                cnt+=1

        if ind == 0:
            if bc_id != None:
                self.gt.create_custom(myt,mytname,key,bc_id)
            else:
                print("[Create a new entry]")
                self.gt.create(myt,mytname)
        elif ind == 1:
            if bc_id != None:
                return self.gt.read_custom(myt,mytname,key,bc_id)
            else:
                print("[Read some entries]")
                return self.gt.read(myt,mytname)
        elif ind == 2:
            if bc_id != None:
                self.gt.update_custom(myt,mytname,key,bc_id)
            else:
                print("[Update some entries]")
                self.gt.update(myt,mytname)
        elif ind == 3:
            if bc_id != None:
                self.gt.delete_custom(myt,mytname,key,bc_id)
            else:
                print("[Delete some entries]")
                self.gt.delete(myt,mytname)
        # elif ind == 4:
        #     print("[Read all entries]")
        #     self.gt.readAll(mytname)
        # elif ind == 5:
        #     print("[Delete all entries]")
        #     self.gt.truncateAll(mytname)
        else:
            print(self.errors["input_mismatch_in_query"])

# to set
    def bank_account_op(self, acc_num):
        mytname = self.myTables[1][0] 
        myt = self.myTables[1][1] 
        req_ops = [0,1,1,0,0,0]

        # print(mytname)
        # print(myt)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp,"account_number",acc_num)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def customer_phone_number_op(self):
        mytname = self.myTables[6][0] 
        myt = self.myTables[6][1] 
        req_ops = [1,1,0,1,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def current_account_op(self):
        mytname = self.myTables[12][0] 
        myt = self.myTables[12][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            # self.print_query_menu(mytname,req_ops)
            # inp = input("Enter your choice : ")
            acc_num = self.execute_query(myt,mytname,req_ops,2,"cin",self.bc_id)
            # print(acc_num)
            if acc_num==[]:
                print(self.statements["nothing_found"])
            else:
                return self.bank_account_op(acc_num[0][0])
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def card_op(self, card_num):
        mytname = self.myTables[15][0] 
        myt = self.myTables[15][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp,"card_number",card_num)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def debit_card_op(self):
        mytname = self.myTables[16][0] 
        myt = self.myTables[16][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            # self.print_query_menu(mytname,req_ops)
            inp = input(myt["linked_account"])
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            elif int(inp) in self.bank_accounts:
                card_num = self.execute_query(myt,mytname,req_ops,2,"linked_account",inp)
            else:
                print(self.errors["invalid_account_access"])
                return
            # print(acc_num)
            if card_num==[]:
                print(self.statements["nothing_found"])
            else:
                return self.card_op(card_num[0][0])
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def atm_card_op(self):
        mytname = self.myTables[18][0] 
        myt = self.myTables[18][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            # self.print_query_menu(mytname,req_ops)
            # inp = input("Enter your choice : ")
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            inp = input(myt["linked_account"])
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            elif int(inp) in self.bank_accounts:
                card_num = self.execute_query(myt,mytname,req_ops,2,"linked_account",inp)
            else:
                print(self.errors["invalid_account_access"])
                return
            # print(acc_num)
            if card_num==[]:
                print(self.statements["nothing_found"])
            else:
                return self.card_op(card_num[0][0])
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def credit_card_op(self):
        mytname = self.myTables[19][0] 
        myt = self.myTables[19][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            # self.print_query_menu(mytname,req_ops)
            # inp = input("Enter your choice : ")
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            card_num = self.execute_query(myt,mytname,req_ops,2,"cin",self.bc_id)
            # print(acc_num)
            if card_num==[]:
                print(self.statements["nothing_found"])
            else:
                return self.card_op(card_num[0][0])
            
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def account_linked_creditcard_op(self):
        mytname = self.myTables[20][0] 
        myt = self.myTables[20][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            # self.print_query_menu(mytname,req_ops)
            # inp = input("Enter your choice : ")
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            inp = input(myt["linked_account"])
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            elif int(inp) in self.bank_accounts:
                card_num = self.execute_query(myt,mytname,req_ops,2,"linked_account",inp)
            else:
                print(self.errors["invalid_account_access"])
                return
            # print(acc_num)
            if card_num==[]:
                print(self.statements["nothing_found"])
            else:
                return self.card_op(card_num[0][0])
            
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def loan_op(self):
        mytname = self.myTables[21][0] 
        myt = self.myTables[21][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp,"loan_given_to",self.bc_id)
            
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def collateral_loan_op(self):
        mytname = self.myTables[22][0] 
        myt = self.myTables[22][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.loan_ids == []:
                print(self.statements["nothing_found"])
                return
            for i in self.loan_ids:
                temp2 = self.execute_query(myt,mytname,req_ops,inp,"loan_id",i)
                if temp2!=[]:
                    temp+=temp2
            return temp
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def non_collateral_loan_op(self):
        mytname = self.myTables[23][0] 
        myt = self.myTables[23][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.loan_ids == []:
                print(self.statements["nothing_found"])
                return
            for i in self.loan_ids:
                temp2 = self.execute_query(myt,mytname,req_ops,inp,"loan_id",i)
                if temp2!=[]:
                    temp+=temp2
            return temp
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def loan_account_op(self):
        mytname = self.myTables[25][0] 
        myt = self.myTables[25][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.loan_ids == []:
                print(self.statements["nothing_found"])
                return
            if inp=="2":
                for i in self.loan_ids:
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"loan_id",i)
                    if temp2!=[]:
                        temp+=temp2
                return temp
            else:
                self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def insurance_op(self):
        mytname = self.myTables[26][0] 
        myt = self.myTables[26][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp,"nominee_id",self.bc_id)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def asset_insurance_op(self):
        mytname = self.myTables[27][0] 
        myt = self.myTables[27][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.policy_ids == []:
                print(self.statements["nothing_found"])
                return
            for i in self.policy_ids:
                temp2 = self.execute_query(myt,mytname,req_ops,inp,"policy_id",i)
                if temp2!=[]:
                    temp+=temp2
            return temp
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def loan_protection_insurance_op(self):
        mytname = self.myTables[28][0] 
        myt = self.myTables[28][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.loan_ids == []:
                print(self.statements["nothing_found"])
                return
            for i in self.loan_ids:
                temp2 = self.execute_query(myt,mytname,req_ops,inp,"loan_id",i)
                if temp2!=[]:
                    temp+=temp2
            return temp
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def transaction_details_op(self):
        mytname = self.myTables[31][0] 
        myt = self.myTables[31][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            if inp=="2":
                for i in self.bank_accounts:
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"from_account_number",i)
                    if temp2!=[]:
                        temp+=temp2
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"to_account_number",i)
                    if temp2!=[]:
                        temp+=temp2
                return temp
            else:
                self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def passbook_op(self):
        mytname = self.myTables[32][0] 
        myt = self.myTables[32][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            inp = input(myt["passbook_account_number"])
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            elif int(inp) in self.bank_accounts:
                pass_books = self.execute_query(myt,mytname,req_ops,2,"passbook_account_number",inp)
            else:
                print(self.errors["invalid_account_access"])
                return
            # print(acc_num)
            if pass_books==[]:
                print(self.statements["nothing_found"])
            else:
                return pass_books
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def upi_op(self):
        mytname = self.myTables[33][0] 
        myt = self.myTables[33][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            inp = input(myt["account_number_linked"])
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            elif int(inp) in self.bank_accounts:
                upi_ids = self.execute_query(myt,mytname,req_ops,2,"account_number_linked",inp)
            else:
                print(self.errors["invalid_account_access"])
                return
            # print(acc_num)
            if upi_ids==[]:
                print(self.statements["nothing_found"])
            else:
                return upi_ids
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def upi_transactions_op(self):
        mytname = self.myTables[34][0] 
        myt = self.myTables[34][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.upi_ids == []:
                print(self.statements["nothing_found"])
                return
            if inp=="2":
                for i in self.upi_ids:
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"from_upi_id",i)
                    if temp2!=[]:
                        temp+=temp2
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"to_upi_id",i)
                    if temp2!=[]:
                        temp+=temp2
                return temp
            else:
                self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def bill_payment_op(self):
        mytname = self.myTables[35][0] 
        myt = self.myTables[35][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def card_transactions_op(self):
        mytname = self.myTables[36][0] 
        myt = self.myTables[36][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def auto_payment_op(self):
        mytname = self.myTables[37][0] 
        myt = self.myTables[37][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            if inp=="2":
                for i in self.bank_accounts:
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"autodebit_account_number",i)
                    if temp2!=[]:
                        temp+=temp2
                return temp
            else:
                self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def auto_payment_loan_op(self):
        mytname = self.myTables[38][0] 
        myt = self.myTables[38][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            if inp=="2":
                for i in self.bank_accounts:
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"linked_loan_account",i)
                    if temp2!=[]:
                        temp+=temp2
                return temp
            else:
                self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def auto_bill_payment_op(self):
        mytname = self.myTables[39][0] 
        myt = self.myTables[39][1] 
        req_ops = [1,1,1,0,0,0]

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
        req_ops = [0,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp,"user_id",self.bc_id)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
 
    def closed_account_op(self):
        mytname = self.myTables[45][0] 
        myt = self.myTables[45][1] 
        req_ops = [1,1,0,1,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            if inp=="2":
                for i in self.bank_accounts:
                    temp2 = self.execute_query(myt,mytname,req_ops,inp,"account_number",i)
                    if temp2!=[]:
                        temp+=temp2
                return temp
            else:
                self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def blocked_card_op(self):
        mytname = self.myTables[46][0] 
        myt = self.myTables[46][1] 
        req_ops = [1,1,0,1,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def chequebook_op(self):
        mytname = self.myTables[49][0] 
        myt = self.myTables[49][1] 
        req_ops = [1,1,0,0,0,0]

        # print(mytname)

        try:
            inp = input(myt["account_number"])
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            elif int(inp) in self.bank_accounts:
                pass_books = self.execute_query(myt,mytname,req_ops,2,"account_number",inp)
            else:
                print(self.errors["invalid_account_access"])
                return
            # print(acc_num)
            if pass_books==[]:
                print(self.statements["nothing_found"])
            else:
                return pass_books
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def bank_statement_op(self):
        mytname = self.myTables[50][0] 
        myt = self.myTables[50][1] 
        req_ops = [0,1,0,0,0,0]

        # print(mytname)

        try:
            inp = input(myt["account_number"])
            # self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
            if self.bank_accounts == []:
                print(self.statements["nothing_found"])
                return
            elif int(inp) in self.bank_accounts:
                pass_books = self.execute_query(myt,mytname,req_ops,2,"account_number",inp)
            else:
                print(self.errors["invalid_account_access"])
                return
            # print(acc_num)
            if pass_books==[]:
                print(self.statements["nothing_found"])
            else:
                return pass_books
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def otps_op(self):
        mytname = self.myTables[51][0] 
        myt = self.myTables[51][1] 
        req_ops = [1,1,0,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            return self.execute_query(myt,mytname,req_ops,inp,"cin",self.bc_id)
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def installment_op(self):
        mytname = self.myTables[52][0] 
        myt = self.myTables[52][1] 
        req_ops = [1,1,1,0,0,0]

        # print(mytname)

        try:
            self.print_query_menu(mytname,req_ops)
            inp = input("Enter your choice : ")
            temp = []
            if self.loan_ids == []:
                print(self.statements["nothing_found"])
                return
            for i in self.loan_ids:
                temp2 = self.execute_query(myt,mytname,req_ops,inp,"loan_id",i)
                if temp2!=[]:
                    temp+=temp2
            return temp
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
