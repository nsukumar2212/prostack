
def login_req(func):
    def inner(name,status):
        if status==False:
            print("login required")
        else:
            return func(name,status)
    return inner

def home_page(name,status):
    print("Home page")

def product_page(name,status):
    print("product page")

@login_req
def profile_page(name,status):
    print("profile page")

@login_req
def order_page(name,status):
    print("Order Details")

home_page("RG",False)
product_page("RG",False)
profile_page("RG",False)
order_page("RG",False)