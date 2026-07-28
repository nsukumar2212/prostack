def login_req(func):
    def inner(name,status):
        if status!=true:
            print("Login request")
        else:
            return func(name,status)
        return inner

def index(name, status):
    print("Home page")

def product_page(name,status):
    print("product page")

def order_page(name,status):
    print("placed order")

def profile_page(name,status):
    print("profile Details")

index("Rg",False)
product_page("rg",True)
order_page("rg",False)
profile_page("rg",False)