import json
from myLib.basics import connect_to_db
from myLib.basics import basic_functionalities as bf
from myLib import generalized_tables as GT
from myLib import root_user as ru

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

myrootuser = ru.root_user(myTable,lis)
myrootuser.branch_op()

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