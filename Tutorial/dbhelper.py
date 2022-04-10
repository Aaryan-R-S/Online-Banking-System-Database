import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            database='pythontest'
        )
        queryCreateDB='''
            CREATE DATABASE IF NOT EXISTS Pythontest
        '''
        queryCreateTable='''
            CREATE TABLE IF NOT EXISTS User(
                userId int primary key,
                userName VARCHAR(200),
                phone VARCHAR(12)
            ) 
        '''
        cur = self.con.cursor()
        cur.execute(queryCreateDB)
        cur.execute(queryCreateTable)
        print("[Connected to Database]")
        
    def insert_user(self, userId, userName, phone):
        queryInsertUser = '''
            INSERT INTO User VALUES('{}','{}','{}')
        '''.format(userId, userName, phone)
        cur = self.con.cursor()
        cur.execute(queryInsertUser)
        self.con.commit()
        print('[User Inserted]')
    
    def fetch_all(self):
        queryFetchData = '''
            SELECT * FROM User
        '''
        cur = self.con.cursor()
        cur.execute(queryFetchData)
        for row in cur:
            print(row)
        print('[Fetched All User]')
        
    def delete_user(self, userId):
        queryDeleteUser = f'''
            DELETE FROM User WHERE userId={userId}
        '''
        cur = self.con.cursor()
        cur.execute(queryDeleteUser)
        self.con.commit()
        print('[Deleted User]')
        
    def update_user(self, userId, userName, phone):
        queryUpdateUser = f'''
            UPDATE User SET userName='{userName}', phone='{phone}' WHERE userId={userId}
        '''
        cur = self.con.cursor()
        cur.execute(queryUpdateUser)
        self.con.commit()
        print('[Updated User]')
    
if __name__ =="__main__":
    helper = DBHelper()
    # helper.insert_user(1000, "Res Nae", "9912404528")
    # helper.insert_user(1001, "Bes Dae", "9924023528")
    # helper.insert_user(1003, "Ves Gae", "9952s404528")
    # helper.insert_user(1002, "Hes Oae", "9912404554")
    # helper.insert_user(1005, "Aes Pae", "9240454328")
    # helper.insert_user(1004, "Yes Lae", "8491204528")
    # helper.delete_user(1003)
    # helper.fetch_all()
    # helper.update_user(1003, "Tes Bae", "8359304567")
    helper.fetch_all()

    