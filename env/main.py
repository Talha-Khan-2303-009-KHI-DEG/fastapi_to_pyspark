from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()

@app.get("/")
async def root():
    return{"message": "hello world"}

@app.post("/")
async def post():
    return{"message": "hello world from post"}

@app.put("/")
async def put():
    return{"message": "hello world from put"}

# @app.get("/items")
# async def List_items():
#     return{"message": "list items from route"}

# @app.get("/items/{item_id}")
# async def get_items(item_id: int):
#     return{"item_id": item_id}

@app.get("/users")
async def List_users():
    return{"message": "list users route"}

@app.get("/users/me")
async def get_current_user():
    return{"message": "this is the current user"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return{"user_id": user_id}

class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"
    
@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "you're healthy"}
    
    if food_name.value == 'fruits':
        return {"foodname": food_name, "message": "you're still healthy"}
    
    return {"food_name": food_name, "message": "I like choclate shake"}

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(
    item_id: str, sample_query_param: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "sample_query_param": sample_query_param}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
            }
        )
    return item

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut consectetur."
            }
        )
    return item