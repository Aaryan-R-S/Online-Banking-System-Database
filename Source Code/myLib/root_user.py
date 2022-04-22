import json

class root_user:

    def __init__(self,gt,myTables):
        self.gt = gt
        self.myTables = myTables

        with open('myLib/basics/print_errors.json') as f:
            self.errors = json.load(f)
        with open('myLib/basics/print_statements.json') as fs:
            self.statements = json.load(fs)

    def branch_op(self):

        mytname = self.myTables[0][0] 
        myt = self.myTables[0][1] 

        print(mytname)
        print(myt)

        print("Following operations are available for this table : ")
        print("1. Create")
        print("2. Read")
        print("3. Update")
        print("4. Read all")
        print("5. Delete all")

        try:
            
            inp = input("Enter your choice : ")

            if inp == "1":
                self.gt.create(myt,mytname)
            elif inp == "2":
                self.gt.read(myt,mytname)
            elif inp == "3":
                self.gt.update(myt,mytname)
            elif inp == "4":
                self.gt.readAll(mytname)
            elif inp == "5":
                self.gt.truncateAll(mytname)
            else:
                print(self.errors["invalid_input"])
            
        
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)




        
