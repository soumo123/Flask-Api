from flask import Flask,request
import json
from handler import Handler  
  
  
app = Flask(__name__)

#Trial 1

@app.route("/")
def home():
    return "Testing here"

@app.route("/<name>")
def setname(name):
    return f"hey {name}"

@app.route("/login",methods=['GET'])
def login():
    name = request.args.get('name')  # by pasing name as query
    return name

# @app.route("/sign-up",methods=["POST"])
# def register():
#     data = request.get_json()
#     fname = data["first_name"]
#     lname = data["last_name"]
#     with open("data.json") as file:
#         json_data = json.load(file)
    
#     for new_data in json_data:
#         j_f_name ,j_l_name= new_data["first_name"],new_data["last_name"]
#         if(j_f_name==fname and j_l_name==lname):
#             return {
#                 "success":True,
#                 "message":"Login Success"
#             }
#         return {
#             "success":False,
#             "message":"Login Fail"
#         }
        


# @app.route("/sign-up",methods=["POST"])
# def register():
#     data = request.get_json()
#     fname = data["first_name"]
#     lname = data["last_name"]
 
#     DB = client["Demo"]
    
#     result = DB["Users"].find_one({"first_name":fname,"last_name":lname})
#     if result:
#         client.close()
#         return {
#                 "success":True,
#                 "message":"Login Success"
#             }
            
#     client.close()
#     return {
#             "success":False,
#             "message":"Login Fail"
#         }
    




@app.route("/login",methods=["POST"])
def login():
    data = request.get_json()
    fname = data["first_name"]
    lname = data["last_name"]
 
    handler = Handler()
    result = handler.validation(fname,lname)
    return result , 200




@app.route("/insert",methods=["POST"])
def login():
    data = request.get_json()
 
    handler = Handler()
    result = handler.validation(data)
    return result , 200



if __name__ == "__main__":
    app.run()