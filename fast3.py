from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

'''
 reposne model , data validation, hide sensitive data 

video 10 - repo branch Response-Model

reponse model & request model 

request model - when we need info from the client ,like form filling 
data(JSON format) which is sent by the client (in request body)

response model - data sent to the client 



here we are making pass word hiding process
'''

class User(BaseModel):
    name:str
    age:int
    password:str

class UserResponse(BaseModel): #data sent shown to client
    name:str
    age:int

@app.get("/user", response_model=UserResponse)
def get_user():
    return{
        "name":"MK",
        "age":12,
        "password":"123456"
    }