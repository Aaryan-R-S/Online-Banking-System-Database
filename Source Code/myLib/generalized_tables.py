import json

class Gen_Table:
    def __init__(self, myBf):
        self.bf = myBf
        with open('myLib/basics/print_errors.json') as f:
            self.errors = json.load(f)
        with open('myLib/basics/print_statements.json') as fs:
            self.statements = json.load(fs)
            
    def create(self, myTable, myTableName):
        myDict = {}
        lis = list(myTable.items())
        try:
            for i in range(len(lis)):
                myDict[lis[i][0]] = input(lis[i][1])
            queryObj = {
                "relation": myTableName,
                "op_type": "c",
                "data": myDict
            }
            self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
            
    def create_custom(self, myTable, myTableName, key, val):
        myDict = {}
        lis = list(myTable.items())
        try:
            for i in range(len(lis)):
                myDict[lis[i][0]] = input(lis[i][1])
            myDict[key] = val
            queryObj = {
                "relation": myTableName,
                "op_type": "c",
                "data": myDict
            }
            self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)

    def read(self, myTable, myTableName, primary_key=None):
        myDict = {}   
        lis = list(myTable.items())
        try:
            if primary_key!=None:
                myDict[lis[0][0]] = primary_key
            else:
                myDict[lis[0][0]] = input(lis[0][1])
            queryObj = {
                "relation": myTableName,
                "op_type": "r",
                "data": myDict
            }
            return self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def read_custom(self, myTable, myTableName, key, val):
        myDict = {}   
        lis = list(myTable.items())
        try:
            myDict[key] = val
            queryObj = {
                "relation": myTableName,
                "op_type": "r",
                "data": myDict
            }
            return self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
    
    def update(self, myTable, myTableName, primary_key=None):
        myDict = {}
        lis = list(myTable.items())
        try:
            if primary_key!=None:
                myDict[lis[0][0]] = primary_key
            else:
                myDict[lis[0][0]] = input(lis[0][1])
            print("Press enter if you do not want to update the entry!")
            for i in range(1, len(lis)):
                myDict[lis[i][0]] = input(lis[i][1])
            delList = []
            for k, v in myDict.items():
                if v == "":
                    delList.append(k)
            for k in delList:
                myDict.pop(k, None)
            queryObj = {
                "relation": myTableName,
                "op_type": "u",
                "data": myDict
            }
            self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
          
    def update_custom(self, myTable, myTableName, key, val):
        myDict = {}
        lis = list(myTable.items())
        try:
            myDict[key] = val
            print("Press enter if you do not want to update the entry!")
            for i in range(0, len(lis)):
                myDict[lis[i][0]] = input(lis[i][1])
            myDict[key] = val
            delList = []
            for k, v in myDict.items():
                if v == "":
                    delList.append(k)
            for k in delList:
                myDict.pop(k, None)
            queryObj = {
                "relation": myTableName,
                "op_type": "u",
                "data": myDict
            }
            self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
          
    def delete(self, myTable, myTableName):
        myDict = {}
        lis = list(myTable.items())
        try:
            myDict[lis[0][0]] = input(lis[0][1])
            queryObj = {
                "relation": myTableName,
                "op_type": "d",
                "data": myDict
            }
            self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
          
    def delete_custom(self, myTable, myTableName, key, val):
        myDict = {}
        lis = list(myTable.items())
        try:
            myDict[key] = val
            queryObj = {
                "relation": myTableName,
                "op_type": "d",
                "data": myDict
            }
            self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
      
    def readAll(self, myTableName):
        myDict = {}
        try:
            myDict["1"] = "1"
            queryObj = {
                "relation": myTableName,
                "op_type": "r",
                "data": myDict
            }
            return self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)
        
    def truncateAll(self, myTableName):
        myDict = {}
        try:
            myDict["1"] = "1"
            queryObj = {
                "relation": myTableName,
                "op_type": "d",
                "data": myDict
            }
            self.bf.run_query(queryObj)
        except Exception as e:
            print(self.errors["input_mismatch_in_query"])
            print(e)