from connection import Connection


class Handler:
    
    def __init__(self) -> None:
        self.connection = Connection()
        self.DB = self.connection.DB
        
    def validation(self,fname,lastname):
        DB = self.connection.setDb(self.DB)
        result = DB["users"].find_one({"first_name":fname,"last_name":lastname})
        if result:
            self.connection.close_connection()
            return {"success":True,"message":"User Exists"}
        
    def insert_data(self,data):
        fname = data["first_name"]
        lname=data["last_name"]
        DB = self.connection.setDb(self.DB)
        
        result = {
            "fist_name":fname,
            "last_name":lname
        }
        try:
            DB["users"].insert_one(result)
            self.connection.close_connection()
            return {"success":True,"message":"User Added"}
        except:
            return {"success":False,"message":"User Not Added"}
            
            
        
        