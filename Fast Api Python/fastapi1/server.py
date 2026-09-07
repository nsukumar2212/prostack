from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home_page():
    return {"message": "Welcome to the FastAPI application!"}

def about_page():
    return {"message": "About this FastAPI application."}