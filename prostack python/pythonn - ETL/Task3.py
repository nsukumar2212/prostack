import requests
import json
import csv
import mysql.connector
from pymongo import MongoClient
from pathlib import Path


try:

    # =====================================
    # EXTRACT
    # =====================================

    url = "https://dummyjson.com/products"

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    products = data["products"]


    # =====================================
    # TRANSFORM
    # =====================================

    beauty_products = []

    for product in products:

        if product["category"] == "beauty":

            beauty_products.append({

                "pid": product["id"],

                "pname": product["title"],

                "price": product["price"],

                "category": product["category"],

                "rating": product["rating"]

            })


    print("Beauty products:", len(beauty_products))


    # =====================================
    # CREATE OUTPUT FOLDER
    # =====================================

    folder = Path("output")

    folder.mkdir(exist_ok=True)


    # =====================================
    # LOAD 1: JSON
    # =====================================

    json_path = folder / "product.json"

    with open(json_path, "w") as file:

        json.dump(
            beauty_products,
            file,
            indent=4
        )


    # =====================================
    # LOAD 2: CSV
    # =====================================

    csv_path = folder / "product.csv"

    fields = [
        "pid",
        "pname",
        "price",
        "category",
        "rating"
    ]

    with open(csv_path, "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=fields
        )

        writer.writeheader()

        writer.writerows(beauty_products)


    # =====================================
    # LOAD 3: MYSQL
    # =====================================

    conn = mysql.connector.connect(

        host="localhost",

        user="root",

        password="root",

        database="taskdb"
    )

    cursor = conn.cursor()


    # Create Product table

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Product (

        pid INT PRIMARY KEY,

        pname VARCHAR(200),

        price DECIMAL(10,2),

        category VARCHAR(100),

        rating DECIMAL(3,2)

    )
    """)


    # Insert data

    query = """
    INSERT INTO Product
    (pid, pname, price, category, rating)
    VALUES (%s, %s, %s, %s, %s)
    """

    for product in beauty_products:

        cursor.execute(

            query,

            (
                product["pid"],
                product["pname"],
                product["price"],
                product["category"],
                product["rating"]
            )
        )

    conn.commit()

    cursor.close()

    conn.close()


    # =====================================
    # LOAD 4: MONGODB
    # =====================================

    client = MongoClient(
        "mongodb://localhost:27017/"
    )

    db = client["taskdb"]

    collection = db["Product"]


    # Insert transformed data

    collection.insert_many(
        beauty_products
    )

    client.close()


    print("Task 3 completed successfully!")


except requests.exceptions.RequestException as e:

    print("REST API Error:", e)


except mysql.connector.Error as e:

    print("MySQL Error:", e)


except Exception as e:

    print("Error:", e)