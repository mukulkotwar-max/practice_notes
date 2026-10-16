from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

TODO = []

class Todo_schema(BaseModel):
    id:int
    name:str
    status:bool

@app.post("/todo_add")
def add_todo(todo_add:Todo_schema):
    TODO.append(todo_add)
    return {
        "meassage":"item added to the list",
        "data":todo_add
    }


@app.get("/get_todos")
def get_todos():
    return TODO

@app.get("/get_todo")
def get_todo(todo_id:int):
    for i in TODO:
        if i.id == todo_id:
            return i
    return{"error":"todo not found"}

@app.put("/put_todo/{todo_id}")
def update_todo(todo_id:int, updated_todo:Todo_schema):
    for index,i in enumerate(TODO):
        if i.id == todo_id:
            TODO[index]=updated_todo
            return{
                "message":"data updated",
                "data": updated_todo
            }
    return{"error": "todo not found"}


@app.delete("/delete/{todo_id}")
def del_todo(todo_id:int):
    for index,i in enumerate(TODO):
        if i.id == todo_id:
            TODO.pop(index)
            return {"message":"data deleted"}

    return {"error":" todo not found"}