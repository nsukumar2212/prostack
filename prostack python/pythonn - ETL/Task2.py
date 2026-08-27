import requests
import json
import csv
import mysql.connector
from pymongo import MongoClient
from pathlib import Path


try:

    # --------------------------------
    # 1. Invoke REST API
    # --------------------------------

    url = "https://dummyjson.com/products"

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    products = data["products"]


    # --------------------------------
    # 2. Create output folder
    # --------------------------------

    folder = Path("output")

    folder.mkdir(exist_ok=True)


    # --------------------------------
    # 3. Write JSON
    # --------------------------------

    json_path = folder / "product.json"

    with open(json_path, "w") as file:

        json.dump(products, file, indent=4)


    # --------------------------------
    # 4. Write CSV
    # --------------------------------

    csv_path = folder / "product.csv"

    fields = [
        "id",
        "title",
        "price",
        "category",
        "rating"
    ]

    with open(csv_path, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fields,
            extrasaction="ignore"
        )

        writer.writeheader()

        writer.writerows(products)


    # --------------------------------
    # 5. MySQL connection
    # --------------------------------

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="taskdb"
    )

    cursor = conn.cursor()


    # --------------------------------
    # 6. Create Product table
    # --------------------------------

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Product (
        pid INT PRIMARY KEY,
        pname VARCHAR(200),
        price DECIMAL(10,2),
        category VARCHAR(100),
        rating DECIMAL(3,2)
    )
    """)


    # --------------------------------
    # 7. Insert into MySQL
    # --------------------------------

    query = """
    INSERT INTO Product
    (pid, pname, price, category, rating)
    VALUES (%s, %s, %s, %s, %s)
    """

    for product in products:

        cursor.execute(
            query,
            (
                product["id"],
                product["title"],
                product["price"],
                product["category"],
                product["rating"]
            )
        )

    conn.commit()

    cursor.close()
    conn.close()


    # --------------------------------
    # 8. MongoDB
    # --------------------------------

    client = MongoClient(
        "mongodb://localhost:27017/"
    )

    db = client["taskdb"]

    collection = db["Product"]


    # --------------------------------
    # 9. Insert into MongoDB
    # --------------------------------

    collection.insert_many(products)

    client.close()


    print("Task 2 completed successfully!")

    try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json() 


except requests.exceptions.RequestException as e:

    print("REST API Error:", e)


except mysql.connector.Error as e:

    print("MySQL Error:", e)


except Exception as e:

    print("Other Error:", e)