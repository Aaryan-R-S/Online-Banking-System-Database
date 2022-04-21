import json

class root_user:

    def __init__(self,myBf):
        self.bf=myBf
        with open('myLib/basics/print_errors.json') as f:
            self.error = json.load(f)
        with open('myLib/basics/print_statements.json') as fs:
            self.success = json.load(fs)

    def query_create(slef):
        
