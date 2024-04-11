from flask import Flask,redirect,url_for,request,jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import json
from CRUD import *
# from CRUD import select_all


app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"

# This line is to reduce the number of warning apperaing on the terminal while running the app. 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  
# both below lines used to register the sqlalchemy instance with the flask app. we can use either of it. but using db.init_app has different method
db = SQLAlchemy(app)
# db.init_app(app)



# * Important we cannot create a database just by using the db.create_all() method. because in the 3.0 or above versions 
# of  flask-sqlalchemy are required to go with in the app_context and then use the db.create_all() function



# we use the create_all() functionality to create the database when we use sqlite3 only because using the psotgres, mysql, we need to create
# the database first manually and then create the tables only inside the database. 
# 
# create_all does not update tables if they are already in the database. If you change a model’s columns, use a migration library like 
# Alembic with Flask-Alembic or Flask-Migrate to generate migrations that update the database schema. 

# with app.app_context():
#     db.create_all()



# * IMPORTANT FLASK
# There are two methods we can use to write get,put,patch requests, 
# 1- If user sends id in route with vairable (as a parameter) like {base_url}/user?id=user_id
# 2- if user just sends id just like this route "user/5" and we capture this id=5 in the id variable in Flask 
# 
# For 1st approach we donot need to change the route (user/), user is requesting with method "GET" and passing id like 
#   {base_url}/user?id={user_id} this, we can easily check either id is passed or not by id = request.args.get("id") 
# above code, but in this approach route gets complicated for the client side 

# For 2nd approach we need to define another route like "app.rouute('/user/<int:id>', methods=["GET"])"
# and also we need to get the id as a parameter like user(id = None) 
# and we will check if id is passed then we perform a function and if id is not passed we perform something else

# I am writing code here for both scenarios

@app.route("/user", methods=["POST","GET", "PUT", "DELETE", "PATCH"])
def user():
    if request.method == "POST":
        data = request.json
        name, email = data.get("user", None),  data.get("email", None)
        if name is None or email is None:
            error = json.dumps({"Fields Error": "Required Fields Are Not Available"})
            return make_response(error, 400)
        print(name,email)
        # print(data)
        print(type(data))
        response = add_user(name,email)
        if response == True:
            response = json.dumps({"msg":"Data Added Successfully"})
            return make_response(response, 200)
        
        return make_response(json.dumps(response), 403)
    
    if request.method == "GET": 
        # everything comes as a string
        try:
            id = request.args.get("id")
            if id:
                id = int(id)
                response = select_user_by_id(id)
                # if user not found
                print("RESPONSE IS: ",response)
                if response == None:
                    error = json.dumps({"error":"User Does Not Exists"})
                    return make_response(error, 404)
                # if user found
                return make_response(json.dumps(response), 200)
            
            else:
                response = select_all()
                return make_response(json.dumps(response),200)
        
        except:
            return make_response(json.dumps({"error":"Invalid Input"}),404)

    
    if request.method == "PUT":
        try:
            id = request.args.get("id")
            name = request.args.get("name")
            print(type(name), name)
            if id:
                id = int(id)
                response,status = update_name(id,name)
                return make_response(json.dumps(response), status)
        except ValueError:
            return make_response(json.dumps({"error":"Invalid Input"}),404)
        
    
    if request.method == "DELETE":
        try: 
            id = request.args.get("id")
            print(id)
            if id:
                id = int(id)
                response,status = delete(id)
                print(response)
                print(status)
                return make_response(json.dumps(response),status)
        
        except ValueError:
            return make_response(json.dumps({"error":"Invalid Input"}), 404)



# @app.route("/user/<int:id>", methods = ["GET"])
# @app.route("/user", methods=["POST","GET", "PUT", "DELETE", "PATCH"])
# def user(id=None):
#     if request.method == "GET": 
#         # everything comes as a string
#         try:
#             # id = request.args.get("id")
#             if id:
#                 # id = int(id)
#                 response = select_user_by_id(id)
#                 # if user not found
#                 print("RESPONSE IS: ",response)
#                 if response == None:
#                     error = json.dumps({"error":"User Does Not Exists"})
#                     return make_response(error, 404)
#                 # if user found
#                 return make_response(json.dumps(response), 200)
            
#             else:
#                 response = select_all()
#                 return make_response(json.dumps(response),200)
        
#         except:
#             return make_response(json.dumps({"error":"Invalid Input"}),404)



            
if __name__ == "__main__":
    app.run(debug=True,port=5000)