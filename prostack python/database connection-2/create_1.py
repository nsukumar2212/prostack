import requests
from pymongo import MongoClient

try:

    # CONNECT TO MONGODB
    client = MongoClient("mongodb://localhost:27017/")

    db = client["dbone"]

    users_col = db["users"]


    # DELETE OLD DATA
    users_col.delete_many({})


    # EXTRACT - GET DATA FROM API
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)

    users = response.json()


    # LOAD - INSERT API DATA INTO MONGODB
    users_col.insert_many(users)

    print("API users inserted successfully")


except Exception as err:
    print(err)

finally:
    client.close()