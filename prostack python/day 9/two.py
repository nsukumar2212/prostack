def smart_div(func):
    def inner(a,b):
        if b==0:
            print("Cannot divide by 2")
        else:
            return func(a,b)
    return inner
@smart_div
def division(a,b):
    print(a/b)
    print("Hello World")
division(10,5)           #2 Hello World
division(10,0)           #Zero division error