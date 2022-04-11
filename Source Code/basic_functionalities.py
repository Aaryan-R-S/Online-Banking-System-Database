import json
import connect_to_db

class RunQuery:
    # query_obj = {
    #     "relation" : "r_name",
    #     "op_type" : "c",    # OR "r", "u", "d"
    #     "data": {"f_name_1":"val_1", "f_name_2":"val_2"}, 
    #     # "c" (all fields in sorted order) 
    #     # "r" (one field)
    #     # "u" (first field 'where' and second field 'set')
    #     # "d" (one field)
    # } 
    
    def __init__(self):
        self.connection = connect_to_db.DBConnector()
        with open('print_errors.json') as f:
            self.errors = json.load(f)
    
    def run_query(self, query_obj):
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
        pass
    
    def fetch_query(self, query_obj):
        pass
    
    def update_query(self, query_obj):
        pass
    
    def delete_query(self, query_obj):
        pass

if __name__ == "__main__":
    runQuery = RunQuery()
    myObj = {
        "op_type":"d"
    }
    runQuery.run_query(myObj)
    print("[Program Exited]")