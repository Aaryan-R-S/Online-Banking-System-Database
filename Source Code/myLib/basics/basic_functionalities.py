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
            self.fetch_query(query_obj)
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
            print(self.statements["query_success"])
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
        try:
            self.connection.cur.execute(queryFetch)
            print(self.statements["query_success"])
            print(self.connection.cur.fetchall())
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records fetched.")
            else:
                print(self.connection.cur.rowcount, "record fetched.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
    
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
            print(self.statements["query_success"])
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
            print(self.statements["query_success"])
            if self.connection.cur.rowcount>1:
                print(self.connection.cur.rowcount, "records deleted.")
            else:
                print(self.connection.cur.rowcount, "record deleted.")
        except Exception as e:
            print(self.errors["invalid_query"])
            print(e)
