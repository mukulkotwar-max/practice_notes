from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

TODO = []

class todo_format(BaseModel):
    id:int
    tittle: str
    completed : bool

@app.post("/todos")
def create_todo(todos:todo_format):
    TODO.append(todos)
    return{
        "message":"todo list updated ",
        "data":todos
    }



@app.get("/todos")
def get_todos():
    return TODO

@app.get("/todos/{todo_id}")
def get_id(todo_id:int):
    for x in TODO:
        if x.id == todo_id:
            return x
    return{
        "error":"todo_id not found"
    }


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, update_todo:todo_format):
    for index, x in enumerate(TODO):
        if x.id == todo_id:
            x[index]= update_todo
            return{
                "message":"data updated",
                "data":update_todo
            }
    return{ "error":"no such id exist"}


