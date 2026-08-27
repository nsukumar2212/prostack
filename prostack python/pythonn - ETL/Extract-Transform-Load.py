import requests
import json
from pymongo import MongoClient
import csv


# Extract

user_resp = requests.get(
    "https://jsonplaceholder.typicode.com/users"
)

users = user_resp.json()

status_code = user_resp.status_code

print(users)
print(status_code)


# Transform

users_json = []
users_csv = []

for user in users:

    users_json.append({
        "uid": user["id"],
        "uname": user["name"],
        "email": user["email"],
        "city": user["address"]["city"]
    })

    users_csv.append([
        user["id"],
        user["name"],
        user["email"],
        user["address"]["city"]
    ])


print(users_json)


# Load into JSON

fp1 = open("users.json", "w")

json.dump(users_json, fp1, indent=4)

fp1.close()

print("New JSON file created")


# Load into MongoDB

client = None

try:

    client = MongoClient("mongodb://localhost:27017/")

    db = client["userdb"]

    collection = db["users"]

    collection.insert_many(users_json)

    print("Data inserted into MongoDB successfully")

except Exception as err:

    print("MongoDB Error:", err)

finally:

    if client:
        client.close()

        print("MongoDB connection closed")


# Load into CSV

fp2 = open("users.csv", "w", newline="")

csv_writer = csv.writer(fp2)

csv_writer.writerow([
    "uid",
    "uname",
    "email",
    "city"
])

csv_writer.writerows(users_csv)

fp2.close()

print("New CSV file created")