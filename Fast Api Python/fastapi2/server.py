from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home_page():
    return {"message": "Welcome to the Home Page!"}

@app.get("/about", description="About Request")
def about_page():
    return {"message": "This is the About Page!"}

@app.get("/contact", description="Contact Request")
def contact_page():
    return {"message": "This is the Contact Page!"}
