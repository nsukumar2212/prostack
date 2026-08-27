import requests
import json
import csv
import mysql.connector
from pymongo import MongoClient
from pathlib import Path


# -----------------------------
# 1. Invoke REST API
# -----------------------------

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()


# -----------------------------
# 2. Extract required fields
# -----------------------------

users = []

for user in data:

    users.append({
        "uid": user["id"],
        "uname": user["name"],
        "email": user["email"],
        "city": user["address"]["city"]
    })


# -----------------------------
# 3. Create output folder
# -----------------------------

folder = Path("output")

folder.mkdir(exist_ok=True)


# -----------------------------
# 4. Write JSON file
# -----------------------------

json_path = folder / "users.json"

with open(json_path, "w") as file:

    json.dump(users, file, indent=4)


# -----------------------------
# 5. Write CSV file
# -----------------------------

csv_path = folder / "users.csv"

with open(csv_path, "w", newline="") as file:

    fieldnames = ["uid", "uname", "email", "city"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()

    writer.writerows(users)


# -----------------------------
# 6. MySQL connection
# -----------------------------

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="taskdb"
)

cursor = conn.cursor()


# -----------------------------
# 7. Create MySQL table
# -----------------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS user (
    uid INT PRIMARY KEY,
    uname VARCHAR(100),
    email VARCHAR(150),
    city VARCHAR(100)
)
""")


# -----------------------------
# 8. Insert data into MySQL
# -----------------------------

query = """
INSERT INTO user
(uid, uname, email, city)
VALUES (%s, %s, %s, %s)
"""

for user in users:

    cursor.execute(
        query,
        (
            user["uid"],
            user["uname"],
            user["email"],
            user["city"]
        )
    )

conn.commit()

cursor.close()
conn.close()


# -----------------------------
# 9. MongoDB connection
# -----------------------------

client = MongoClient("mongodb://localhost:27017/")

db = client["taskdb"]

collection = db["user"]


# -----------------------------
# 10. Insert data into MongoDB
# -----------------------------

collection.insert_many(users)

client.close()


print("Task 1 completed successfully!")