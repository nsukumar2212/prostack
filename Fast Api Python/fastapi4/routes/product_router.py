from fastapi import APIRouter
router=APIRouter(prefix='/products')
products=[
    {'pid':101,'pname':'Marker Pen','price':30,'category':'Stationary'},
    {'pid':102,'pname':'Lenovo Mouse','price':400,'category':'Electronics'},
    {'pid':103,'pname':'ThinkPad','price':108000,'category':'Electronics'},
    {'pid':104,'pname':'Water Bottle','price':10,'category':'Groceries'},
    {'pid':105,'pname':'Dell Inspiron','price':150000,'category':'Electronics'},
    {'pid':106,'pname':'Mac Book Pro','price':183000,'category':'Electronics'},
    {'pid':107,'pname':'Stappler','price':35,'category':'Stationary'},
    {'pid':108,'pname':'R Pen','price':10,'category':'Stationary'},
    {'pid':109,'pname':'Parker Pen','price':200,'category':'Stationary'},
    {'pid':110,'pname':'Meta Rayban','price':40000,'category':'Electronics'}
]

@router.get("/stationary")
def get_stationary_products():
    filtered_products = list(
        filter(lambda product: product["category"]== "Stationary", products)
    )

    return filtered_products
'''
Rest API -1
________________
Usage: Fetch All products
Rest API URL: http://127.0.0.1:8000/products/
Method Type:GET
Required Fields:None
Access Type:Public
'''
@router.get("/")
def get_products():
    return products

@router.get("/{pid}")
def get_product_by_id(pid: int):
    filtered_products = [product for product in products if product["pid"] == pid]
    if filtered_products:
        return filtered_products
    return {"msg": "Product not found"}

@router.get("/category/{category}")
def get_products_by_category(category: str):
    filtered_products = [product for product in products if product["category"].lower() == category.lower()]
    if filtered_products:
        return filtered_products
    return {"msg": "No products found in this category"}

@router.get("/name/{pname}")
def get_product_by_name(pname: str):
    filtered_products = list(
        filter(lambda product: product["pname"].lower() == pname.lower(), products)
    )

    if filtered_products:
        return filtered_products

    return {"msg": "Product not found"}

