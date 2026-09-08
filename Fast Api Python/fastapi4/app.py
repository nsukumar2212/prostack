from fastapi import FastAPI
app=FastAPI()
from routes.product_router import router as product_router
'''
Usage:Application Root Requst
Rest API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type:Public
'''
@app.get("/")
def application_root():
    return {'msg':"Application Root"}


app.include_router(product_router)