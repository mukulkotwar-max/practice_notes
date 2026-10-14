from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"Hello": "World at home"}

'''
  we have made a object of FastAPI() called app , now using a get function which just shows
  the information on the specific url here it ("/") is nothing but a localhost:8000 which we normaly called as home 
  similarly the ("/users") which shows the info of the users which is defined in the function below  
'''


@app.get("/users")
def user_id():
    return{
        'users' : ['mohit','ram','krishna']
    }




#  dynamic routes 
@app.get("/get_users/{user_id}")
def get_users(user_id: int):
    return{"user_id":user_id}

'''
# dynamic routing allows a single url pattern to capture variable values direclty from the path insted of
 hardcoding separate routes for each value
'''


'''
In FastAPI, you define dynamic segments using curly braces {variable_name}, which are passed directly to your view 
function as arguments: Data Type Validation
Without type hints, dynamic route parameters default to raw strings. Data type validation forces incoming inputs
to conform to a specific type (e.g., int, float, str, UUID).

In FastAPI, adding standard Python type annotations triggers automatic type parsing and validation powered by Pydantic:



What is the Docs Page?
The /docs page in FastAPI is an interactive, auto-generated web interface
powered by Swagger UI (using the OpenAPI standard).

Whenever you define an endpoint, path parameter, query parameter, or request body in Python, FastAPI automatically 
compiles that information into an OpenAPI schema and serves it as an interactive visual dashboard at:

'''


# -------------------------------------
# Query parameters
# 
#  Query (/users?role=admin) 
# 
#  Filters, searches, or sorts the results

# here we are loking for the user hows role is admin


#  Optional parameter - 

@app.get("/users")
def get_users(name: str= None):
    return{"name":name}


#  here the optional paramter is str= none , it helps to avoide error and returns none


#  defaault value
'''
used when we need to set some default values and can be 
changed when we want , we are some as deafult

'''
@app.get("/products")
def get_products(limit:int = 10):
    return{"limit":limit}


#  if we set http://127.0.0.1:8080/products?limit=200
# then will get     {"limit":200} in the output



# mutliple query parameters

@app.get("/items")
def get_items(name:str= None, price : int= 0 ):
    return {
        "name" : name,
        "price" : price 
    }


# request body  - is the information sent from the client to the backend 
# eg filling a form -- this is done by post reqest and this all is done in JSON format 
# we can test get resuest on browser but for post (also put, delete, patch ) request we need to use  swager ui

@app.post("/user_maker")
def user_maker(name:str, age:int):
    return{
        "name":name,
        "age":age
    }

# when we open the swager ui will get the page where will see 
# get post and all the other methods ,when we open the post
# will see the /user_maker and name and age will get in the boxs and then  will click try it our
# and then  will see the response if we pass the proper feild in the proper datatype 

# http://127.0.0.1:8080/user_maker?name=mukul&age=45
# this is the request url will get 

@app.post("/create_user")
def create_user(user:dict):
    return{
        "message":"user created",
        "data":user
    }