from fastapi import FastAPI
app=FastAPI()


'''
Usage : create new user
Rest API URL: http://127.0.0.1:8000/
Method Type:POST
Required Fields:uid,uname,loc
Access Type:Public
'''
@app.post("/",description="Create- New User")
def create_user():
    return {'msg':'New User Created Successfully'}

'''
Usage : fetch all users
Rest API URL: http:127.0.0.1:8000/
Method Type:GET
Required Fields:None
Access Type:Public
'''

@app.get("/",description="Fetch all users")
def get_Users():
    return {'msg':'Fetching all users'}

'''
Usage : Update user
Rest API URL: http://127.0.0.1:8000/
Method Type:PUT
Required Fields:uid,uname,loc 
Access Type:Public
'''

@app.put("/", description='User Update')
def update_user():
    return {'msg':'User Updated Successfully'}

'''
Usage : Delete user
Rest API URL: http:127.0.0.1:8000/
Method Type:DELETE
Required Fields:None
Access Type:Public
'''

@app.delete("/",description='User Delete')
def delete_user():
    return {'msg':'user deleted successfully'}