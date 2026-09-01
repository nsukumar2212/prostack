def change_case(func):
    def inner(name):
        return func(name.upper())
    return inner

    
@change_case
def greet(name):
    print("Hi",name)
greet("rahul")
greet("Gandhiji")