from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client = None

try:
    client = MongoClient("mongodb://localhost:27017")

    db = client["dbone"]

    users_col = db["users"]

    users = list(users_col.find({}))

    for user in users:
        print(user["username"])

except ConnectionFailure as err:
    print("Error: Failed to connect to MongoDB")

except Exception as err:
    print(err)

finally:
    if client:
        client.close()
        