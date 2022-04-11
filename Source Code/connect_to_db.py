import mysql.connector as connector
import json

class DBConnector:
    def __init__(self):
        try:
            self.con = connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='root',
                database='online_banking_system'
            )
            self.cur = self.con.cursor()
            with open('print_errors.json') as fe:
                self.errors = json.load(fe)
            with open('print_statements.json') as fs:
                self.statements = json.load(fs)
            print(self.statements["connected_to_db"])

        except Exception as e:
            print(self.errors["not_connected_to_db"])
            print(e)

if __name__ =="__main__":
    print("Connecting to Database...")
    helper = DBConnector()
    print("Program exited")
    