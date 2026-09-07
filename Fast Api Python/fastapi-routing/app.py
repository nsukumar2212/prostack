from fastapi import FastAPI

app=FastAPI()

@app.get("/")

def home_page():
    return {"message": "Welcome to the Home Page!"}