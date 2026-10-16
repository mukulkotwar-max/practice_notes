
'''
path + query + body combo

vedio9
mix all input realworld api structure 

'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_list=[]

class User(BaseModel):
    name:str
    age:int

@app.post("/users")
def create_user(user:User):
    user_list.append(user)
    return{
        "message":"user added",
        "data":user
    }

@app.put("users/{user_id}")
def updated_user(user_id:int, user:User, notify:bool=False):
    if user_id < len(user_list):
        user_list[user_id]=user
        return {
            "message":"User Updated",
            "notify":notify,
            "data":user
        }
    return {
        "error":"User not found"
    }