from fastapi import FastAPI, Depends
from fa-aa-dd import verify_user
app=FastAPI()

# http://127.0.0.1:8000/profile 
@app.get("/profile")
def user_profile(uname:str=Depends(verify_user)):
    return {'msg':'Dashboard','user':uname}