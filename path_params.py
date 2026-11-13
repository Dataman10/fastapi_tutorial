from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello fastapi"
    }


@app.get("/users/{user_id}")
def users(user_id):
    return {
     "user_id": user_id   
   }


@app.get("/products/{item_id}")
def products(item_id : int):
    return {
        "id" :item_id 
    }