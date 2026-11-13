from fastapi import FastAPI

app = FastAPI()

# home route 
@app.get('/')
def home():
    return {
        "message" : "Hello World!"
    }


@app.get("/about")
def about():
    return {
        "message": "About page"
    }

@app.get("/contact")
def contact():
    return{
        "contact_info":[
            {
                "name": "Hitesh",
                "phone": 1234567890,
                "email": "[EMAIL_ADDRESS]"
            },
            {
                "name": "Hitesh",
                "phone": 1234567890,
                "email": "[EMAIL_ADDRESS]"
            }
        ]
    }