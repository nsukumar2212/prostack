import requests
import mysql.connector

# ---------------- EXTRACT ----------------

url = "https://dummyjson.com/products"

response = requests.get(url)

data = response.json()

products = data["products"]


# ---------------- TRANSFORM ----------------

beauty_products = []

for product in products:

    if product["category"] == "beauty":

        beauty_products.append((
            product["id"],
            product["title"],
            product["price"],
            product["category"],
            product["discountPercentage"]
        ))


# ---------------- LOAD ----------------

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db15"
)

cursor = con.cursor()

sql = """
INSERT INTO Product
(p_id, prod_name, price, category, discount)
VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(sql, beauty_products)

con.commit()

print("Beauty products inserted successfully")

cursor.close()
con.close()