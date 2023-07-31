from pymongo import MongoClient

class Connection:
    
    
    def _init_connection(self):
        self.DB = "Demo"
        self.HOST = "localhost"
        self.CLIENT = MongoClient("mongodb://{self.HOST}")
    
    def setDb(self, db_name):
        return self.CLIENT[db_name]
    
    def close_connection(self):
        return self.CLIENT.close()
        