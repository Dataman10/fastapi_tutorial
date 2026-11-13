from fastapi import FastAPI
app = FastAPI()

@app.post("/zashu")
def ret(users : dict):
    return {
        "message" : "User Created",
        "dict" : users
}

