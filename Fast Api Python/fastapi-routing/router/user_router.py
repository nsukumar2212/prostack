from fastapi import APIRouter
router=APIRouter(prefix="/user")

'''
Rest API - End Point: 2
--------------------------
Usage: create new user
Rest API URL: http://127.0.0.1:8000/user/create
Method Type:POST
Requried Fields : uid,uname,email,loc
Access Type:Public 

'''
@router.post("/create")
def create_user():
    return {'msg':'User created Successfully'}