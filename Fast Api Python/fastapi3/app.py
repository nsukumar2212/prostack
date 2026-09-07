from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def home_page():
    return {"message": "Welcome to the FastAPI application!"}

@app.post("/create")
def create_user():
    return {"message": "User created successfully!"}

@app.get("/read")
def read_user():
    return {"message": "Reading user information..."}

@app.put("/update")
def update_user():
    print("Updating user information...")

@app.delete("/delete")
def delete_user():
    print("Deleting user...")