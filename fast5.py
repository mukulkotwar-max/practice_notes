from fastapi import FastAPI,  Depends,Header,HTTPException
from pydantic import BaseModel

app=FastAPI()

'''
video 13 depends()- Depends is FastAPI’s built-in tool to declare a dependency inside route parameters.
Dependency Injection is a design pattern where a function or object receives the other functions, 
resources, or objects it depends on from the outside, 
rather than instantiating them internally.

'''



def comman_logic():
    return{
        "messsage":"common logic excecuted "
    }

@app.get("/home")
def home(data=Depends(comman_logic)):
    return data

def get_current_user():
    return{
        "user":"Mohit"
    }

@app.get("/profile")
def profile(user = Depends(get_current_user)):
    return user    #getting the user from the above function 


@app.get("/dashboard")
def dashboard(user= Depends(get_current_user)):
    return user


#----------------------------------------------



