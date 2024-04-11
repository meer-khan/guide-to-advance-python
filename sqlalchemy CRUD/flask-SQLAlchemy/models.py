
from app import app , db
from datetime import datetime


# to create a DB we use db.create_all() function, we can use it in direct or or we can do it with the help of the python terminal 
# by typing the python in the terminal accessing the terminal, importing the "db" from "app" and typing the code 
# db.create_all() 
# this will create the sqlite file in the same directory that we can open it in the DB Browser





class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column (db.String(50))
    email = db.Column(db.String(100), unique=True)  
    date_joined = db.Column(db.Date, default = datetime.utcnow)
    
    # def __repr__(self):
    #     # return f"<User: {self.email}, Name: {self.name}>"
    #     return {"name":self.name, "email": self.email} 