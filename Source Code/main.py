import json
from myLib.basics import connect_to_db
from myLib.basics import basic_functionalities as bf
from myLib import generalized_tables as GT

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
currTableName = lis[0][0]
currTable = lis[0][1]

# myTable.create(currTable, currTableName)
# myTable.read(currTable, currTableName)
# myTable.update(currTable, currTableName)
# myTable.delete(currTable, currTableName)
# myTable.readAll(currTableName)
# myTable.truncateAll(currTableName)

