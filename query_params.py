from fastapi import FastAPI
app = FastAPI()

@app.get("/users")
def get_users(name : str = "Zoro" , prof: str = "Swordsman"):
    return {
        "name" : name,
        "prof" : prof
    }